# V10 TODO — 7-state QC: research DONE, application PAUSED

Status snapshot, August 5, 2026. The session was wound down mid-task at the user's request.
Everything below is captured so a future session can finish without redoing any research.

## Where the live map stands

The **shipped file is v0.2** (the WI/IL/MI QC pass): 158 rivers, 347 pinned landings, core-fade
(BYO tails) rendering, QC gate green. It is mirrored at project doc `river-map/midwest-kayak-rivers.html`
and live at https://maherjr-lab.github.io/RiverMaps/ (user renames the file to index.html and pushes
via GitHub Desktop from C:\Users\maher\Documents\Rivers\RiverMaps).

## What got FINISHED this round (do not redo)

1. **7-state QC research is COMPLETE.** Five research agents covered all 65 green rivers in
   KY, WV, OH, MN, IN, IA, MO — full-run extents, corrected mileages, 3–6 sourced access points
   per river (coordinates only where a source published them), dam/portage hazards, and new
   outfitter finds. Their verified JSON payloads are saved as project docs:
   - `river-map/qc7/KYWV.json` (17 rivers)  ·  `river-map/qc7/OH.json` (10)
   - `river-map/qc7/MNIA.json` (18)  ·  `river-map/qc7/IN.json` (11)  ·  `river-map/qc7/MO.json` (9)

2. **The application script is WRITTEN and saved**: `river-map/qc7-apply-script.py`.
   It encodes every editorial decision — corrected TRIP miles for all 65 rivers, bbox
   unions + 7 bbox overrides for truncated runs, 9 spine rewrites, which landings get pinned
   vs. unpinned (null-coord or chain-breaking ones), and full rewritten stretch/watch texts
   for every river. Copy it next to build_data.py and run `python3 apply.py` — it edits
   build_data.py in place. (It expects the payload JSONs at /tmp/qc7/ — adjust the path at top.)

