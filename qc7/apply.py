import json, re

BD = "/home/claude/rivermap/build_data.py"
src = open(BD).read()

payloads = {}
for k in ["OH","MO","IN","KYWV","MNIA"]:
    payloads[k] = json.load(open(f"/tmp/qc7/{k}.json"))["corrections"]
corr = {c["id"]: c for p in payloads.values() for c in p}
print("rivers in payloads:", len(corr))

# ---- decisions ----
FORCE_UNPIN = {   # landings with coords we still don't pin (would break the A->B chain)
 "rockcastle": ["Bee Rock Boat Ramp / Campground (KY 192, Daniel Boone NF) - whitewater-section take-out only, NOT part of this float"],
 "mississinewa": ["SR 221 bridge boat ramp","Gas City Park launch (South H St)","Canoe Launch, 1811 N Washington St","CR 500 N bridge (last take-out above Mississinewa Lake)"],
}
MILES = {  # id -> corrected mapped-run miles
 "elkhorn":13,"red-ky":8,"barren":14.4,"nolin":9.2,"rockcastle":16.6,"floydsfork":19.7,"gasper":18.5,"rough-ky":23.5,
 "greenbrier":55,"sbpotomac":11.5,"cacapon":75,"cheat":44,"elk-wv":80,"coal-wv":11,"bluestone":19,
 "mohican":16.6,"littlemiami":42,"bigdarby":18,"kokosing":19.3,"mad-oh":9.6,"littlebeaver":23,"cuyahoga":16,"grand-oh":23,"stillwater-oh":14.2,"sandusky-oh":65,
 "rum":154,"cannon":58,"root-mn":45,"zumbro":72,"crowwing":65.5,"snake-mn":42,"kettle":22,"crow-mn":23,"missheadwaters":58,
 "upperiowa":38,"yellow-ia":22,"turkey-ia":34,"volga":50,"maquoketa":14,"wapsi":48,"boone-ia":27,"midraccoon":16.5,"raccoon":31,
 "sugarcreek":29,"tippecanoe":12,"blue-in":37,"whitewater-in":18,"wildcat":27,"bigpine":7,"flatrock-in":9,"driftwood":16,"eel-in":90,"cedarck-in":9,"mississinewa":5.3,
 "current":88,"jacksfork":37.6,"elevenpoint":35.6,"niangua":18.5,"meramec":60,"gasconade":75.8,"bigpiney":46,"huzzah":8.9,"northfork-mo":23,
}
BBOX_OVERRIDE = {  # truncated runs: replace bbox instead of union
 "red-ky":[37.75,-83.67,37.90,-83.44],
 "licking-ky":[38.08,-83.73,38.26,-83.50],
 "rockcastle":[37.15,-84.35,37.35,-84.10],
 "tippecanoe":[40.94,-86.75,41.18,-86.52],
 "mississinewa":[40.70,-86.12,40.80,-85.96],
 "wildcat":[40.42,-86.92,40.52,-86.46],
 "cedarck-in":[41.13,-85.17,41.28,-84.99],
}
SPINE_OVERRIDE = {
 "red-ky":[[37.802,-83.484],[37.817,-83.571],[37.820,-83.575],[37.828,-83.60],[37.835,-83.627]],
 "licking-ky":[[38.116,-83.537],[38.176,-83.619],[38.221,-83.698]],
 "rockcastle":[[37.30,-84.21],[37.24,-84.24],[37.17,-84.30]],
 "bluestone":[[37.479,-81.072],[37.538,-81.008],[37.584,-80.972],[37.607,-80.944]],
 "tippecanoe":[[41.117,-86.603],[41.052,-86.600],[40.956,-86.66]],
 "mississinewa":[[40.7498,-86.0126],[40.7507,-86.0664]],
 "wildcat":[[40.481,-86.509],[40.455,-86.65],[40.443,-86.763],[40.4385,-86.803],[40.441,-86.830],[40.476,-86.871]],
 "cedarck-in":[[41.252,-85.136],[41.23,-85.06],[41.203,-85.027],[41.146,-85.100]],
 "flatrock-in":[[39.55,-85.45],[39.43,-85.63],[39.30,-85.80],[39.205,-85.927]],
}

