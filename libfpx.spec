#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	FlashPIX OpenSource Toolkit
Summary(pl.UTF-8):	Biblioteka do obróbki obrazków FlashPIX
Name:		libfpx
Version:	1.3.1.10
Release:	1
License:	distributable (see COPYING)
Group:		Libraries
Source0:	http://www.imagemagick.org/download/delegates/%{name}-1.3.1-10.tar.xz
# Source0-md5:	6855850cde24262e3d7fd7b8514d0b1d
Patch0:		%{name}-link.patch
URL:		http://www.imagemagick.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libstdc++-devel >= 3.2.2
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Provides:	fpx
Obsoletes:	fpx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FlashPIX OpenSource Toolkit is based on source obtained from the
Digital Imaging Group Inc. and includes a sample FlashPIX library
implementation contributed by Eastman Kodak Company.

%description -l pl.UTF-8
FlashPIX OpenSource Toolkit jest bazowany na źródłach uzyskanych od
Digital Imaging Group i zawiera przykładową implementację biblioteki
FlashPIX, do której przyczynił się Eastman Kodak Company.

%package devel
Summary:	FlashPIX header file and documentation
Summary(pl.UTF-8):	Plik nagłówkowy i dokumentacja do FlashPIX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	fpx-devel

%description devel
FlashPIX header files and programmer's documentation.

%description devel -l pl.UTF-8
Plik nagłówkowy potrzebny do kompilowania programów korzystających z
biblioteki FlashPIX oraz dokumentacja do tej biblioteki.

%package static
Summary:	FlashPIX static library
Summary(pl.UTF-8):	Statyczna biblioteka FlashPIX
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	fpx-static

%description static
Static version of FlashPIX library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki FlashPIX.

%prep
%setup -q -n %{name}-1.3.1-10
%patch0 -p1

ln -f flashpix.h COPYING

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
%attr(755,root,root) %ghost %{_libdir}/libfpx.so.1

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
