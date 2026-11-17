Name:           python3-zstandard
Version:        0.25.0
Release:        1%{?dist}
Summary:        Python bindings for Zstandard
License:        BSD-3-Clause
URL:            https://github.com/indygreg/python-zstandard
Source0:        zstandard-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  python3-devel
BuildRequires:  python3-packaging
BuildRequires:  python3-setuptools
Requires:       libzstd
Requires:       python3
Provides:       python3dist(zstandard) = %{version}

%description
Python bindings for the Zstandard compression library.

%prep
%setup -q -n zstandard-%{version}

%build
%{__python3} setup.py build --system-zstd --no-cffi-backend

%install
%{__python3} setup.py install --skip-build --root=%{buildroot} \
  --prefix=%{_prefix} --single-version-externally-managed \
  --record=installed-files.txt

%files
%license LICENSE
%{python3_sitelib}/zstandard/
%{python3_sitelib}/zstandard*.egg-info/
