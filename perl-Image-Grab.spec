%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	Grab
Summary:	Image::Grab perl module
Summary(pl):	Modu� perla Image::Grab
Name:		perl-Image-Grab
Version:	1.4
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libwww
BuildRequires:	perl-libnet
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image::Grab is a perl module for Grabbing images off the Internet.

%description -l pl
Image::Grab jest modu�em do �ci�gania obrazk�w z Internetu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "N" | perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Image/Grab.pm
%{perl_sitelib}/Image/Grab.pod
%{perl_sitelib}/Image/Grab
%{_mandir}/man3/*
