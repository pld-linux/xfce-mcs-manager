Summary: 	Multi channel settings manager
Summary(pl):	Zarządca ustawień wielokanałowych
Name: 		xfce-mcs-manager
Version: 	3.99.2
Release: 	1
License:	LGPL
Group: 		X11/Applications
Source0: 	http://linux.imp.mx/xfce4/rc2/xfce4-rc2/src/%{name}-%{version}.tar.gz
# Source0-md5:	406f84f0ced5bc5a41e49fd060f08895
URL: 		http://www.xfce.org/
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= 3.99.2
BuildRequires: 	libxfcegui4-devel >= 3.99.2
BuildRequires:	pkgconfig >= 0.9.0
Requires:	libxfce4mcs >= 3.99.2
Requires:	libxfcegui4 >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-manager is a multi channel settings manager for xfce4.

%description -l pl
xfce-mcs-manager to zarządca ustawień wielokanałowych dla xfce4.

%package devel
Summary:	Header file to build xfce-mcs-manager plugins
Summary(pl):	Plik nagłówkowy do tworzenia wtyczek xfce-mcs-managera
Group:		Development/Libraries
Requires:	libxfce4mcs-devel >= 3.91.0
Requires: 	libxfcegui4-devel >= 3.91.0
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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins

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

%files devel
%defattr(644,root,root,755)
%{_includedir}/xfce4/xfce-mcs-manager
%{_pkgconfigdir}/*.pc
