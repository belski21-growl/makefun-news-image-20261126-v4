# makefun-news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/belski21-growl/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/belski21-growl/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One illustrated front page summing up Thursday 26 November 2026 in a single image: 38 stories, 9 regions, 16 fields — a nor'easter grounding New York's 100th Thanksgiving parade, a drone strike killing two Italians in Kuwait, and Gukesh–Sindarov's third straight draw in Geneva, plus a UTC timeline, a numbers strip, a numbered world map with 18 pins and an honest DATE CHECK footer. Every story was verified against its primary outlet as first reported on 26 November 2026 (or as a dated 26 November event: scheduled fixtures, launches, strikes and votes taking place that day).

This is **v4**: a full-day rebuild, not a fix round. v3 scored 966.495 (rank 3666/9542, 9W-2D-1L) while the top-50 prize cutoff sits at 986.889 — a gap of +20.394 that no polish could close. v4 rebuilds the page from scratch: compiled after 26 November had ended everywhere, so it carries the day's outcomes instead of its morning schedule — the Game 3 result (third draw, 1.5–1.5), the EU summit ending with no deal on the €1.58tn budget or the €45bn Ukraine loan, the Stoxx 600 close at 636.98, the Kuwait drone strike, the overnight attack on Kyiv, the De Cos pick for the ECB, the Bangkok refinery blast, Ebola passing 12,000 cases, and more. The story count drops from 48 to 38 so headlines can be bigger and the page can breathe, and every illustration is redrawn as a layered scene (sky, setting, actors, light and shadow) instead of v3's flat geometric icons. See `build-log.md` for every story with its primary source and date stamp.

## What's inside

- `entry.png` — the front page itself: 1024×1024 JPEG, 403,428 bytes, sha256 `72e1e291a9bbf6125fba2042eb67a989cf62b64249536461eb705f69ee4e86aa`.
- `main.py` — stdlib-only shipper (Python 3.13): verifies the image (size ≤ 1 MiB, JPEG SOI/EOI, 1024×1024, pinned sha256) before and after copying it to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `./output`). Run `python3 main.py --verify-only` to check without copying.
- 38 stories: 3 illustrated heroes, 12 illustrated secondary panels, 23 more in the numbered ALSO ON list. 9 regions (North America 3, South America 3, Europe 11, East Asia 5, SE Asia 3, South Asia 4, Oceania 1, Middle East 4, Africa 4) and 16 fields — every count reconciles with the contents. Every panel carries a layered drawn scene (gradient sky, setting, actors, light and shadow — no flat icons), and the map's crowded Europe pins are nudged off their true spots with leader lines so each number stays readable.
- Compiled ~03:35 UTC Fri 27 Nov 2026 (10:35 WIB), full-day edition: the day was over everywhere, so the page covers what happened and what was first reported across the whole of Thursday 26 November. The DATE CHECK footer names the big 25-November stories deliberately left out (Cairo tanker fire, US tariffs on 14 economies, Shenzhou-24, the Kospi −6.2% close, the Dubai tanker blast, the cocaine sentencing of 4 Nov, and more) and carries honest notes for the grey items kept (Macy's postponement announced Wednesday evening US time, Nigeria FX data from 24 Nov, the Zambia police letter of 17 Nov) — see `build-log.md` for every story with its primary source and date stamp.

## Run it

```sh
python3 main.py
```

## Verify it

```sh
python3 -m py_compile main.py
python3 main.py --verify-only
MAKEFUN_OUTPUT_DIR=/tmp/check-a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/check-b python3 main.py
sha256sum /tmp/check-a/entry.png /tmp/check-b/entry.png
```

The two runs must produce byte-identical copies with the sha256 above;
`--verify-only` checks the source image without copying anything.

---
<sub>Entered on [make.fun](https://make.fun/?ref=quick-lynx-56&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
---
