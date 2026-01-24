# Unofficial APT Repository of IME-Support Preview for some COSMIC Apps

Since COSMIC apps in Pop!_OS do not currently support IME, there are issues inputting characters for languages that require an IME, such as Japanese, Chinese, and Korean.

While the latest version of the **iced** toolkit (which COSMIC apps use) has implemented IME support, it is expected to take several months before COSMIC apps officially adopt this latest version. Therefore, I have backported the IME support in advance to enable IME functionality for specific apps.

## Supported COSMIC Apps

[How to install](#how-to-install) (ja: [インストール方法](#インストール方法)).

|APT Package Name|Upstream Version|Fork or Patch|
|-|-|-|
|cosmic-term-**ime**|[epoch-1.0.0](https://github.com/pop-os/cosmic-term/releases/tag/epoch-1.0.0)|[Fork](https://github.com/kenz-gelsoft/cosmic-term/tree/backport-input-method)|
|cosmic-edit-**ime**|[epoch-1.0.0](https://github.com/pop-os/cosmic-edit/releases/tag/epoch-1.0.0)|[Fork](https://github.com/kenz-gelsoft/cosmic-edit/tree/backport-input-method)|
|cosmic-files-**ime**|[epoch-1.0.0](https://github.com/pop-os/cosmic-files/releases/tag/epoch-1.0.0)|[Patched `libcosmic`](https://github.com/kenz-gelsoft/cosmic-ext-imenabled/blob/main/.github/workflows/build.yml#L21)|
|cosmic-launcher-**ime**|[epoch-1.0.0](https://github.com/pop-os/cosmic-launcher/releases/tag/epoch-1.0.0)|[Patched `libcosmic`](https://github.com/kenz-gelsoft/cosmic-ext-imenabled/blob/main/.github/workflows/build.yml#L21)|
|cosmic-app-library-**ime**|[epoch-1.0.0](https://github.com/pop-os/cosmic-applibrary/releases/tag/epoch-1.0.0)|[Patched `libcosmic`](https://github.com/kenz-gelsoft/cosmic-ext-imenabled/blob/main/.github/workflows/build.yml#L21)|

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

## How to Install

Add this public APT repository to your `/etc/apt/sources.list` and run `apt update`.

```shell
$ sudo cat << EOF >> /etc/apt/sources.list
deb [trusted=yes] https://kenz-gelsoft.github.io/cosmic-ext-imenabled stable main
EOF

$ sudo apt update
```

You can now install the desired apps via `apt install`. For example:

```shell
$ sudo apt install cosmic-term-ime
```

---

Following is Japanese translation.

# COSMIC アプリの非公式 IME 対応プレビュー apt リポジトリ

Pop!_OS の COSMIC アプリは IME に非対応のため、日本語・中国語・韓国語などの IME を必要とする言語の文字入力に問題があります。

COSMIC アプリが使っている **iced** ツールキットは最新版にて IME サポートが実装されましたが、COSMIC アプリが iced ツールキットの最新版を採用するにはまだ数ヶ月かかる見込みであるため、先行して IME サポートのみをバックポートして一部のアプリのみ IME が動作するようにしました。

## 対応済みの COSMIC アプリ

[こちら](#supported-cosmic-apps)

## インストール方法

`/etc/apt/sources.list` にこのリポジトリから公開されている apt リポジトリを追加し、`apt update` します。
```shell
$ sudo cat << EOF >> /etc/apt/sources.list
deb [trusted=yes] https://kenz-gelsoft.github.io/cosmic-ext-imenabled stable main
EOF

$ sudo apt update
```

入れたいアプリを `apt install` できるようになります。例：
```shell
$ sudo apt install cosmic-term-ime
```
