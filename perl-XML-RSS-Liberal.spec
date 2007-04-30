#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	RSS-Liberal
Summary:	XML::RSS::Liberal - XML::RSS With A Liberal Parser
#Summary(pl.UTF-8):	
Name:		perl-XML-RSS-Liberal
Version:	0.03_01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DM/DMAKI/XML-RSS-Liberal-0.03_01.tar.gz
# Source0-md5:	2d626250801895d50a41e32aca6f0cd7
URL:		http://search.cpan.org/dist/XML-RSS-Liberal/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(XML::Liberal)
BuildRequires:	perl-XML-RSS-LibXML >= 0.30
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::RSS::Liberal is a subclass of XML::RSS::LibXML, for those of you who
want to parse broken RSS files (as they often are). It uses XML::Liberal as
its core parser, and therefore it can parse whatever broken XML you provided,
so as long as XML::Liberal can tolerate it.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-0.03

%build
%{__perl} Makefile.PL \
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
%doc Changes
%{perl_vendorlib}/XML/RSS/*.pm
%{_mandir}/man3/*
