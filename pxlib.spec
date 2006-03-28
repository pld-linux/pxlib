#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	A library to read Paradox DB files
Summary(pl):	Biblioteka do odczytu plików baz danych Paradox DB
Name:		pxlib
Version:	0.6.0
Release:	2
Epoch:		0
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/pxlib/%{name}-%{version}.tar.gz
# Source0-md5:	14afa3d5f65be74e701668e47c0a1759
Patch0:		%{name}-stderr.patch
URL:		http://pxlib.sourceforge.net/
BuildRequires:	docbook-utils
BuildRequires:	libgsf-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
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
%patch0 -p1

%build
# man pages are build by docbook2man
sed -i -e 's#mv PXLIB.3 pxlib.3##g' doc/Makefile*
sed -i -e 's#docbook-to-man#docbook2man#g' configure*
sed -i -e 's#docbook-to-man $<.*#docbook2man $<#g' doc/Makefile*
for man in doc/*.sgml; do
	name=$(basename "$man" .sgml)
	sed -i -e "s#$name#$name#gi" $man
done
CPPFLAGS="$(pkg-config glib-2.0 --cflags)"
%configure \
	--with-gsf \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
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
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
