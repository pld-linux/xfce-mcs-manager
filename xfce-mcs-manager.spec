Summary:	Multi channel settings manager
Summary(pl):	Zarządca ustawień wielokanałowych
Name:		xfce-mcs-manager
Version:	4.0.5
Release:	1
License:	LGPL
Group:		X11/Applications
#Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	7b56465800c3c5665caf5c48f21f5087
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-manager is a multi channel settings manager for XFce.

%description -l pl
xfce-mcs-manager to zarządca ustawień wielokanałowych dla XFce.

%package devel
Summary:	Header file to build xfce-mcs-manager plugins
Summary(pl):	Plik nagłówkowy do tworzenia wtyczek xfce-mcs-managera
Group:		Development/Libraries
Requires:	libxfce4mcs-devel >= %{version}
Requires:	libxfcegui4-devel >= %{version}
# doesn't require base

%description devel
Header file for other apps to be able to build their own mcs plugins.

%description devel -l pl
Plik nagłówkowy umożliwiający innym aplikacjom budowanie wtyczek mcs.

%prep
%setup -q

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
cp -f /usr/share/automake/config.sub .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/xfce4/mcs-plugins,%{_sysconfdir}/xfce4}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/xfce4
%dir %{_libdir}/xfce4/mcs-plugins
%docdir %{_datadir}/xfce4/doc
%dir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C
%lang(fr) %{_datadir}/xfce4/doc/fr
# common for some other xfce* packages
%dir %{_sysconfdir}/xfce4

%files devel
%defattr(644,root,root,755)
%{_includedir}/xfce4/xfce-mcs-manager
%{_pkgconfigdir}/*.pc
