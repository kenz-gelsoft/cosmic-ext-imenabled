%define debug_package %{nil}
%define _build_id_links none

Name:           cosmic-term-ime
Version:        0.1.0
Release:        1%{?dist}
Summary:        COSMIC Terminal Emulator(IME)
Group:          Applications/System

License:        GPLv3+
URL:            https://github.com/kenz-gelsoft/cosmic-term
Source0:        https://github.com/kenz-gelsoft/cosmic-term/archive/refs/heads/backport-input-method.tar.gz#/%{name}-%{version}.tar.gz

# DebianのBuild-Dependsに対応するRPMの依存
BuildRequires:  just
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  gcc-c++

Conflicts:      cosmic-term
Provides:       cosmic-term

%description
The terminal emulator for the COSMIC Desktop Environment,
built with the Iced GUI library and the Alacritty terminal backend.

%prep
%setup -q

%build
export CARGO_HOME=%{?cargo_home}%{!?cargo_home:$HOME/.cargo}
just build-release

%install
# DESTDIR を指定してインストール
just rootdir=%{buildroot} install

%files
%{_bindir}/cosmic-term
%{_datadir}/applications/*.desktop
# パスを scalable ではなく hicolor 以下の全ての svg を拾うように修正
%{_datadir}/icons/hicolor/*/apps/*.svg
# その他、必要に応じてマニュアルやメタデータを追加
%{_datadir}/metainfo/*.xml

%changelog
* Sun Feb 01 2026 Developer <dev@example.com> - 0.1.0-1
- Initial RPM release based on Debian control file
