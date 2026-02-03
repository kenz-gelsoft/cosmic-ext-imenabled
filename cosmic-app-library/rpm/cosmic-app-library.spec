%define debug_package %{nil}
%define _build_id_links none

Name:           cosmic-app-library-ime
Version:        0.1.0
Release:        1%{?dist}
Summary:        COSMIC App Library(IME)
Group:          Applications/System

License:        GPLv3+
URL:            https://github.com/pop-os/cosmic-applibrary
Source0:        https://github.com/pop-os/cosmic-applibrary/archive/refs/tags/epoch-1.0.3.tar.gz#/%{name}-%{version}.tar.gz

# DebianのBuild-Dependsに対応するRPMの依存
BuildRequires:  just
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  gcc-c++

Conflicts:      cosmic-app-library
Provides:       cosmic-app-library

%description
The App Library for the COSMIC Desktop Environment.
It provides a categorized view of all installed applications.

%prep

%build

%install
# debian/rules の override_dh_install に準拠
export CARGO_TARGET_DIR=%{?cargo_target_dir}%{!?cargo_target_dir:%{_builddir}/target}
just rootdir=%{buildroot} install

%files
%{_bindir}/cosmic-app-library
%{_datadir}/applications/*.desktop
# パスを scalable ではなく hicolor 以下の全ての svg を拾うように修正
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/metainfo/*.xml

%changelog
* Mon Feb 02 2026 Developer <dev@example.com> - 0.1.0-1
- Initial RPM release for cosmic-app-library
