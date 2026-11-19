#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	MockModule
Summary:	Test::MockModule - Override subroutines in a module for unit testing
#Summary(pl.UTF-8):	
Name:		perl-Test-MockModule
Version:	0.185.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/G/GF/GFRANKS/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	1a524d6e937b0a2ff1e575ec9628e110
URL:		https://metacpan.org/release/Test-MockModule
BuildRequires:	perl-Module-Build >= 0.4234
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-SUPER >= 1.20
BuildRequires:	perl-Test-Warnings
%endif
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
%setup -q -n %{pdir}-%{pnam}-v%{version}

%build
%{__perl} Build.PL \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT \
	--create_packlist=0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