# ---- 1. TRIP miles ----
n_trip=0
for rid, mi in MILES.items():
    pat = re.compile(r'("%s":\()\s*[\d.]+\s*,' % re.escape(rid))
    src, n = pat.subn(lambda m: m.group(1)+str(mi)+",", src, count=1)
    n_trip += n
    if not n: print("TRIP MISS:", rid)
print("TRIP updated:", n_trip)

# ---- 2. spine overrides ----
for rid, sp in SPINE_OVERRIDE.items():
    lit = "[" + ",".join("[%s,%s]" % (a,b) for a,b in sp) + "]"
    pat = re.compile(r'( "%s":)\[\[.*?\]\],' % re.escape(rid))
    src, n = pat.subn(lambda m: m.group(1)+lit+",", src, count=1)
    if not n: print("SPINE MISS:", rid)
print("spines done")

# ---- 3. bbox: override or union ----
def parse_bbox(rid):
    m = re.search(r'\("%s","[^"]*","green",\[([^\]]+)\]' % re.escape(rid), src)
    if not m: return None, None
    return [float(x) for x in m.group(1).split(",")], m
n_bbox=0
for rid, c in corr.items():
    pts=[]
    for l in c.get("landings",[]):
        if l.get("lat") is not None and l.get("lon") is not None and l["name"] not in FORCE_UNPIN.get(rid,[]):
            pts.append((l["lat"],l["lon"]))
    for k in ("extend_upstream","extend_downstream"):
        e=c.get(k)
        if e and e.get("to"): pts.append(tuple(e["to"]))
    if rid in SPINE_OVERRIDE: pts += [tuple(p) for p in SPINE_OVERRIDE[rid]]
    old, m = parse_bbox(rid)
    if old is None: print("BBOX MISS:", rid); continue
    if rid in BBOX_OVERRIDE:
        nb = BBOX_OVERRIDE[rid]
    else:
        if not pts: continue
        la=[p[0] for p in pts]; lo=[p[1] for p in pts]
        nb=[min(old[0],min(la)-0.03), min(old[1],min(lo)-0.03), max(old[2],max(la)+0.03), max(old[3],max(lo)+0.03)]
        nb=[round(x,3) for x in nb]
    if nb!=old:
        lit=",".join(("%g"%x) for x in nb)
        src = src[:m.start(1)] + lit + src[m.end(1):]
        n_bbox+=1
print("bboxes changed:", n_bbox)

# ---- 4. landings block ----
rows=[]
extra_unpin={}
for state_key in ["KYWV","OH","MNIA","IN","MO"]:
    rows.append(" # ---- v10 QC pass: %s ----" % state_key)
    for c in payloads[state_key]:
        rid=c["id"]
        for l in c.get("landings",[]):
            nm=l["name"].replace('"',"'"); tn=(l.get("town") or "").replace('"',"'")
            if l.get("lat") is None or l.get("lon") is None or nm in [x.replace('"',"'") for x in FORCE_UNPIN.get(rid,[])]:
                extra_unpin.setdefault(rid,[]).append(nm + (" ("+tn+")" if tn and tn.lower() not in nm.lower() else ""))
                continue
            ty={"put-in":"p","take-out":"t","both":"b"}[l["type"]]
            rows.append(' ["%s","%s","%s","%s",%s,%s,"%s"],' % (rid,nm,tn,ty,l["lat"],l["lon"],l["source"]))
block="\n".join(rows)+"\n"
anchor=' ["nbchicago","Clark (Richard) Park / WMS Boathouse","Chicago","t",41.94336,-87.69515,"https://www.chicagoparkdistrict.com/parks-facilities/clark-richard-boat-launch"],\n'
assert anchor in src, "landing anchor missing"
src = src.replace(anchor, anchor + block, 1)
print("landing rows added:", sum(1 for r in rows if r.startswith(' [')))

