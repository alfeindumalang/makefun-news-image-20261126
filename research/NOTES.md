# Research notes — news-image-20261126
Date of research: Thursday 26 November 2026, ~07:30–08:00 WIB (00:30–01:00 UTC).
Competition: "Sum up 26 November's world news in one image". Deadline 28 Nov 2026 07:00 WIB.
Opened 26 Nov 2026 00:00 UTC; this session starts after the opening.

## Method
Searched with the news vertical for stories tied to Thursday 26 November 2026,
then verified each candidate's date. A story counts if the event happened on
26 Nov, or was first reported late on 25 Nov (US evening) so that it is the
morning's news in WIB on 26 Nov — the same rule the 25 Nov entry used for
its own day. Anything whose event/report date was 25 Nov in every time zone
was REJECTED, even if it was still topping the feeds this morning.

## Rejected (not 26 Nov — NOT used)
- PCE October (+3.8% YoY) + GDP Q3 revised to 4.3% + Fed December hike odds
  ~96% — reported Wed 25 Nov 20:30 WIB. Yesterday's news; the briefing
  already covered it. The Beige Book below is the fresh 26 Nov angle on
  the same Fed story.
- BTC fell to ~US$57,300 then rebounded above US$60,000 — Wed 25 Nov.
- ETF spot BTC November outflow record US$4.94 billion — through 24 Nov,
  reported 25 Nov.
- Trump unveils new Section 301 tariffs on 14 partners — unveiled Wed
  25 Nov (Reuters, WASHINGTON Nov 25). Only Taipei's reply on the 26th
  is used, as its own story.
- Sudan RSF drone strikes kill 19 in Blue Nile — strikes Tue 24 Nov night,
  reported Wed 25 Nov (Reuters Nov 25). A 25 Nov story.
- Houthis claim attack on Saudi refinery Ras Tanura, Brent tops $94 —
  Wed 25 Nov.
- Two tankers hit naval mines in the Strait of Hormuz — Wed 25 Nov
  (Reuters, DUBAI Nov 25).
- FCC authorises SpaceX to deploy 1 million satellites ("Starmind") —
  Nov 25 (FCC document DA-26-1273).
- Israeli airstrike kills Hamas official Mohammad Abuelouf and family in
  Gaza — early Wed 25 Nov (Reuters, CAIRO Nov 25).
- Lebanon plans second airport at Kleiat — Reuters, Nov 25.
- Bangladesh raises garment minimum wage 36% to 17,000 taka — Wed 25 Nov
  (AP 02:20 ET = 14:20 WIB 25 Nov).
- Germany 2027 budget / aid cuts — budget committee finalised 13 Nov;
  Wadephul's Bundestag speech Wed 25 Nov.
- US government shutdown risk over Iran war funding — Reuters, 20 Nov.
- Jensen Huang / Nvidia CEO status — contradictory across sources;
  excluded entirely per the brief. No Nvidia item in the paper.
- Shenzhou-24 launch carrying a Pakistani astronaut — 25 Nov.
- Pope Leo XIV lung cancer — October story; stale.

## Used — all genuinely tied to Thursday 26 November 2026

### 1. LEAD — Fuel tanker fire on Cairo's Ring Road, 31 killed
- A fuel tanker overturned and exploded on the Greater Cairo Ring Road,
  above a tunnel in the Al-Warraq district of Giza, on Wednesday,
  setting dozens of cars and motorcycles ablaze. Egypt's Health Ministry
  first reported at least 30 dead; the toll was updated to 31 killed
  and 21 injured, described as preliminary.
- AP timestamped the report 25 Nov 15:15 ET (20:15 UTC) — 03:15 WIB
  on Thursday 26 Nov, so it is the morning's news in Asia.
- The paper uses the updated toll: 31 killed, 21 injured.
- Sources: Associated Press (Cairo, 25 Nov); Reuters (CAIRO, Nov 25,
  via SRN News).

