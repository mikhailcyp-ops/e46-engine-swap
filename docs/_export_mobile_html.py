"""One-off export: photos_ebox_wiring_analysis.md -> self-contained HTML with embedded images."""
from __future__ import annotations

import base64
import re
from pathlib import Path

import markdown
from markdown.extensions.tables import TableExtension

DOCS = Path(__file__).resolve().parent
MD_PATH = DOCS / "photos_ebox_wiring_analysis.md"
OUT_PATH = DOCS / "photos_ebox_wiring_analysis_mobile.html"
PHOTOS_DIR = DOCS / "wiring-photos"


def embed_images(md: str) -> str:
    def repl(match: re.Match[str]) -> str:
        alt, path = match.group(1), match.group(2)
        path = path.replace("%20", " ")
        if path.startswith("wiring-photos/"):
            file_path = DOCS / path
        else:
            file_path = (DOCS / path).resolve()
        if not file_path.is_file():
            return match.group(0)
        data = base64.b64encode(file_path.read_bytes()).decode("ascii")
        mime = "image/jpeg" if file_path.suffix.lower() in {".jpg", ".jpeg"} else "image/png"
        return (
            f'<figure class="photo">\n'
            f'<img src="data:{mime};base64,{data}" alt="{alt}" loading="lazy">\n'
            f"<figcaption>{alt}</figcaption>\n</figure>"
        )

    # Replace markdown images with HTML figures (before markdown pass)
    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl, md)


def mermaid_to_html(html: str) -> str:
    """Wrap mermaid code blocks for optional CDN render; add text fallback."""
    pattern = re.compile(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        re.DOTALL,
    )

    def repl(m: re.Match[str]) -> str:
        src = m.group(1).strip()
        # HTML-escape already done by markdown; unescape common entities for mermaid
        src = (
            src.replace("&quot;", '"')
            .replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
        )
        return (
            '<div class="mermaid-wrap">'
            '<p class="mermaid-note">Схема (нужен интернет для отрисовки Mermaid):</p>'
            f'<pre class="mermaid-fallback">{src}</pre>'
            f'<div class="mermaid">{src}</div>'
            "</div>"
        )

    return pattern.sub(repl, html)


def main() -> None:
    md_raw = MD_PATH.read_text(encoding="utf-8")
    md_embedded = embed_images(md_raw)
    body = markdown.markdown(
        md_embedded,
        extensions=[
            TableExtension(),
            "fenced_code",
            "sane_lists",
            "nl2br",
        ],
        output_format="html5",
    )
    body = mermaid_to_html(body)

    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>E-box E46 — стыковка с косой X5 (MS43)</title>
  <style>
    :root {{
      --bg: #f5f5f0;
      --fg: #1a1a1a;
      --muted: #555;
      --border: #ccc;
      --card: #fff;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #121212;
        --fg: #e8e8e8;
        --muted: #aaa;
        --border: #444;
        --card: #1e1e1e;
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 1rem 1rem 3rem;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      font-size: 16px;
      line-height: 1.55;
      color: var(--fg);
      background: var(--bg);
      max-width: 42rem;
      margin-left: auto;
      margin-right: auto;
    }}
    .export-banner {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      margin-bottom: 1.25rem;
      font-size: 0.9rem;
      color: var(--muted);
    }}
    h1 {{ font-size: 1.35rem; line-height: 1.25; }}
    h2 {{ font-size: 1.15rem; margin-top: 1.75rem; border-bottom: 1px solid var(--border); padding-bottom: 0.25rem; }}
    h3 {{ font-size: 1.05rem; margin-top: 1.25rem; }}
    h4 {{ font-size: 1rem; }}
    a {{ color: #0b57d0; word-break: break-all; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      margin: 1rem 0;
      display: block;
      overflow-x: auto;
    }}
    th, td {{
      border: 1px solid var(--border);
      padding: 0.4rem 0.5rem;
      text-align: left;
      vertical-align: top;
    }}
    th {{ background: var(--card); }}
    blockquote {{
      margin: 1rem 0;
      padding: 0.5rem 1rem;
      border-left: 4px solid #c9a227;
      background: var(--card);
      color: var(--muted);
    }}
    code {{
      font-size: 0.88em;
      background: var(--card);
      padding: 0.1em 0.35em;
      border-radius: 4px;
    }}
    pre {{
      overflow-x: auto;
      font-size: 0.8rem;
      background: var(--card);
      padding: 0.75rem;
      border-radius: 6px;
      border: 1px solid var(--border);
    }}
    figure.photo {{
      margin: 1.25rem 0;
      background: var(--card);
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border);
    }}
    figure.photo img {{
      display: block;
      width: 100%;
      height: auto;
    }}
    figure.photo figcaption {{
      padding: 0.5rem 0.75rem;
      font-size: 0.85rem;
      color: var(--muted);
    }}
    .mermaid-note {{ font-size: 0.85rem; color: var(--muted); }}
    .mermaid-fallback {{
      white-space: pre-wrap;
      font-size: 0.75rem;
    }}
    ul {{ padding-left: 1.25rem; }}
    li {{ margin: 0.35rem 0; }}
    hr {{ border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }}
  </style>
</head>
<body>
  <div class="export-banner">
    Офлайн-копия отчёта <strong>photos_ebox_wiring_analysis.md</strong> (ревизия 2).
    Все фото встроены в этот файл. Ссылки на файлы репозитория на телефоне без проекта не откроются.
  </div>
  <article class="content">
{body}
  </article>
  <script type="module">
    import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
    mermaid.initialize({{ startOnLoad: true, theme: "neutral", securityLevel: "loose" }});
  </script>
</body>
</html>
"""

    OUT_PATH.write_text(html, encoding="utf-8")
    size_mb = OUT_PATH.stat().st_size / (1024 * 1024)
    print(f"Wrote {OUT_PATH} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
