%global npm_name node-forge

Name:           nodejs-%{npm_name}
Version:        0.10.0
Release:        1%{?dist}
Summary:        JavaScript implementations of network transports, cryptography, ciphers, PKI, message digests, and various utilities.

License: 	MIT
URL:		https://github.com/digitalbazaar/forge
Source0:	http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

Requires:	nodejs
BuildRequires:	nodejs-devel

%description
The Forge software is a fully native implementation of the TLS protocol in JavaScript, a set of cryptography utilities, and a set of tools for developing Web Apps that utilize many network resources.

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
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
