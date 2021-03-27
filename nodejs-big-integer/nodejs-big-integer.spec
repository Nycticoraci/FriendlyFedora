%global npm_name big-integer

Name:           nodejs-%{npm_name}
Version:        1.6.48
Release:        1%{?dist}
Summary:        An arbitrary length integer library for Javascript

License: 	Public Domain
URL:		https://github.com/peterolson/BigInteger.js
Source0:	http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source2:	%{npm_name}-%{version}-nm-dev.tgz
Source3:	%{npm_name}-%{version}-bundled-licenses.txt

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

Requires:	nodejs
BuildRequires:	nodejs-devel

%description
BigInteger.js is an arbitrary-length integer library for Javascript, allowing arithmetic operations on integers of unlimited size, notwithstanding memory and time limitations.

%prep
%setup -q -n package
cp %{SOURCE3} .

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr . \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

%check
%{__nodejs} -e 'require("./")'

%files
%doc README.md
%license LICENSE 
%{nodejs_sitelib}/%{npm_name}

%changelog
