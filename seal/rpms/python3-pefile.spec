Name:           python3-pefile
Version:        2024.8.26
Release:        1%{?dist}
Summary:        Python PE parsing module
License:        MIT
URL:            https://github.com/erocarrera/pefile
Source0:        pefile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3
Provides:       python3dist(pefile) = %{version}

%description
Pure Python module for parsing Portable Executable files.

%prep
%setup -q -n pefile-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --root=%{buildroot} --prefix=%{_prefix} \
  --single-version-externally-managed --record=installed-files.txt

%files
%license LICENSE
%{python3_sitelib}/ordlookup/
%{python3_sitelib}/pefile.py
%{python3_sitelib}/peutils.py
%{python3_sitelib}/pefile*.egg-info/
