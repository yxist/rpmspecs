%global fontname termsyn
%global fontconf 64-%{fontname}.conf

# Font catalog
%global catalog %{_sysconfdir}/X11/fontpath.d

Name:           %{fontname}-fonts
Version:        1.8.7
Release:        2%{?dist}
Summary:        Monospaced font based on terminus and tamsyn

License:        GPLv2
URL:            https://sourceforge.net/projects/termsyn
Source0:        https://downloads.sourceforge.net/project/%{fontname}/%{fontname}-%{version}.tar.gz
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:	/usr/bin/mkfontdir
BuildRequires:  libappstream-glib
	
Requires:       fontpackages-filesystem


%description


%prep
%autosetup -n %{fontname}-%{version}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.pcf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


install -m 0755 -d %{buildroot}%{catalog}
ln -s %{_fontdir} %{buildroot}%{catalog}/%{fontname}:unscaled
/usr/bin/mkfontdir %{buildroot}%{_fontdir}

# Add AppStream metadata file
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.pcf

%doc README.termsyn
%{catalog}/%{fontname}:unscaled
%{_fontdir}/fonts.dir
%{_datadir}/metainfo/%{fontname}.metainfo.xml


%changelog
* Sun Sep 08 2019 Peter Mann <pm@xdd.sk> - 1.8.7-2
- Make font discoverable by Xorg

* Sun Sep 08 2019 Peter Mann <pm@xdd.sk> - 1.8.7-1
- Initial package
