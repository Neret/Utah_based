#!/usr/bin/env bash
set -euo pipefail

topdir=/tmp/python-rpm-build
mkdir -p "$topdir/BUILD" "$topdir/BUILDROOT" "$topdir/RPMS" \
  "$topdir/SOURCES" "$topdir/SPECS" "$topdir/SRPMS" /out

python3 - "$topdir/SOURCES" <<'PY'
import hashlib
import pathlib
import sys
import urllib.request

if sys.version_info[:2] != (3, 14):
    raise SystemExit("The pinned zstandard wheel requires Python 3.14")

sources = (
    (
        "pefile-2024.8.26.tar.gz",
        "https://files.pythonhosted.org/packages/03/4f/2750f7f6f025a1507cd3b7218691671eecfd0bbebebe8b39aa0fe1d360b8/pefile-2024.8.26.tar.gz",
        "3ff6c5d8b43e8c37bb6e6dd5085658d658a7a0bdcd20b6a07b1fcfc1c4e9d632",
    ),
    (
        "zstandard-0.25.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl",
        "https://files.pythonhosted.org/packages/31/dc/cc50210e11e465c975462439a492516a73300ab8caa8f5e0902544fd748b/zstandard-0.25.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl",
        "e09bb6252b6476d8d56100e8147b803befa9a12cea144bbe629dd508800d1ad0",
    ),
)

destination = pathlib.Path(sys.argv[1])
for filename, url, expected in sources:
    path = destination / filename
    digest = hashlib.sha256()
    with urllib.request.urlopen(url, timeout=60) as response:
        with path.open("wb") as output:
            while chunk := response.read(1024 * 1024):
                output.write(chunk)
                digest.update(chunk)
    if digest.hexdigest() != expected:
        raise SystemExit(f"SHA-256 mismatch for {filename}")
PY

cp /tmp/seal-rpms/python3-pefile.spec /tmp/seal-rpms/python3-zstandard.spec \
  "$topdir/SPECS/"
python_sitelib="$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')"
rpmbuild --define "_topdir $topdir" --define "_python_sitelib $python_sitelib" \
  -ba "$topdir/SPECS/python3-pefile.spec"
rpmbuild --define "_topdir $topdir" --define "_python_sitelib $python_sitelib" \
  -ba "$topdir/SPECS/python3-zstandard.spec"

for package in "$topdir"/RPMS/*/*.rpm; do
  cp "$package" /out/
done
