%define upstream_name    Path-Class-File-Stat
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Cache and compare stat() calls on a Path::Class::File object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Path/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Path::Class)
BuildArch:	noarch

%description
Path::Class::File::Stat is a simple extension of Path::Class::File.
Path::Class::File::Stat is useful in long-running programs (as under
mod_perl) where you might have a file handle opened and want to check if
the underlying file has changed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 657821
- rebuild for updated spec-helper

* Tue Oct 26 2010 Buchan Milne <bgmilne@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 589484
- import perl-Path-Class-File-Stat