### 2. Fed Beige Book: wages pick up as growth holds
- The Federal Reserve's Beige Book, released Wednesday, says eight of
  its twelve districts grew slightly to moderately and four were flat.
  Employment rose slightly; wages and benefits rose moderately, an
  uptick from modest increases in the previous report, driven by
  hard-to-fill posts, cost-of-living adjustments and benefit costs.
  Prices rose moderately overall, while input-cost growth generally
  outpaced selling prices.
- Coverage reached the wires late Wednesday US time (TradingView
  2026-11-25T23:19:38Z = 06:19 WIB Thursday) — morning news in WIB.
  It lands alongside the hot October PCE (+3.8% YoY) and the 4.3% GDP
  revision, leaving markets pricing a December hike at roughly 96–100%.
  The paper claims only the Beige Book's own findings, not the PCE
  figures as today's news.
- Sources: Federal Reserve (Beige Book, 25 Nov); Bloomberg Law;
  TradingView.

### 3. Taiwan confident of keeping its 15% tariff rate
- TAIPEI, Nov 26 (Reuters) — Taiwan's government said on Thursday it
  is confident of keeping its existing 15% tariff rate from the United
  States, after Washington proposed new duties of up to 40% on 14
  trading partners under its Section 301 overcapacity probe.
- The USTR plan caps China at 20%, South-East Asia (incl. Indonesia)
  at 18%, Japan, South Korea, Taiwan, the EU and Switzerland at 15%,
  Singapore at 10%; India 17% (25% if talks fail), Vietnam 20% (35%
  if talks fail). Rates are proposals only: public comments run to
  5 Jan 2027, hearings from 25 Jan, nothing effective before January.
  Taiwan points to the reciprocal-trade agreement and investment MOU
  signed in Jan–Feb 2026, covering semiconductors and tech worth over
  70% of its exports to the US.
- Sources: Reuters (TAIPEI, Nov 26); Executive Yuan press release
  (just after midnight, 26 Nov).

### 4. Indonesia gold mine flood: 9 dead, 17 trapped
- Heavy rain late Monday caused the Ciseureuh River to overflow into a
  100-metre shaft at an unauthorised gold mine in the Pongkor area of
  Bogor regency, West Java. Eleven miners escaped; rescuers recovered
  nine bodies on Wednesday and were searching for 17 more believed
  trapped, with 325 rescuers pumping water from the shafts.
- The AP report was filed 25 Nov 12:28 ET — 00:28 WIB Thursday 26 Nov
  — so the toll rising to nine is the morning's news in WIB. The mine
  is unauthorised and unrelated to state miner Antam's nearby Pongkor
  operations; the rescue was delayed ~16 hours because the illegal
  operation was not reported.
- Sources: Associated Press (JAKARTA, 25 Nov).

## Image plan (1024x1024 newspaper front page)
- Masthead: THE WORLD TODAY — THURSDAY, 26 NOVEMBER 2026.
- Lead story 1 (Cairo fire) across the top, with a drawn panel: a night
  highway, cars on the ring road, two-tone flames and rising smoke.
- Stories 2 (Beige Book) and 3 (Taiwan tariffs) side by side in the
  middle, text only.
- Story 4 (Indonesia mine) as a bottom strip, plus a sources footer.
- All text drawn with PIL (DejaVu fonts); no AI image generation, no network.
- main.py draws the page itself; assets/entry.png (rendered by the same
  code) is a fallback if Pillow/fonts are missing in the grading container.

## Build log (this session)
- Rev 1: main.py written in full, fresh code; rendered twice,
  byte-identical, 131,772 bytes.
- Rev 2: lead panel flames redrawn with a hotter inner tongue; bottom
  strip text shortened so it no longer collides with the footer rule.
  Re-rendered twice, byte-identical, 128,938 bytes.
- Rev 3: smoke repositioned to rise from the two tallest flames.
  Re-rendered twice, byte-identical, 128,780 bytes. Fallback path
  tested: fallback_bytes() returns the shipped image (same sha256).
