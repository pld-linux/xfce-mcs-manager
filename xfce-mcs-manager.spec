#
# TODO:
# - check the icon & the desktop file

Summary:	Multi channel settings manager
Summary(pl):	Zarz±dca ustawieñ wielokana³owych
Name:		xfce-mcs-manager
Version:	4.2.1
Release:	1
License:	LGPL v2
Group:		X11/Applications
Source0:        http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	72b68d04bd5ec76fd0a147f824ee049c
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-manager is a multi channel settings manager for Xfce.

%description -l pl
xfce-mcs-manager to zarz±dca ustawieñ wielokana³owych dla Xfce.

%package devel
Summary:	Header file to build xfce-mcs-manager plugins
Summary(pl):	Plik nag³ówkowy do tworzenia wtyczek xfce-mcs-managera
Group:		Development/Libraries
Requires:	libxfce4mcs-devel >= %{version}
Requires:	libxfcegui4-devel >= %{version}
# doesn't require base

%description devel
Header file for other apps to be able to build their own mcs plugins.

%description devel -l pl
Plik nag³ówkowy umo¿liwiaj±cy innym aplikacjom budowanie wtyczek mcs.

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
#%lang(fr) %{_datadir}/xfce4/doc/fr
#%lang(it) %{_datadir}/xfce4/doc/it

# common for some other xfce* packages
%dir %{_sysconfdir}/xdg/xfce4

%files devel
%defattr(644,root,root,755)
%{_includedir}/xfce4/xfce-mcs-manager
%{_pkgconfigdir}/*.pc
