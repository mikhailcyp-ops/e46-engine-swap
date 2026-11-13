# Local mirror of handoff sources (S01–S42)

Snapshot date: **2026-10-20**. Original list: [docs/BMW_E46_M43_to_M54_MS43_handoff.md](../../docs/BMW_E46_M43_to_M54_MS43_handoff.md) §6–§9.

## Layout

| Path | Contents |
|------|----------|
| [manifest.md](manifest.md) | Per-link download status, local filename, notes |
| [files/](files/) | Raw HTML, wiki markup, PDFs (binaries) |
| [pages/](pages/) | Human-readable extracts (markdown / text) |
| [scripts/](scripts/) | One-off conversion helpers (optional) |

## Best starting points for wiring

1. **MS43 full pinout** — [pages/S01_ms4x_ms43_pinout.wiki](pages/S01_ms4x_ms43_pinout.wiki) (from MS4X, action=raw).
2. **BMS46 X60004 (WDS PA6000D)** — [pages/S_wds_E46_PA6000D_pinouts.md](pages/S_wds_E46_PA6000D_pinouts.md) (mirror of WDS sheet cited on BMW FAQ).
3. **M52/M54-style X60004 (A6000 generic WDS PDF text)** — [pages/S23_vems_pinout.txt](pages/S23_vems_pinout.txt) (verify DME variant before treating as BMS46).
4. **Practical M43→M54 wiring (Polish forum)** — [pages/S04_e46forum_pl_m43_m54.md](pages/S04_e46forum_pl_m43_m54.md).
5. **M52TU→MS43 how-to (pedal, X6011, adapters)** — [pages/S02_ms4x_m52tu_to_ms43.wiki](pages/S02_ms4x_m52tu_to_ms43.wiki).

## PDFs on disk

Stored under `files/` (git may track them via `!research/sources/files/*.pdf` in `.gitignore`):

- `S06_pinoutbms46.pdf` — **not** a 40-pin table; extracted text is Autodata diagnostics for E46 316i M43 ([pages/S06_pinoutbms46.txt](pages/S06_pinoutbms46.txt)).
- `S22_bmw_st055_ms42_ms43.pdf` — BMW training ST055 MS42/MS43 (~8.5 MB).
- `S23_vems_bmw_pinout.pdf` — WDS-style A6000 pinout export.

## Forums blocked to bots

E46Fanatics, Bimmerfest threads, ECUConnections, RealOEM, and some others return Cloudflare / paywall / login shells in automated downloads. See [manifest.md](manifest.md) and [pages/S_forum_fetch_gaps.md](pages/S_forum_fetch_gaps.md). Open those URLs in a browser and save manually if needed.
