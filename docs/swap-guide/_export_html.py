"""Собрать один HTML, в котором фотографии вшиты в файл, без ссылок на картинки."""
from __future__ import annotations

import base64
import re
from pathlib import Path

import markdown
from markdown.extensions.tables import TableExtension

HERE = Path(__file__).resolve().parent

DOCS = [
    (
        "e46-318i-m43b19-to-m54b30-x5.md",
        "e46-318i-m43b19-to-m54b30-x5.html",
        "ru",
        "Свап BMW E46 318i M43B19 на M54B30 от X5",
        (
            "Пошаговый свап BMW E46 318i с мотора M43B19 на M54B30 от X5 E53, коса и MS43. "
            "Бензонасос не качает, реле, стартер, pin 10, педаль газа, прошивка immo off EWS "
            "через MS4X flasher, кардан, скоба коробки, лапы, поддон, расширительный бачок. "
            "Фотографии вшиты в этот файл."
        ),
    ),
    (
        "e46-318i-m43b19-to-m54b30-x5.en.md",
        "e46-318i-m43b19-to-m54b30-x5.en.html",
        "en",
        "BMW E46 318i M43B19 to X5 M54B30 swap",
        (
            "Step-by-step swap of a BMW E46 318i from the M43B19 to an M54B30 from an X5 E53, "
            "with the X5 harness and MS43. Fuel pump, starter, pin 10, accelerator pedal, "
            "immo-off EWS flash with MS4X flasher, driveshaft, gearbox bracket, mounts, "
            "oil pan, expansion tank. The photos are embedded in this file."
        ),
    ),
]


def embed_images(md: str) -> str:
    def repl(match: re.Match[str]) -> str:
        alt, path = match.group(1), match.group(2)
        file_path = (HERE / path).resolve()
        if not file_path.is_file():
            raise SystemExit(f"Нет файла фотографии: {path}")
        data = base64.b64encode(file_path.read_bytes()).decode("ascii")
        return (
            f'<figure class="photo">\n'
            f'<img src="data:image/jpeg;base64,{data}" alt="{alt}">\n'
            f"<figcaption>{alt}</figcaption>\n</figure>"
        )

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl, md)


def render(md_name: str, out_name: str, lang: str, title: str, description: str) -> None:
    md_raw = (HERE / md_name).read_text(encoding="utf-8")
    body = markdown.markdown(
        embed_images(md_raw),
        extensions=[TableExtension(), "sane_lists", "nl2br"],
        output_format="html5",
    )
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <style>
    :root {{
      --bg: #f4f1ea;
      --fg: #1c1a16;
      --muted: #5c564c;
      --border: #d5cfc3;
      --card: #fffdf8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0 auto;
      padding: 1.25rem 1rem 3rem;
      max-width: 44rem;
      font-family: system-ui, "Segoe UI", Roboto, sans-serif;
      font-size: 17px;
      line-height: 1.55;
      color: var(--fg);
      background: var(--bg);
    }}
    h1 {{ font-size: 1.45rem; line-height: 1.25; }}
    h2 {{ font-size: 1.2rem; margin-top: 2rem; border-bottom: 1px solid var(--border); }}
    h3 {{ font-size: 1.05rem; margin-top: 1.4rem; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.92rem; margin: 1rem 0; }}
    th, td {{ border: 1px solid var(--border); padding: 0.4rem 0.5rem; text-align: left; vertical-align: top; }}
    th {{ background: var(--card); }}
    figure.photo {{
      margin: 1rem 0 1.25rem;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
    }}
    figure.photo img {{ display: block; width: 100%; height: auto; }}
    figure.photo figcaption {{ padding: 0.45rem 0.75rem 0.6rem; font-size: 0.85rem; color: var(--muted); }}
    code {{ background: var(--card); padding: 0.05em 0.3em; border-radius: 4px; }}
  </style>
</head>
<body>
  <article>
{body}
  </article>
</body>
</html>
"""
    out_path = HERE / out_name
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path} ({out_path.stat().st_size / (1024 * 1024):.1f} MB)")


def main() -> None:
    for md_name, out_name, lang, title, description in DOCS:
        render(md_name, out_name, lang, title, description)


if __name__ == "__main__":
    main()
