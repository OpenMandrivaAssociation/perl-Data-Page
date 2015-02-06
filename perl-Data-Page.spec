%define upstream_name    Data-Page
%define upstream_version 2.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Help when paging through sets of results
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Chained)
BuildRequires:	perl(Test::Exception)
Requires:	perl(Class::Accessor::Chained::Fast)
BuildArch:	noarch

%description
When searching through large amounts of data, it is often the case
that a result set is returned that is larger than we want to display
on one page. This results in wanting to page through various pages of
data. The maths behind this is unfortunately fiddly, hence this
module.

The main concept is that you pass in the number of total entries, the
number of entries per page, and the current page number. You can then
call methods to find out how many pages of information there are, and
what number the first and last entries on the current page really are.

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
%doc README CHANGES
%{perl_vendorlib}/Data/*
%{_mandir}/*/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2.20.0-2mdv2011.0
+ Revision: 681378
- mass rebuild

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 2.20.0-1mdv2011.0
+ Revision: 474737
- update to 2.02

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.10.0-1mdv2010.0
+ Revision: 406973
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2009.1
+ Revision: 292074
- update to new version 2.01

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.00-6mdv2009.0
+ Revision: 241199
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.00-4mdv2008.0
+ Revision: 48594
- fix runtime dependencies, not buildtime ones

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.00-3mdv2008.0
+ Revision: 48529
- fix dependencies


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.00-2mdv2007.0
+ Revision: 73456
- import perl-Data-Page-2.00-2mdv2007.1

* Sun Jan 15 2006 Frederic Lepied <flepied@mandriva.com> 2.00-1mdk
- Initial package

