#
# TODO:
# - check the icon & the desktop file

%define		_snap 20040816

Summary:	Multi channel settings manager
Summary(pl):	Zarz±dca ustawieñ wielokana³owych
Name:		xfce-mcs-manager
Version:	4.1.4
Release:	0.%{_snap}.1
License:	LGPL
Group:		X11/Applications
Source0:	http://ep09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	1a0cb66446b73fddb739350e467f86a2
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= 4.1.3
BuildRequires:	libxfcegui4-devel >= 4.1.27
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
Requires:	libxfce4mcs >= 4.1.3
Requires:	libxfcegui4 >= 4.1.27
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-manager is a multi channel settings manager for XFce.

%description -l pl
xfce-mcs-manager to zarz±dca ustawieñ wielokana³owych dla XFce.

%package devel
Summary:	Header file to build xfce-mcs-manager plugins
Summary(pl):	Plik nag³ówkowy do tworzenia wtyczek xfce-mcs-managera
Group:		Development/Libraries
Requires:	libxfce4mcs-devel >= 4.1.3
Requires:	libxfcegui4-devel >= 4.1.27
# doesn't require base

%description devel
Header file for other apps to be able to build their own mcs plugins.

%description devel -l pl
Plik nag³ówkowy umo¿liwiaj±cy innym aplikacjom budowanie wtyczek mcs.

%prep
%setup -q -n %{name}
%patch0 -p1

mv -f po/{fa_IR,fa}.po
mv -f po/{pt_PT,pt}.po

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
%dir %{_sysconfdir}/xfce4

%files devel
%defattr(644,root,root,755)
%{_includedir}/xfce4/xfce-mcs-manager
%{_pkgconfigdir}/*.pc
