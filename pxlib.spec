#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	A library to read Paradox DB files
Summary(pl.UTF-8):	Biblioteka do odczytu plików baz danych Paradox DB
Name:		pxlib
Version:	0.6.8
Release:	1
Epoch:		0
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/pxlib/%{name}-%{version}.tar.gz
# Source0-md5:	220578ab27348613a35a55902c3999f3
Patch0:		%{name}-stderr.patch
Patch1:		%{name}-pc.patch
URL:		http://pxlib.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-to-man
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	libgsf-devel >= 1.14.1
BuildRequires:	libtool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxlib is a simply and still small C library to read Paradox DB files.
It supports all versions starting from 3.0. It currently has a very
limited set of functions like to open a DB file, read its header and
read every single record.

%description -l pl.UTF-8
pxlib jest prostą i ciągle małą biblioteką do odczytu plików baz
danych Paradox DB. Obsługuje wszystkie wersje począwszy od 3.0.
Aktualnie ma bardzo ograniczony zbiór funkcji, takich jak otworzenie
pliku DB, odczyt nagłówka i odczyt pojedynczego rekordu.

%package devel
Summary:	Header files for pxlib
Summary(pl.UTF-8):	Pliki nagłówkowe pxlib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgsf-devel >= 1.14.1

%description devel
Header files for pxlib.

%description devel -l pl.UTF-8
Pliki nagłówkowe pxlib.

%package static
Summary:	Static pxlib library
Summary(pl.UTF-8):	Statyczna biblioteka pxlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static pxlib library.

%description static -l pl.UTF-8
Statyczna biblioteka pxlib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e '/RECODE_LIBDIR=/ s,/lib$,/%{_lib},' configure.ac

%build
#{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--with-gsf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpx.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README doc/*.txt
%attr(755,root,root) %{_libdir}/libpx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpx.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpx.so
%{_includedir}/paradox*.h
%{_includedir}/pxversion.h
%{_pkgconfigdir}/pxlib.pc
%{_mandir}/man3/PX_*.3*
%{_mandir}/man3/pxlib.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpx.a
%endif
