# Created by pyp2rpm-3.3.5
%global pypi_name wget

Name:           python-%{pypi_name}
Version:        3.2
Release:        1%{?dist}
Summary:        pure python download utility

License:        Public Domain
URL:            http://bitbucket.org/techtonik/python-wget/
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
python -m wget [options] <URL> options: -o --output FILE|DIR output filename
or directory

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
python -m wget [options] <URL> options: -o --output FILE|DIR output filename
or directory


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# Fix shebang, make executable
%py3_shebang_fix %{buildroot}%{python3_sitelib}/wget.py
chmod a+x %{buildroot}%{python3_sitelib}/wget.py

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jan 02 2021 Gerard Bechard - 3.2-1
- Initial package.
