# Forum / vendor pages not fully captured

Automated download saved **Cloudflare challenge** HTML (~3 KB) for:

- S24, S25, S26, S30, S31, S41 — `www.e46fanatics.com`
- S29 — `www.bimmerfest.com` (WebFetch also returned 402)

## Manual capture suggestion

1. Open the URL in your browser while logged in (if required).
2. Save as **Complete HTML** or copy the thread text into `research/sources/pages/Sxx_manual.md`.
3. For attachments (PDF/images), save into `research/sources/files/` with the Sxx prefix.

## High-value threads to capture manually

| ID | Why |
|----|-----|
| S24 | 318i B30 swap — X6011 / body wiring |
| S30 | MS43 X6011 pinout (confirm E46 vs X5 labels) |
| S26 | BMS46 DME pinout discussion |
| S41 | No crank — EWS/starter diagnostics |
| S29 | M54 conversion help |

## E46Fanatics — auto → manual wiring (not in handoff list)

Useful for **clutch switch** on X60004 pin 23 and EWS pin 8:

- https://www.e46fanatics.com/threads/diy-auto-to-manual-transmission-swap-wiring-changes.1291211/

Not fetched (402/block). Summary for planning:

- Clutch shift module **35426876898** (4-pin on master cylinder).
- Pin 2 → **DME X60004 pin 23**; pin 4 → **EWS X1659 pin 8**; power/ground per thread.
