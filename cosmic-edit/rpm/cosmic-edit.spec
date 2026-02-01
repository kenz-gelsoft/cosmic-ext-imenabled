%define debug_package %{nil}
%define _build_id_links none

Name:           cosmic-edit-ime
Version:        0.1.0
Release:        1%{?dist}
Summary:        COSMIC text editor(IME)
License:        GPLv3
URL:            https://github.com/kenz-gelsoft/cosmic-edit
Source0:        https://github.com/kenz-gelsoft/cosmic-edit/archive/refs/heads/backport-input-method.tar.gz#/%{name}-%{version}.tar.gz

# DebianのBuild-Dependsに対応するRPMの依存
BuildRequires:  just
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  gcc-c++

Conflicts:      cosmic-edit
Provides:       cosmic-edit

%description
COSMIC Edit is a multi-window text editor for the COSMIC Desktop Environment,
built using the iced GUI library and the cosmic-text shaping engine.

%prep
%setup -q

%build
just build-release

%install
# Debianのdh_auto_install相当
just rootdir=%{buildroot} install


# デバッグ情報パッケージの生成でエラーが出る場合は以下を有効に（任意）
# %define debug_package %{nil}

%files
%{_bindir}/cosmic-edit
%{_datadir}/applications/*.desktop
# パスを scalable ではなく hicolor 以下の全ての svg を拾うように修正
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/metainfo/*.xml

%changelog
* Sat Jan 31 2026 Your Name <you@example.com> - 0.1.0-1
- Initial RPM build using just and AlmaLinux 10