# ---- 5. v10 patch block (stretch/watch/unpinned) before final data dump ----
STRETCH = {
 "elkhorn":"The Bluegrass classic, ~13 mi: Forks of the Elkhorn -> the Class I-II ledge water (upper ~6 mi to the AW/Elkhorn Acres access) -> Peaks Mill flatwater -> the Kentucky River (Still Waters Campground, fee).",
 "red-ky":"The Middle Red through Red River Gorge: KY 715 bridge -> Copperas Creek (USFS) -> the KY 77 iron bridge at Nada, 8 mi of Class I under the sandstone arches. Upper Red (Big Branch -> KY 715) is Class II-III+ expert water.",
 "barren":"Bowling Green water trail, 14.4 mi: State Street Bridge (below the low-head dam) -> Beech Bend -> Hines Landing -> Lonnie White Ramp at Thomas Landing. (The dam-release tailwater trail near Scottsville is a separate reach.)",
 "nolin":"Nolin dam tailwater -> the Green River confluence inside Mammoth Cave NP (7.5 mi) + 1.7 mi down the Green to Houchin Ferry, ~9 mi total.",
 "rockcastle":"Upper Rockcastle float water, 16.6 mi: Old Wilderness Road Ford (Livingston) -> I-75 bridge -> KY 1956 at Billows. TAKE OUT AT BILLOWS - the expert Class III-IV Narrows lie just below.",
 "licking-ky":"Cave Run Lake tailwater smallmouth float: dam tailwater ramp -> Moore's Ferry (KDFWR) -> Wyoming Ford carry-down below Slate Creek. (Blue Licks is 40+ river miles further - not a day-trip take-out.)",
 "floydsfork":"The Parklands of Floyds Fork water trail, 19.7 mi: North Beckley -> Fisherville -> Cane Run -> Seaton Valley -> Broad Run -> Cliffside (mandatory last take-out).",
 "gasper":"Scenic bluff run west of Bowling Green: River Road Bridge -> KY 1083 -> the KY 626 rapids cluster -> US 231 (classic 8.5-mi leg) -> the Barren River confluence VPA ramp, ~18.5 mi in all.",
 "rough-ky":"Rough River Dam tailwater -> Dundee (KY 69), 23.5 mi Class I-II. The Falls of Rough ledge/mill dam sits ~6 mi below the dam - portage (private property).",
 "greenbrier":"The longest free-flowing river in the East: Marlinton -> Seebert (Watoga SP) -> Renick -> Anthony -> Caldwell -> Ronceverte, ~55 river miles with the rail-trail alongside for bike shuttles. Classic day floats: Marlinton->Seebert (~10) and Anthony->Caldwell (~11).",
 "sbpotomac":"The Trough: Old Fields Bridge (US 220) -> South Branch WMA (McNeill) -> Harmison's Landing, 11.5 mi of Class I-II eagle-country canyon; continues to Romney. (Smoke Hole canyon upstream is a separate advanced run.)",
 "cacapon":"Wardensville -> Capon Lake -> Capon Bridge -> the Rt 127 'Caudy's Castle' Class II reach -> Cacapon Crossing -> Great Cacapon, ~75 river miles. Classic day trip: Capon Bridge -> Rt 127 (11.6 mi).",
 "cheat":"Upper Cheat River Water Trail: Parsons -> Holly Meadows -> St. George -> Rowlesburg (~36 mi Class I), then the Cheat Narrows (Class II-III) 8 mi from Rowlesburg to the Friends-of-the-Cheat lot near US 50.",
 "elk-wv":"Elk River Water Trail: Sutton Dam tailwaters -> Gassaway -> Frametown -> Duck -> Clendenin (~80 mi of the 97-mi trail to Charleston). Classic day reach: Sutton -> Frametown, ~15 mi of trout tailwater.",
 "coal-wv":"Coal River Water Trail, 11 mi: Meadowood Park (Tornado) -> Coal River Bend -> Lower Falls -> St. Albans at the Kanawha - the annual Tour de Coal float.",
 "bluestone":"Bluestone gorge: Eads Mill Rd -> Pipestem (aerial tram access) -> the Lilly site -> Bluestone SP on Bluestone Lake, ~19 mi (the NPS National Scenic River is the lower 10.5).",
 "mohican":"Loudonville livery country, 16.6 mi: Mohican State Park (SR 3) -> Greer Landing -> Bridge of Dreams (Brinkhaven) -> the Kokosing confluence at Walhonding (ODNR water trail).",
 "littlemiami":"National Scenic River water trail, ~42 mi: Corwin -> Fort Ancient -> Morrow -> Foster -> Loveland -> Milford. (The river passes east of Xenia - Corwin is the on-river anchor.)",
 "bigdarby":"Battelle Darby metro-parks run, ~18 mi: Prairie Oaks (Amity Rd) -> Darby Bend Lakes -> Battelle Darby main launch -> Osprey Lake -> Scioto Darby Rd (Pickaway Co).",
 "kokosing":"Ohio's first water trail, 19.3 mi: Mount Vernon (Riverside Park) -> Gambier -> Big Run -> Howard (Pipesville Rd) -> Millwood. (Order fix: Gambier comes before Howard.)",
 "mad-oh":"Ohio's spring-fed trout stream, ~10 mi: US 36 (west of Urbana) -> SR 55 -> Eagle City -> St. Paris Pike / Snyder Park north of Springfield. (The core run ends at Springfield, not Dayton.)",
 "littlebeaver":"Wild & Scenic canyon, ~23 mi: Elkton -> Lusk Lock -> Gaston's Mill (Beaver Creek SP) -> Sprucevale -> Fredericktown -> the Ohio River at Glasgow PA. Remote, roadless, rain-dependent.",
 "cuyahoga":"Cuyahoga Valley National Park water trail, ~16 mi: Northampton Point (Cuyahoga Falls) -> Peninsula (Lock 29) -> Boston -> Red Lock -> Station Road Bridge (Brecksville); a further 12-mi Class I run continues from Lock 39 toward Cleveland (advanced - shipping channel).",
 "grand-oh":"Wild & Scenic lower gorge, ~23 mi: Harpersfield covered bridge (below the dam) -> Hidden Valley -> Indian Point -> Helen Hazen Wyman Park -> Beaty Landing (Painesville) -> Grand River Landing at Fairport Harbor.",
 "stillwater-oh":"State Scenic dam country north of Dayton, 14.2 mi: Stillwater Prairie Reserve -> Covington -> Pleasant Hill -> Ludlow Falls -> West Milton -> the MANDATORY take-out above Englewood Dam.",
 "sandusky-oh":"The 65-mi State Scenic corridor Upper Sandusky -> Tiffin -> Fremont, paddled in segments; the featured leg is Wolf Creek Park -> Rodger Young Park (~7 mi) through the free-flowing Sandusky Rapids at the removed Ballville dam site.",
 "rum":"State water trail, ~154 river miles: Lake Onamia -> Milaca -> Cambridge -> St. Francis -> Anoka at the Mississippi; flatwater/Class I paddled in day legs.",
 "cannon":"Faribault -> Dundas -> Northfield -> Cannon Falls -> Welch -> Red Wing, ~58 river miles; Cannon Falls -> Welch is the classic livery leg.",
 "root-mn":"Bluff-country classic, ~45 mi: Chatfield (Parsley Bridge) -> Moen's Bridge -> Lanesboro -> Whalan -> Peterson -> Rushford, beside the Root River bike trail.",
 "zumbro":"Rochester -> Zumbro Falls -> Millville -> Theilman -> Kellogg, ~72 river miles through the driftless bluffs; the livery leg centers on Zumbro Falls.",
 "crowwing":"Sandy, easy wilderness water trail, ~65 mi: Nimrod -> Little White Dog -> Cottingham -> McGivern -> Crow Wing State Park at the Mississippi, with county-park landings every 4-6 mi.",
 "snake-mn":"Mora -> Cross Lake -> Chengwatana State Forest at the St. Croix, ~42 mi; Class I Pine City rapids in the lower reach (the whitewater is upstream of Mora).",
 "kettle":"MN's wild & scenic river, ~22 mi: Hwy 23 (Sandstone) -> the Banning gorge rapids (Class II-IV) -> Robinson Park -> Hwy 48 -> Maple Island; mellow water below Sandstone.",
 "crow-mn":"Rockford -> Hanover -> Dayton at the Mississippi, ~23 mi of easy farm-country flatwater - the old Hanover and Berning Mill dams are gone (fast current over the rubble).",
 "missheadwaters":"Paddle the Mississippi at 20 feet wide: Itasca State Park -> Coffee Pot Landing (15.4 mi, the classic day trip) -> Iron Bridge -> Lake Bemidji (Nymore Beach), ~58 mi.",
 "upperiowa":"Iowa's crown jewel, ~38 mi: Kendallville -> Chimney Rock/Bluffton palisades -> Malanaphy Springs -> Decorah (Trout Run Park). The chimney-rock bluffs are BETWEEN Kendallville and Bluffton.",
 "yellow-ia":"Iowa's fastest coldwater river through Effigy Mounds country, ~22 mi: Volney -> Sixteen Bridge -> Ion -> the Mississippi at Yellow River Landing (Hwy 76).",
 "turkey-ia":"Elkader (below the dam, whitewater-park ledges) -> Motor Mill -> Garber -> Osterdock -> Millville, ~34 mi on the Turkey River Water Trail.",
 "volga":"Fayette (Klock's Island) -> Volga River Rec Area -> Osborne -> Mederville -> Littleport -> the Turkey confluence at Garber, ~50 river miles.",
 "maquoketa":"Mon-Maq Dam (Monticello) -> Pictured Rocks palisades -> Eby's Mill, 14 mi. (Maquoketa Caves SP is not on the river; the lower river continues ~26 mi to the town of Maquoketa.)",
 "wapsi":"'The Wapsi', ~48 mi: Independence (Three Elms, below the dam) -> Quasqueton -> Troy Mills -> Pinicon Ridge -> Stone City -> Anamosa (Wapsipinicon SP launch below the dam).",
 "boone-ia":"Boone River Water Trail, ~27 mi: Webster City (Riverside Park) -> Briggs Woods -> Bells Mill -> Boone Forks at the Des Moines River - rock riffles and glacial boulder gardens.",
 "midraccoon":"Central Iowa's favorite quick float, 16.5 mi: Lenon Mill Park (Panora, below the dam) -> Cowles Access -> the upper access ABOVE Redfield Dam.",
 "raccoon":"Raccoon River Water Trail, ~31 mi: Redfield (below the dam) -> Two Rivers -> Booneville -> Walnut Woods SP -> the East Greenway ramp at Des Moines (no launching on Water Works property).",
 "sugarcreek":"THE Indiana paddle, ~29 mi: Crawfordsville (below the dam) -> Deer's Mill (Shades SP) -> the Narrows & Cox Ford covered bridges (Turkey Run SP) -> West Union covered bridge.",
 "tippecanoe":"'The Tippy' day float, ~12 mi: Tippecanoe River State Park -> Winamac town park (the livery's standard 5-6 hr run); optional 7 mi more to Pulaski. (Monticello sits behind the Lake Shafer dams - not a float destination.)",
 "blue-in":"Indiana's first Natural & Scenic river, ~37 mi: Fredericksburg -> Totten Ford -> Milltown (dangerous dam - portage right) -> Rothrock Mill -> Blue River Chapel in Wyandotte caves country.",
 "whitewater-in":"Brookville tailwater, ~18 mi: below the dam -> Brookville town park -> New Trenton -> Whitewater Township Park at Harrison OH. The fastest gradient in Indiana (~6 ft/mi).",
 "wildcat":"Wildcat Creek water trail, ~27 mi: Adams Mill covered bridge (Cutler) -> Mis-So-La -> Wildcat Creek Park -> Peters Mill -> Davis Ferry on the Wabash. Popular legs: Mis-So-La->Wildcat Park (4.5) and Wildcat Park->Davis Ferry (10).",
 "bigpine":"Indiana's mini-whitewater: Rainsville bridge -> Twin Bridges (6.7 mi Class II-II+, spring flows only); optional 7-mi Class I continuation to Ouabache Park, Attica.",
 "flatrock-in":"Owens Bend County Park -> Noblitt Park -> Mill Race Park (Columbus), ~9 mi - the Flatrock joins the Driftwood at Mill Race to form the East Fork White. (It flows TO Columbus from the northeast, never through Edinburgh.)",
 "driftwood":"Edinburgh (Atterbury FWA) -> Lowell Bridge -> Mill Race Park (Columbus), ~16 mi of fast wooded water forming up at the Big Blue/Sugar Creek junction.",
 "eel-in":"Eel River Water Trail, ~90 mi: Columbia City -> Liberty Mills -> North Manchester -> Stockdale Mill -> Logansport (Riverside Park). Classic leg: North Manchester -> Stockdale, ~15 mi. Six-plus low-head dams - know every portage.",
 "cedarck-in":"Cedar Creek Canyon (state Natural & Scenic), ~9 mi: Cook's Landing (Huntertown) -> Metea County Park -> the SR 1 DNR access, then optionally 9.6 mi down the St. Joseph to Shoaff Park, Fort Wayne.",
 "mississinewa":"The Seven Pillars run, 5.3 mi: Mississinewa Dam tailwater (Fire Ln) -> SR 124 at Peru, past the Seven Pillars limestone bluffs (view from the water - the shore is private). The Marion-to-lake upper river is a separate reach.",
 "current":"THE Ozark float, 88 mi of spring-fed Class I: Baptist Camp (below Montauk SP) -> Akers Ferry -> Pulltite -> Round Spring -> Two Rivers -> Van Buren -> Big Spring (Ozark National Scenic Riverways), floated in day legs.",
 "jacksfork":"Buck Hollow (Hwy 17) -> Alley Spring -> Eminence -> the Current confluence at Two Rivers, 37.6 mi; upper river needs spring water, Alley Spring keeps the lower running all season.",
 "elevenpoint":"National Wild & Scenic, 35.6 mi: Thomasville -> Greer Crossing (the spring doubles the flow) -> Turner Mill -> Whitten -> Riverton East (US 160).",
 "niangua":"Bennett Spring country, 18.5 mi: Moon Valley -> Bennett Spring (Hwy 64) -> Barclay -> Prosperine gravel-bar landing (last good take-out above Tunnel Dam water).",
 "meramec":"Maramec Spring (fee) -> Scotts Ford -> Bird's Nest -> Onondaga Cave SP -> Sappington Bridge -> Meramec State Park, ~60 river miles floated in day legs.",
 "gasconade":"Ozark hills, ~76 river miles: Hazelgreen (I-44) -> Schlicht Springs -> Riddle Bridge -> Boiling Spring -> Jerome at the Little Piney confluence. Day legs: Riddle->Jerome (~21) or Boiling Spring->Jerome (~7.5).",
 "bigpiney":"Dogs Bluff (Houston) -> Mason Bridge -> Slabtown (USFS) -> Ross Access, ~46 guidebook miles; Slabtown->Ross is 14.9. Ross is the LAST take-out before Fort Leonard Wood's restricted water.",
 "huzzah":"The Meramec's clear-water little sister: Hwy 8 bridge -> Huzzah CA low-water bridge (5.4 mi) -> the Meramec confluence -> Onondaga Cave SP ramp, 8.9 mi total.",
 "northfork-mo":"Twin Bridges -> Hammond Camp -> Blair Bridge -> Patrick Bridge -> Dawt Mill, ~23 mi; Rainbow Spring pours in mid-run (Hodgson Mill is on neighboring Bryant Creek).",
}
WATCH = {
 "red-ky":"Rain-dependent; watch strainers. The Upper Red above KY 715 is expert Class II-III+ only.",
 "barren":"Low-head dam at the State Street Bridge - put in below it. Beech Bend ramps are for registered campers only.",
 "nolin":"Dam releases raise water fast; KDFWR flags the tailwater ramp status - check before driving. A Class II rapid now runs at the old Lock & Dam 6 site below Houchin Ferry.",
 "rockcastle":"MANDATORY take-out at Billows (KY 1956): the Narrows below run Class III-IV over undercut, sieved rock to Bee Rock.",
 "licking-ky":"Flows swing with Cave Run releases; Wyoming Ford's access road is often muddy with 1-2 car parking.",
 "floydsfork":"Flashy rain-driven creek with frequent strainers; remnant blown-out dam ~1 mi below North Beckley; Cliffside is the last take-out for ~20 mi.",
 "gasper":"Rapids cluster near KY 626 (Class II-III at high water); AW reports a parking dispute at the KY 626 bridge - use other accesses.",
 "rough-ky":"The Falls of Rough ledge/mill dam (~6 mi down, private property) is a mandatory portage; dam-controlled releases.",
 "greenbrier":"Famously low in late summer - check levels; ledgy Class I-II throughout.",
 "sbpotomac":"Class II ledges in The Trough; gravel-bar scraping at low water; rail-or-river country with no mid-run road access.",
 "cacapon":"Strongly level-dependent: below ~2 ft at Great Cacapon it scrapes, above 4 ft it pushes hard for novices; wood hazard at Hutchinson Rapid.",
 "cheat":"Parsons gauge under ~4 ft = scraping; the Narrows below Rowlesburg is Class II-III (Calamity Rock III+).",
 "elk-wv":"Flows depend on Sutton Dam releases; watch strainers and island channels.",
 "coal-wv":"Two runnable-or-portage drops: Upper Falls at Tornado and Lower Falls near St. Albans.",
 "bluestone":"Needs 4-7 ft on the Pipestem gauge (often too low in summer); remote gorge - mid-run access only by the Pipestem tram (fee, seasonal) or gravel road to the Lilly site.",
 "mohican":"Partially breached low-head dam at Brinkhaven near the Bridge of Dreams - portage left. Loudonville's new Riverside kayak launch breaks ground in 2026.",
 "littlemiami":"Turbulence at the Caesar Creek confluence during lake discharges; log jams. Morgan's Fort Ancient livery closed Jan 2025 - the access itself remains public.",
 "bigdarby":"Scenic-river rules apply; strainers and flashy post-rain water; the Pickaway access needs 150+ cfs and closes Nov-Apr.",
 "kokosing":"Strainers between Big Run and Pipesville; Factory Rapids below Millwood runs Class III at high water - stay left or portage right.",
 "mad-oh":"2-3 ft low-head dam immediately below the US 36 put-in (portage right); cold swift channel with frequent strainers.",
 "littlebeaver":"Remote roadless canyon - self-rescue country; one Class II+ rapid below Fredericktown nears III at high water; spring/post-rain flows only.",
 "cuyahoga":"Portage the waterfall/dam remnant above Lock 29 (river left near SR 303); mandatory river-left take-out above Fitzwater Rd; avoid after heavy rain (sewer overflows); freighter traffic in the last 4 mi toward Cleveland.",
 "grand-oh":"Put in BELOW the Harpersfield low-head dam. Flashy: 2-5 ft optimal, under 2 ft a slow drag, over 8 ft dangerous.",
 "stillwater-oh":"Dam-heavy: portages at Covington, below Bridge St, Falknor Rd, Fenner Rd and West Milton; MANDATORY take-out above Englewood Dam. Ludlow Falls is on the tributary creek - avoid its mouth.",
 "sandusky-oh":"Dams remain upstream (Upper Sandusky, Indian Mill, Tiffin, Pioneer Mill, partial Huss St); the Sandusky Rapids run Class I-III with level; heavy angler crowds during the spring walleye run.",
 "rum":"Portage the Anoka dam (river right; Akin Riverside is below it) and the Onamia rock rapids; log jams multiply above Princeton.",
 "cannon":"Northfield dam has NO developed portage; Lake Byllesby dam needs a ~1,000-yd portage via the regional park; last easy take-out is the Hwy 61 access.",
 "root-mn":"Portage the Lanesboro dam (left) and the rock rapids above it; two submerged dams lower down; Peterson access closed during 2026 bridge work.",
 "zumbro":"Put in below Rochester's two dams; portage the Lake Zumbro hydro dam (right); notorious strainers; water rises fast after rain.",
 "crowwing":"Two hydro dams low down: Pillager (portage right) and Sylvan (portage left), with slackwater from ~river mile 15.",
 "snake-mn":"The old Cross Lake outlet dam at Pine City is now rock rapids - portage left if not running it; very scrapey at low water.",
 "kettle":"Banning gorge (Blueberry Slide -> Hell's Gate) is Class II-IV - portage trail available; Big Spring Falls/Sandstone Rapids below Robinson Park are II-IV (portage right).",
 "crow-mn":"Fast current and rubble at the old Hanover and Berning Mill dam sites; deadfall on bends.",
 "missheadwaters":"Beaver dams and road culverts can force portages in the narrow upper channel; Class I rapids below Vekins Dam.",
 "upperiowa":"Scrapey below ~200 cfs on the Bluffton gauge; the dams are below Decorah - end at Trout Run Park.",
 "yellow-ia":"Swift with strainers on hairpin bends; ~20-ft drop in the mile below Ion bridge; confusing Mississippi backwaters at high water.",
 "turkey-ia":"Portage the Elkader dam river-right at the Keystone Bridge; Class I-II whitewater-park ledges just below.",
 "volga":"Strainers, Class I ledges and old railroad concrete debris in the lower river; runnable above ~150 cfs at Littleport.",
 "maquoketa":"Put in BELOW Mon-Maq Dam (drowning hazard); scrapes below ~200 cfs; logjams in the Jackson County reaches downstream.",
 "wapsi":"Anamosa's low-head dam is EXTREMELY dangerous - take out at Stone City or the city ramp above it; put in below the Independence dam; Quasqueton's old dam is now a rock-arch rapids.",
 "boone-ia":"A ~200-yd rock-ledge rapid below Albright Access (strainers river-right); county rentals suspend above 2,000 cfs.",
 "midraccoon":"Low-head Redfield Dam at the run's end - take out at the upper access above it.",
 "raccoon":"No boat launching on Des Moines Water Works property (infiltration weir) - end at Walnut Woods or the East Greenway ramp; the Scott Ave dam waits just past the confluence.",
 "sugarcreek":"CRITICAL low-head dam at Crawfordsville - put in at the access below it; scrapey by late summer.",
 "tippecanoe":"Logjams and strainers; canoe camping in the state park; the SP coordinate marks the park, not the exact ramp.",
 "blue-in":"Dangerous dam at Milltown (portage right) and a partially breached dam at Rothrock Mill (portage); late-summer low water.",
 "whitewater-in":"Keeper hole at the rapid above the US 52 bridge during high dam releases; cold fluctuating tailwater - stay well below the spillway; banks mostly private.",
 "wildcat":"Old mill dam at Adams Mill (portage; separate accesses above/below); frequent logjams; confirm Wildcat Creek Park access status (county lease ended 2022).",
 "bigpine":"Spring-only (~400-500 cfs, Mar-May); S-Curve develops a nasty hole above ~4 ft; no livery - self-shuttle.",
 "flatrock-in":"Low-head dam between Owens Bend and Mill Race near Noblitt Park - portage; frequent strainers; usually too low by August.",
 "driftwood":"Fast current through the Atterbury woods - watch strainers.",
 "eel-in":"Low-head dams at Collamer (portage left), Liberty Mills (right), North Manchester, Stockdale (200-yd portage), Chili (scout) and Mexico (reported breached), plus the Logansport dams - take out at Riverside Park.",
 "cedarck-in":"Shifting logjams; stay clear of the Cedarville Dam outflow on the St. Joseph at the creek mouth; best at spring/fall water.",
 "mississinewa":"Tailwater fluctuates with USACE releases - check discharge; NO public landing at Seven Pillars (private, barriers up).",
 "current":"Baptist Camp -> Akers is narrow and fast with strainers at higher flows; boating is prohibited through Montauk's hatchery water.",
 "elevenpoint":"Mary Decker Shoal and Halls Bay Chute run Class II; Thomasville access has flood damage; motors to 25 hp below Greer.",
 "niangua":"Low-water bridge on the Moon Valley approach; Prosperine is a gravel-bar landing; Tunnel Dam lies downstream - don't overshoot.",
 "meramec":"Maramec Spring Park is fee access (James Foundation).",
 "gasconade":"Easy flatwater but a multi-day corridor - pick a day leg.",
 "bigpiney":"Ross is the last take-out before Fort Leonard Wood (restricted, two low dams).",
 "huzzah":"Often too low by mid-late summer; duck the low-water bridges.",
 "northfork-mo":"The Falls (Class II ledge below Hammond) usually runs via its chute; portage or run the right-side chute at the Dawt Mill low dam (landing is private livery water).",
}
patch = "\n# ---- v10 QC pass (7 states): corrected stretches, hazards, extra unpinned accesses ----\n"
patch += "STRETCH_FIX = " + json.dumps(STRETCH, indent=0).replace("\n","\n") + "\n"
patch += "WATCH_FIX = " + json.dumps(WATCH, indent=0) + "\n"
patch += "EXTRA_UNPINNED = " + json.dumps(extra_unpin, indent=0) + "\n"
patch += '''for r in R:
    if r["id"] in STRETCH_FIX: r["stretch"] = STRETCH_FIX[r["id"]]
    if r["id"] in WATCH_FIX:   r["watch"] = (WATCH_FIX[r["id"]] + (" " + r["watch"] if r["watch"] and r["watch"] not in WATCH_FIX[r["id"]] else "")).strip()
    if r["id"] in EXTRA_UNPINNED:
        seen = set(r["unpinned"])
        r["unpinned"] = r["unpinned"] + [u for u in EXTRA_UNPINNED[r["id"]] if u not in seen]
'''
anchor2 = 'data = {"rivers":R,"landings":L,'
assert anchor2 in src
src = src.replace(anchor2, patch + "\n" + anchor2, 1)

open(BD,"w").write(src)
print("build_data.py patched. unpinned rivers:", len(extra_unpin))
