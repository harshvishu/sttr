# Skills

This repo contains Agent Skills in `.claude/skills/`.

## Available skills

- `sttr` - Use the sttr CLI for text transformations (case changes, encoding/decoding, hashing, JSON/YAML, line ops).

## sttr commands

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
