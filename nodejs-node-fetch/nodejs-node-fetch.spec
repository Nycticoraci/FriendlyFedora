%global npm_name node-fetch

Name:           nodejs-%{npm_name}
Version:        2.6.1
Release:        1%{?dist}
Summary:        A light-weight module that brings window.fetch to node.js

License: 	MIT
URL:		https://github.com/bitinn/node-fetch
Source0:	http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

Requires:	nodejs
BuildRequires:	nodejs-devel

%description
Instead of implementing XMLHttpRequest in Node.js to run browser-specific Fetch polyfill, why not go from native http to fetch API directly? Hence, node-fetch, minimal code for a window.fetch compatible API on Node.js runtime.

%prep
%setup -q -n package

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
%license LICENSE.md
%{nodejs_sitelib}/%{npm_name}

%changelog
