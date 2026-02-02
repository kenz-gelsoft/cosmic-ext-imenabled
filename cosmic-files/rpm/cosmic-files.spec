%define debug_package %{nil}
%define _build_id_links none

Name:           cosmic-files-ime
Version:        0.1.0
Release:        1%{?dist}
Summary:        COSMIC File Manager(IME)
Group:          Applications/System

License:        GPLv3+
URL:            https://github.com/pop-os/cosmic-files
Source0:        https://github.com/pop-os/cosmic-files/archive/refs/tags/epoch-1.0.3.tar.gz#/%{name}-%{version}.tar.gz
# もしオフラインビルド用に vendor.tar.gz を作成している場合は Source1 に追加
# Source1:      vendor.tar.gz

# DebianのBuild-Dependsに対応するRPMの依存
BuildRequires:  just
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  gcc-c++

Conflicts:      cosmic-files
Provides:       cosmic-files

%description
The file manager for the COSMIC Desktop Environment.

%prep
%setup -q

%build
export CARGO_HOME=%{?cargo_home}%{!?cargo_home:$HOME/.cargo}
export CARGO_TARGET_DIR=%{?cargo_target_dir}%{!?cargo_target_dir:%{_builddir}/target}
just build-release

%install
# rules の override_dh_auto_install と同様の処理
export CARGO_TARGET_DIR=%{?cargo_target_dir}%{!?cargo_target_dir:%{_builddir}/target}
just rootdir=%{buildroot} install

%files
%{_bindir}/cosmic-*
# これで cosmic-files も cosmic-files-applet も一括で含まれます
%{_datadir}/applications/*.desktop
# パスを scalable ではなく hicolor 以下の全ての svg を拾うように修正
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/metainfo/*.xml

%changelog
* Mon Feb 02 2026 Developer <dev@example.com> - 0.1.0-1
- Optimized for vendored build based on debian/rules
