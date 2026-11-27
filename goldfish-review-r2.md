# Goldfish Review R2 — news-image-20261126 (entry v2, fix round)

**Verdict: LAYAK LANJUT BELUM LAYAK SUBMIT**

Ditulis: 26 Nov 2026 ~12:40 WIB (re-review independen, Goldfish). Entry v2 dikompilasi ~05:16 UTC (12:16 WIB).
Yang diperiksa langsung: `entry.png` full-size + downscale 300px + crop sekunder/peta/footer/timeline;
`build-log.md` v2; `top10-analysis.md`; review v1 (`goldfish-review.md`).
Verifikasi fakta independen via pencarian web ke sumber primer bernama (Reuters/BBC/Met Police/
Northants Police/ICC/MUA/FIDReC/dll.). Saya TIDAK build, TIDAK ubah file entry, TIDAK submit.
CATATAN: file pembanding `/tmp/ni26-top/r1-witty-panda-51.webp` dan `r4-hazel-orca-14.webp`
SUDAH TIDAK ADA di VM ini (hilang saat restart) — perbandingan di bawah memakai catatan rinci
rank 1 & rank 4 dari review v1 + top10-analysis.md yang saya baca langsung sesi ini, bukan
tampilan ulang. Itu cukup untuk verdict, tapi bukan re-view segar.

Ringkasan satu kalimat: ronde fix ini MENUTUP semua 5 blocker v1 dan 5 dari 6 major v1 — tapi
memasukkan SATU kegagalan tanggal baru dengan pola yang persis sama (B1–B4): #46 kokain £80m,
vonisnya 4 Nov, bukan 26 Nov, dan stempel build-log-nya ("sentencing Wed 25 Nov") salah.
Satu item itu saja yang menghalangi submit; ganti #46 dan entry ini akhirnya sampai di
estimasi pasca-fix review v1.

---

## Status blocker v1 (B1–B5): SEMUA TERTUTUP

### B1 — #11 Tanker Dubai: TERTUTUP
- Gambar v2: tidak ada lagi tanker Dubai, tidak ada lagi entri timeline 00:42.
- Footer DATE CHECK: "Dubai tanker" ada di daftar "Left out on purpose, first reported Wed 25 Nov
  or earlier" ✓. Pengganti #11 Brent $94,71 terverifikasi LOLOS (Reuters SINGAPORE, Nov 26;
  Brent $94,71 +0,1% pukul 0137 GMT; klaim Houthi Ras Tanura + ranjau Hormuz).

### B2 — #12 Iowa "huge success": TERTUTUP
- Gambar v2: tidak ada lagi Iowa. Footer: "Iowa blast" di daftar eksklusi ✓.
- Pengganti #12 NFL triple-header terverifikasi LOLOS (Bears–Lions 1 p.m. ET CBS;
  Eagles–Cowboys 4:30 p.m. ET FOX; Chiefs–Bills 8:20 p.m. ET NBC; Mahomes v Allen).

### B3 — #18 Samsung ₩1,73tn: TERTUTUP
- Gambar v2: tidak ada lagi Samsung. Footer: "Samsung ₩1.73tn" di daftar eksklusi ✓.
- Slot kini #18 bad-loan bank Korea (dulu v1 #19, LOLOS di v1).

### B4 — #38 Bonus Singapura 1,55 bulan: TERTUTUP
- Gambar v2: tidak ada lagi bonus 1,55 bulan. Footer: "Singapore bonus" di daftar eksklusi ✓.
- Slot kini #38 mogok feri Palm Beach (rilis MUA 25 Nov; mogok mulai 07:30 Kam 26 Nov — LOLOS, grey,
  dicatat jujur di footer "Palm Beach release 25 Nov").

### B5 — #5 BOK subline: TERTUTUP
- Gambar v2 kini: "Third hike since July; first time above 3% since Nov 2024" — persis seperti
  yang diminta fix v1.
