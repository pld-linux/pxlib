
# TODO:
# - manual pages generation (missing docbook-to-man tool)

Summary:	A library to read Paradox DB files
Name:		pxlib
Version:	0.4.3
Release:	1
Epoch:		0
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/pxlib/%{name}-%{version}.tar.gz
# Source0-md5:	1155f6704ca05c4cb6af000dd6cb5787
URL:		http://pxlib.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxlib is a simply and still small C library to read Paradox DB files.
It supports all versions starting from 3.0. It currently has a very
limited set of functions like to open a DB file, read its header and
read every single record.

%package devel
Summary:	Header files and develpment documentation for pxlib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
pxlib is a simply and still small C library to read Paradox DB files.
It supports all versions starting from 3.0. It currently has a very
limited set of functions like to open a DB file, read its header and
read every single record.

%package static
Summary:	Static pxlib library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
pxlib is a simply and still small C library to read Paradox DB files.
It supports all versions starting from 3.0. It currently has a very
limited set of functions like to open a DB file, read its header and
read every single record.

%prep
%setup -q

%build
%configure
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
