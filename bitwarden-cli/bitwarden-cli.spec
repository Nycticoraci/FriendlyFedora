%global npm_name bitwarden-cli

Name:           %{npm_name}
Version:        1.15.1
Release:        1%{?dist}
Summary:        A secure and free password manager for all of your devices

License: 	GPLv3
URL:		https://bitwarden.com/
Source0: 	https://registry.npmjs.org/@bitwarden/cli/-/cli-%{version}.tgz
Source1:	%{npm_name}-%{version}-nm-prod.tgz
Source2:	%{npm_name}-%{version}-nm-dev.tgz
Source3:	%{npm_name}-%{version}-bundled-licenses.txt

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

Requires:	nodejs
BuildRequires:	nodejs-devel

%description
The Bitwarden CLI is a powerful, full-featured command-line interface (CLI) tool to access and manage a Bitwarden vault. The CLI is written with TypeScript and Node.js and can be run on Windows, macOS, and Linux distributions.

%prep
%setup -q -n package
cp %{SOURCE3} .
# Setup bundled runtime(prod) node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .

# Fix coffee shebangs
sed -i s/'#!.*'/'#!\/usr\/bin\/coffee'/ ../node_modules_prod/performance-now/test/scripts/*
popd

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr . \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

chmod +x %{buildroot}%{nodejs_sitelib}/%{npm_name}/build/bw.js 

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{npm_name}/build/bw.js %{buildroot}%{_bindir}/bw

%check 
#%{__nodejs} -e 'require("./")'

%files
%doc README.md
%license LICENSE.txt %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/bw

%changelog
