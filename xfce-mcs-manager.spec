Summary: 	Multi channel settings manager
Name: 		xfce-mcs-manager
Version: 	3.90.0
Release: 	0.1
License:	LGPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	c28f72c5fbec2321aae1139943e2b5cf
Group: 		X11/Applications
Requires:	libxfce4mcs >= 3.90.0
Requires:	libxfcegui4 >= 3.90.0
BuildRequires:	libxfce4mcs-devel >= 3.90.0
BuildRequires: 	libxfcegui4-devel >= 3.90.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-mcs-manager is a multi channel settings manager for xfce4

%package devel
Summary:	header file to build xfce-mcs-manager plugins
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for other apps to be able to build their own mcs plugins.

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
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL TODO COPYING AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xfce4/doc/
%{_datadir}/locale/

%files devel
%defattr(644,root,root,755)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/xfce-mcs-manager
