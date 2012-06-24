
# TODO:
# - manual pages generation (missing docbook-to-man tool)

Summary:	A library to read Paradox DB files
Summary(pl):	Biblioteka do odczytu plik�w baz danych Paradox DB
Name:		pxlib
Version:	0.4.3
Release:	1
Epoch:		0
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/pxlib/%{name}-%{version}.tar.gz
# Source0-md5:	1155f6704ca05c4cb6af000dd6cb5787
URL:		http://pxlib.sourceforge.net/
BuildRequires:	libgsf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxlib is a simply and still small C library to read Paradox DB files.
It supports all versions starting from 3.0. It currently has a very
limited set of functions like to open a DB file, read its header and
read every single record.

%description -l pl
pxlib jest prost� i ci�gle ma�� bibliotek� do odczytu plik�w baz
danych Paradox DB. Obs�uguje wszystkie wersje pocz�wszy od 3.0.
Aktualnie ma bardzo ograniczony zbi�r funkcji, takich jak otworzenie
pliku DB, odczyt nag��wka i odczyt pojedynczego rekordu.

%package devel
Summary:	Header files for pxlib
Summary(pl):	Pliki nag��wkowe pxlib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for pxlib.

%description devel -l pl
Pliki nag��wkowe pxlib.

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
