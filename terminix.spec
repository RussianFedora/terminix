Summary:	A tiling terminal emulator based on GTK+ 3
Name:		terminix
Version:	0.52.1
Release:	1%{dist}

License:	MPLv2.0
Group:		User Interface/Desktops
URL:		http://github.com/gnunn1/terminix
Source0:	https://github.com/gnunn1/%{name}/releases/download/%{version}/terminix.zip

%description
A tiling terminal emulator

%prep

%build

%install
unzip -q -x -d %{buildroot} %{SOURCE0}
strip -p %{buildroot}%{_bindir}/%{name}

sed -i 's@Categories.*@Categories=GNOME;GTK;System;TerminalEmulator;@g' \
	%{buildroot}%{_datadir}/applications/com.gexperts.Terminix.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/com.gexperts.Terminix.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/com.gexperts.Terminix.gschema.xml
%{_datadir}/nautilus-python/extensions/
%{_datadir}/%{name}

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%changelog
* Thu Mar 10 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.52.1-1.R
- update to 0.52.1

* Fri Mar  4 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.51.0-1.R
- Initial package.

