Name:           srain
Version:        1.1.3
Release:        1
Summary:        Modern IRC client written in GTK+ 3
License:        GPLv3+, GPLv2+ and BSD
URL:            https://srain.im/
Source0:        https://github.com/SrainApp/srain/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  intltool
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(openssl)
 
Requires:       hicolor-icon-theme

%description
Modern IRC client written in GTK
 
%prep
%autosetup -p1 -n %{name}-%{version}
 
%build
%configure

%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.rst
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml
%{_sysconfdir}/%{name}
