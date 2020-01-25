#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	MockModule
Summary:	Test::MockModule - Override subroutines in a module for unit testing
#Summary(pl.UTF-8):	
Name:		perl-Test-MockModule
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b013aeeb221f83e7f325a2f98169296
URL:		http://search.cpan.org/dist/Test-MockModule/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::MockModule lets you temporarily redefine subroutines in other
packages for the purposes of unit testing.

A Test::MockModule object is set up to mock subroutines for a given
module. The object remembers the original subroutine so it can be
easily restored. This happens automatically when all MockModule
objects for the given module go out of scope, or when you unmock() the
subroutine.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
