# Created by pyp2rpm-3.3.5
%global pypi_name wget

Name:           python-%{pypi_name}
Version:        3.2
Release:        1%{?dist}
Summary:        Pure python download utility

License:        Public Domain
URL:            http://bitbucket.org/techtonik/python-wget/
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
python -m wget [options] <URL> options: -o --output FILE|DIR output filename
or directory}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

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
%pycached %{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 20 2021 Manuel Martinez <mannyy687@fedoraproject.org> - 3.2
- Update files

* Mon Apr 12 2021 Gerard Bechard <gbechard@fedoraproject.org> - 3.2
- Initial package.
