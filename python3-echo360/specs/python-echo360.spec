# Created by pyp2rpm-3.3.5
%global pypi_name echo360

Name:           python-%{pypi_name}
Version:        2.0.3
Release:        1%{?dist}
Summary:        Command line tool for automated downloads of echo360 videos

License:        MIT
URL:            https://cs.tinyiu.com/echo360
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
echo360 is a command-line Python tool that allows you
to download lecture videos from any university's Echo360 system and echo360
Cloud platform. All that's required is the particular course's url. See the FAQ
for tips on how to find it.The way this script works _should_ support all
university's echo360 system in theory, see FAQ for details.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
echo360 is a command-line Python tool that allows you
to download lecture videos from any university's Echo360 system and echo360
Cloud platform. All that's required is the particular course's url. See the FAQ
for tips on how to find it.The way this script works _should_ support all
university's echo360 system in theory, see FAQ for details.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/echo360-download
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jan 02 2021 Gerard Bechard - 2.0.3-1
- Initial package.
