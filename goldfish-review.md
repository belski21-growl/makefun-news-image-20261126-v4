# Goldfish Review — news-image-20261126 (entry v1)

**Verdict: LAYAK LANJUT BELUM LAYAK SUBMIT**

Ditulis: 26 Nov 2026 ~11:05 WIB (review independen, Goldfish). Entry v1 dikompilasi ~03:53 UTC (10:53 WIB).
Yang diperiksa langsung: `entry.png` full-size + downscale 300px + crop hero/sekunder/bawah; `build-log.md`;
`top10-analysis.md`; pembanding `/tmp/ni26-top/r1-witty-panda-51.webp` dan `r4-hazel-orca-14.webp`.
Verifikasi fakta independen via pencarian web ke sumber primer bernama (Reuters/AP/BBC/BEA/KCNA/UKMTO/
Al Jazeera/Yonhap/dll.). Saya TIDAK build, TIDAK ubah file entry, TIDAK submit.

Ringkasan satu kalimat: struktur sudah pola top-10 (3 hero benar, 48 cerita, 20 field, DATE CHECK jujur
soal eksklusi) — tapi klaim tanggal sentralnya ("Every story above was first reported on Thursday
26 November 2026") TERBUKTI SALAH untuk 4 dari 48 cerita, plus 1 sub-angka faktual salah di panel
sekunder. Itu 4 cerita 25 Nov yang lolos sebagai cerita 26 Nov, dengan standar yang sama yang dipakai
entry ini sendiri untuk meng-eksklusi Cairo/tarif/Shenzhou. Satu ronde fix (hapus/ganti 4 item +
perbaiki 1 subline + seimbangkan blok Korea + gambar ulang peta) bisa menaikkan estimasi secara nyata.

---

## Blockers (harus diperbaiki sebelum submit)

### B1 — #11 Tanker Dubai: tanggal + jam SALAH. Kejadian dan laporan pertamanya 25 Nov, bukan 26 Nov 00:42 UTC
- Gambar: "Explosion near tanker 50 nm west of Dubai — UKMTO reports the blast at 00:42 UTC."
  Timeline juga memimpin dengan "00:42 Tanker blast off Dubai".
- Bukti primer: dokumen peringatan UKMTO 222-26 sendiri menulis Incident Date **25 Nov 2026, 21:30 UTC**,
  sumber Master. InvestingLive: "2130 GMT on Wednesday". Pers sudah memberitakannya 25 Nov malam
  (pouyam 23:41 UTC, jbiznews 23:59 UTC). Angka "00:42 UTC 26 Nov" hanya muncul di agregator sekunder
  (Global Incident Tracker) — kemungkinan jam ingest, bukan jam kejadian.
- Fix: HAPUS #11 (dan entri timeline 00:42-nya), ganti dengan cerita 26 Nov terverifikasi. Jangan
  cuma ubah jamnya: kejadiannya memang 25 Nov.

### B2 — #12 Iowa "huge success": ledakan DAN pernyataannya sama-sama 25 Nov
- Gambar: "US Army calls Iowa blast a 'huge success'" / "Controlled blast of 68 barrels of lead azide."
- Bukti: detonasi Rabu 25 Nov 09:00 CST, Middletown, Iowa. Kutipan "HUGE success" adalah post X
  Acting Secretary of the Army Adam Telle bertanggal **25 Nov 2026** (dikutip KWQC/AP). Reuters
  "UPDATE 3" berstempel 26 Nov 02:48 IST = 25 Nov 21:18 UTC. AP/Reuters/KWQC semua 25 Nov waktu AS.
- Build-log sendiri sudah menulis pengecualian "US Army Iowa lead-azide detonation itself — Wed 25 Nov"
  di daftar eksklusi — tapi versi "pernyataan"-nya dimasukkan. Itu tidak konsisten: pernyataannya pun
  25 Nov. Judge yang kenal berita ini (ledakan Iowa adalah cerita besar AS tanggal 25 Nov) akan
  mengenalinya sebagai berita kemarin.
- Fix: HAPUS #12, pindahkan ke DATE CHECK sebagai eksklusi (sudah setengah ada di sana).

### B3 — #18 Samsung Electro-Mechanics ₩1,73tn: laporan Yonhap-nya 25 Nov
- Gambar/daftar ALSO ON: "Samsung Electro-Mechanics to cancel ₩1.73tn of own shares — Yonhap",
  build-log menstempel "SEOUL, Nov. 26, 2026".
- Bukti: Yonhap via Korea JoongAng Daily: "said **Wednesday**", published **2026-11-25T11:33:31Z**;
  board decision 25 Nov, pembatalan dijadwalkan 2 Des. Angkanya benar (₩1,73tn ≈ $1,28 miliar,
  2.053.430 saham, ~2,65%), tanggalnya salah.
- Fix: HAPUS #18. Ini juga bukti bahwa stempel tanggal blok Korea di build-log tidak bisa dipercaya
  buta-buta (lihat M3).

### B4 — #38 Bonus Singapura 1,55 bulan: diumumkan 25 Nov
- Gambar: "Singapore civil servants get 1.55-month year-end bonus — Straits Times".
- Bukti: angka 1,55 bulan BENAR (PSD: AVC 1,55 bulan + $300/$600 junior), tapi PSD **mengumumkannya
  Rabu 25 Nov 2026** (psd.gov.sg, redhot.sg: "announced on Wednesday (Nov 25)"; CNA 25 Nov).
  Koran Straits Times edisi 26 Nov memuatnya — tapi "first reported" adalah 25 Nov, standar yang sama
  dengan yang dipakai entry untuk meng-eksklusi tarif AS (diumumkan 25 Nov).
- Fix: HAPUS #38 (atau ganti dengan cerita Singapura 26 Nov yang lain bila ada).

### B5 — #5 BOK: subline "First hike in two years" SALAH secara faktual
- Gambar: "Bank of Korea lifts key rate to 3.25% — First hike in two years; growth raised to 3.9%."
- Bukti: 3,25% dan growth 3,3%→3,9% BENAR (Reuters/MoneyToday, 26 Nov). Tapi ini adalah **kenaikan
  ketiga sejak Juli 2026** (AJP: "third rate hike this year"; investinglive: "third increase since
  July"). Yang "pertama dalam dua tahun" adalah LEVEL-nya (pertama kali di atas 3% sejak Nov 2024),
  bukan hike-nya. Subline ini tertukar level dengan hike.
- Fix: ganti subline menjadi "Third hike since July; first time above 3% since Nov 2024"
  (atau hapus klausa "First hike in two years").

Catatan: B1–B4 semuanya cerita 25 Nov yang masuk dengan standar yang sama yang dipakai entry untuk
meng-eksklusi Cairo/tarif/GDP/Shenzhou. Setelah B1–B4 diperbaiki, klaim DATE CHECK menjadi benar lagi.
Tidak ada blocker soal hero: ketiganya lolos verifikasi (lihat tabel).

---

## Majors (menurunkan rank secara berarti)

### M1 — Skew regional: East Asia 14/48 (29%), 10 cerita Yonhap/Korea beruntun #16–25
- Bukti: region bar entry sendiri: East Asia 14 · Europe 11 = 25/48 (52%) di dua region; South America 1,
  Africa 2, Middle East 3. Rank 1: East Asia 3, South Asia 6, Europe 6, max 6 per region — jauh lebih
  seimbang. Pola APAC/Korea-heavy yang sama sudah jadi major M6 di ni25.
- Dampak: kriteria judge #2 eksplisit "lintas region dan field". Field kita bagus (20 field, lebih baik
  dari rank 1 yang 15 dan rank 4 yang 10), tapi distribusi regionnya timpang dan 10 item Yonhap
  berurutan sangat terlihat saat judge memindai daftar ALSO ON.
- Fix: pangkas blok Korea #16–25 menjadi 4–5 terkuat (BOK #5, Kospi #8, Kim #4, dialog #17, plus satu),
  isi slot yang lepas dengan cerita 26 Nov terverifikasi dari region tipis (Afrika/LatAm/Timur Tengah).
  Kandidat yang dibawa kompetitor dan layak dicek tanggalnya dulu sebelum dimasukkan: serangan Niger
  (30 tewas, halaman depan Punch 26 Nov), serangan Gaza/Hamas, pemadaman listrik Rusia di Ukraina,
  upah garmen Bangladesh +36%. Jangan masukkan tanpa verifikasi tanggal independen — itu jebakan yang
  sama dengan B1–B4.

### M2 — Peta "WHERE IT HAPPENED" hampir tak terbaca sebagai peta
- Bukti: di full-size, peta adalah strip abu-abu pucat; benua nyaris tak dikenali (Amerika Selatan
  tinggal segitiga kecil tempat pin 16 menempel), pin merah melayang di atas gumpalan abu-abu.
  Di 300px tinggal pita abu-abu samar. Rank 1 dan rank 4 sama-sama punya peta dunia yang langsung
  dikenali bentuk benuanya + pin bernomor yang jelas.
- Dampak: craft (kriteria #5) — ini elemen visual terlemah di halaman, dan peta adalah salah satu pola
  wajib top-10.
- Fix: gambar ulang peta dengan bentuk benua yang tegas + kontras lebih tinggi (atau pakai outline
  benua yang lebih tebal); pastikan pin 1–17 menempel di lokasi yang benar. Ini satu-satunya perbaikan
  craft yang butuh kerja gambar, sisanya edit teks.

### M3 — Stempel tanggal build-log tidak bisa dipercaya buta-buta; butuh re-verifikasi 44 cerita sisa
- Bukti: build-log menstempel #18 "Nov. 26" padahal 25 Nov (B3), #11 "00:42 UTC 26 Nov" padahal 21:30 UTC
  25 Nov (B1), #38 "26 Nov" padahal diumumkan 25 Nov (B4), #12 "statement 26 Nov" padahal 25 Nov (B2).
  Empat stempel salah dari 48. Saya hanya memverifikasi independen hero + sekunder rawan-tanggal +
  angka kunci + semua eksklusi + spot-check (#17, #19, #27, #29, #38, #39, #43); sisanya (#9, #13–#16,
  #20–#26, #28, #30–#36, #40–#42, #44–#48) masih mengandalkan stempel log.
- Fix: sebelum submit ulang, verifikasi independen tiap cerita yang tersisa (minimal tanggal publikasi
  pertama dari sumber bernama). Grey items di bawah (#17, #29, #37) perlu catatan jujur di DATE CHECK
  atau diganti — jangan biarkan satu klaim tanggal salah lagi lolos.

### M4 — Seleksi: ekor ALSO ON berisi filler ringan, sementara cerita berat 26 Nov milik kompetitor tidak ada
- Bukti: #32 BBC–Met Office kerja sama cuaca, #40 HealthHub slot poliklinik, #46 perang gitar
  Stratocaster, #25 KBO pemain asing 2027, #23 kunjungan ketua Hanwha ke Ourhome, #20 Seoul minta Oman
  dukung unit Cheonghae — semuanya benar tapi ringan. Bandingkan sekunder rank 1 (Gaza, laser Blysk,
  Rusia potong listrik 5 region, upah Bangladesh +36%, data ~500.000 tewas perang Rusia) dan rank 4
  (Nigeria 30 tewas, blokir birthright order, Rusia ~500.000, Nepal ₹15.000 crore, Bogotá sandera).
- Dampak: kriteria #2 (cerita paling konsekuensial). Hitung cerita 48 tidak menolong bila 8–10 di
  antaranya filler sementara kompetitor membawa cerita berat yang sama harinya.
- Fix: dalam ronde fix yang sama, ganti 4–6 filler teringan dengan cerita berat 26 Nov yang tanggalnya
  sudah diverifikasi (lihat kandidat di M1). Catatan jujur: saya belum memverifikasi tanggal kandidat
  tersebut satu per satu — verifikasi dulu, jangan ulangi B1–B4.

### M5 — #7 Riyadh: peristiwanya BENAR, tapi sumber + subline-nya lemah
- Bukti: pencegatan 2 rudal balistik Houthi ke Riyadh dini hari 26 Nov TERKONFIRMASI — Al Jazeera live
  blog 26 Nov 04:52 ("A blast hits Sanaa… as the Saudi coalition intercepts missiles over Riyadh"),
  plus banyak laporan se-hari yang sama; rank 4 bahkan menjadikannya hero #1. Jadi #7 boleh bertahan.
  Tapi sumber yang dikutip hanya "The Insight International" — outlet niche nyata (25 tahun online,
  meliput beat ini tiap hari) tapi bukan AP/Reuters; dan subline "a day after Jeddah drone" TIDAK
  terverifikasi (yang ada: serangan drone Houthi ke menara finansial Riyadh hari Selasa, bukan Jeddah).
- Fix: ganti atribusi menjadi koalisi/Al Jazeera (yang menguatkan peristiwa), dan hapus/perbaiki klausa
  "a day after Jeddah drone".

### M6 — Item abu-abu tanggal (bukan blocker, tapi rawan ketahuan judge — putuskan di ronde fix)
- #29 Nigeria FX: angka BENAR (82,36% → $164,28jt dari $931,23jt) dan headline Punch BENAR bertanggal
  26 Nov 00:54 GMT — tapi datanya adalah perdagangan **Selasa 24 Nov**. Report-date 26 Nov membuatnya
  defensible, tapi judge bisa membacanya sebagai cerita 24 Nov. Pertahankan hanya bila DATE CHECK
  menambahkan catatan jujur, atau ganti.
- #37 Zambia: laporan Al Jazeera BENAR terbit 26 Nov, tapi surat polisi pemblokirannya **17 Nov** dan
  protes yang diblokir dijadwalkan **25 Nov**. Sama seperti #29: report-nya 26 Nov, peristiwanya bukan.
  Framing gambar ("Zambia blocks protest…") tidak menyebut tanggal — abu-abu, bukan salah terang.
- #17 Dialog Korea-Jepang: Yonhap BENAR 26 Nov 02:33 UTC, tapi pertemuannya 25 Nov di Tokyo.
  Sama: report-date defensible.
- Prinsip yang saya pakai: report pertama 26 Nov = lolos; report pertama 25 Nov = gagal (B1–B4).
  Ketiga item ini lolos di report-date — tapi ketiganya akan lebih aman dengan satu baris jujur di
  DATE CHECK (seperti yang sudah dilakukan untuk Macy's dan Guzmán).

---

## Verifikasi fakta (independen, via pencarian web 26 Nov 2026 ~11:00 WIB)

| # | Cerita | Hasil | Bukti / sumber |
|---|---|---|---|
| 1 | Macy's 100th parade pindah ke Sabtu | **LOLOS** | Reuters 25 Nov: ditunda ke Sabtu 28 Nov 08:30 EST, pertama kali karena cuaca dalam 100 tahun; NWS gusts 50–60 mph. Pengumuman Rabu malam AS — footer gambar jujur soal ini; rank 1 melakukan hal yang sama. |
| 2 | India 18 tahun 26/11 + Constitution Day | **LOLOS** | 26 Nov 2026 = 18 tahun serangan Mumbai (166 tewas) + Hari Konstitusi ke-77; Preamble dibaca 23 bahasa (MyGov/PIB). |
| 3 | Gukesh–Sindarov Game 3, Jenewa | **LOLOS** | Game 3 Kam 26 Nov 15:00 CET, Sindarov Putih, skor 1–1 setelah 2 remis (38 + 20 langkah), pertama ke 7,5 poin, hadiah $2,5jt (FIDE/ChessBase). Satu sumber agregator menulis Game 3 27/11 — ditolak mayoritas sumber. |
| 4 | Kim nuklir taktis | **LOLOS** | KCNA lapor Kam 26 Nov; inspeksi 25 Nov; "tactical nukes across multiple domains" (Reuters/ Yonhap via AJP). |
| 5 | BOK 3,25% | **LOLOS angka, GAGAL subline** | 3,25% (+25bp dari 3,00%), growth 3,3%→3,9% BENAR (Reuters, 26 Nov 01:00 GMT). Tapi "First hike in two years" SALAH — kenaikan ketiga sejak Juli (B5). |
| 6 | KTT EU Brussels | **LOLOS** | Special European Council 26–27 Nov, MFF 2028–34 + pendanaan Ukraina 2027 (Consilium). Timeline 09:00 UTC = 10:00 CET, benar. |
| 7 | Rudal Riyadh | **LOLOS peristiwa, sumber lemah** | 2 rudal balistik dicegat dini hari 26 Nov — Al Jazeera live blog 26 Nov 04:52 + laporan se-hari; rank 4 hero-kan. The Insight International = outlet niche nyata, bukan tier-1. Subline "Jeddah drone" tak terverifikasi (M5). |
| 8 | Kospi +1,9%, Nikkei +1,6% | **LOLOS** | Snapshot intraday 26 Nov: Kospi +1,2% pagi → +1,94%/+2,07%; Nikkei +1,3% → +1,65%/+1,81%. Angka entry dalam rentang. |
| 9 | BOJ Tamura | **BELUM DIVERIFIKASI independen** | Sumber Reuters, pidato Tokyo 26 Nov (klaim log). Risiko rendah, tapi belum saya cek sendiri. |
| 10 | Ledakan Sanaa | **LOLOS** | Al Jazeera live blog 26 Nov: "A blast hits Sanaa after air strikes near the airport". (Ada juga ronde serangan Selasa malam — item ini yang 26 Nov.) |
| 11 | Tanker Dubai 00:42 UTC | **GAGAL** | UKMTO 222-26: insiden **25 Nov 21:30 UTC**; pers terbit 25 Nov 23:41 UTC. Lihat B1. |
| 12 | Iowa "huge success" | **GAGAL** | Ledakan + pernyataan 25 Nov (post X SecArmy 25 Nov; Reuters 25 Nov 21:18 UTC). Lihat B2. |
| 13–15 | UK-EU treaties / stalking / Norfolk | **BELUM DIVERIFIKASI independen** | Klaim BBC terbit 26 Nov (log). Risiko rendah; cek ulang di ronde fix (M3). |
| 16 | Seoul shares open higher | **BELUM DIVERIFIKASI independen** | Cerita pagi 26 Nov, plausibel; belum dicek sendiri. |
| 17 | Dialog Korea-Jepang | **LOLOS (abu-abu)** | Yonhap 26 Nov 02:33 UTC; pertemuan dengan Mori 25 Nov di Tokyo. Report-date lolos. |
| 18 | Samsung ₩1,73tn | **GAGAL tanggal, angka benar** | Yonhap 25 Nov 11:33 UTC, board 25 Nov. Lihat B3. |
| 19 | Bad-loan bank Korea Q3 | **LOLOS** | Data FSS "showed Thursday": SBL 0,62% akhir Sep (Korea JoongAng Daily/Yonhap). |
| 27 | Baterai 600.000+ rumah | **LOLOS (atribusi salah)** | Climate Council release "THURSDAY NOVEMBER 26 2026": 600.000+ keluarga. Tapi sumbernya **Climate Council (NGO)**, bukan "Australian Govt" seperti tertulis. Minor. |
| 29 | Nigeria FX 82%→$164m | **LOLOS angka, ABU-ABU tanggal** | 82,36% → $164,28jt dari $931,23jt BENAR (CBN via Punch/BusinessDay); headline Punch 26 Nov 00:54 GMT — tapi data perdagangan Selasa 24 Nov (M6). |
| 38 | Bonus Singapura 1,55 bln | **GAGAL tanggal, angka benar** | 1,55 bulan BENAR, tapi PSD umumkan **25 Nov** (B4). |
| 39 | Fraud 23%→1.515 | **LOLOS (angka)** | SG digest 26 Nov: 1.515 kasus fraud/scam, +23%. Tanggal laporan FIDReC belum dicek independen. |
| 43 | Guzmán 98, pemakaman | **LOLOS** | Wafat Sel 24 Nov umur 98; misa + pemakaman Kam 26 Nov (Meganoticias/CHV). Framing log jujur. |
| — | Angka kunci lain | **LOLOS** | 60 mph (gusts 50–60, NWS); 100 tahun parade; 18 tahun 26/11; +1,9% Kospi (snapshot, lihat #8). |
| — | Eksklusi DATE CHECK | **SEMUA BENAR** | Cairo 31 tewas = AP 25 Nov 19:54 EST ✓; tarif AS 14 ekonomi = Reuters 25 Nov ✓; GDP AS 4,3% = BEA release 25 Nov ✓; Shenzhou-24 = 25 Nov 00:18 UTC, astronot Pakistan pertama ✓; Kospi −6,2% = Rabu 25 Nov ✓. Daftar eksklusi ini akurat — yang membuat B1–B4 makin disayangkan: standar yang sama tidak diterapkan ke cerita yang masuk. |

Tidak diverifikasi independen (mengandalkan build-log; risiko dicatat di M3): #9, #13–#16, #20–#26,
#28, #30–#36, #40–#42, #44–#48.

---

## Perbandingan vs rank 1 & rank 4

**Yang sudah setara:**
- 3 hero SAMA dan semuanya benar (Macy's / India 26/11 / Gukesh Game 3) — lead wajib top-10 terpenuhi.
- Format koran bergambar: masthead + tanggal + region bar + fields bar + timeline UTC + numbers strip
  6 angka + 3 hero + 12 sekunder SEMUA berilustrasi + ALSO ON bernomor + peta + DATE CHECK.
- Jumlah cerita 48 (rank 1: 36, rank 4: 50) dan 20 fields (rank 1: 15, rank 4: 10) — breadth
  hitungannya kompetitif, bahkan unggul di fields.
- DATE CHECK dengan daftar eksklusi panjang dan catatan jujur (Macy's diumumkan Rabu malam; Guzmán
  wafat 24 Nov) — sejajar dengan rank 4 yang juga meng-eksklusi Cairo/tarif/Shenzhou secara eksplisit.
- Keterbacaan 300px: masthead + headline hero terbaca; ALSO ON jadi blur kecil — SAMA seperti
  rank 1 dan rank 4 (daftar mereka juga tak terbaca di 300px). Bukan pembeda.

**Yang kalah:**
- **Tanggal:** rank 1 sendiri memasukkan cerita 25 Nov (Cairo, tarif, Ras Tanura, Shenzhou) sebagai
  cerita — tapi entry kita mengklaim universal "every story first reported 26 Nov" dan melanggarnya
  di 4 item, termasuk 2 item sekunder bernomor (#11, #12) yang mudah dicek judge. Rank 4 lebih bersih
  di titik ini (eksklusinya eksplisit dan konsisten).
- **Keseimbangan region:** rank 1 max 6/region; kita East Asia 14 + Europe 11, South America 1,
  Afrika 2. Rank 4 juga menumpuk (banyak New Delhi) tapi tidak 10-berurutan dari satu wire.
- **Peta:** rank 1 dan rank 4 punya peta dunia yang langsung dikenali; peta kita strip abu-abu pucat
  yang nyaris tak terbaca sebagai peta (M2).
- **Bobot seleksi sekunder:** 10 sekunder rank 1 semuanya berat (perang, tarif, upah, data tewas);
  sekunder kita bagus, tapi ekor ALSO ON kita lebih banyak filler ringan (M4).
- **Ilustrasi hero:** rank 1 sedikit lebih kuat (balon + lilin + jam catur 1:32); hero kita setara
  dalam komposisi, selangkah di bawah dalam detail.
- **Timeline:** rank 1 enam entri ber-waktu semua; kita 7 entri tapi 2 tak ber-waktu ("EARLY",
  "ALL DAY") dan entri pertamanya justru item tanggal-salah B1.

**Kompilasi pagi 03:53 UTC (gap 2):** terkonfirmasi BUKAN kerugian vs lapangan — rank 4 sendiri
menulis "Not yet: Chess Game 3's result (15:00 CET) and the parade (09:00 EST)". Hasil Game 3 dan
hasil KTT EU belum diketahui saat review ini (~04:00 UTC); tidak ada cerita siang 26 Nov yang
sudah diketahui dan terlewat yang merugikan vs kompetitor pagi ini. Rebuild sehari-penuh (~23:30 UTC)
tetap bisa menaikkan estimasi (hasil Game 3 + hasil KTT + pasar), tapi itu ronde kedua — ronde fix
pertama (B1–B5 + M1 + M2) adalah yang paling berdampak per usaha.

---

## Estimasi rank + peluang top 50 (jujur)

- **Entry v1 apa adanya: estimasi rank ~45–70, peluang top 50 ~25–35%.**
  Alasan: lapangan padat — top 25 semua masih 12W-0L/11W-1D provisional dari 3.149 submission, urutan
  ditentukan tie-break. Struktur v1 sudah pola top-10, tapi dalam duel 2v2 lawan entry berstruktur
  sama, v1 kalah di sumbu yang paling dijaga judge (tanggal/faithful): 4 cerita 25 Nov + 1 subline
  faktual salah + skew Korea + peta lemah. Koordinator memperkirakan top-50 35–45% SEBELUM
  verifikasi ini; temuan B1–B4 memaksa revisi ke bawah. Target TOP 10 dan lantai rank 25 TIDAK
  kredibel untuk v1.
- **Setelah 1 ronde fix (B1–B5 + M1 + M2 + ganti 4–6 filler): estimasi rank ~20–40,
  peluang top 50 ~50–60%, top 25 menjadi mungkin.** Satu ronde fix menaikkan secara nyata karena
  semua blocker adalah penghapusan/penggantian item + 1 perbaikan subline + gambar ulang peta —
  bukan rebuild. Yang TIDAK bisa dijanjikan ronde fix ini: top 10 (butuh juga hasil Game 3 + hasil
  KTT + seleksi berat yang setara rank 1 — itu baru didapat rebuild sehari-penuh).
- **Satu putaran perbaikan paling berdampak:** hapus #11, #12, #18, #38 + perbaiki subline BOK +
  pangkas blok Korea ke 4–5 item dan isi dengan 3–4 cerita berat 26 Nov terverifikasi dari
  Afrika/LatAm/Timur Tengah + gambar ulang peta. Itu satu ronde, dan itu yang harus dikerjakan
  sebelum submit apa pun.

---

## Minors

- #27 atribusi sumber: tulis "Climate Council", bukan "Australian Govt" (rilisnya dari Climate Council).
- Timeline: beri jam pada "EARLY Riyadh" dan "ALL DAY India" bila ada jam pastinya; kalau tidak ada,
  biarkan — tapi jangan memimpin timeline dengan item tanggal-salah (B1).
- #7: ganti atribusi ke koalisi/Al Jazeera (M5).
- Hero art sedikit di bawah rank 1 dalam detail — bukan prioritas; jangan sentuh bila waktu mepet.
- File teknis bersih: 432.185 byte ≤ 1 MiB, JPEG 1024×1024 lengkap (SOI/EOI), tanpa teks
  terpotong/overlap/garble di full-size; build deterministik (2× byte-identik, sha256 cocok).
  Tidak ada masalah teknis yang menghalangi submit — masalahnya murni isi/tanggal/seleksi.
