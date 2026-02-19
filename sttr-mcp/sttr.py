import subprocess
import sys
import logging
import tempfile
from mcp.server.fastmcp import FastMCP

logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.StreamHandler(sys.stderr)],
        )

mcp = FastMCP("sttr")

SUPPORTED_COMMANDS = {
        "upper", "lower", "snake", "kebab", "camel", "pascal",
        "base64-encode", "base64-decode",
        "json", "json-yaml", "yaml-json",
        "md5", "sha1", "sha256", "sha512",
        "count-words", "count-lines",
        "hex-encode", "hex-decode",
        "url-encode", "url-decode",
        "rot13-encode",
        # add the rest
}

@mcp.tool()
async def transform(text: str, command: str) -> str:
    """
    Transform text using the `sttr` CLI.

    This tool writes the input text to a temporary file and executes:
        sttr <command> <filename>

    Args:
        text: The input text to transform.
        command: The sttr operation to apply.

    Supported command examples:
        - String case: upper, lower, camel, pascal, snake, kebab, title
        - Encoding/decoding: base64-encode, base64-decode, url-encode, url-decode
        - Hashing: md5, sha1, sha256, sha512
        - JSON/YAML: json, json-escape, json-unescape, json-yaml, yaml-json
        - Lines/count: count-lines, count-words, reverse-lines
        - Misc: rot13-encode, hex-encode, hex-decode

    Returns:
        The transformed text output produced by sttr, or an error message
        if the command is unsupported or execution fails.
    """

    try:
        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as f:
            f.write(text)
            f.flush()

            result = subprocess.run(
                    ["sttr", command, f.name],
                    capture_output=True,
                    text=True,
                    check=True,
                    )

        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        return e.stderr.strip()

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()

