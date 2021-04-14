# Created by pyp2rpm-3.3.5
%global pypi_name pytorch

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        1%{?dist}
Summary:	Tensors and Dynamic neural networks in Python with strong GPU acceleration.

License:        None
URL:            http://pytorch.org/#pip-install-pytorch
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
Tensors and Dynamic neural networks in Python with strong GPU acceleration.}

%description %_description

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Apr 14 2021 jaki <jacqueline_elaine@outlook.com> - 0.1.2-1
- Initial package.
