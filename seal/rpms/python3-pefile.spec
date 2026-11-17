Name:           python3-pefile
Version:        2024.8.26
Release:        1%{?dist}
Summary:        Python PE parsing module
License:        MIT
URL:            https://github.com/erocarrera/pefile
Source0:        pefile-%{version}.tar.gz
BuildArch:      noarch
AutoReqProv:    no
Requires:       python3
Provides:       python3dist(pefile) = %{version}

%description
Pure Python module for parsing Portable Executable files.

%prep
%setup -q -n pefile-%{version}

%install
install -d "%{buildroot}%{_python_sitelib}/ordlookup"
install -m 0644 pefile.py peutils.py "%{buildroot}%{_python_sitelib}/"
install -m 0644 ordlookup/*.py "%{buildroot}%{_python_sitelib}/ordlookup/"
install -D -m 0644 LICENSE \
  "%{buildroot}%{_licensedir}/%{name}/LICENSE"

%files
%license %{_licensedir}/%{name}/LICENSE
%{_python_sitelib}/ordlookup/
%{_python_sitelib}/__pycache__/
%{_python_sitelib}/pefile.py
%{_python_sitelib}/peutils.py
