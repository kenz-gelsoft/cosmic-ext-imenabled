# IME enabled COSMIC Apps for Pop!_OS 24.04/Fedora

(ja: [日本語の説明はこちら](#cosmic-アプリ-日本語入力対応版リポジトリ))

**NEWS!**: Now there are RPM packages for Fedora.

This is **unofficial** APT/YUM repo. **Don't report bugs or issues to official** repos.

Since [COSMIC apps do not currently support IME](https://github.com/pop-os/cosmic-epoch/issues/2174), there are issues inputting characters for languages that require an IME, such as Japanese, Chinese, and Korean.

While the latest version of the **iced** toolkit (which COSMIC apps use) has implemented IME support, ~~it is expected to take several months before COSMIC apps officially adopt this latest version. Therefore, I have backported the IME support in advance to enable IME functionality for specific apps.~~

Now, [COSMIC apps are getting rebased onto the latest iced toolkit](https://github.com/pop-os/libcosmic/issues/1089), so this repo publishes WIP test builds that have minimum IME functionality for specific apps.

![](screenshots/term.png)

## Supported COSMIC Apps

[How to install](#how-to-install) (ja: [インストール方法](#インストール方法)).

|Package Name|Upstream Version|Fork or Patch|
|-|-|-|
|cosmic-term-**ime**|[f62abce@master](https://github.com/pop-os/cosmic-term/commit/f62abcea4efbcd824297b269279826699c47d335)|[Fork](https://github.com/pop-os/cosmic-term/compare/master...kenz-gelsoft:cosmic-term:minimal-input-method-support?expand=1)|
|cosmic-edit-**ime**|[6326f65@master](https://github.com/pop-os/cosmic-edit/commit/6326f65d84cd696dceb5c31ebb63842cd756051d)|[Fork](https://github.com/pop-os/cosmic-edit/compare/master...kenz-gelsoft:cosmic-edit:minimal-input-method-support?expand=1)|
|cosmic-files-**ime**|[49d353d@master](https://github.com/pop-os/cosmic-files/commits/master/)|[Patched `libcosmic`](https://github.com/pop-os/libcosmic/compare/master...kenz-gelsoft:libcosmic:minimal-input-method-support)|
|cosmic-launcher-**ime**|[a3d950b@master](https://github.com/pop-os/cosmic-launcher/commits/master/)|[Patched `libcosmic`](https://github.com/pop-os/libcosmic/compare/master...kenz-gelsoft:libcosmic:minimal-input-method-support)|
|cosmic-app-library-**ime**|[08ab631@master](https://github.com/pop-os/cosmic-app-library/commits/master/)|[Patched `libcosmic`](https://github.com/pop-os/libcosmic/compare/master...kenz-gelsoft:libcosmic:minimal-input-method-support)|

## Screenshots

### cosmic-term-ime
![](screenshots/term.png)

### cosmic-edit-ime
![](screenshots/edit.png)

### cosmic-files-ime
![](screenshots/files.png)

### cosmic-launcher-ime
![](screenshots/launcher.png)

### cosmic-app-library-ime
![](screenshots/app-library.png)

---

## How to Install

### for Pop!_OS 24.04

Add this public APT repository to your `/etc/apt/sources.list` and run `apt update`.

```shell
$ sudo sh -c "cat << EOF >> /etc/apt/sources.list
deb [trusted=yes] https://kenz-gelsoft.github.io/cosmic-ext-imenabled stable main
EOF"

$ sudo apt update
```

You can now install the desired apps via `apt install`. For example:

```shell
$ sudo apt install cosmic-term-ime
```

### for Fedora

Add this public YUM repository to your `/etc/yum.repos.d/*.repo`.

```shell
$ sudo sh -c "cat << EOF > /etc/yum.repos.d/cosmic-ext-imenabled.repo
[cosmic-ext-imenabled]
name=IME Enabled COSMIC Apps Repository
baseurl=https://kenz-gelsoft.github.io/cosmic-ext-imenabled
enabled=1
gpgcheck=0
EOF"
```

You can now install the desired apps via `dnf install --allowerasing`. For example:

```shell
$ sudo dnf install --allowerasing cosmic-term-ime
```

---

Following is Japanese translation.

# COSMIC アプリ 日本語入力対応版リポジトリ

これは**非公式** APT/YUM リポジトリです。不具合や問題を**公式リポジトリに報告しないでください**。

[COSMIC アプリは IME に非対応](https://github.com/pop-os/cosmic-epoch/issues/2174)のため、日本語・中国語・韓国語などの IME を必要とする言語の文字入力に問題があります。

COSMIC アプリが使っている **iced** ツールキットは最新版にて IME サポートが実装されましたが、~~COSMIC アプリが iced ツールキットの最新版を採用するにはまだ数ヶ月かかる見込みであるため、先行して IME サポートのみをバックポートして一部のアプリのみ IME が動作するようにしました。~~

現在、[COSMIC アプリは最新版の iced ツールキットに切り替わりつつあります。](https://github.com/pop-os/libcosmic/issues/1089)そこで、このリポジトリではいくつかのアプリについて最低限の IME 機能をもたせた作業中のテストビルドを公開しています。

## 対応済みの COSMIC アプリ

[こちら](#supported-cosmic-apps)

---

## インストール方法

### Pop!_OS 24.04

`/etc/apt/sources.list` にこのリポジトリから公開されている apt リポジトリを追加し、`apt update` します。
```shell
$ sudo sh -c "cat << EOF >> /etc/apt/sources.list
deb [trusted=yes] https://kenz-gelsoft.github.io/cosmic-ext-imenabled stable main
EOF"

$ sudo apt update
```

入れたいアプリを `apt install` できるようになります。例：
```shell
$ sudo apt install cosmic-term-ime
```

### Fedora

`/etc/apt/yum.repos.d/*.repo` にこのリポジトリから公開されている yum リポジトリを追加します。
```shell
$ sudo sh -c "cat << EOF > /etc/yum.repos.d/cosmic-ext-imenabled.repo
[cosmic-ext-imenabled]
name=IME Enabled COSMIC Apps Repository
baseurl=https://kenz-gelsoft.github.io/cosmic-ext-imenabled
enabled=1
gpgcheck=0
EOF"
```

入れたいアプリを `dnf install --allowerasing` できるようになります。例：
```shell
$ sudo dnf install --allowerasing cosmic-term-ime
```
