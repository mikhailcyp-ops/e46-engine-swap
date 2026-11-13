# S04 — BMW E46 Forum (PL): M43 → M54 swap, page 2

Source: https://e46forum.pl/bmw-e46-swap-m43-na-m54-18149-5  
Saved: 2026-10-20 via WebFetch (automated curl blocked by Cloudflare).

## ECU / EWS (author: mariryb)

- Swap includes **new DME with engine harness**, **EWS**, **ignition lock insert**, and **new key**.
- **Do not turn ignition on** with mismatched DME/EWS without understanding sync — risk of EWS/DME desync (INPA sync mentioned).

## Electrical — core steps (mariryb, M43 → M54 + MS43 on E46 body)

### Electronic throttle pedal → X60004 (gray part of 40-pin)

| Pedal pin | ECU X60004 pin |
|----------:|---------------:|
| 1 | 7 |
| 2 | 12 |
| 3 | 14 |
| 4 | 8 |
| 5 | 9 |
| 6 | 13 |

### Remove / relocate from X60004 (body side, M43 routing)

From the **40-pin body plug**, depin and reroute:

| Old X60004 pin | Function |
|---------------:|----------|
| 1 | Battery charge indicator |
| 2 | Engine start signal feedback |
| 3 | Secondary air pump (author left unconnected — no SAP on his M54) |
| 11 | Oil pressure switch |
| 21 | Oil level sensor |

### X6011 (8-pin black — engine ↔ body bridge)

On **MS43 / M54**, cluster-related lines go through **X6011** (not present on M43). Author’s MS43 pin assignment:

| X6011 pin | Function |
|----------:|----------|
| 1 | Starter |
| 2 | Alternator excitation (D+) |
| 3 | Oil pressure |
| 4 | Charge indicator |
| 5 | Oil level |
| 6 | Start signal feedback / mass cut (author wording: “odcięcie masy”) |

**Reroute body wires to X6011 (engine-side half):**

| Body wire (from old X60004) | → X6011 pin |
|-----------------------------|------------:|
| 11 oil pressure | 3 |
| 1 charge lamp | 4 |
| 21 oil level | 5 |
| 2 start feedback | 6 |

**Starter / alternator (were on a different M43 body plug):**

- Cut body-side plug; connect **black → X6011 pin 1**, **brown/green → pin 2** (author’s colors — verify on your car).

### Third bridge plug (fender box)

- M43 had **4 wires**; M54 harness has **3 matching** — author cut engine-side connector and mated to remaining M43 body plug; **4th wire removed** (reverse light related per author).

### Extra X60004 wires for full M54 function (manual / cruise)

Author lists missing vs full M54 body harness:

| X60004 pin | Function |
|----------:|----------|
| 23 | Clutch switch |
| 24 | Brake light switch |
| 27 | MFL / cruise data |
| 28 | Brake switch |

- **23** → clutch switch (author planned — without it, RPM blip on fast upshifts when clutch pressed).
- **24 / 28** → brake switch / LCM (author not finished at write-up time).

## Follow-up (Haraz, 2019)

- Donor M54 had **automatic**; car had **manual throttle pedal** retrofit per above — **no throttle response** until brake/clutch parts addressed.
- Needs **4-wire brake pedal switch (black)** and **clutch sensor** per friend’s advice.
- Pedal: bought **manual** pedal though auto vs manual pedal differs.

## Images referenced on forum

Original thread embeds WDS pinout PNGs (`PA6000D`, `PA6000J`) and connector photos — not mirrored here; see forum URL in browser.
