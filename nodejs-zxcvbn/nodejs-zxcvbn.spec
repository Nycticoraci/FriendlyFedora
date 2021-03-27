%global npm_name zxcvbn

Name:           nodejs-%{npm_name}
Version:        4.4.2
Release:        1%{?dist}
Summary:        realistic password strength estimation

License: 	MIT
URL:		https://github.com/dropbox/zxcvbn
Source0:	http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source2:	%{npm_name}-%{version}-nm-dev.tgz
Source3:	%{npm_name}-%{version}-bundled-licenses.txt

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

Requires:	nodejs
BuildRequires:	nodejs-devel

%description
zxcvbn is a password strength estimator inspired by password crackers. Through pattern matching and conservative estimation, it recognizes and weighs 30k common passwords, common names and surnames according to US census data, popular English words from Wikipedia and US television and movies, and other common patterns like dates, repeats (aaa), sequences (abcd), keyboard patterns (qwertyuiop), and l33t speak.

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
%license LICENSE.txt
%{nodejs_sitelib}/%{npm_name}

%changelog
