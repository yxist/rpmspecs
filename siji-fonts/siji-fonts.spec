%global _git_commit c691f200c1c66e76daa2afc9cbbd1aa39045c906
%global fontname siji

# Font catalog
%global catalog %{_sysconfdir}/X11/fontpath.d

Name:           %{fontname}-fonts
Version:        20190218git
Release:        2%{?dist}
Summary:        Iconic bitmap font based on stlarch with additional glyphs

License:        GPLv2
URL:            https://github.com/stark/siji
Source0:        https://github.com/stark/siji/archive/%{_git_commit}.zip
Source1:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  /usr/bin/mkfontdir
BuildRequires:  libappstream-glib
	
Requires:       fontpackages-filesystem


%description


%prep
%autosetup -n %{fontname}-%{_git_commit}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p pcf/*.pcf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{catalog}
ln -s %{_fontdir} %{buildroot}%{catalog}/%{fontname}:unscaled
/usr/bin/mkfontdir %{buildroot}%{_fontdir}

# Add AppStream metadata file
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg *.pcf

%license LICENSE
%doc Readme.md
%{catalog}/%{fontname}:unscaled
%{_fontdir}/fonts.dir
%{_datadir}/metainfo/%{fontname}.metainfo.xml


%changelog
* Fri Sep 06 2019 Peter Mann <pm@xdd.sk> - 20190218git-2
- Make font discoverable by Xorg

* Fri Sep 06 2019 Peter Mann <pm@xdd.sk> - 20190218git-1
- Initial package
