---
name: sttr
description: Use the sttr CLI to transform text (case changes, encoding/decoding, hashing, JSON/YAML conversion, line ops). Use when a user asks to transform strings, files, or piped input.
---

# sttr Skill

This skill documents the sttr CLI and its supported commands so agents can discover and use them reliably.

## When to use

- The user requests a text transformation (hash, encode/decode, case change, JSON/YAML conversion).
- The user provides a string or file and asks for a conversion.
- You need a quick deterministic text conversion in a workflow.

## How to use

1. Pick the command from the list below.
2. Choose input mode:
   - Direct input: `sttr <command> "text"`
   - File input: `sttr <command> path/to/file.txt`
   - Pipe input: `echo "text" | sttr <command>`
3. Return the output only; avoid interactive mode unless explicitly requested.

## Commands (from `sttr --help`)

- Checksums and hashes: `adler32`, `bcrypt`, `blake2b`, `blake2s`, `crc32`, `md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `xxh-32`, `xxh-64`, `xxh-128`
- Encodings: `ascii85-encode`, `ascii85-decode`, `base32-encode`, `base32-decode`, `base58-encode`, `base58-decode`, `base62-encode`, `base62-decode`, `base64-encode`, `base64-decode`, `base64url-encode`, `base64url-decode`, `crockford-base32-encode`, `crockford-base32-decode`, `hex-encode`, `hex-decode`, `html-encode`, `html-decode`, `morse-encode`, `morse-decode`, `rot13`, `url-encode`, `url-decode`
- String case/format: `camel`, `kebab`, `lower`, `pascal`, `slug`, `snake`, `title`, `upper`
- JSON/YAML/Markdown: `json`, `json-escape`, `json-unescape`, `json-yaml`, `json-msgpack`, `msgpack-json`, `yaml-json`, `markdown-html`
- Lines and text: `count-chars`, `count-lines`, `count-words`, `number-lines`, `reverse`, `reverse-lines`, `shuffle-lines`, `sort-lines`, `unique-lines`, `remove-newlines`, `remove-spaces`, `zeropad`, `escape-quotes`
- Extractors and utilities: `extract-emails`, `extract-ip`, `extract-url`, `hex-rgb`, `qr`, `completion`, `interactive`, `version`

## Install

```shell
npx skills add ./.claude/skills --skill sttr
```

## Install sttr CLI

If the `sttr` CLI is not installed, use one of these options:

```shell
# Quick install
curl -sfL https://raw.githubusercontent.com/abhimanyu003/sttr/main/install.sh | sh

# Homebrew (macOS)
brew install abhimanyu003/sttr/sttr

# Snap
sudo snap install sttr

# Arch Linux
yay -S sttr-bin

# Docker
docker run -it --rm -e TERM=xterm-256color ghcr.io/abhimanyu003/sttr:latest

# Winget (Windows)
winget install -e --id abhimanyu003.sttr

# Scoop (Windows)
scoop bucket add sttr https://github.com/abhimanyu003/scoop-bucket.git
scoop install sttr

# X-CMD
x install sttr

# Webi (macOS / Linux)
curl -sS https://webi.sh/sttr | sh

# Webi (Windows)
curl.exe https://webi.ms/sttr | powershell

# Go
go install github.com/abhimanyu003/sttr@latest
```

Binary downloads (from Releases):

- macOS: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Darwin_all.tar.gz
- Linux: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Linux_x86_64.tar.gz (amd64)
- Linux: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Linux_arm64.tar.gz (arm64)
- Linux: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Linux_i386.tar.gz (i386)
- Windows: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Windows_x86_64.zip (amd64)
- Windows: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Windows_arm64.zip (arm64)
- Windows: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Windows_i386.zip (i386)
- FreeBSD: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Freebsd_x86_64.tar.gz (amd64)
- FreeBSD: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Freebsd_arm64.tar.gz (arm64)
- FreeBSD: https://github.com/abhimanyu003/sttr/releases/latest/download/sttr_Freebsd_i386.tar.gz (i386)
