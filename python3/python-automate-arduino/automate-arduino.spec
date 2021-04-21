# Created by pyp2rpm-3.3.6
%global pypi_name automate-arduino

Name:           python-%{pypi_name}
Version:        0.9.2
Release:        1%{?dist}
Summary:        Arduino Support for Automate

License:        GPL
URL:            http://github.com/tuomas2/automate-arduino
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

%description
Arduino Support for Automate < Read the full documentation at Readthedocs.org <
Install from Pypi:: pip install automate-arduinoOptionally, you could install
also by cloning GIT repository and installing manually:: git clone cd automate-
arduino ./setup.py installLicence Automate is free software: you can
redistribute it and/or modify it under the terms of the GNU General Public
License as published by

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       (python2dist(automate) >= 0.9.2 with python2dist(automate) < 0.10)
Requires:       python2dist(mock) = 1.0.1
Requires:       python2dist(pyfirmata) = 1.0.3
Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
Arduino Support for Automate < Read the full documentation at Readthedocs.org <
Install from Pypi:: pip install automate-arduinoOptionally, you could install
also by cloning GIT repository and installing manually:: git clone cd automate-
arduino ./setup.py installLicence Automate is free software: you can
redistribute it and/or modify it under the terms of the GNU General Public
License as published by


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install

%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitelib}/automate_arduino
%{python2_sitelib}/automate_arduino-%{version}-py%{python2_version}.egg-info

%changelog
* Wed Apr 21 2021 Joe Kim <joekim0923@gmail.com> - 0.9.2-1
- Initial package.
