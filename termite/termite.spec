%global _vte_version 0.56.2.a
%global _util_commit 62faf9e46b8c4ab213ac42aaf6343dea9e2dfc1e

Name:           termite
Version:        15
Release:        3%{?dist}
Summary:        A simple VTE-based terminal

License:        LGPLv2+
URL:            https://github.com/thestinger/termite
Source0:        https://github.com/thestinger/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/thestinger/util/archive/%{_util_commit}.tar.gz
Source2:        https://github.com/thestinger/vte-ng/archive/%{_vte_version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: g++
BuildRequires: gnutls-devel
BuildRequires: gtk-doc
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: libtool
Requires: gnutls
Requires: gtk3
Requires: pcre2
Requires: vte-profile

%description
A keyboard-centric VTE-based terminal, aimed at use within a window manager with tiling and/or
tabbing support.

# hopefully temporary measure
%global debug_package %{nil}

%prep
%autosetup -b 2 -a 1
rmdir util
mv util-%{_util_commit} util
sed -i  -e "s/VERSION =.*/VERSION = %{version}/" \
        -e "s/PREFIX =.*/PREFIX = \\/usr/" \
        Makefile
cd ../vte-ng-%{_vte_version}
echo 'sources: $(BUILT_SOURCES)' >> src/Makefile.am
NOCONFIGURE=1 ./autogen.sh

%build
cd ../vte-ng-%{_vte_version}
./configure \
    --prefix="%{buildroot}/vte-static" \
    --localedir="/usr/share/%{name}/locale" \
    --enable-static \
    --disable-shared \
    enable_introspection=no \
    enable_vala=no \
    --disable-gtk-doc \
    --disable-glade-catalogue
make -C src sources install-exec install-data -j 1 # makefile bug does not allow -j
make install-pkgconfigDATA
cd ../%{name}-%{version}
export PKG_CONFIG_PATH="%{buildroot}/vte-static/lib/pkgconfig"
%make_build

%install
%make_install

%check


%files
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man*/%{name}*
%{_datadir}/terminfo/x/xterm-%{name}
%doc README.rst

%changelog
* Wed Sep 04 2019 Peter Mann <pm@xdd.sk> - 15-3
- Initial package
