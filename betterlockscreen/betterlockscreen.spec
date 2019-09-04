Name:           betterlockscreen
Version:        3.0.1
Release:        1%{?dist}
Summary:        A nice i3lock-color wrapper

License:        MIT
URL:            https://github.com/pavanjadhaw/betterlockscreen
Source0:        https://github.com/pavanjadhaw/betterlockscreen/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       ImageMagick
Requires:       bash
Requires:       bc
Requires:       feh
Requires:       i3lock-color
Requires:       xorg-x11-utils
Requires:       xorg-x11-server-utils

%description
The script takes image adds various effects and caches those images in special directory and then
uses those images as lockscreen background depending on argument provided by user.

%global debug_package %{nil}

%prep
%autosetup

%build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%check

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md examples

%changelog
* Wed Sep 04 2019 Peter Mann <pm@xdd.sk> - 3.0.1-1
- Initial package
