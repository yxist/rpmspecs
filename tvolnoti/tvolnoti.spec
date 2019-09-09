%global _git_commit 4dd4c7edc68d629bcb12d3b1d12d7296e8c889b5

Name:           tvolnoti
Version:        20160801git
Release:        1%{?dist}
Summary:        Lightweight volume notification for Linux (with skin support) 

License:        GPLv3
URL:            https://github.com/LightAir/tvolnoti
Source0:        https://github.com/LightAir/tvolnoti/archive/%{_git_commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-2.0)
Requires: dbus
Requires: dbus-glib
Requires: gtk2

%description
Volnoti is a lightweight volume notification daemon for GNU/Linux and other POSIX operating
systems. It is based on GTK+ and D-Bus and should work with any sensible window manager.
The original aim was to create a volume notification daemon for lightweight window managers like
LXDE or XMonad. It is known to work with a wide range of WMs, including GNOME, KDE, Xfce, LXDE,
XMonad, i3 and many others. The source code is heavily based on the GNOME notification-daemon.

This fork adds some additional options to the original volnoti program and adds theme support


%prep
%autosetup -n %{name}-%{_git_commit}


%build
%configure
%make_build


%install
%make_install


%check


%files
%{_bindir}/volnoti*
%{_datadir}/pixmaps/tvolnoti/*
%license COPYING
%doc README.md


%changelog

