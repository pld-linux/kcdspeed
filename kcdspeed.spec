Summary:	A KDE little Kicker applet that allows selecting CD-ROM speed
Summary(pl.UTF-8):	Aplet do kontrolowania prędkości CD-ROM-u z panelu KDE
Name:		kcdspeed
Version:	0.8
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://kcdspeed.riadoklan.sk/data/%{name}-%{version}.tar.gz
# Source0-md5:	ead045707dfa8f28fdbdeb8224fd3130
URL:		http://kcdspeed.riadoklan.sk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdebase-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE little Kicker applet that allows selecting CD-ROM speed, eject
and close CD-ROM tray, and mount and unmount disc.

%description -l pl.UTF-8
Aplet do kontrolowania prędkości CD-ROM-u, wysuwania i zamykania
szuflady CD-ROM-u, montowania i odmontowania płytki z panelu KDE.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/*.so
# *.la are required
%{_libdir}/*.la
%{_datadir}/apps/kicker/applets/%{name}.desktop