- Verifikasi: Reuters 26 Nov — "its third increase since July" (back-to-back Juli + Agustus,
  jeda Oktober); "highest since November 2024" / "first time the benchmark has topped 3% in
  about two years since November 2024" (Seoul Daily). Kedua klausa BENAR.

---

## Status major v1 (M1–M6)

### M1 — Skew regional / blok Korea: TERTUTUP (dengan sisa kecil)
- Blok Korea ALSO ON 10 → 3 (#16 Seoul shares, #17 dialog Korea-Jepang, #18 bad-loan).
  East Asia 14 → 10/48 (20,8%). Region bar rekonsiliasi PERSIS, saya hitung ulang per cerita:
  North America 5 · South America 3 · Europe 11 · East Asia 10 · SE Asia 2 · South Asia 7 ·
  Oceania 4 · Middle East 3 · Africa 3 = 48 ✓. Fields 20 item, jumlah 48 ✓.
  South America 1→3, Afrika 2→3, Oceania 3→4, South Asia 3→7.
- Sisa: Europe 11 masih region terbesar dan East Asia 10 kedua (21/48 = 44% di dua region;
  rank 1 max 6/region). SE Asia menipis jadi 2 (hanya #29 Singapura + #39 Manila). Ini
  sekarang soal derajat, bukan major — tidak ada lagi 10 item satu wire berurutan.

### M2 — Peta hampir tak terbaca: TERTUTUP (dengan sisa kecil)
- Peta v2: laut biru-abu pucat, benua tan/beige dengan outline gelap — LANGSUNG dikenali sebagai
  peta dunia di full-size maupun 300px. Jauh di atas strip abu-abu v1.
- 17 pin dicek posisinya: 1 New York + 12 Detroit (Amerika Utara, berdekatan, benar);
  30 Santiago di ujung selatan Amerika Selatan ✓; 21 Lagos + 35 Abuja di Afrika Barat,
  28 Lusaka di Afrika Selatan ✓; 14 London / 6 Brussels / 3 Geneva menggerombol di Eropa ✓;
  7 Riyadh / 10 Sanaa / 11 Hormuz di Timur Tengah ✓; 2 Mumbai di India ✓; 29 Singapura di
  ujung Semenanjung Malaya ✓; 4 Pyongyang di Korea ✓; 8 Tokyo di Jepang ✓; 20 Canberra di
  tenggara Australia ✓. Tidak ada pin yang salah benua/lokasi.
- Sisa kecil: ujung utara peta terpotong panel (Kanada/Eurasia utara ter-clip); pin 29 duduk
  sedikit lepas dari ujung semenanjung. Di 300px peta tetap strip tipis — sama seperti rank 1/4.

### M3 — Stempel tanggal build-log tak tepercaya: TETAP TERBUKA
- Builder mengklaim re-verifikasi semua cerita + menemukan/menghapus 10 kegagalan tanggal lagi
  (Norfolk, Lee housing, tuna, DART, marine research, Grab $500m, dst.) — daftar eksklusi baru
  itu konsisten dan kredibel.
- TAPI: verifikasi independen saya menemukan SATU kegagalan tanggal baru di v2, #46 (lihat B6
  di bawah) — pola yang sama persis dengan B1: stempel waktu sekunder dikira first-report.
  Selama masih ada 1 klaim tanggal salah yang lolos, M3 belum tertutup. Standar v1: "jangan
  biarkan satu klaim tanggal salah lagi lolos" — belum terpenuhi.

### M4 — Seleksi / filler ringan di ekor: TERTUTUP (dengan sisa kecil)
- 17 cerita baru, mayoritas berat: Brent/Hormuz, trust tax Australia, revolt data-centre Jepang,
  protes tarif Jepang, ICC/Duterte, bensin Pakistan, dam Gargai, Navy Nigeria, CGT, Correios.
  Ekor v1 yang paling ringan (HealthHub, Stratocaster, Oman/Cheonghae, Hanwha/Ourhome,
  Changwon, KBO) sudah hilang.
- Sisa: ekor masih punya 4–5 item ringan (#23 BBC–Met Office, #25 Milk Day, #27 pastor,
  #32 Borthwick, #41 survei parenting) — tapi bukan lagi filler dominan, dan semuanya
  bertanggal 26 Nov terverifikasi. Catatan: kandidat berat v1 (serangan Niger, Gaza, pemadaman
  Rusia, upah Bangladesh) memang gagal dating 26 Nov menurut daftar eksklusi v2 — konsisten
  dengan pola B1–B4, jadi benar tidak dimasukkan.

### M5 — #7 Riyadh sumber + subline: TERTUTUP
- Gambar v2: "Two missiles downed over Riyadh — Coalition intercepts two ballistic missiles
  over the capital. Coalition · Al Jazeera" ✓. Klausa "a day after Jeddah drone" HILANG ✓.

### M6 — Item abu-abu tanggal: TERTUTUP
- Footer DATE CHECK v2 memuat catatan jujur untuk SEMUA 13 item abu-abu + Macy's — saya baca
  langsung dari gambar (bukan cuma klaim log): "Macy's postponement announced Wed evening US ·
  Nigeria FX data 24 Nov · Zambia letter 17 Nov · Korea-Japan talks 25 Nov · Borthwick comments
  Wed · AIHW page 25 Nov · PIA announced 25 Nov · Palm Beach release 25 Nov · ICC briefing
  24 Nov · Islamabad notified 25 Nov · cocaine sentencing Wed · Japan tariffs announced 25 Nov ·
  Correios called 18 Nov · CGT announced Tue." 14 catatan, lengkap, tidak ada yang hilang.
  (Satu catatan di antaranya — "cocaine sentencing Wed" — ternyata SALAH tanggalnya; lihat B6.)

---

## Blocker BARU di v2

### B6 (BARU) — #46 kokain £80m: vonisnya 4 Nov, BUKAN 26 Nov — HARUS DIHAPUS SEBELUM SUBMIT
- Gambar: "£80m cocaine smugglers jailed after lorry driver's tea break — BBC".
- Bukti primer:
  - Artikel BBC-nya sendiri bertanggal **4 November 2026** ("Trio jailed after £80m cocaine
    smuggled in lorry in Northampton", 4 Nov 2026).
  - Northamptonshire Police + Metropolitan Police: Craig Le-Mare divonis 20 tahun pada
    **Rabu, 4 November** (bukan 25 Nov); Michael Weston divonis 22 Mei 2026; Kelly Robertson
    divonis November 2024. Total 47+ tahun.
  - Feature BBC "How £80m of cocaine was found after a lorry break-in" bertanggal 6 Nov 2026;
    video penangkapan bandara 7 Nov 2026. TIDAK ADA sumber yang melaporkan ini sebagai cerita
    26 Nov.
- Yang salah di build-log v2: "Published 2026-11-26T02:02:43Z; Craig Le-Mare sentenced 20 years
  at the Old Bailey; sentencing Wed 25 Nov". Kedua klaim itu salah: tidak ada publikasi pertama
  26 Nov, dan vonisnya Rabu 4 Nov — bukan Rabu 25 Nov. Ini pola B1 yang sama: stempel waktu
  sekunder/re-publish dikira first-report.
- Footer note "cocaine sentencing Wed" ikut menyesatkan: tanpa tanggal, "Wed" dibaca sebagai
  Rabu 25 Nov — padahal 4 Nov.
- Tambahan: headline "smugglers jailed" (jamak) — hanya Le-Mare yang divonis November; dua
  lainnya divonis 2024 dan Mei 2026.
- Fix: HAPUS #46, ganti dengan cerita 26 Nov terverifikasi, dan hapus catatan "cocaine
  sentencing Wed" dari footer (atau ganti dengan catatan eksklusi yang benar). Ini pekerjaan
  satu item — tapi ini blocker, bukan minor: cerita ini khas dan mudah diingat judge
  ("tea break"), dan tanggal 4 Nov-nya terpampang di artikel BBC-nya sendiri.

---

## Verifikasi fakta — 17 cerita BARU v2 (independen, via pencarian web 26 Nov 2026 ~12:30 WIB)

| # | Cerita | Hasil | Bukti / sumber |
|---|---|---|---|
| 11 | Brent $94,71 | **LOLOS** | Reuters SINGAPORE, Nov 26: Brent $94,71 (+0,1%) 0137 GMT, WTI $84,03; Houthi Ras Tanura + ranjau Hormuz. |
| 12 | NFL triple-header | **LOLOS** | Bears–Lions 1 p.m. ET CBS; Eagles–Cowboys 4:30 FOX; Chiefs–Bills 8:20 NBC; Mahomes v Allen (NBC/ESPN). Jadwal 26 Nov. |
| 13 | Dam Gargai 650 ha | **LOLOS** | Indian Express front page 26 Nov 2026; BMC ₹3.065-crore; ~650 ha hutan Tansa terendam; 3 lakh pohon ditransplantasi. (Sumber lain 652–658 ha — "650 ha" pembulatan wajar.) |
| 35 | Navy Nigeria | **LOLOS** | Seminar R&D Navy di Naval HQ Abuja, Kamis 26 Nov; CNS Vice Admiral Idi Abbas keynote; rencana research institute + sel R&D. |
| 36 | Trust tax Australia 30% | **LOLOS** | Main bill lolos DPR 26 Nov (setujui amandemen Senat); rates bill lolos kedua kamar 25 Nov; deal Labor–Greens 25 Nov; 30%; ~350.000 usaha kecil; mulai 1 Jul 2028. Headline "passes" akurat untuk 26 Nov. |
| 37 | PIA 777 | **LOLOS (abu-abu)** | Reuters 25 Nov: PIA pindah operasi UK ke 777 sendiri mulai 26 Nov; PK786/PK710 batal Rabu 25 Nov. Footer jujur ("PIA announced 25 Nov"). |
| 38 | Feri Palm Beach | **LOLOS (abu-abu)** | Rilis MUA 25 Nov 2026: mogok mulai 07:30 Kam 26 Nov. Footer jujur ("Palm Beach release 25 Nov"). |
| 39 | ICC Duterte ~100 saksi | **LOLOS (abu-abu)** | ICC Q&A: sidang dibuka 30 Nov 2026, ~100 saksi; juru bicara ICC briefing Sel 24 Nov. Footer jujur ("ICC briefing 24 Nov"). Catatan: stempel "explainer 26/11 03:45" tidak saya konfirmasi independen — substansinya terverifikasi. |
| 40 | Bensin Pakistan Rs314/Rs348 | **LOLOS (abu-abu)** | OGRA umumkan Rab 25 Nov; berlaku 26 Nov: bensin Rs314 (dari Rs318), diesel Rs348 (dari Rs353). Footer jujur ("Islamabad notified 25 Nov"). |
| 41 | Survei parenting 76% | **LOLOS** | Guardian 26 Nov 00:01; Kindred Squared 2026 National Early Childhood Parenting Survey; 76% anxiety naik; ~3.500 orang tua. |
| 42 | India A v Sri Lanka A | **LOLOS** | Semi 1 ACC Rising Stars, Kam 26 Nov 15:30 IST, West End Park Doha; Sri Lanka A tak terkalahkan. |
| 43 | Data-centre Jepang | **LOLOS** | Reuters KASHIWA, Japan, Nov 26: "Japan's data centre boom faces growing revolt from urban residents". |
| 44 | Protes tarif Jepang | **LOLOS (abu-abu)** | Kihara jumpa pers pagi 26 Nov: tarif AS "extremely regrettable", Jepang protes ke pemerintah AS. Tarifnya diumumkan 25 Nov — footer jujur ("Japan tariffs announced 25 Nov"). Framing BENAR: yang 26 Nov adalah protesnya. |
| 45 | Long March 2D 09:35 UTC | **LOLOS tanggal, ABU-ABU framing** | Jadwal NET 26 Nov 09:35 UTC, Xichang LC-3, GO FOR LAUNCH, payload unknown, "58th CASC launch of 2026" ✓. TAPI kompilasi 05:16 UTC = 4 jam 19 mnt SEBELUM liftoff; headline "lifts off" (present tense) untuk peluncuran yang belum terjadi + identitas payload/roket pun dicatat "uncertain" (NOTAM). Footer menutup kelas ini ("dated 26 Nov event (scheduled today)") — defensible, tapi baca "lifts off" sebagai sudah terjadi itu menyesatkan. Lihat M7 baru. |
| 46 | Kokain £80m | **GAGAL** | Vonis Le-Mare **4 Nov 2026** (BBC 4 Nov; Northants + Met Police). Bukan 25 Nov, bukan 26 Nov. Lihat B6. |
| 47 | Mogok Correios 22:00 | **LOLOS (abu-abu)** | 36 serikat + Fentect/Findect setujui 17 Nov (diumumkan 18 Nov); mogok nasional mulai 22:00 Kam 26 Nov, jelang Black Friday; kerugian R$7,5 miliar Jan–Sep 2026 ✓. Nuansa: keikutsertaan per negara bagian masih diputuskan majelis lokal 26 Nov — "starts 22:00" adalah jadwal yang diumumkan, bukan fakta yang sudah terjadi saat kompilasi. Footer jujur ("Correios called 18 Nov"). |
| 48 | CGT Argentina | **LOLOS (abu-abu)** | CGT konfirmasi Sel 24 Nov: mars ke Superintendencia de Servicios de Salud (Bartolomé Mitre 400) Kam 26 Nov; stoppage 2–4 jam sebelum pertengahan Des. Footer jujur ("CGT announced Tue"). |

**Cerita lama v2 yang saya verifikasi ulang / konfirmasi di ronde ini:** #5 BOK (B5, LOLOS),
#9 Tamura (LOLOS — Reuters TOKYO Nov 26; WSJ 2026-11-26T01:58Z), #14 traktat UK-EU (LOLOS —
BBC 2026-11-26T02:13:00; dua traktat sore ini; klausa terminasi 10 tahun), #15 stalking
(LOLOS — BBC 2026-11-26T00:12:38Z), #16 Seoul shares (LOLOS — Yonhap SEOUL, Nov 26),
#19 AIHW (LOLOS abu-abu — rilis FARE/medianet 26/11 07:30; 3,2 juta wanita 2025, +800 ribu
sejak 2022–23; footer "AIHW page 25 Nov" ✓), #22 king tides (LOLOS — BBC 2026-11-26T01:05:47Z),
#23 BBC–Met Office (LOLOS — Met Office 00:05 UTC 26 Nov; kemitraan live hari ini),
#27 pastor (LOLOS — BBC 2026-11-26T00:24:25; Doug Wilson, Moscow Idaho, cabut Amendemen 19),
#29 FIDReC (LOLOS — 5.344 klaim diterima +23% dari 4.355; fraud/scam ditangani 1.515 +18% dari
1.285; FIDReC umumkan Kamis 26 Nov; pembetulan v1 — dua angka tidak lagi dicampur),
#31 Davis Cup (LOLOS — GB v Jerman QF Kam 26 Nov 10:00 CET, Bologna),
#32 Borthwick (LOLOS abu-abu — Sky Sports 26 Nov; komentar ke media Rabu; footer
"Borthwick comments Wed" ✓), #33 NEET (LOLOS — Sky News 2026-11-26T04:09Z; 26% vs 13%,
Shelter–UCL Millennium Cohort), #34 Treasury/Milburn (LOLOS — Guardian 26 Nov; Healey "not
happy"; £5,8 miliar/tahun), #36 sudah di tabel. **#17/#21/#28** (abu-abu v1) tetap LOLOS
dengan catatan footer yang kini lengkap. **#20 Climate Council** LOLOS + atribusi diperbaiki.
Hero #1–#3, #4, #6, #8, #10, #18, #24, #26, #30: LOLOS di v1, tidak berubah di v2.

