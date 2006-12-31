#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	FlashPIX OpenSource Toolkit
Summary(pl):	Biblioteka do obróbki obrazków FlashPIX
Name:		libfpx
Version:	1.2.0.13
Release:	2
License:	distributable (see COPYING)
Group:		Libraries
# Strange... [URL] says you can order it (for money) and doesn't contain any
# link, but sources can be freely redistributed. Can be found on any IM mirror.
Source0:	ftp://ftp.simplesystems.org/pub/ImageMagick/delegates/%{name}-%{version}.tar.bz2
# Source0-md5:	5e781a17ec96e8f9af8c2ff319e8d706
URL:		http://www.i3a.org/i_flashpix.html
BuildRequires:	autoconf >= 2.55
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libstdc++-devel >= 3.2.2
Provides:	fpx
Obsoletes:	fpx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FlashPIX OpenSource Toolkit is based on source obtained from the
Digital Imaging Group Inc. and includes a sample FlashPIX library
implementation contributed by Eastman Kodak Company.

%description -l pl
FlashPIX OpenSource Toolkit jest bazowany na ¼ród³ach uzyskanych od
Digital Imaging Group i zawiera przyk³adow± implementacjê biblioteki
FlashPIX, do której przyczyni³ siê Eastman Kodak Company.

%package devel
Summary:	FlashPIX header file and documentation
Summary(pl):	Plik nag³ówkowy i dokumentacja do FlashPIX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	fpx-devel

%description devel
FlashPIX header files and programmer's documentation.

%description devel -l pl
Plik nag³ówkowy potrzebny do kompilowania programów korzystaj±cych z
biblioteki FlashPIX oraz dokumentacja do tej biblioteki.

%package static
Summary:	FlashPIX static library
Summary(pl):	Statyczna biblioteka FlashPIX
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	fpx-static

%description static
Static version of FlashPIX library.

%description static -l pl
Statyczna wersja biblioteki FlashPIX.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-fast-install \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libfpx.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.pdf doc/readme.txt
%attr(755,root,root) %{_libdir}/libfpx.so
%{_libdir}/libfpx.la
%{_includedir}/fpxlib.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfpx.a
%endif
