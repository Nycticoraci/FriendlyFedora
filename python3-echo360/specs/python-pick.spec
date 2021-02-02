# Created by pyp2rpm-3.3.5
%global pypi_name pick

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        pick an option in the terminal with a simple GUI

License:        MIT
URL:            https://github.com/wong2/pick
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(setuptools)

%description
pick is a small python library to help you create curses based interactive
selection list in the terminal.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
pick is a small python library to help you create curses based interactive
selection list in the terminal.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jan 02 2021 Gerard Bechard - 1.0.0-1
- Initial package.
