Summary:	FlashPIX OpenSource Toolkit
Summary(pl):	Biblioteka do obrÛbki obrazkÛw FlashPIX
Name:		fpx
Version:	1.2.0
Release:	3
License:	distributable (see COPYING for details)
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
# Strange... [URL] says you can order it (for money) and doesn't contain any
# link, but sources can be freely redistributed. Can be found on any IM mirror.
Source0:	ftp://ftp.simplesystems.org/pub/ImageMagick/delegates/%{name}-%{version}.tar.gz
Patch0:		%{name}-wchar-conflict.patch
Patch1:		%{name}-swap.patch
Patch2:		%{name}-statfs.patch
Patch3:		%{name}-shared.patch
Patch4:		%{name}-nolibrt.patch
URL:		http://www.digitalimaging.org/i_flashpix.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FlashPIX OpenSource Toolkit is based on source obtained from the
Digital Imaging Group Inc. and includes a sample FlashPIX library
implementation contributed by Eastman Kodak Company.

%description -l pl
FlashPIX OpenSource Toolkit jest bazowany na ºrÛd≥ach uzyskanych od
Digital Imaging Group i zawiera przyk≥adow± implementacjÍ biblioteki
FlashPIX, do ktÛrej przyczyni≥ siÍ Eastman Kodak Company.

%package devel
Summary:	FlashPIX header file and documentation
Summary(pl):	Plik nag≥Ûwkowy i dokumentacja do FlashPIX
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
FlashPIX header files and programmer's documentation.

%description devel -l pl
Plik nag≥Ûwkowy potrzebny do kompilowania programÛw korzystaj±cych z
biblioteki FlashPIX oraz dokumentacja do tej biblioteki.

%package static
Summary:	FlashPIX static library
Summary(pl):	Statyczna biblioteka FlashPIX
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static version of FlashPIX library.

%description static -l pl
Statyczna wersja biblioteki FlashPIX.

%prep
%setup -q -n lib%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
mv -f oless/h/wchar.h oless/h/owchar.h

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS COPYING ChangeLog NEWS README doc/readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.pdf doc/*.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
