%global npm_name papaparse

Name:           nodejs-%{npm_name}
Version:        5.3.0
Release:        1%{?dist}
Summary:        Fast and powerful CSV parser for the browser that supports web workers and streaming large files. Converts CSV to JSON and JSON to CSV. 

License: 	MIT
URL:		http://papaparse.com/
Source0:	http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source2:	%{npm_name}-%{version}-nm-dev.tgz
Source3:	%{npm_name}-%{version}-bundled-licenses.txt

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

Requires:	nodejs
BuildRequires:	nodejs-devel

%description
Papa Parse is the fastest in-browser CSV (or delimited text) parser for JavaScript.

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
