#
# TODO:
# - check the icon & the desktop file

Summary:	Multi channel settings manager
Summary(pl):	Zarządca ustawień wielokanałowych
Name:		xfce-mcs-manager
Version:	4.1.99.3
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7ff0224f1bb2312553947a17e5e20d98
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-manager is a multi channel settings manager for Xfce.

%description -l pl
xfce-mcs-manager to zarządca ustawień wielokanałowych dla Xfce.

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
%patch0 -p1

mv -f po/{pt_PT,pt}.po
mv -f po/{nb_NO,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/xfce4/mcs-plugins,%{_sysconfdir}/xdg/xfce4}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/hicolor/48x48/apps/xfce4-settings.png
%{_desktopdir}/*.desktop

%dir %{_libdir}/xfce4
%dir %{_libdir}/xfce4/mcs-plugins

%docdir %{_datadir}/xfce4/doc
%dir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C
%lang(fr) %{_datadir}/xfce4/doc/fr
%lang(it) %{_datadir}/xfce4/doc/it

# common for some other xfce* packages
%dir %{_sysconfdir}/xdg/xfce4

%files devel
%defattr(644,root,root,755)
%{_includedir}/xfce4/xfce-mcs-manager
%{_pkgconfigdir}/*.pc