**Rekap angka baru:** $94,71 ✓ · 650 ha ✓ (652–658 di sumber lain) · 30% ✓ · 350.000 ✓ ·
Rs314/Rs348 ✓ · 5.344 +23% ✓ (1.515 +18% terpisah) · 76% ✓ · £80m ✓ (angkanya benar,
tanggalnya yang salah) · 2–4 jam CGT ✓ · 09:35 UTC ✓ (jadwal, bukan hasil).

---

## Major/minor BARU di v2

### M7 (baru, major-ringan) — Item "scheduled today" ditulis seolah sudah terjadi
- #45 "Long March 2D lifts off from Xichang at 09:35 UTC" — present tense untuk peluncuran
  4+ jam di masa depan saat kompilasi; NET time bisa bergeser/scrub; payload unknown.
  Polanya konsisten di 6 item (#12 NFL, #31 Davis Cup, #42 kriket, #45 roket, #47 mogok 22:00,
  #48 mars) — semuanya event terjadwal, semuanya ditulis seperti sudah terjadi. Footer
  ("dated 26 Nov event (scheduled today)") memang mengungkapkan aturannya, jadi ini BUKAN
  blocker — tapi satu kata ("lifts off" → "set to lift off") menghilangkan celah yang bisa
  dipakai judge untuk #45. Perbaikan murah, lakukan sekalian dengan fix B6.

### Minor (baru)
- **Timeline "13:30 NBC parade rerun":** parade tayang Sabtu 08:30 EST = 13:30 UTC *Sabtu*,
  bukan Kamis. Menaruhnya di timeline Kamis pukul 13:30 menyesatkan. Ganti jadi "SAT 13:30"
  atau hapus.
- **#9 subline "Tokyo speech":** pidato Tamura di Yamanashi (WSJ), bukan Tokyo — Reuters
  hanya dateline TOKYO. Kecil, tapi salah tempat.
- **#13 subline tertutup badge:** kata "follow" di "leopards to follow" setengah tertutup badge
  REPORTED merah. Satu-satunya overlap teks di halaman; perbaiki spasi/wrap.
- **Timeline masih "EARLY Riyadh" + "ALL DAY India"** tanpa jam (minor v1 yang belum
  diperbaiki; tidak wajib).
- **Peta:** ujung utara ter-clip (lihat M2).

### Minor v1 — status
- #20 atribusi: DIPERBAIKI ("Climate Council") ✓. Timeline jam: belum (lihat minor di atas).
  Hero art: tidak disentuh, setara v1.

---

## Perbandingan vs rank 1 & rank 4 (berdasar catatan v1 — file pembanding hilang, lihat catatan atas)

**Yang kini setara / unggul:**
- 3 hero SAMA dan benar (Macy's / India 26/11 / Gukesh Game 3); 48 cerita (rank 1: 36,
  rank 4: 50); 20 fields (rank 1: 15, rank 4: 10); region bar + fields bar rekonsiliasi persis;
  timeline UTC; numbers strip 6 angka; DATE CHECK dengan daftar eksklusi + catatan abu-abu
  (kini 14 catatan — lebih lengkap dari rank 1 maupun rank 4).
- Keterbacaan 300px: masthead + hero + numbers strip terbaca; ALSO ON blur kecil — SAMA
  seperti rank 1/4. Peta kini terbaca sebagai peta di 300px.
- Tanggal: v2 kini LEBIH bersih dari rank 1 (rank 1 sendiri memasukkan Cairo/tarif/Ras Tanura/
  Shenzhou 25 Nov sebagai cerita) — kecuali #46, satu-satunya noda.

**Yang masih kalah:**
- **Tanggal (satu item):** #46 adalah cerita 4 Nov yang lolos — persis kesalahan yang rank 4
  hindari dengan eksklusi eksplisitnya. Satu item ini saja cukup untuk kalah duel lawan entry
  bersih.
- **Bobot sekunder:** 10 sekunder rank 1 semuanya berat (Gaza, laser Blysk, Rusia potong
  listrik 5 region, upah Bangladesh +36%, ~500.000 tewas). Sekunder v2 bagus (Kim, BOK, KTT EU,
  Riyadh, Brent, NFL, Gargai) tapi 3–4 di antaranya ringan/olahraga (NFL, Davis Cup di ALSO ON,
  Borthwick). Ekor ALSO ON v2 masih lebih ringan dari rank 1.
- **Peta:** rank 1/4 penuh; peta kita ter-clip di utara (minor).
- **Hero art:** masih selangkah di bawah rank 1 dalam detail (tidak berubah dari v1).
- **Kompilasi pagi 05:16 UTC:** masih morning edition — sama seperti lapangan pagi ini
  (rank 4: "Not yet: Chess Game 3's result"). Bukan kerugian vs lapangan; rebuild sehari-penuh
  tetap bisa menaikkan estimasi, tapi itu ronde terpisah.

---

## Estimasi rank + peluang top 50 (jujur)

- **Entry v2 apa adanya: estimasi rank ~30–55, peluang top 50 ~40–50%.**
  Alasan: ronde fix menutup hampir semua yang dijanjikan v1 (B1–B5, M1, M2, M4, M5, M6) —
  tapi #46 mengulangi kegagalan tanggal kelas B1–B4 di cerita baru. Dalam duel 2v2 lawan entry
  berstruktur sama dan bersih, satu cerita 4 Nov yang disajikan sebagai 26 Nov adalah
  pukulan faithful yang terlihat. Ini DI BAWAH estimasi pasca-fix review v1 (rank ~20–40,
  P(top50) 50–60%) — bukan karena fix-nya gagal, tapi karena proyeksinya mengasumsikan NOL
  kegagalan tanggal, dan v2 masih punya satu.
- **Setelah 1 ronde mikro-fix (hapus/ganti #46 + perbaiki footer + M7 wording + minor
  timeline/#13/#9): estimasi rank ~20–40, peluang top 50 ~50–60%, top 25 mungkin.**
  Yaitu estimasi pasca-fix v1 — akhirnya tercapai, satu ronde terlambat. Top 10 tetap TIDAK
  kredibel tanpa rebuild sehari-penuh (hasil Game 3 + hasil KTT EU + pasar AS + sekunder
  seberat rank 1).
- **Satu putaran perbaikan paling berdampak:** ganti #46 dengan cerita 26 Nov terverifikasi
  (dan hapus catatan footer "cocaine sentencing Wed") + ubah #45 jadi "set to lift off".
  Itu saja. Jangan rebuild, jangan sentuh yang lain — sisanya sudah cukup baik.

## Catatan teknis (singkat)
- File: entry.png 451.079 byte ≤ 1 MiB, JPEG 1024×1024, sha256
  `b785184e06ee4ae3ae8a02716f01aa97949d017bc96033e1d4e4de239ebbe35e` (cocok dengan build-log).
  Tidak ada teks garbled/overlap besar (kecuali "follow" #13) atau terpotong; tidak ada watermark.
  Tidak ada masalah teknis yang menghalangi submit — masalahnya satu item tanggal + wording.
