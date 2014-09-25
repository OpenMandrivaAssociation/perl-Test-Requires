%define modname	Test-Requires
%define modver 0.08

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
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc  META.yml Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
