#!/usr/bin/env bash
set -euo pipefail

topdir=/tmp/python-rpm-build
mkdir -p "$topdir/BUILD" "$topdir/BUILDROOT" "$topdir/RPMS" \
  "$topdir/SOURCES" "$topdir/SPECS" "$topdir/SRPMS" /out

curl --fail --location --retry 3 \
  https://files.pythonhosted.org/packages/03/4f/2750f7f6f025a1507cd3b7218691671eecfd0bbebebe8b39aa0fe1d360b8/pefile-2024.8.26.tar.gz \
  --output "$topdir/SOURCES/pefile-2024.8.26.tar.gz"
curl --fail --location --retry 3 \
  https://files.pythonhosted.org/packages/fd/aa/3e0508d5a5dd96529cdc5a97011299056e14c6505b678fd58938792794b1/zstandard-0.25.0.tar.gz \
  --output "$topdir/SOURCES/zstandard-0.25.0.tar.gz"

cd "$topdir/SOURCES"
printf '%s  %s\n' \
  3ff6c5d8b43e8c37bb6e6dd5085658d658a7a0bdcd20b6a07b1fcfc1c4e9d632 \
  pefile-2024.8.26.tar.gz \
  7713e1179d162cf5c7906da876ec2ccb9c3a9dcbdffef0cc7f70c3667a205f0b \
  zstandard-0.25.0.tar.gz | sha256sum --check

cp /tmp/seal-rpms/python3-pefile.spec /tmp/seal-rpms/python3-zstandard.spec \
  "$topdir/SPECS/"
rpmbuild --define "_topdir $topdir" -ba "$topdir/SPECS/python3-pefile.spec"
rpmbuild --define "_topdir $topdir" -ba "$topdir/SPECS/python3-zstandard.spec"

for package in "$topdir"/RPMS/*/*.rpm; do
  cp "$package" /out/
done
