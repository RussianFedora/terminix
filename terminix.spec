Summary:	A tiling terminal emulator based on GTK+ 3
Name:		terminix
Version:	1.0.0
Release:	1%{dist}

License:	MPLv2.0
Group:		User Interface/Desktops
URL:		http://github.com/gnunn1/terminix
Source0:	https://github.com/gnunn1/%{name}/releases/download/%{version}/terminix.zip
Source1:	com.gexperts.Terminix.gschema.override

ExclusiveArch:	x86_64

%description
A tiling terminal emulator. This is binary repack for x86_64 from
https://github.com/gnunn1/terminix/releases

%prep

%build

%install
unzip -q -x -d %{buildroot} %{SOURCE0}
strip -p %{buildroot}%{_bindir}/%{name}
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/glib-2.0/schemas/

sed -i 's@Categories.*@Categories=GNOME;GTK;System;TerminalEmulator;@g' \
	%{buildroot}%{_datadir}/applications/com.gexperts.Terminix.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/com.gexperts.Terminix.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/com.gexperts.Terminix.gschema.xml
%{_datadir}/glib-2.0/schemas/com.gexperts.Terminix.gschema.override
%{_datadir}/nautilus-python/extensions/
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/com.gexperts.Terminix.png
%{_datadir}/appdata/com.gexperts.Terminix.appdata.xml

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

%changelog
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

