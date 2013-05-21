%define upstream_name    Test-Requires
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Checks to see if the module can be loaded
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
Test::Requires checks to see if the module can be loaded.

If this fails rather than failing tests this *skips all tests*.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-4mdv2012.0
+ Revision: 765747
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-3
+ Revision: 764252
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2
+ Revision: 656972
- rebuild for updated spec-helper

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 596040
- update to new version 0.06

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 554173
- import perl-Test-Requires


* Fri Jul 16 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
