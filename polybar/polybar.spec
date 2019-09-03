%global         _i3ipcpp_ver  0.7.1
%global         _xpp_ver 1.4.0

Name:           polybar
Version:        3.4.0
Release:        1%{?dist}
Summary:        A fast and easy-to-use status bar
License:        MIT
URL:            https://github.com/jaagr/polybar
Source0:        https://github.com/jaagr/polybar/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	    https://github.com/jaagr/i3ipcpp/archive/v0.7.1.tar.gz#/i3ipcpp-%{_i3ipcpp_ver}.tar.gz
Source2:	    https://github.com/jaagr/xpp/archive/1.4.0.tar.gz#/xpp-%{_xpp_ver}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  python2 >= 2.6
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xrm)

%description
The main purpose of Polybar is to help users create awesome status bars.
It aims to help users build beautiful and highly customizable status bars
for their desktop environment.

%prep
%setup 
tar xzf %{SOURCE1} -C lib/i3ipcpp --strip-components 1
tar xzf %{SOURCE2} -C lib/xpp --strip-components 1
%patch0 -p1
%patch1 -p1

%build
mkdir build
cmake . 
%make_build 

%install
install -Dm755 bin/polybar      %{buildroot}%{_bindir}/polybar
install -Dm755 bin/polybar-msg  %{buildroot}%{_bindir}/polybar-msg
install -Dm755 doc/config       %{buildroot}%{_datadir}/doc/polybar/config
install -Dm755 doc/bash/polybar %{buildroot}%{_datadir}/bash-completion/completions/polybar
install -Dm755 doc/zsh/_polybar %{buildroot}%{_datadir}/zsh/site-functions/_polybar
install -Dm755 doc/zsh/_polybar %{buildroot}%{_datadir}/zsh/site-functions/_polybar_msg
install -Dm755 man/polybar.1    %{buildroot}%{_mandir}/man1/polybar.1

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%{_bindir}/polybar*
%{_datadir}/bash-completion/completions/polybar
%{_datadir}/doc/polybar/config
%{_datadir}/zsh/site-functions/_polybar*
%{_mandir}/man1/polybar.*

%changelog
* Wed Sep 04 2019 Peter Mann <pm@xdd.sk> 3.4.0-1
- Updated version


* Thu Nov 15 2018 Greg Wildman <greg@techn.co.za> 3.2.1-1
- Updated version
- Clean up spec file

* Tue Jul 24 2018 Spencer <morecode@teknik.io>
- 

