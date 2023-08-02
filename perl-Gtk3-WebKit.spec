#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Gtk3-WebKit
Version  : 0.06
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/P/PO/POTYL/Gtk3-WebKit-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PO/POTYL/Gtk3-WebKit-0.06.tar.gz
Summary  : 'WebKit bindings for Perl'
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-Gtk3-WebKit-license = %{version}-%{release}
Requires: perl-Gtk3-WebKit-perl = %{version}-%{release}
Requires: webkitgtk
BuildRequires : buildreq-cpan
BuildRequires : perl(Cairo)
BuildRequires : perl(Cairo::GObject)
BuildRequires : perl(Glib)
BuildRequires : perl(Glib::Object::Introspection)
BuildRequires : perl(Gtk3)
BuildRequires : perl(Test::NeedsDisplay)
BuildRequires : pkgconfig(webkit2gtk-4.1)
BuildRequires : util-linux
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: Gtk3-WebKit-0.06-Port-to-webkitgtk4.patch

%description
This archive contains the distribution Gtk3-WebKit,
version 0.06:
WebKit bindings for Perl

%package dev
Summary: dev components for the perl-Gtk3-WebKit package.
Group: Development
Provides: perl-Gtk3-WebKit-devel = %{version}-%{release}
Requires: perl-Gtk3-WebKit = %{version}-%{release}

%description dev
dev components for the perl-Gtk3-WebKit package.


%package license
Summary: license components for the perl-Gtk3-WebKit package.
Group: Default

%description license
license components for the perl-Gtk3-WebKit package.


%package perl
Summary: perl components for the perl-Gtk3-WebKit package.
Group: Default
Requires: perl-Gtk3-WebKit = %{version}-%{release}

%description perl
perl components for the perl-Gtk3-WebKit package.


%prep
%setup -q -n Gtk3-WebKit-0.06
cd %{_builddir}/Gtk3-WebKit-0.06
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Gtk3-WebKit
cp %{_builddir}/Gtk3-WebKit-%{version}/COPYING %{buildroot}/usr/share/package-licenses/perl-Gtk3-WebKit/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/Gtk3-WebKit-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Gtk3-WebKit/e31ca32ae3719c91db4befb50294a04ca9c46f0a || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Gtk3::WebKit.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Gtk3-WebKit/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/perl-Gtk3-WebKit/e31ca32ae3719c91db4befb50294a04ca9c46f0a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
