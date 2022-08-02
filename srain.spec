Name:           srain
Version:        1.4.1
Release:        1
Summary:        Modern IRC client written in GTK+ 3
License:        GPLv3+, GPLv2+ and BSD
URL:            https://srain.im/
Source0:        https://github.com/SrainApp/srain/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  glib-networking
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  python3dist(sphinx)
 
Requires:       hicolor-icon-theme
Requires:       glib-networking

%description
Modern IRC client written in GTK
 
%prep
%autosetup -p1 -n %{name}-%{version}
 
%build
%meson

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.rst
#{_datadir}/doc/srain/html/
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml
%{_sysconfdir}/%{name}
#{_mandir}/man1/srain.1.*
