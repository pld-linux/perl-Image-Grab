%include	/usr/lib/rpm/macros.perl
Summary:	Image-Grab perl module
Summary(pl):	Modu³ perla Image-Grab
Name:		perl-Image-Grab
Version:	0.9.5
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Image/Image-Grab-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-libwww
BuildRequires:	perl-libnet
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-Digest-MD5
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image-Grab is a perl module for Grabbing images off the Internet.

%description -l pl
Image-Grab jest modu³em do ¶ci±gania obrazków z Internetu.

%prep
%setup -q -n Image-Grab-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Image/Grab
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Image/Grab.pm
%{perl_sitelib}/Image/Grab
%{perl_sitelib}/auto/Image/Grab
%{perl_sitearch}/auto/Image/Grab

%{_mandir}/man3/*
