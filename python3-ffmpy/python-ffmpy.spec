# Created by pyp2rpm-3.3.5
%global pypi_name ffmpy

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        1%{?dist}
Summary:        A simple Python wrapper for ffmpeg

License:        MIT
URL:            https://github.com/Ch00k/ffmpy
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
ffmpy is a simplistic FFmpeg command line wrapper. It implements a
Pythonic interface for FFmpeg command line compilation and uses Python
sub-process module to execute compiled command line.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 12 2021 Joe Kim<joebkim@fedoraproject.org> - 0.3.0-1
- Initial package.
