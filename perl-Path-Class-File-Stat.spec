%define upstream_name    Path-Class-File-Stat
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Cache and compare stat() calls on a Path::Class::File object
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Path/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Path::Class)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Path::Class::File::Stat is a simple extension of Path::Class::File.
Path::Class::File::Stat is useful in long-running programs (as under
mod_perl) where you might have a file handle opened and want to check if
the underlying file has changed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


