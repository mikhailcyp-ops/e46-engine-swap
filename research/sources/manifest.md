# Source manifest (handoff links S01–S42)

Legend: **ok** = useful payload saved · **partial** = shell/block/challenge only · **fail** = HTTP error · **extract** = text saved under `pages/`

| ID | URL | Local file(s) | Status |
|----|-----|---------------|--------|
| S01 | [MS43 Pinout](https://www.ms4x.net/index.php?title=Siemens_MS43_Pinout) | `files/S01_ms4x_ms43_pinout.wiki`, `pages/S01_ms4x_ms43_pinout.wiki` | **ok** |
| S02 | [M52TU→MS43 HowTo](https://www.ms4x.net/index.php?title=HowTo:_Convert_M52TU_Engine_to_MS43) | `files/S02_…`, `pages/S02_…` | **ok** |
| S03 | [Harness connectors](https://www.ms4x.net/index.php?title=Engine_Wiring_Harness_Connectors) | `files/S03_…`, `pages/S03_…` | **ok** |
| S04 | [e46forum.pl M43→M54 p.2](https://e46forum.pl/bmw-e46-swap-m43-na-m54-18149-5) | `pages/S04_e46forum_pl_m43_m54.md` | **extract** (WebFetch; curl blocked by CF) |
| S05 | [GitHub krided/E46](https://github.com/krided/E46) | `files/S05_github_krided_e46.html` | **ok** (repo page) |
| S06 | [pinoutbms46.pdf](https://github.com/krided/E46/blob/main/pinoutbms46.pdf) | `files/S06_pinoutbms46.pdf`, `pages/S06_pinoutbms46.txt` | **partial** (PDF is Autodata diagnostics, not X60004 table) |
| S07 | [ECUConnections BMS46](https://www.ecuconnections.com/forum/viewtopic.php?t=81616) | — | **fail** (registration) |
| S08 | [ecu.design BMS46](https://ecu.design/ecu-pinout/pinout-bosch-bms46-bmw-main-connector/) | `files/S08_ecu_design_bms46.html` | **partial** (geo block page) |
| S09 | [Scribd BMS46](https://www.scribd.com/document/756953671/Bosch-Bms46-Bmw-Main-Connector) | `files/S09_scribd_bms46.html` | **partial** (viewer shell) |
| S10 | [GS Tuning BMS46 V4](https://www.gstuning.net/mediawiki/index.php?title=BMW_M43_BMS46_V4) | `files/S10_gstuning_bms46_v4.html` | **ok** |
| S11 | [BimmerTuningTools pinouts](https://www.bimmertuningtools.com/pinouts/) | `files/S11_bimmertuningtools_pinouts.html` | **ok** (index page) |
| S12 | [ECU Backup BMS46](https://www.ecubackup.com/bmw/bmw-3xx/bmw-316-0261204420-dme1430940-bms46-e46-000442941/) | — | **fail** |
| S13 | [Centraline Motore listing](https://www.centralinemotore.com/product-page/0261204420-bosch-bms46-dme-1430940-centralina-motore-ecu-bmw-z3-e36-e46-318ci) | `files/S13_centralinemotore_bms46.html` | **ok** |
| S14 | [rusEFI E46 DME pinout wiki](https://github.com/rusefi/rusefi/wiki/2002-BMW-325-and-2004-BMW-330Ci-E46-DME-pinout) | `pages/S14_rusefi_bmw_e46.md` (from rusefi_documentation) | **partial** (old wiki 404; alternate doc saved) |
| S15 | [rusEFI BMW e46](https://github.com/rusefi/rusefi/wiki/BMW-e46) | `files/S15_rusefi_bmw_e46.md`, `pages/S15_rusefi_bmw_e46_wiki_raw.md` | **ok** |
| S16 | [BMWteka E46 root](https://bmwteka.com/wds/en/e46) | `files/S16_bmwteka_e46.html` | **partial** (SPA shell) |
| S17 | [BMWteka f770ef12](https://bmwteka.com/wds/en/e46/f770ef12) | `files/S17_bmwteka_f770ef12.html` | **partial** (SPA shell) |
| S18 | [WDS psjr Drive](https://wds.psjr.org/en/e46/Complete%20vehicle/Drive) | `files/S18_wds_psjr_drive.html` | **ok** (tree index) |
| S19 | [NewTIS X6011](https://www.newtis.info/tisv2/a/en/e46-316ci-cou/…/x6011-x6011/) | — | **fail** |
| S20 | [NewTIS BMS46 A/C](https://www.newtis.info/tisv2/a/en/e46-m3-cou/…/pAleAsK) | — | **fail** |
| S21 | [RealOEM VIN JK85100](https://www.realoem.com/bmw/enUS/partgrp?vin=JK85100) | — | **fail** |
| S22 | [Archive ST055 MS42/MS43 PDF](https://ia800902.us.archive.org/…/01_MS42%20MS43.pdf) | `files/S22_bmw_st055_ms42_ms43.pdf` | **ok** (binary only) |
| S23 | [vems.hu pinout.pdf](http://www.vems.hu/files/BMW/pinout.pdf) | `files/S23_vems_bmw_pinout.pdf`, `pages/S23_vems_pinout.txt` | **ok** |
| S24 | [E46Fanatics 318i B30](https://www.e46fanatics.com/threads/318i-b30-swap.1214217/) | `files/S24_*` | **partial** (CF challenge) |
| S25 | [E46Fanatics swap issue](https://www.e46fanatics.com/threads/swap-issue.1343319/) | `files/S25_*` | **partial** |
| S26 | [E46Fanatics BMS46 pinout](https://www.e46fanatics.com/threads/bms46-dme-pinout.1336970/) | `files/S26_*` | **partial** |
| S27 | [BMW FAQ BMS46 thread](https://www.bmwfaq.org/threads/busco-pinout-ms46.1042949/) | `files/S27_bmwfaq_bms46.html`, `pages/S27_bmwfaq_extract.md` | **ok** + **extract** |
| S28 | [Bimmerforums wiring](https://www.bimmerforums.com/forum/showthread.php?2007379-…) | — | **fail** |
| S29 | [Bimmerfest M54 conversion](https://www.bimmerfest.com/threads/m54-conversion-help.678869/) | `files/S29_*` | **partial** |
| S30 | [E46Fanatics X6011](https://www.e46fanatics.com/threads/ms43-x6011-connector-pinout.1301334/) | `files/S30_*` | **partial** |
| S31 | [MS42→MS43 teething](https://www.e46fanatics.com/threads/upgrade-from-ms42-to-ms43-teething-problems-and-updates.1231278/) | `files/S31_*` | **partial** |
| S32 | [Bimmerfest MS43 PDF](https://www.bimmerfest.com/attachments/siemens-ms43-pinout-pdf.879427/) | — | **fail** (409); use S01 instead |
| S33 | [MS4x Flasher](https://www.ms4x.net/index.php?title=MS4x_Flasher) | `files/S33_…`, `pages/S33_…` | **ok** |
| S34 | [TunerPro patchlist](https://www.ms4x.net/index.php?title=TunerPro_MS43_Community_Patchlist) | `files/S34_…`, `pages/S34_…` | **ok** |
| S35 | [Siemens MS43](https://www.ms4x.net/index.php?title=Siemens_MS43) | `files/S35_…`, `pages/S35_…` | **ok** |
| S36 | [Bimmerworld MS45→MS43](https://www.bimmerworld.com/About-Us/MS45-to-MS43-Conversion/) | `files/S36_bimmerworld_ms45_ms43.html` | **ok** |
| S37–S40 | Tulay product pages | `files/S37`–`S40` | **ok** (HTML) |
| S41 | [E46Fanatics EWS/starter](https://www.e46fanatics.com/threads/no-crank-no-start-down-to-starter-ews.1083782/) | `files/S41_*` | **partial** |
| S42 | [Scribd EWS](https://www.scribd.com/document/128057819/BMW-Ews) | `files/S42_scribd_ews.html` | **partial** |

## Extra mirrors (not in original handoff)

| File | Source | Notes |
|------|--------|-------|
| `files/S_wds_bms46_PA6000D_mirror.html` | [iho-bmw E46_PA6000D](http://iho-bmw.s3-website-us-west-2.amazonaws.com/zinfo/E46_PA6000D.htm) | Same document family as BMW FAQ attachment `PA6000D.pdf` |
| `pages/S_wds_E46_PA6000D_pinouts.md` | converted from mirror | **Primary local BMS46-era X60004 table** |
| `files/S_wds_ms43_a6000_41dd562c.html` | BMWteka doc id | SPA shell only |
