
Summary:	A library to read Paradox DB files
Summary(pl):	Biblioteka do odczytu plików baz danych Paradox DB
Name:		pxlib
Version:	0.5.1
Release:	1
Epoch:		0
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/pxlib/%{name}-%{version}.tar.gz
# Source0-md5:	38f049b2ffe9370f98e1cf755d18a3fb
URL:		http://pxlib.sourceforge.net/
BuildRequires:	perl-XML-Parser
BuildRequires:	libgsf-devel
BuildRequires:	docbook-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxlib is a simply and still small C library to read Paradox DB files.
It supports all versions starting from 3.0. It currently has a very
limited set of functions like to open a DB file, read its header and
read every single record.

%description -l pl
pxlib jest prost± i ci±gle ma³± bibliotek± do odczytu plików baz
danych Paradox DB. Obs³uguje wszystkie wersje pocz±wszy od 3.0.
Aktualnie ma bardzo ograniczony zbiór funkcji, takich jak otworzenie
pliku DB, odczyt nag³ówka i odczyt pojedynczego rekordu.

%package devel
Summary:	Header files for pxlib
Summary(pl):	Pliki nag³ówkowe pxlib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for pxlib.

%description devel -l pl
Pliki nag³ówkowe pxlib.

%package static
Summary:	Static pxlib library
Summary(pl):	Statyczna biblioteka pxlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static pxlib library.

%description static -l pl
Statyczna biblioteka pxlib.

%prep
%setup -q

%build
# man pages are build by docbook2man
sed -i -e 's#mv PXLIB.3 pxlib.3##g' doc/Makefile*
sed -i -e 's#docbook-to-man#docbook2man#g' configure*
sed -i -e 's#docbook-to-man $<.*#docbook2man $<#g' doc/Makefile*
for man in doc/*.sgml; do
	name=$(basename "$man" .sgml)
	sed -i -e "s#$name#$name#gi" $man
done
%configure \
	--with-gsf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog doc/*.txt
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_libdir}/lib*.la
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
