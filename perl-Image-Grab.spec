%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Image-Grab perl module
Summary(pl):	Modu� perla Image-Grab
Name:		perl-Image-Grab
Version:	0.9.2
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Image/Image-Grab-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-libwww
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-URI
BuildRequires:	perl-Digest-MD5
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-libwww
Requires:	perl-HTML-Tree
Requires:	perl-URI
Requires:	perl-Digest-MD5
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Image-Grab is a perl module for Grabbing images off the Internet. 

%description -l pl
Image-Grab jest modu�em do �ci�gania obrazk�w z Internetu.

%prep
%setup -q -n Image-Grab-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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
