#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Image
%define		pnam	Grab
Summary:	Image::Grab perl module
Summary(pl):	Modu³ perla Image::Grab
Name:		perl-Image-Grab
Version:	1.4.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8a62dcff23997e525f7557451f5758dd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-libnet
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image::Grab is a perl module for Grabbing images off the Internet.

%description -l pl
Image::Grab jest modu³em do ¶ci±gania obrazków z Internetu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "N" | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Image/Grab.pm
%{perl_vendorlib}/Image/Grab
%{_mandir}/man3/*
