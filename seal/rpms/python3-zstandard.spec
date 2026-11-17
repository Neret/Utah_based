Name:           python3-zstandard
Version:        0.25.0
Release:        1%{?dist}
Summary:        Python bindings for Zstandard
License:        BSD-3-Clause
URL:            https://github.com/indygreg/python-zstandard
Source0:        zstandard-%{version}-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl
AutoReqProv:    no
Requires:       python(abi) = 3.14
Provides:       python3dist(zstandard) = %{version}

%description
Python bindings for the Zstandard compression library.

%prep
mkdir -p zstandard-wheel
python3 -m zipfile -e %{SOURCE0} zstandard-wheel

%install
install -d "%{buildroot}%{_python_sitelib}"
cp -a zstandard-wheel/zstandard \
  zstandard-wheel/zstandard-%{version}.dist-info \
  "%{buildroot}%{_python_sitelib}/"

%files
%license %{_python_sitelib}/zstandard-%{version}.dist-info/licenses/LICENSE
%{_python_sitelib}/zstandard/
%dir %{_python_sitelib}/zstandard-%{version}.dist-info/
%dir %{_python_sitelib}/zstandard-%{version}.dist-info/licenses/
%{_python_sitelib}/zstandard-%{version}.dist-info/METADATA
%{_python_sitelib}/zstandard-%{version}.dist-info/RECORD
%{_python_sitelib}/zstandard-%{version}.dist-info/WHEEL
%{_python_sitelib}/zstandard-%{version}.dist-info/top_level.txt