3. **BYO-boat toggle is CODED in template.html** (saved as project doc `river-map/template.html`).
   Mirrors the Big Rivers toggle exactly as requested: checkbox "BYO-Boat Rivers: Visible/Hidden"
   (default Visible) next to the big-river toggle; when hidden, outfitter-less green rivers draw
   as the same thin grey ghost dash (non-interactive) and their rows disappear from the sidebar
   (CSS `body.nobyo .riv.byo{display:none}`). Code paths touched: legend row area (#bigrow),
   `hiddenByToggle()`, new `applyByoToggle()`, row-class assignment (`byo` class), listener at boot.
   **NOT yet built into the deliverable HTML and NOT yet tested.**

4. **build_data.py current state saved** as project doc `river-map/build_data.py` — this is the
   v9/v0.2 data layer (WI/IL/MI corrections applied; 7-state corrections NOT yet applied).
   `outfitters_data.py` is unchanged from the mirror in `river-map/outfitters-data.md`.

## What is NOT done (the actual TODO, in order)

1. Run `qc7-apply-script.py` against build_data.py, then `python3 build_data.py` (expect
   ~158 rivers, ~570+ landings, 0 bbox violations). Fix any assert it trips (bbox/spine fit).
2. Rebuild the HTML: inject data.json into template.html at `%%DATA%%` →
   midwest-kayak-rivers.html (edit in place, never a new filename).
3. Run the offline QC gate (test/qc_v9.py pattern): all rivers glow, everyRiverDashed,
   casingsDashSync, buttCasings, core-fade present. Add a check that the BYO toggle ghosts
   rivers and hides their sidebar rows. Screenshot both toggle states.
4. **Outfitter roadmap Excel — user's question was never answered in-file.** Answer:
   river-outfitter-roadmap.xlsx (93 entries) covers the CAND dict as of v8 — that includes
   ~40 of the 65 seven-state rivers (e.g. mohican, littlemiami, cannon, root-mn, current,
   niangua...). It does NOT contain the 18 NEW candidates the QC agents just found (list
   below). Produce a NEW VERSION of the workbook that adds these rows (yellow Approved?
   columns blank — the user has approved NOTHING yet, on any river). Also add the same
   entries to CAND in outfitters_data.py (marks those rivers as outfitter-candidate =
   dashed style on the map).
5. Deliver the rebuilt HTML + new roadmap workbook; update project mirrors
   (midwest-kayak-rivers.html, outfitters-data.md, V3-PLAN.md → add v10 entry).

## 18 new outfitter candidates from the QC agents (for the roadmap + CAND)

| river id | outfitter | url |
|---|---|---|
| nolin | Lincoln Trail Outfitters | (tripadvisor listing only — verify site) |
| cacapon | Cacapon River Outfitters | https://cacaponriveroutfitters.com |
| elk-wv | Elk River Paddle and Yak | https://elkriverpaddleandyak.com/ |
| kokosing | Kokosing Valley Camp & Canoe | https://www.kokosingvalley.com |
| littlebeaver | Beaver Creek Kayak Company | https://beavercreekkayak.wordpress.com/ |
| grand-oh | Grand River Canoe & Kayak Rentals | https://grandrivercanoe.com/ |
| stillwater-oh | Barefoot Canoe | https://barefootcanoe.com |
| sandusky-oh | Ghoul Runnings Kayak Adventures | https://ghoulrunnings.com |
| rum | Country Camping — Rum River Tubing & Paddling | https://www.country-camping.com/tubing-and-paddling/ |
| zumbro | Zumbro Valley Canoe Rental | https://www.zumbrovalleycanoerental.com/ |
| crowwing | Gloege's Northern Sun Canoe & Kayak | https://canoethecrowwing.com |
| snake-mn | Snake River Outfitters of Minnesota | https://snakeriveroutfittersmn.com |
| kettle | Hard Water Sports | https://hardwatersports.com |
| yellow-ia | Big Foot Canoe Rentals | https://www.mononachamber.com/big-foot-canoe-rentals.html |
| turkey-ia | Turkey River Rentals | https://www.turkeyriverrentals.com/ |
| wapsi | Pinicon Ridge Watercraft Concession (Linn Co) | https://www.linncountyiowa.gov/1448/Watercraft-Concession |
| midraccoon | Raccoon River Retreats | https://raccoonriverretreats.com/ |
| wildcat | Wildcat Canoe and Kayak Too | https://www.wildcatcanoeandkayaktoo.com/ |

Updates to EXISTING candidates worth carrying into the roadmap notes: Morgan's Fort Ancient
livery (littlemiami) CLOSED Jan 2025; sugarcreek's Clements Canoes domain is now clementscanoes.net;
cuyahoga's Burning River Adventures now operates as paddletheriver.com; eel-in's only livery
(Ride the Eel) closed early 2025 — eel-in stays outfitter-less.

## Headline data corrections waiting in the payloads (why this matters)

Many mapped mileages were badly short: Rum 18→154, Zumbro 15→72, Cannon 15→58, Crow Wing
20→65, Missfl. Headwaters 30→58, Greenbrier 25→55, Cacapon 12→75, Cheat 10→44 (and the
"Cheat Narrows" label was on the wrong reach), Volga 10→50, Wapsi 15→48, Eel-IN 15→90 (six+
low-head dams), Current 25→88, Gasconade 25→76, Meramec 20→60, Little Miami 25→42.
Extent/endpoint errors fixed in the payloads: Red River KY (standard float ends at KY 77,
not Clay City), Licking KY (Blue Licks is 40+ mi away), Barren (two reaches conflated),
Rockcastle (MUST take out at Billows above the Narrows), Tippecanoe (Monticello is behind
the Lake Shafer dams — truncated to the SP→Winamac 12-mi float), Mississinewa (reservoir
splits the mapped run — remapped to the 5.3-mi Seven Pillars tailwater), Flatrock-IN
(direction was wrong — it flows TO Columbus), Maquoketa (Caves SP is not on the river),
Sandusky (Upper Sandusky→Fremont is ~65 mi, not 12), Cuyahoga (Kent/Cleveland are outside
CVNP), Wildcat (Adams Mill→Davis Ferry run), Upper Iowa (chimney rocks are ABOVE Decorah).
Safety-critical pins in watch texts: Wapsi's Anamosa low-head dam, Stillwater's mandatory
Englewood take-out, Grand-OH's Harpersfield dam, Mad River's dam below the put-in.

## Standing rules (unchanged)

Never invent coordinates or phone numbers (null/blank instead). New rivers only with a known
outfitter. NO public outfitter listings without user approval/agreements/legals/fees. Every
river line dashed/dotted, never solid (in-sync dashArray + butt caps on casings). Always edit
midwest-kayak-rivers.html in place. User has approved NOTHING in either workbook yet.
