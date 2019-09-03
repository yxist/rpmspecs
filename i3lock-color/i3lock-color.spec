Name:		i3lock-color
Version:	2.12.c
Release:	1%{?dist}
Summary:	Improved improved screen locker - "the ricing fork of i3lock"
License:	BSD
URL:		https://github.com/PandorasFox/i3lock-color
Source0:	https://github.com/PandorasFox/i3lock-color/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Conflicts:	i3lock

BuildRequires:	pkg-config
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	gcc

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)

BuildRequires:	libev-devel
BuildRequires:	pam-devel

%description
i3lock is a simple screen locker like slock. After starting it, you will see a white screen
(you can configure the color/an image). You can return to your screen by entering your
password. This fork allows color configuration.

%prep
%autosetup

%build
autoreconf -i
%configure
#make %{?_smp_mflags}
%make_build -C *-redhat-linux-gnu CFLAGS+="-U_FORTIFY_SOURCE"

%install
%make_install

%files
%doc CHANGELOG README* lock_bar.sh lock.sh
%license LICENSE
%{_bindir}/i3lock
%{_sysconfdir}/pam.d/i3lock
%{_mandir}/man1/i3lock.*

%changelog
* Thu Nov 15 2018 Greg Wildman <greg@techno.co.za> - 2.12.c-1
- Initial spec
