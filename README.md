# Unofficial APT Repository of IME-Support Preview for some COSMIC Apps

Since COSMIC apps in Pop!_OS do not currently support IME, there are issues inputting characters for languages that require an IME, such as Japanese, Chinese, and Korean.

While the latest version of the **iced** toolkit (which COSMIC apps use) has implemented IME support, it is expected to take several months before COSMIC apps officially adopt this latest version. Therefore, I have backported the IME support in advance to enable IME functionality for specific apps.

## Supported COSMIC Apps

* **cosmic-term-ime**
* **cosmic-files-ime**
* **cosmic-edit-ime**

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

- **cosmic-term-ime**
- **cosmic-files-ime**
- **cosmic-edit-ime**

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
