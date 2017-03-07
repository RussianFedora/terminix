Summary:	A tiling terminal emulator based on GTK+ 3
Name:		terminix
Version:	1.5.2
Release:	1%{dist}

License:	MPLv2.0
Group:		User Interface/Desktops
URL:		http://github.com/gnunn1/terminix
Source0:	https://github.com/gnunn1/terminix/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	com.gexperts.Terminix.gschema.override

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ldc >= 1.1.1
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtkd-3)
BuildRequires:	pkgconfig(vted-3)
BuildRequires:	pkgconfig(x11)

%description
A tiling terminal emulator. This is binary repack for x86_64 from
https://github.com/gnunn1/terminix/releases

%prep
%autosetup

%build
find po -name "*\.po" -printf "%f\\n" | sed "s/\.po//g" | sort > po/LINGUAS
autoreconf -fi
%configure
%make_build

%install
%make_install

install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/glib-2.0/schemas/

sed -i 's@Categories.*@Categories=GNOME;GTK;System;TerminalEmulator;@g' \
	%{buildroot}%{_datadir}/applications/com.gexperts.Terminix.desktop

mv %{buildroot}%{_datadir}/metainfo %{buildroot}%{_datadir}/appdata
chmod +x %{buildroot}%{_datadir}/%{name}/scripts/terminix_int.sh

%find_lang %{name}

%post
update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
  /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%license LICENSE
%doc README.md CREDITS.md 
%{_bindir}/%{name}
%{_datadir}/applications/com.gexperts.Terminix.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/com.gexperts.Terminix.gschema.xml
%{_datadir}/glib-2.0/schemas/com.gexperts.Terminix.gschema.override
%{_datadir}/nautilus-python/extensions/
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/com.gexperts.Terminix*
%{_datadir}/appdata/com.gexperts.Terminix.appdata.xml
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Mar  7 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 1.5.2-1
- update to 1.5.2
- build from sources for Fedora 26+

* Wed Jan 18 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 1.4.2-1
- update to 1.4.2

* Wed Oct 12 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 1.3.0-1
- update to 1.3.0

* Tue Sep 13 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 1.2.0-1
- update to 1.2.0

* Mon Jun 27 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 1.0.0-1
- update to 1.0.0

* Wed Apr 13 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.57.0-1.R
- update 0.57.0

* Tue Apr  5 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.56.0-1.R
- update to 0.56.0

* Fri Apr  1 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.55.0-1.R
- update to 0.55.0

* Fri Mar 11 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.52.1-4.R
- use override file

* Fri Mar 11 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.52.1-3.R
- use dark theme by default
- use Ctrl+` shortcut to view side bar
- disable menu accelerator

* Thu Mar 10 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.52.1-2.R
- binary build exist only for x86_64

* Thu Mar 10 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.52.1-1.R
- update to 0.52.1

* Fri Mar  4 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.51.0-1.R
- Initial package.

