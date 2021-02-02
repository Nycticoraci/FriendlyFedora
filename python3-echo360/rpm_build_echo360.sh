#!/bin/bash

# This script builds the RPM package for echo360, and its dependencies.
# 
# This script must be executed in the same working directory as the "specs" and "srcs"
# directories containing the package specfiles and source tarballs, respectively.

if [[ `dirname "$0"` != '.' ]]; then
	echo "Run this script in its own directory (./`basename "$0"`)"
	exit 1
fi

if [[ -d "$HOME/rpmbuild" ]]; then
	echo -n "$HOME/rpmbuild exists. Overwrite? [y/N] "
	read IN
	case $IN in
		y|Y)	rm -rf "$HOME/rpmbuild"
			;;
		*)	echo "Abort."
			exit 1
			;;
	esac	
fi

rpmdev-setuptree
BUILDDIR="$HOME/rpmbuild"

cp specs/*.spec $BUILDDIR/SPECS
cp srcs/{*.tar.gz,*.zip} $BUILDDIR/SOURCES

rpmbuild -bs $BUILDDIR/SPECS/*
rpmbuild --rebuild $BUILDDIR/SRPMS/*

if [[ ! -d "rpms" ]]; then
	mkdir rpms
fi

mv $BUILDDIR/RPMS/noarch/* rpms/

echo -e "\nThe following RPMS have been created:"
ls -d1 rpms/*
