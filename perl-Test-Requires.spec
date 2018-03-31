%define modname	Test-Requires
%define modver 0.10

Summary:	Checks to see if the module can be loaded
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Test::Requires checks to see if the module can be loaded.

If this fails rather than failing tests this *skips all tests*.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc  META.yml Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
