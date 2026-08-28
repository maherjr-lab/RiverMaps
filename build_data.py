import json

# ---------------- RIVERS ----------------
R = []
def river(id,name,cls,bbox,qname=None,stretch="",motor="",depth="",gauge=None,gauge2=None,watch="",unpinned=None,sources=None,latmin=None,latmax=None,state="WI"):
    R.append(dict(id=id,name=name,cls=cls,bbox=bbox,qname=qname or name.split(" — ")[0],
        stretch=stretch,motor=motor,depth=depth,gauge=gauge,gauge2=gauge2,watch=watch,
        unpinned=unpinned or [],sources=sources or [],latmin=latmin,latmax=latmax,state=state))

river("baraboo","Baraboo River","green",[43.30,-90.40,43.75,-89.42],qname="Baraboo River",
 stretch="The longest restored free-flowing river in the U.S. — ~64 commonly-paddled miles: Union Center (Hwy 33) → Wonewoc → La Valle → Reedsburg → Rock Springs → Baraboo → the Wisconsin River south of Portage (logjams on the upper reaches cleared in 2025). Classic day trip: Haskins Park → Hwy 113 through the restored downtown Baraboo rapids (~4.3 mi, Class I–II).",
 motor="Free-flowing (all dams removed) with carry-in park landings only — effectively non-motorized water.",
 depth="Drought-sensitive and it has run low in recent summers. Flatwater sections float at typical summer flows, but the Baraboo rapids stretch shouldn't be attempted below ~350 cfs (400–600 optimal) — May–June is most reliable.",
 gauge={"site":"05405000","name":"Baraboo R nr Baraboo","min":350,"lo":400,"hi":600},
 watch="Check the gauge before driving out — the rapids run disappears in dry spells.",
 unpinned=["Union Center landing (Hwy 33)","La Valle boat launch (W. Main St, La Valle)","Reedsburg Landing (Friends of the Boo)","Wisconsin R. confluence take-outs (S of Portage)"],
 sources=[["Miles Paddled guide","https://milespaddled.com/baraboo-river-paddle-guide/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/baraboo-river"],["Friends of the Boo","https://friendsoftheboo.org/river-sections"]])

river("kickapoo","Kickapoo River","green",[43.03,-90.95,43.85,-90.40],
 stretch="Ontario → La Farge through the Kickapoo Valley Reserve: 22.5 mi with 20 numbered landings (classic day trip: Landing 1 → Landing 12, Rockton). The quieter lower river continues Viola → Readstown → Soldiers Grove → Gays Mills → Steuben → Wauzeka at the Wisconsin River (~60 mi total) — bring-your-own water below La Farge.",
 motor="Narrow, twisting spring-fed stream with carry-in canoe landings only — non-motorized in practice.",
 depth="The most reliable summer river of the set — spring-fed, floatable nearly all season (ideal 60–100 cfs at La Farge). Flashy after storms: above ~200 cfs the gorge sections get unsafe.",
 gauge={"site":"05408000","name":"Kickapoo R at La Farge","min":40,"lo":60,"hi":100,"flood":200},
 unpinned=["Wildcat Mountain State Park canoe landing (Ontario)","Banker Park (Viola)","Hwy B canoe landing (N of Gays Mills)"],
 sources=[["Kickapoo Valley Reserve paddling guide","https://kvr.state.wi.us/Documents/Upper%20Kickapoo%20River%20Guide%202024%20WEB.pdf"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/kickapoo-river"],["Miles Paddled","https://milespaddled.com/kickapoo-river-i/"]])

river("sugar","Sugar River","green",[42.42,-89.75,43.05,-89.15],
 stretch="Belleville → Albany → Brodhead water trail (~25 mi of sandy, easy water). Day trips: Belleville Community Park → Exeter Park (4.7 mi) and Bowman Park (Albany) → Brodhead (7.25 mi). Below Brodhead the documented water continues ~36 mi through Avon Bottoms and Colored Sands into Illinois to the Pecatonica confluence at Shirland — bring-your-own paddling.",
 motor="River run is carry-in and non-motorized in practice; motorboats and jet skis stay on the Decatur Lake impoundment at Brodhead.",
 depth="Floatable most of the summer; below ~50 cfs at the Verona gauge it turns scrapey. Sluggish backwater above the Albany and Decatur dams.",
 gauge={"site":"05435950","name":"Sugar R at Verona","min":50,"lo":60,"hi":150},
 sources=[["Miles Paddled guide","https://milespaddled.com/sugar-river-paddle-guide/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/sugar-river"]])

river("wolf-upper","Wolf River — Upper (whitewater)","green",[44.95,-89.05,45.33,-88.55],qname="Wolf River",latmin=44.95,latmax=45.33,
 stretch="Lily → Hollister → Langlade → County M (Sections I–III): continuous Class I–III boulder gardens at ~17 ft/mi. Below County M the river enters Menominee tribal land (Otter Slide → Big Smokey Falls) — access bracelet required.",
 motor="No motor traffic — continuous rapids and boulder gardens make it kayak/raft water only (no formal ban on record).",
 depth="Runnable spring through fall in normal years; want ≥250 cfs at Langlade to avoid rock-bashing, 400–600+ optimal. Can get bony in late-summer dry spells.",
 gauge={"site":"04074950","name":"Wolf R at Langlade","min":250,"lo":400,"hi":800},
 watch="Heads up: Dragonfly Paddlers is not on this stretch — they run the flatwater lower Wolf out of Shiocton, ~100 river miles downstream (shown in blue).",
 unpinned=["Otter Slide Landing (Menominee Reservation — tribal permit)","Big Smokey Falls (Menominee Reservation — tribal permit)"],
 sources=[["Wisconsin Trail Guide","https://wisconsintrailguide.com/paddle/wolf-river.html"],["American Whitewater","https://www.americanwhitewater.org/content/River/view/river-detail/2319/main"],["Miles Paddled","https://milespaddled.com/wolf-river-i/"]])

river("black","Black River","green",[43.94,-91.40,44.46,-90.60],
 stretch="Hatfield (below the Lake Arbutus dam) → Black River Falls → Irving → Melrose → North Bend: sandstone bluffs, sandbars and swimming holes. Melrose → North Bend is the most popular stretch. Below North Bend, Hwy 53 → Hwy 35 → Lytle's Landing runs the Van Loon floodplain forest — quieter bring-your-own water.",
 motor="Legally open to motors but the shallow sand-bottom channel strands power boats — kayak water in practice (guides report almost no motor traffic).",
 depth="Good most of the summer; ≥250 cfs (Galesville gauge) avoids sandbar dragging, 300–700 typical May–Sept. 'Even at its lowest it probably never becomes too shallow to paddle' below the falls.",
 gauge={"site":"05382000","name":"Black R nr Galesville","min":250,"lo":300,"hi":700},
 gauge2={"site":"053813595","name":"Black R at Black River Falls"},
 unpinned=["Mason's Landing (Black River Falls)","Lost Falls Campground landing (private livery)"],
 sources=[["Wisconsin Trail Guide","https://wisconsintrailguide.com/paddle/black-river.html"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/black-river/melrose"],["Miles Paddled","https://milespaddled.com/black-river-iii/"]])

river("milwaukee","Milwaukee River","green",[43.02,-88.30,43.65,-87.85],
 stretch="Newburg → Waubeka → Grafton (riffly, rural, ~24 mi) plus the Milwaukee Urban Water Trail from Lincoln/Estabrook Park through downtown to the harbor. Portage the Grafton dams (Lime Kiln rapids below). Upstream, Kewaskum → Barton → West Bend → Newburg (~23 mi) is regularly paddled bring-your-own water with dam portages at Barton and West Bend.",
 motor="The Urban Water Trail is designated for non-motorized craft, and the upper river is too shallow/riffly for motors. Exceptions: the Thiensville millpond carries powerboats and the downtown estuary is shared no-wake water.",
 depth="Above Grafton wants ~250–350 cfs at Cedarburg — often too low mid–late summer ('scrape city'). The downtown estuary is deep year-round.",
 gauge={"site":"04086600","name":"Milwaukee R nr Cedarburg","min":250,"lo":300,"hi":500},
 sources=[["Milwaukee Urban Water Trail","https://milwaukeeriverkeeper.org/our-waterways/milwaukee-urban-water-trail/"],["Miles Paddled","https://milespaddled.com/milwaukee-river-i/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/milwaukee-river"]])

river("bark","Bark River","green",[42.88,-88.90,43.18,-88.25],
 stretch="Upper: Merton → Hartland → Nemahbin Lakes → Dousman. Lower: Rome → Burnt Village Park → Fort Atkinson (mouth at the Rock River) — the most reliable water.",
 motor="The river itself is too narrow and shallow for motorboats. It does cross motorized lakes (Nagawicka, Upper/Lower Nemahbin, Rome Pond) — busy on summer weekends.",
 depth="Upper river scrapey below ~50 cfs at Delafield; Burnt Village → Fort Atkinson is floatable nearly all season (200–300 cfs at Rome ideal).",
 gauge={"site":"05426067","name":"Bark R at Delafield","min":50,"lo":60,"hi":150},
 gauge2={"site":"05426250","name":"Bark R nr Rome"},
 sources=[["Miles Paddled","https://milespaddled.com/bark-river-i/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/bark-river"]])

river("mukwonago","Mukwonago River","green",[42.78,-88.55,42.90,-88.18],qname="Mukwonago River",
 stretch="Rainbow Springs (KM State Forest) → Beulah Rd → County I → Phantom Lakes: 5–8 mi of spring-fed, glass-clear fen paddling. Continuation: below the Mukwonago dam → Fox River confluence → Big Bend (9 mi).",
 motor="Narrow, wild-rice-lined channel — carry-in kayak water only (DNR's Lower Phantom access is canoe/kayak only). Motors only on adjacent Eagle Spring and Phantom lakes.",
 depth="Spring-fed and floatable all summer; best ≥64 cfs / 2.5 ft at the Mukwonago gauge. Wild rice can choke the channel late summer.",
 gauge={"site":"05544200","name":"Mukwonago R at Mukwonago","min":64,"lo":70,"hi":120},
 unpinned=["Nature Rd access (Lulu Lake SNA)","Rainbow Springs put-in off Hwy LO","Beulah Rd crossing","County Hwy I pull-off","Indianhead Park (Mukwonago)"],
 sources=[["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/mukwonago-river"],["Friends of the Mukwonago River","https://mukwonagoriver.org/summer-mukwonago-river-paddles/"],["Miles Paddled","https://milespaddled.com/mukwonago-river/"]])

river("fox-il","Fox River (Illinois Fox)","green",[42.49,-88.55,43.06,-88.15],qname="Fox River",
 stretch="Fabulous Fox Water Trail: Frame Park (Waukesha) → Vernon Marsh → Big Bend → Waterford → Rochester → Burlington, then the Kenosha County water trail on to Wilmot at the Illinois line (~18 more miles). Portage the Waterford and Rochester dams.",
 motor="Quiet paddling water Waukesha → Big Bend and Rochester → Burlington. Exception: the Tichigan Lake–Waterford impoundment pool is a busy motorized flowage (jet skis around Big Bend too) — plan around it.",
 depth="Dam-controlled and floatable most of the season. The riffly Waterford → Burlington run wants ~4 ft on the Rochester gauge; upper river minimum ~90 cfs at Waukesha.",
 gauge={"site":"05543830","name":"Fox R at Waukesha","min":90,"lo":100,"hi":300},
 gauge2={"site":"05544475","name":"Fox R at Rochester"},
 unpinned=["CTH JB access (Wheatland)","Fox River Park access (Silver Lake)","Wilmot access (Salem Lakes)"],
 sources=[["Fabulous Fox Water Trail — access sites","https://fabulousfoxwatertrail.org/access-sites/"],["Itineraries","https://fabulousfoxwatertrail.org/itineraries/"],["Miles Paddled","https://milespaddled.com/fox-river-ii-illinois-tributary/"]])

river("root","Root River","green",[42.60,-88.10,42.85,-87.75],
 stretch="Caledonia (5/6 Mile Rd) → Hwy 31 → Horlick Dam: ledges and boulder gardens (annual Root River Paddle Challenge). Urban continuation Lincoln Park → Island Park → the harbor.",
 motor="Upper river is unmotorable riffle water; the mile-long pool above Horlick Dam is electric-motors-only; below Island Park it becomes Racine's motorized harbor.",
 depth="Flashy and often low in summer: wants ≥2 ft (~41+ cfs) at the Franklin gauge, 3 ft optimal. Below 2 ft you'll be walking.",
 gauge={"site":"04087220","name":"Root R nr Franklin","min":41,"lo":50,"hi":120},
 unpinned=["County Line Rd access (Caledonia)","6 Mile Rd bridge","Quarry Lake Park (below Horlick Dam)","Lincoln Park canoe launch (Racine)","Island Park launch (Racine)","Cedar Bend/Clayton Park launch","Root River Environmental Center (REC) launch"],
 sources=[["Miles Paddled","https://milespaddled.com/root-river/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/root-river"],["Trailville","https://www.trailville.com/wiki/WI_Racine_Root_River"]])

# ---- BLUE ----
river("wisconsin","Wisconsin River","blue",[42.95,-91.25,46.30,-89.15],
 stretch="The state's big trip river. The Lower Wisconsin Riverway (Sauk City → Spring Green → Boscobel → the Mississippi) is the classic multi-day sandbar float.",
 motor="Open motorized water throughout — you'll share it with fishing boats; wide channel with sandbars.",
 depth="Dam-controlled and always floatable.",
 sources=[["Lower Wisconsin Riverway","https://lwr.wisconsin.gov/"]])
river("rock","Rock River","blue",[42.49,-89.20,43.55,-88.45],stretch="Horicon → Watertown → Jefferson → Janesville → Beloit.",motor="Open motorized water with flowages.",depth="Big, reliable water.")
river("chippewa","Chippewa River","blue",[44.30,-92.20,46.00,-90.60],stretch="Eau Claire → Durand → the Mississippi; wide and sandy with a paved state trail alongside the lower river.",motor="Open motorized water.",depth="Reliable.")
river("fox-lower","Fox River (Green Bay)","blue",[43.53,-89.65,44.60,-87.90],qname="Fox River",stretch="Portage → Berlin → Lake Winnebago → De Pere → Green Bay; locks and big water.",motor="Open motorized water.",depth="Reliable.")
river("wolf-lower","Wolf River — Lower (Shiocton flatwater)","blue",[44.05,-89.00,44.95,-88.35],qname="Wolf River",latmin=44.05,latmax=44.95,
 stretch="Keshena → Shawano → Shiocton → New London → Fremont. This is Dragonfly Paddlers' home water: ~5-mi lazy floats from Koepke's Access back to their Shiocton base.",
 motor="Deep flatwater shared with motorboats — hence blue, even though it's a lovely easy paddle.",
 depth="Deep and reliable all season.",
 unpinned=["Koepke's Access (Dragonfly Paddlers put-in, Shiocton)","Dragonfly Paddlers base landing (Shiocton)"],
 sources=[["Dragonfly Paddlers","https://dragonflypaddlers.com/"]])
river("stcroix","St. Croix River","blue",[44.75,-92.90,46.35,-91.60],qname="St. Croix River",stretch="National Scenic Riverway along the Minnesota border.",motor="Motorized on the lower river; quieter upstream.",depth="Reliable.")
river("menominee","Menominee River","blue",[45.05,-88.35,45.95,-87.50],stretch="Michigan border river — whitewater sections up high (Piers Gorge), motorized flowages elsewhere.",motor="Mixed — dams, flowages, and gorge sections.",depth="Reliable.")

# ============ SOUTHERN WISCONSIN — round 2 ============
river("yahara","Yahara River","green",[42.75,-89.45,43.29,-89.10],
 stretch="Two documented runs: DeForest → Cherokee Marsh (upper, ~6 mi), and Stoughton (below the Mandt Park dam) → Dunkirk → Fulton at the Rock River (lower, ~17 mi to Murwin Park). The Madison chain of lakes sits between them. Note: the Stebbinsville Rd access has been posted private since 2021 — use Mandt and Murwin parks.",
 motor="The riverine reaches are narrow and shallow — motors impractical. The lakes chain in the middle (Mendota–Monona–Waubesa–Kegonsa) is heavily motorized.",
 depth="Lower Stoughton–Fulton run is generally reliable (best 330–500 cfs at Fulton). The upper DeForest run needs ~2 ft at Windsor and usually doesn't have it — catch it after rain.",
 gauge={"site":"05430175","name":"Yahara R nr Fulton","min":330,"lo":330,"hi":500},
 watch="Motorboats everywhere on the lakes section — the green rating applies to the river runs above and below.",
 sources=[["Miles Paddled guide","https://milespaddled.com/yahara-river-paddle-guide/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/yahara-river/deforest-2"]])
river("badfish","Badfish Creek","green",[42.75,-89.42,42.96,-89.10],
 stretch="Sunrise Rd → Cooksville (Old Stage Rd) → Casey Rd is the classic 7-mi run; water continues to the Yahara confluence near Fulton.",
 motor="Narrow, twisty riffle creek — no motorboat use documented anywhere.",
 depth="The most reliable summer creek near Madison — most of its flow is Madison's treated effluent, so it floats even in drought (70 cfs is still a good depth; normal summer 100–150).",
 gauge={"site":"05430150","name":"Badfish Ck nr Cooksville","min":70,"lo":100,"hi":200},
 sources=[["Miles Paddled guide","https://milespaddled.com/badfish-creek-paddle-guide/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/badfish-creek/old-stage-rd-to-casey-rd"]])
river("pecatonica","Pecatonica River","green",[42.30,-90.25,42.80,-89.60],
 stretch="Calamine → Darlington (Black Bridge / Trails Park) → Wells Landing; a lower documented run crosses into Illinois from Browntown to Winslow.",
 motor="Muddy banks, logjams and shallow riffles — no motor traffic reported on the Wisconsin reaches.",
 depth="One of the more reliable southern-WI rivers — floats all summer. 220 cfs at Darlington is marginal; 360+ comfortable.",
 gauge={"site":"05432500","name":"Pecatonica R at Darlington","min":220,"lo":320,"hi":600},
 sources=[["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/pecatonica-river"],["Miles Paddled","https://milespaddled.com/pecatonica-river-i/"]])
river("grant","Grant River","green",[42.55,-90.90,42.90,-90.55],
 stretch="Short Cut Rd (west of Lancaster) → Beetown (County U) → Chaffie Hollow Rd → Potosi Point at the Mississippi. Limestone outcrops and riffles.",
 motor="Impractical on the river itself; the Potosi Point take-out is a Mississippi backwater ramp shared with fishing boats.",
 depth="Holds its water surprisingly well; ~175 cfs at Burton is the scrape threshold, 260+ recommended. Usually floatable through summer except late dry spells.",
 gauge={"site":"05413500","name":"Grant R at Burton","min":175,"lo":200,"hi":300},
 sources=[["Miles Paddled","https://milespaddled.com/grant-river-i/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/grant-river/hwy-u"]])
river("platte-wi","Platte River (WI)","green",[42.60,-90.70,42.95,-90.40],qname="Platte River",
 stretch="County E (Annaton) → Ellenboro bridges → Platte Rd; lower access at Banfield Bridge near the Mississippi mouth.",
 motor="Limestone boulders, rapids and fence crossings — no motor traffic except slow fishing boats in the final backwater mile.",
 depth="Remarkably stable for the Driftless, but it can run dry late summer: ideal 100–200 cfs at Rockville, below ~100 expect rock-bumping.",
 gauge={"site":"05414000","name":"Platte R nr Rockville","min":100,"lo":100,"hi":200},
 watch="Watch for barbed-wire and electric fence crossings on the upper runs.",
 sources=[["Miles Paddled","https://milespaddled.com/platte-river-i/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/platte-river"]])
river("lacrosse","La Crosse River","green",[43.80,-91.25,44.00,-90.55],
 stretch="Sparta (Fishermen's Park) → Bangor along the Elroy-Sparta corridor; a second run below the Lake Neshonoc dam (West Salem) → Veterans Memorial Park toward the Mississippi.",
 motor="Small, sandy and riffly — motors only on the Lake Neshonoc flowage in the middle.",
 depth="Reliable sandy spring-fed stream: ~150–170 cfs at Sparta is a good depth (recorded mid-August); the lower run liked ~450 cfs on the La Crosse gauge.",
 gauge={"site":"05382325","name":"La Crosse R at Sparta","min":140,"lo":150,"hi":300},
 sources=[["Miles Paddled","https://milespaddled.com/la-crosse-river-i/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/la-crosse-river"]])
river("lemonweir","Lemonweir River","green",[43.70,-90.35,44.00,-89.80],
 stretch="Kennedy County Park → New Lisbon flowage; Mauston dam → 19th Ave (Lemonweir Mills) → Two Rivers landing at the Wisconsin River.",
 motor="Quiet tannin water; only occasional small fishing/hunting motorboats on the New Lisbon flowage.",
 depth="Mostly dependable: ≥170 cfs at New Lisbon (110 was 'too low'), ideal 200–300. Flowage sections float at any summer level.",
 gauge={"site":"05403500","name":"Lemonweir R at New Lisbon","min":170,"lo":200,"hi":300},
 unpinned=["Riverside Park ramp (New Lisbon flowage)","Launch below Mauston dam (north bank)"],
 sources=[["Miles Paddled","https://milespaddled.com/lemonweir-river/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/lemonweir-river/kennedy-park"]])
river("mecan","Mecan River","green",[43.80,-89.60,44.05,-89.10],
 stretch="County JJ (Richford/Dakota) → Hwy 22 → Germania → Lock Rd at the Fox River southwest of Princeton. A glass-clear spring creek.",
 motor="Narrow spring creek with several duck-under bridges — no motorboat use documented.",
 depth="Spring-fed and almost always adequate all summer (no gauge exists — avoid right after hard rain; low bridges get tight).",
 sources=[["Miles Paddled guide","https://milespaddled.com/mecan-river-paddle-guide/"]])
river("crystal","Crystal River","green",[44.28,-89.25,44.38,-89.05],
 stretch="Rural (Main St) → Little Hope / Shadow Lake Rd: the famous 3.75-mi rocky run; documented water runs ~12 mi from the Chain O' Lakes outlet.",
 motor="Tiny, shallow and riffly with Class I ledges — kayak water only. The Chain O' Lakes upstream is busy powerboat water.",
 depth="Spring-fed and stable all summer — runnable even at low water in a kayak (scrapey riffles in drought). No gauge on the Crystal; the Waupaca River gauge is the usual proxy.",
 gauge={"site":"04081000","name":"Waupaca R nr Waupaca (proxy)","min":None,"lo":None,"hi":None},
 unpinned=["Marl Lake south launch (no parking)","Knight Lane bridge launch (Rural)"],
 sources=[["Miles Paddled guide","https://milespaddled.com/crystal-river-paddle-guide/"],["WisconsinRiverTrips","https://www.wisconsinrivertrips.com/segments/crystal-river"]])
river("turtle","Turtle Creek","green",[42.46,-89.06,42.68,-88.55],
 stretch="Springs Park (Delavan) → Clinton → Sweet-Allyn Park (Shopiere) → Dickop St at the Rock River (South Beloit). Clear water and light rapids; Sweet-Allyn → Rock River is the most fun leg.",
 motor="Riffly creek with shallow gravel bars — no motorboat use documented.",
 depth="Trickier levels: runnable to ~100 cfs with scraping, 200+ to stay off the gravel, ~300 ideal; riffles wash out above ~400.",
 gauge={"site":"05431486","name":"Turtle Ck at Carvers Rock Rd","min":100,"lo":200,"hi":300,"flood":400},
 sources=[["Miles Paddled guide","https://milespaddled.com/turtle-creek-paddle-guide/"]])

# ============ ILLINOIS — north of US-24 ============
river("kishwaukee","Kishwaukee River","green",[42.15,-89.10,42.31,-88.60],state="IL",
 stretch="Garden Prairie → Belvidere (dam portage) → Cherry Valley (Baumann Park) → Atwood Park (New Milford/Rockford), then ~5.4 more miles to the Rock River confluence (Rt 251/S Rockford access at mile 8.3 of the lower leg). One of northern Illinois' favorite paddles.",
 motor="Often too small for power boats but well suited for canoes and kayaks; the only pooled water is the small Belvidere dam impoundment (portage).",
 depth="Floatable most of the season but scrapey when low: the Cherry Valley run wants 400+ cfs at Perryville; the Belvidere leg is good 200–600.",
 gauge={"site":"05440000","name":"Kishwaukee R at Perryville","min":400,"lo":400,"hi":600},
 unpinned=["Distillery Road Conservation Area (Belvidere)","Kishwaukee River Forest Preserve (mouth take-out)"],
 sources=[["Illinois Paddle","https://www.illinoispaddle.com/kishwaukee-river.html"],["Miles Paddled","https://milespaddled.com/kishwaukee-river-i/"]])
river("nippersink","Nippersink Creek","green",[42.38,-88.40,42.47,-88.15],state="IL",
 stretch="Keystone Rd Landing (Glacial Park, Richmond) → Pioneer Rd → Spring Grove (Nippersink Canoe Base), ~12–15 mi through McHenry County's prettiest valley.",
 motor="Managed by the county conservation district as a non-motorized canoe/kayak trail — carry-in landings only. Below the Canoe Base it feeds the motorized Chain O'Lakes.",
 depth="Reliably floatable most of the season; scrapey below ~40 cfs at Spring Grove, enjoyable at 65–150. The district closes the trail above 650 cfs (no bridge clearance).",
 gauge={"site":"05548280","name":"Nippersink Ck nr Spring Grove","min":40,"lo":65,"hi":150,"flood":650},
 sources=[["McHenry County Conservation District","https://www.mccdistrict.org/visit___explore/things_to_do/paddle.php"],["Miles Paddled","https://milespaddled.com/nippersink-creek/"]])
river("dupage","DuPage River","green",[41.40,-88.35,41.85,-88.05],state="IL",qname=["DuPage River","West Branch DuPage River"],
 stretch="Knoch Knolls Park (Naperville, at the branch confluence) → Plainfield → Hammel Woods (Shorewood) → Channahon State Park → the Des Plaines confluence, ~29 mi; West Branch add-on from Warrenville (Fawell dam portage). Dam portages at Shorewood and Channahon.",
 motor="Narrow, shallow non-motorized water trail with carry-in launches; no motorized dam pools (the Hammel Woods dam came out in 2021).",
 depth="Floats most of the season; gets bony below ~200 cfs (~2.5 ft) at Shorewood. West Branch riffles go unpaddleable in the driest spells.",
 gauge={"site":"05540500","name":"DuPage R at Shorewood","min":200,"lo":200,"hi":600},
 unpinned=["Mack Rd canoe launch (Warrenville, W Branch)","Riverside Parkway landing (Plainfield)","Hammel Woods Black Rd access (Shorewood)","McKinley Woods / Kerry Sheridan Grove (Channahon)"],
 sources=[["Illinois Paddle","https://www.illinoispaddle.com/dupage-river.html"],["Openlands Paddle Illinois","https://openlands.org/paddle-illinois/mcdowell-grove-to-knoch-knolls-park/"],["Will County Forest Preserves","https://www.reconnectwithnature.org/news-events/big-features/your-guide-to-paddling-will-county/"]])
river("desplaines","Des Plaines River","green",[41.63,-88.10,42.51,-87.80],state="IL",
 stretch="Des Plaines River Water Trail: Russell Rd (Wisconsin line) through six Lake County launches → Wright Woods (Vernon Hills), continuing through Cook County to Columbia Woods (Willow Springs) and on to Isle a la Cache (Romeoville), ~81 mi in all.",
 motor="A designated non-motorized water trail — no trailered ramps, and the Cook County forest preserves ban gasoline motors.",
 depth="Reliable most of the season; the uppermost reach gets scrapey in drought (wading possible below ~35 cfs at Gurnee) and Lake County logjams multiply at low water.",
 gauge={"site":"05528000","name":"Des Plaines R nr Gurnee","min":35,"lo":50,"hi":300},
 unpinned=["Gurnee canoe launch (McClure Ave)","Knollwood launch (Madison St, Burr Ridge)","Isle a la Cache launch (Romeoville)"],
 sources=[["Lake County Forest Preserves","https://www.lcfpd.org/things-to-do/recreation/canoe-launches/"],["Miles Paddled","https://milespaddled.com/des-plaines-river/"],["National Rivers Project","https://www.nationalriversproject.com/il/des-plaines-river-des-plaines-water-trail"]])
river("vermilion-il","Vermilion River (IL)","green",[40.85,-89.10,41.35,-88.55],state="IL",qname="Vermilion River",
 stretch="Illinois' whitewater river: Lowell (IL-178 bridge) → Oglesby boat launch, ~9 mi of Class II–III including Wildcat Rapids. Flatter floats upstream from Pontiac → Streator.",
 motor="Rocky rapids and shallow riffles — raft/kayak/canoe water only; the old cement-plant lowhead dam was removed in 2021.",
 depth="A spring river, not a summer river: outfitters run May–mid-July only. ~500 cfs is tight; good levels start over 1,000. Usually too low from mid-July on.",
 gauge={"site":"05555300","name":"Vermilion R nr Leonore","min":500,"lo":1000,"hi":3000},
 watch="Plan this one for May–June. By late summer it's usually a rock garden.",
 unpinned=["McDowell access (SW of Pontiac)","Play Park ramp (Pontiac)"],
 sources=[["American Whitewater","https://www.americanwhitewater.org/content/River/view/river-detail/651/main"],["Vermillion River Rafting","https://www.vermillionriverrafting.com/ride-the-river.php"]])
river("apple","Apple River","green",[42.20,-90.32,42.51,-89.95],state="IL",
 stretch="Apple River Canyon State Park → S Apple River Rd (~10 mi of Driftless canyon bluffs); a lower run below the Hanover dam to the Mississippi backwaters.",
 motor="Small, shallow, rocky Driftless stream — no motorized use documented.",
 depth="Marginal in dry summers: below 200 cfs not recommended (even 206 meant butt-scooting). Best after rain or in wet years.",
 gauge={"site":"05419000","name":"Apple R nr Hanover","min":200,"lo":250,"hi":300},
 watch="Stay clear of the 11-ft Hanover dam between the two runs.",
 unpinned=["E Townsend Rd bridge"],
 sources=[["Miles Paddled","https://milespaddled.com/apple-river-i-illinois/"],["IL DNR — Apple River Canyon","https://dnr.illinois.gov/parks/activity/park.applerivercanyon.html"]])
river("kankakee","Kankakee River","green",[41.05,-88.35,41.45,-87.50],state="IL",
 stretch="Momence → Aroma Park → Kankakee (Bird Park) → Kankakee River State Park → Wilmington (~38 mi). Best runs: Bird Park → Chippewa (7 mi) and Chippewa → Wilmington dam (11 mi, Area 9 launch 2.4 mi below Chippewa). Avoid the Wilmington millrace.",
 motor="The state-park stretch is shallow, rocky and essentially non-motorized — but the dam pools are not: Momence pool, Six Mile Pool at Aroma Park (heavy powerboat/jet-ski use) and the Wilmington pool.",
 depth="Reliably floatable all season — big dam-regulated river, liveries run all summer. Portages at Momence, Kankakee and Wilmington dams.",
 gauge={"site":"05527500","name":"Kankakee R nr Wilmington","min":None,"lo":None,"hi":None},
 unpinned=["Area 9 launch (Kankakee River SP)"],
 sources=[["Openlands Paddle Illinois","https://openlands.org/paddle-illinois/bird-park-to-chippewa-boat-launch/"],["Kankakee River PPA","https://www.kankakeeriverppa.org/trips-and-distances/"],["IL DNR state park","https://dnr.illinois.gov/parks/park.kankakeeriver.html"]])
river("fox-il2","Fox River (IL — Yorkville to Ottawa)","green",[41.30,-88.90,41.70,-88.35],state="IL",qname="Fox River",
 stretch="Yorkville (Bicentennial Riverfront Park & the Marge Cline whitewater course) → Silver Springs → Millington → Sheridan → Wedron dells → Dayton → Ottawa (~36 mi). Only one dam (Dayton) below Yorkville.",
 motor="Shallow, mostly free-flowing kayak water with only the occasional fishing boat — a different river from the motorized dam pools upstream.",
 depth="Water levels are almost always reliable; expect island scraping below ~5 ft at the Dayton gauge in late-summer lows.",
 gauge={"site":"05552500","name":"Fox R at Dayton","min":700,"lo":700,"hi":2000},
 watch="Powerboat wakes return where the Fox meets the Illinois River at Ottawa.",
 sources=[["Illinois Paddling Council","https://illinoispaddling.org/paddling-the-fox-river/"],["Miles Paddled","https://milespaddled.com/fox-river-i-illinois-tributary/"],["Openlands","https://openlands.org/paddle-illinois/yorkville-to-silver-spring-state-park/"]])
river("fox-chain","Fox River (IL — Chain O'Lakes to Aurora)","blue",[41.70,-88.50,42.50,-88.10],state="IL",qname="Fox River",
 stretch="Chain O'Lakes → McHenry → Algonquin → Elgin → Aurora: a dozen dams in 60 miles, each with a motorized pool.",
 motor="Heavy powerboat water — the Chain O'Lakes requires a waterway sticker and has buoyed channels.",depth="Pooled and deep.",
 sources=[["Illinois Paddling Council","https://illinoispaddling.org/paddling-the-fox-river/"]])
river("illinois-r","Illinois River","blue",[41.05,-89.60,41.55,-88.15],state="IL",
 stretch="The barge waterway: Channahon → Morris → Ottawa → Starved Rock → Peru.",
 motor="Commercial navigation channel — tows, wakes and lock/dam pools.",depth="Always deep; the constraint is traffic and wind.",
 sources=[["Illinois Waterway","https://en.wikipedia.org/wiki/Illinois_Waterway"]])
river("rock-il","Rock River (IL)","blue",[41.45,-90.65,42.50,-88.90],state="IL",qname="Rock River",
 stretch="Rockton → Rockford → Oregon → Dixon → Rock Island; a National Water Trail, but big shared water.",
 motor="Trailered powerboat ramps throughout and ~8 dam pools.",depth="Reliable all summer; headwinds are the bigger issue.",
 sources=[["Rock River Trail","https://rockrivertrail.com/water-trail/"]])

# ============ MICHIGAN — west Lower Peninsula ============
river("peremarquette","Pere Marquette River","green",[43.80,-86.45,44.00,-85.70],state="MI",
 stretch="The full 65-mi National Scenic River: M-37 Bridge at 'The Forks' (Baldwin) → Green Cottage → Gleason's → Bowman Bridge → Rainbow Rapids → Sulak/Branch → Indian Bridge → Custer → Scottville → Old US-31 Bridge (Ludington). Livery water runs to Scottville; the last leg to Ludington is quieter bring-your-own water.",
 motor="Formally non-motorized: motorized vessels are prohibited upstream of Indian Bridge on National Forest lands. A USFS watercraft permit ($2/day, on-river 9am–6pm) is required for ALL craft from the Friday of Memorial Day weekend through Labor Day.",
 depth="Groundwater-fed and rock-steady: 2–4 ft average all summer — the Scottville gauge has never recorded a flow too low to float.",
 gauge={"site":"04122500","name":"Pere Marquette R at Scottville","min":None,"lo":None,"hi":None},
 watch="Buy the USFS permit (recreation.gov) before summer weekends — rangers check.",
 unpinned=["Henry's Landing livery & campground (Scottville)"],
 sources=[["USFS permit","https://www.recreation.gov/permits/249987"],["USFS river page","https://www.fs.usda.gov/r09/huron-manistee/recreation/groups/pere-marquette-national-scenic-river"],["Baldwin Canoe","https://baldwincanoe.com/pere-marquette-river/"]])
river("pine-mi","Pine River (MI)","green",[44.00,-85.95,44.25,-85.45],state="MI",qname="Pine River",
 stretch="Edgetts → Skookum → Elm Flats → Dobson Bridge → Peterson Bridge → Low Bridge (last take-out before Tippy Dam backwaters). The fastest average current in the Lower Peninsula.",
 motor="Formally non-motorized on the Wild & Scenic corridor: launching motorized watercraft is prohibited Elm Flats → Low Bridge, and a USFS watercraft permit is required Memorial Day weekend → Labor Day (covers kayaks, tubes, SUPs).",
 depth="Spring-fed and reliably floatable all season (mid-July ~245 cfs is typical and clean).",
 gauge={"site":"04125460","name":"Pine R nr Hoxeyville","min":None,"lo":None,"hi":None},
 watch="Permit required in summer — reserve on recreation.gov.",
 unpinned=["Silver Creek State Forest Campground (Luther)"],
 sources=[["USFS permit","https://www.recreation.gov/permits/249990"],["Pine River map","https://www.thepineriver.com/pine-river/map"],["USFS Wild & Scenic","https://www.fs.usda.gov/r09/huron-manistee/recreation/pine-national-scenic-river"]])
river("littlemanistee","Little Manistee River","green",[44.05,-86.30,44.25,-85.75],state="MI",
 stretch="Driftwood Valley → Nine Mile Bridge → Six Mile Bridge → Old Stronach Bridge. Tight, fast and woodsy.",
 motor="Narrow, log-filled channel with carry-in launches only — motors impractical (National Scenic Study River).",
 depth="Runnable by kayak most of the season but genuinely shallow in dry summers; expect logs and the occasional pullover.",
 gauge={"site":"04126176","name":"Little Manistee R nr Irons","min":None,"lo":None,"hi":None},
 sources=[["USFS","https://www.fs.usda.gov/r09/huron-manistee/recreation/groups/little-manistee-river-national-scenic-study-river"],["Paddling.com","https://paddling.com/paddle/trips/little-manistee-river-michigan-10"]])
river("platte-mi","Platte River (MI)","green",[44.55,-86.20,44.75,-85.80],state="MI",qname="Platte River",
 stretch="Upper river: Veterans Memorial launch (US-31) → Platte River SFCG → Platte River Park (Honor) — a real but advanced run (~50% tip-over rate per the livery). Lower: Honor (Riverside Canoes / M-22) → Loon Lake → Platte Point at Lake Michigan through Sleeping Bear Dunes — the classic clear-water family float.",
 motor="Slow-no-wake by state watercraft rule on the entire Lower Platte; the NPS caps motorboats on Loon Lake at 5 mph. Kayaks and tubes dominate.",
 depth="Spring-fed, 2–3 ft over sand, floatable all season (mid-July ~169 cfs ≈ 123% of median).",
 gauge={"site":"04126740","name":"Platte R at Honor","min":None,"lo":None,"hi":None},
 unpinned=["Riverside Canoes / M-22 bridge"],
 sources=[["NPS paddle & float","https://www.nps.gov/slbe/planyourvisit/paddle-and-float.htm"],["MI watercraft controls","https://www.michigan.gov/dnr/managing-resources/laws/controls/localcontrols/benzie/watercraft"]])
river("betsie","Betsie River","green",[44.45,-86.26,44.70,-85.75],state="MI",
 stretch="Grass Lake campground (Wallin) → Homestead Dam portage (Benzonia) → US-31 → Grace Rd, then on through the Betsie River State Game Area to Betsie Bay (Elberta/Frankfort). A state Natural River — livery water is firm to Grace Rd; below is wilder bring-your-own paddling.",
 motor="No controls on the river itself, but the narrow, log-strewn channel keeps motorboats down on Betsie Lake at the mouth.",
 depth="Generally floatable all season (~3–5 ft on the lower river) but can scrape in dry spells — no active gauge, so check with local liveries.",
 unpinned=["Wallin Rd bridge access","Betsie River Township Park (Kurick Rd)","Betsie Bay landing (Elberta)"],
 sources=[["Betsie River water trail map","https://s21124.pcdn.co/wp-content/uploads/2024/07/MCTA_BetsieRiver_web2024update.pdf"],["Paddling.com","https://paddling.com/paddle/trips/betsie-river-michigan"]])
river("boardman","Boardman-Ottaway River","green",[44.55,-85.75,44.80,-85.30],state="MI",qname=["Boardman River","Boardman-Ottaway River","Ottaway River"],
 stretch="Forks / Scheck's Place → Brown Bridge Quiet Area → Shumsky's → Beitner Park (Keystone & Sabin rapids — experienced paddlers) → Boardman Lake → downtown Traverse City.",
 motor="Formally non-motorized: the DNR Natural River plan bars motorized vessels from the flowing river — motors only on the impoundments and Boardman Lake.",
 depth="Spring-fed, 2–4 ft, reliable all season (mid-July ~144 cfs sits mid-normal).",
 gauge={"site":"04126970","name":"Boardman R nr Mayfield","min":None,"lo":None,"hi":None},
 watch="HAZARD (as of July 2026): April 2026 flood damage — Beitner Landing is closed indefinitely and the Shumsky → Beitner and Beitner → Jack's sections are unpassable. Open water: Forks → Shumsky (~14.7 mi) and Jack's Landing → Boardman Valley Nature Preserve (2.6 mi). Keystone/Sabin rapids below Beitner Rd are the hardest water.",
 sources=[["Boardman Natural River plan","https://www.michigan.gov/-/media/Project/Websites/dnr/Documents/Fisheries/NaturalRivers/Archive/Boardman_River_Plan.pdf"],["GT Conservation District","https://natureiscalling.org/river-paddle-upper-boardman"]])
river("jordan-mi","Jordan River","green",[44.95,-85.25,45.17,-84.90],state="MI",qname="Jordan River",
 stretch="Graves Crossing (M-66) → Chestonia → Webster's Bridge → Rogers Rd → East Jordan at Lake Charlevoix. Michigan's first designated Natural River.",
 motor="Formally non-motorized: DNR watercraft controls ban motorized vessels on the Jordan throughout Antrim County.",
 depth="Cold, strongly spring-fed and very stable — ~150–200 cfs mid-July is normal; liveries run all season. Graves → Chestonia is the twisty advanced leg; Webster's → Rogers the easy one.",
 gauge={"site":"04127800","name":"Jordan R nr East Jordan","min":None,"lo":None,"hi":None},
 unpinned=[],
 sources=[["MI DNR watercraft controls","https://www.michigan.gov/en/dnr/managing-resources/laws/controls/localcontrols/antrim/watercraft"],["Watershed Council","https://watershedcouncil.org/waterbody/jordan-river-2/"]])
river("white-mi","White River","green",[43.38,-86.40,43.60,-85.95],state="MI",qname="White River",
 stretch="Hesperia dam → Pines Point (USFS) → Diamond Point → Fruitvale Rd (Happy Mohawk) → Whitehall at White Lake. A state Natural River.",
 motor="No formal ban, but shallow and log-obstructed — motors stay on White Lake.",
 depth="Reliable all-summer float (liveries run all season; generally under 3 ft with plenty of wood).",
 gauge={"site":"04122200","name":"White R nr Whitehall","min":None,"lo":None,"hi":None},
 unpinned=["Covell Park launch (Whitehall)"],
 sources=[["Michigan Water Trails","https://www.michiganwatertrails.org/trail.asp?ait=cv&cid=253"],["Paddling.com","https://paddling.com/paddle/trips/white-river-in-michigan"]])
river("rogue","Rogue River (MI)","green",[43.00,-85.75,43.30,-85.45],state="MI",qname="Rogue River",
 stretch="Twelve Mile Rd → Rockford dam portage → Childsdale → Rogue River Rd → Grand Rogue Park at the Grand River confluence. Rocky trout water minutes from Grand Rapids.",
 motor="Small, shallow and rocky — impractical for motors above the Grand confluence (lower river is a state Natural River).",
 depth="Floatable through summer but thin in spots — reports of shallow rock gardens and downed trees at typical levels.",
 gauge={"site":"04118500","name":"Rogue R nr Rockford","min":None,"lo":None,"hi":None},
 unpinned=["Twelve Mile Rd crossing","Childsdale access (Plainfield Twp)","Rogue River Rd bridge"],
 watch="Skip Kent County's 'Rogue River Park' (Belshire Ave) — bank fishing only, no launch.",
 sources=[["American Whitewater","https://www.americanwhitewater.org/content/River/view/river-detail/10363/main"],["LGROW","https://www.lgrow.org/rogue-river"]])
river("manistee","Manistee River (lower)","blue",[44.20,-86.36,44.45,-85.85],state="MI",qname="Manistee River",
 stretch="Tippy Dam → High Bridge → Manistee Lake / Lake Michigan.",
 motor="Big tailwater with heavy motorized fishing traffic (jet sleds, drift boats) in the salmon and steelhead runs.",depth="Dam-controlled and stable year-round.",
 sources=[["USFS High Bridge","https://www.fs.usda.gov/r09/huron-manistee/recreation/high-bridge-river-access"]])
river("muskegon","Muskegon River","blue",[43.20,-86.35,43.50,-85.55],state="MI",
 stretch="Croton Dam → Newaygo (the famous float) → Bridgeton → Muskegon; a 41-mi water trail.",
 motor="Wide dam tailwater shared with drift boats and jet sleds.",depth="Dam-regulated, floatable all summer.",
 sources=[["Muskegon River Water Trail","https://www.nationalriversproject.com/mi/muskegon-river-muskegon-river-water-trail"]])
river("grand-mi","Grand River","blue",[42.85,-86.25,43.10,-85.40],state="MI",qname="Grand River",
 stretch="Grand Rapids → Grand Haven (Lower Grand water trail, 35 access points).",
 motor="Michigan's longest river; motorized launches throughout, busy near Grand Haven.",depth="Large, deep and slow — floatable regardless of rainfall.",
 sources=[["Lower Grand water trail","https://www.lgrow.org/grand-river-water-trail"]])
river("kalamazoo","Kalamazoo River","blue",[42.30,-86.25,42.70,-85.50],state="MI",
 stretch="Allegan → Allegan State Game Area → New Richmond → Saugatuck at Lake Michigan.",
 motor="Lower river and Kalamazoo Lake are a busy harbor (powerboats, tour boat, chain ferry).",depth="Big steady river, floatable all summer.",
 sources=[["Kalamazoo River Water Trail","https://kalamazooriver.org/explore/water-trail/kalamazoo-river/"]])
river("stjoseph","St. Joseph River","blue",[41.78,-86.55,42.12,-86.20],state="MI",
 stretch="Niles → Berrien Springs → St. Joseph/Benton Harbor (67-mi water trail, dam portages).",
 motor="Motorized throughout; the mouth is a working harbor with large boats.",depth="Big, deep, dam-controlled.",
 sources=[["Michigan Water Trails","https://www.michiganwatertrails.org/trail.asp?ait=cv&cid=141"]])
river("manistee-upper","Manistee River — Upper","green",[44.45,-85.43,44.80,-84.78],state="MI",qname="Manistee River",latmin=44.45,latmax=44.80,
 stretch="The classic all-summer float upstream of Tippy, ~90 river miles in order: Cameron Bridge → Upper Manistee SFCG (CR-612) → M-72 bridge → CCC Bridge → Sharon → Smithville (M-66) → Chippewa Landing (Manton). Multi-day livery trips (M-72 → Chippewa Landing sells as ~85 mi).",
 motor="Quiet state-forest water — no formal ban found, but this shallow, sandy upper river sees essentially no motor traffic (liveries and campers instead).",
 depth="Groundwater-fed and stable — floatable all season, typically 2–4 ft over sand. One of Michigan's most dependable summer rivers.",
 watch="Access order matters here: M-72 is upstream of CCC Bridge, and Chippewa Landing sits upstream of Baxter Bridge — plan legs from the pins, not old guidebooks.",
 unpinned=["Cameron Bridge Rd access (Frederic)","Sharon Rd bridge"],
 sources=[["MI DNR Upper Manistee plan","https://www.michigan.gov/dnr/-/media/Project/Websites/dnr/Documents/Fisheries/NaturalRivers/Upper-Manistee-Action-Plan.pdf"],["Chippewa Landing","https://chippewalanding.com/"],["Michigan Water Trails","https://www.michiganwatertrails.org/"]])

# ============ ILLINOIS — south of US-24 ============
def q(id,name,cls,bbox,state,stretch,motor,depth,qn=None,watch="",unpinned=None):
    river(id,name,cls,bbox,state=state,qname=qn,stretch=stretch,motor=motor,depth=depth,watch=watch,unpinned=unpinned)
q("mfvermilion","Middle Fork Vermilion","green",[40.03,-87.85,40.35,-87.60],"IL","Illinois' only National Scenic River: the standard livery run is Kinney's Ford → Kickapoo Landing (Kickapoo SRA), ~13.5 mi with a split point at Bunker Hill (~5.5). Scenic designation starts ~3.5 mi upstream at Higginsville.","Riffly and shallow — canoe/kayak water; liveries in the state rec area.","Best spring–early summer; scrapey by late July.",qn=["Middle Fork Vermilion River","Middle Fork of the Vermilion River"],unpinned=["Higginsville Bridge access (Collison)","Kinney's Ford canoe access","Bunker Hill canoe access"])
q("mackinaw","Mackinaw River","green",[40.45,-89.80,40.75,-88.85],"IL","Sandy, wooded run west of Bloomington: Congerville → Mackinaw → toward the Illinois River.","Too shallow for motors along the paddling reaches.","A spring/early-summer river — often too thin by midsummer.")
q("sangamon","Sangamon River","green",[39.98,-88.65,40.25,-88.30],"IL","Upper Sangamon water trail: Lake of the Woods (Mahomet) → Lodge Park → Monticello (Allerton Park), ~25 mi. A separate Springfield-area trail runs Riverton → Riverside Park → Carpenter Park (~8–9 mi) — the two are ~70 dam-broken river miles apart through Decatur, not one run.","Quiet wooded water; carry-in accesses.","Floats most of the season; slow and muddy in low water.",watch="Don't plan Monticello → Riverton as a trip — Decatur's dams and ~70 river miles sit between the two mapped trails.",unpinned=["Riverbend / Sangamon Greenway launch (Mahomet)","Lodge Park canoe access (Monticello)","Wheeland Park ramp (Riverton)","Riverside Park launch (Springfield)","Carpenter Park (Springfield)"])
q("spoon","Spoon River","green",[40.25,-90.55,40.95,-89.75],"IL","London Mills → Bernadotte (dam portage) → Havana at the Illinois River, ~55 river miles of old mill-town canoe country.","No motor traffic above the backwaters.","Decent through July; sandbars late summer.",unpinned=["Duncan Mills access (informal)","Ellisville access (unverified)"])
q("embarras","Embarras River","green",[39.10,-88.35,39.50,-88.00],"IL","Lake Charleston spillway → Fox Ridge SP → Greenup covered-bridge country, ~31 mi (the Greenup take-out at the Cumberland County covered bridge is informal).","Shallow riffle water — kayaks only in practice.","Best through early July.",unpinned=["County Road 1200N bridge ramp"])
q("cache-il","Cache River (Lower)","green",[37.25,-89.15,37.40,-88.85],"IL","The cypress-tupelo swamp trail near Karnak — Illinois' bayou; marked paddle loops.","Still backwater, electric/paddle only in the state natural area.","Floatable all year — it's a swamp channel, not a riffle river.")
q("bigmuddy","Big Muddy River","green",[37.55,-89.55,38.00,-89.20],"IL","Murphysboro (Riverside Park) → Turkey Bayou Campground (USFS) through the Shawnee bottoms.","Sluggish and deep; occasional jon boat near the Mississippi.","Reliable all season.",unpinned=["Riverside Park ramp (Murphysboro)"])
q("kaskaskia","Kaskaskia River (upper)","green",[38.95,-89.20,39.42,-88.70],"IL","Lake Shelbyville spillway → Cowden → Rend Bridge (Ramsey) → Vandalia, ~50 river miles of wooded, easy water (Rend Bridge → Vandalia alone is ~25).","Quiet water; motors mostly below Carlyle.","Dam-fed — good most of the season.",unpinned=["Cowden bridge access (informal)","Rend Bridge ramp (E of Ramsey)","Vandalia boat ramp (US 40 bridge)"])
q("lusk","Lusk Creek","green",[37.40,-88.60,37.62,-88.40],"IL","The Shawnee canyon gem near Eddyville: Saltpeter Cave (1.5-mi carry in via Trail 481) → the USFS Eddyville Blacktop access, ~8 mi of sandstone gorge.","Tiny canyon creek — kayaks only.","Spring only: needs ~250–400 cfs from recent rain; done by June most years.")

# ============ MICHIGAN — east Lower Peninsula ============
q("ausable","Au Sable River","green",[44.50,-84.80,44.75,-84.05],"MI","Grayling → Mio: the canoe-marathon river; state-forest campgrounds all along.","Non-motorized in practice above Mio; drift boats below the dams.","Spring-fed and steady all season.",qn=["Au Sable River","AuSable River"])
q("rifle","Rifle River","green",[44.00,-84.20,44.45,-83.70],"MI","Ranch Campground launch (Rifle River Rec Area, Lupton) → Selkirk → Moffatt Bridge → Omer, ~32 river miles — Michigan's livery classic. Below Omer is a separate coastal trail.","Shallow and sandy — kayak/tube water.","Reliable all summer.",unpinned=["White's Canoe Livery (Sterling)"])
q("sturgeon-mi","Sturgeon River (LP)","green",[45.15,-84.75,45.45,-84.55],"MI","Trowbridge Rd (S of Wolverine) → Wolverine → Haakwood → Rondo Rd → Burt Lake State Park, ~17 mi: the Lower Peninsula's fastest current.","Too fast and narrow for motors.","Spring-fed — good all season.",qn="Sturgeon River",watch="Fastest river in the LP — strainer hazards; not a first-timer float.")
q("pigeon-mi","Pigeon River","green",[45.05,-84.55,45.45,-84.30],"MI","Pigeon River Country (elk country) → Mullett Lake, ~32 river miles in two characters: Pigeon Bridge SFCG → Pigeon River SFCG up top, and the lower boulder run Afton Rd → Andreae Nature Preserve (~7 mi, high-water only).","Wild state-forest water; carry-in.","Spring-fed and steady; watch deadfall.",qn="Pigeon River",watch="Multiple portages north of Ford Lake Rd; the lower boulder run is not for beginners.",unpinned=["Pigeon River Rd bridge (Afton)"])
q("huron-mi","Huron River","green",[42.05,-83.95,42.65,-83.15],"MI","The 104-mi Huron River National Water Trail: Proud Lake (Milford) → Hudson Mills → Ann Arbor (Argo/Gallup) → Ypsilanti (~62 mi), continuing past Flat Rock to Lake Erie at Pointe Mouillee — the leg below Ypsilanti is quieter bring-your-own water.","Non-motorized on the river; small motors on the chain-of-lakes impoundments.","Dam-controlled — floatable all season.",qn="Huron River",unpinned=["Riverside Park (Ypsilanti)","Lake Erie Metropark launch (trail terminus)"])
q("chippewa-mi","Chippewa River (MI)","green",[43.50,-85.15,43.70,-84.20],"MI","Deerfield Nature Park → Mt. Pleasant (Chipp-A-Waters/Island Park) → Chippewa Nature Center → the Tridge (Midland), ~47 river miles. Common day floats: Deerfield → Mt. Pleasant and Nature Center → Tridge.","Shallow riffle water through town parks.","Good most of the season; thin in drought.",qn="Chippewa River")
q("cass","Cass River","green",[43.20,-84.00,43.65,-83.10],"MI","The official 37.5-mi Cass River Water Trail: M-46 Roadside Park → Vassar → Tuscola → Frankenmuth (dam portage at Heritage Park) → Bridgeport (Davis Park) → M-13 → Wickes Park on the Saginaw River.","Quiet farm-country water; carry-in launches.","Best through July; shallow gravel late summer.",watch="Don't extend above M-46 — a failed dam below Caro is hazardous.",unpinned=["Wickes Park (Saginaw R., trail end)"])
q("thunderbay","Thunder Bay River","green",[44.95,-84.20,45.15,-83.40],"MI","~70 dam-broken river miles Atlanta → Alpena — NOT one continuous run. Paddle it in segments: Atlanta, Hillman (Emerick Park), Long Rapids → Four Mile dam (Class II), and the lower Alpena blueway to Ford Ave at the mouth.","Quiet northwoods water between small dams.","Good spring through July.",watch="Dams at Atlanta, Hillman, Norway/Lake Winyah, Four Mile (portage left) and Ninth St Alpena break the river — plan one segment at a time.")

# ============ KENTUCKY ============
q("elkhorn","Elkhorn Creek","green",[38.10,-84.95,38.40,-84.60],"KY","The Bluegrass classic: Forks of the Elkhorn → Kentucky River, Class I–II ledges.","Riffle creek — kayak water only.","Best spring–July; scrapey late summer.")
q("red-ky","Red River (Gorge)","green",[37.75,-83.80,37.90,-83.45],"KY","Red River Gorge: Copperas Creek → Clay City under the sandstone arches.","Canoe/kayak only through the gorge.","A spring river — usually too low after June.",qn="Red River")
q("green-ky","Green River","green",[37.10,-86.40,37.30,-85.85],"KY","Mammoth Cave NP: Dennison Ferry → Green River Ferry → Houchin Ferry.","Park water — paddle craft and the odd jon boat.","Dam-fed and reliable all season.",qn="Green River")
q("barren","Barren River","green",[36.80,-86.60,37.10,-86.10],"KY","Bowling Green water trail below Barren River Lake.","Slow green water; some fishing boats near ramps.","Reliable all season.")
q("nolin","Nolin River","green",[37.22,-86.30,37.35,-86.00],"KY","Nolin dam tailwater → Green River confluence inside Mammoth Cave NP.","Paddle water in the park.","Tailwater — dependable spring through fall.")
q("rockcastle","Rockcastle River","green",[36.95,-84.40,37.35,-84.10],"KY","Upper river: Livingston area float water (the lower narrows are expert Class III+).","No motors — shallow and rocky.","Spring–early summer; low by July.",watch="Take out above the Narrows unless you're an experienced whitewater boater.")
q("licking-ky","Licking River","green",[38.05,-83.65,38.35,-83.25],"KY","Cave Run Lake tailwater → Blue Licks; smallmouth float water.","Quiet water; jon boats near ramps.","Tailwater-steady through summer.",qn="Licking River")
q("floydsfork","Floyds Fork","green",[38.02,-85.60,38.25,-85.38],"KY","The Parklands of Floyds Fork water trail through Louisville's park system.","Non-motorized park water trail.","Best spring–July; thin in late summer.")
q("gasper","Gasper River","green",[36.90,-86.85,37.05,-86.50],"KY","Scenic bluff run west of Bowling Green.","Narrow kayak creek.","Spring and early summer only.")
q("rough-ky","Rough River","green",[37.50,-86.60,37.70,-86.10],"KY","Below Rough River dam — easy tailwater float.","Quiet tailwater.","Dam-fed; good most of the season.",qn="Rough River")
q("kentucky-r","Kentucky River","blue",[37.55,-85.25,38.70,-83.70],"KY","Locked navigation river through the Palisades near Lexington.","Motorized pools between locks.","Always deep.")
q("cumberland-ky","Cumberland River (KY)","blue",[36.55,-85.55,37.20,-84.20],"KY","Cumberland Falls area and the big tailwaters below Wolf Creek dam.","Motorized in the pools and lake reaches.","Always floatable.",qn="Cumberland River")
q("ohio-r","Ohio River (Louisville–Cincinnati reach)","blue",[37.75,-87.00,39.30,-82.60],"KY","The big border river — barge navigation water.","Commercial tows and powerboats throughout.","Always deep; wakes and wind are the issue.",qn="Ohio River")

# ============ WEST VIRGINIA ============
q("greenbrier","Greenbrier River","green",[37.65,-80.90,38.40,-79.80],"WV","The longest free-flowing river in the East: Marlinton → Ronceverte with the rail-trail alongside.","Shallow ledge river — paddle craft only.","Good through July; famously low in late summer.")
q("sbpotomac","South Branch Potomac","green",[38.85,-79.40,39.45,-78.60],"WV","Smoke Hole canyon and The Trough (eagle country) near Petersburg/Romney.","Canoe water; The Trough is rail-or-river only.","Best spring through July.",qn=["South Branch Potomac River","South Branch of the Potomac River"])
q("cacapon","Cacapon River","green",[39.00,-78.70,39.63,-78.20],"WV","Wardensville → Capon Bridge → Great Cacapon; gentle ledges.","Quiet paddle water.","Spring–July; scrapey after.")
q("cheat","Cheat River (upper)","green",[38.90,-79.90,39.55,-79.30],"WV","Parsons → Rowlesburg 'Cheat Narrows' float reaches (the canyon below is expert).","No motors — rocky free-flowing water.","Best spring–early July.",qn="Cheat River")
q("elk-wv","Elk River (WV)","green",[38.30,-81.70,38.70,-80.20],"WV","Webster Springs → Sutton → Charleston reaches; trout water up top.","Quiet water; a few jon boats low down.","Spring-fed upper river holds up well into summer.",qn="Elk River")
q("coal-wv","Coal River","green",[38.20,-81.95,38.45,-81.55],"WV","The Coal River Water Trail south of Charleston (Meadowood → St Albans).","Designated non-motorized water trail.","Reliable most of the season.",qn="Coal River")
q("bluestone","Bluestone River","green",[37.40,-81.15,37.65,-80.85],"WV","Bluestone National Scenic River gorge → Bluestone Lake.","Remote canyon paddle.","Spring only — low by June most years.")
q("new-wv","New River","blue",[37.20,-81.25,38.20,-80.75],"WV","The New River Gorge — big-volume rafting water with flatwater pools.","Jet boats in the flats; big rapids in the gorge (guided rafting country).","Always has water.",qn="New River")
q("kanawha","Kanawha River","blue",[38.10,-81.95,38.45,-81.15],"WV","Charleston's navigation river below Kanawha Falls.","Barge and powerboat water.","Always deep.")

# ============ OHIO ============
q("mohican","Mohican River","green",[40.45,-82.40,40.75,-82.00],"OH","Loudonville livery country: state park → Brinkhaven through the gorge.","Canoe-livery water — no motors.","Reliable all season (liveries run all summer).")
q("littlemiami","Little Miami River","green",[39.05,-84.35,39.80,-83.80],"OH","National Scenic River water trail: Xenia → Loveland → Milford, 80+ miles of access.","Non-motorized scenic river.","Reliable spring through fall.")
q("bigdarby","Big Darby Creek","green",[39.75,-83.35,40.10,-83.10],"OH","Battelle Darby metro parks run west of Columbus — a National Scenic stream.","Carry-in metro-park water.","Best through July; thin in dry spells.")
q("kokosing","Kokosing River","green",[40.30,-82.65,40.50,-82.15],"OH","Ohio's first water trail: Mount Vernon → Howard → Gambier.","Quiet college-country stream.","Good most of the season.")
q("mad-oh","Mad River","green",[39.80,-84.10,40.05,-83.70],"OH","Ohio's spring-fed trout stream: Urbana → Springfield → Dayton.","Narrow, cold and quick — kayak water.","Spring-fed — floats all season.",qn="Mad River")
q("littlebeaver","Little Beaver Creek","green",[40.68,-80.80,40.85,-80.45],"OH","Wild & Scenic canyon near East Liverpool (Beaver Creek SP).","No motors in the gorge.","Spring–June; drops fast after rain season.")
q("cuyahoga","Cuyahoga River","green",[41.10,-81.60,41.42,-81.30],"OH","Cuyahoga Valley National Park water trail: Kent → Peninsula → Cleveland.","Non-motorized through the park.","Good most of the season; check after storms.")
q("grand-oh","Grand River (OH)","green",[41.55,-81.30,41.85,-80.80],"OH","Harpersfield covered bridge → Painesville — Wild & Scenic lower gorge.","Quiet water; some fishing boats near the mouth.","Best through July.",qn="Grand River")
q("stillwater-oh","Stillwater River","green",[39.85,-84.50,40.25,-84.25],"OH","Covington → Englewood dam country north of Dayton.","Carry-in park water.","Spring through July.",qn="Stillwater River")
q("sandusky-oh","Sandusky River","green",[40.80,-83.35,41.40,-82.85],"OH","Upper Sandusky → Tiffin → Fremont water trail (dam removed at Ballville).","Riffle water; walleye-run jon boats near Fremont.","Good through July.",qn="Sandusky River")
q("maumee","Maumee River","blue",[41.30,-84.60,41.75,-83.45],"OH","Big NW-Ohio river: Napoleon → Grand Rapids → Toledo.","Motorized; famous walleye-run boat traffic.","Always floatable.")
q("muskingum","Muskingum River","blue",[39.35,-82.10,40.10,-81.40],"OH","Historic hand-operated locks: Zanesville → Marietta.","Motorized navigation river.","Always deep.")

# ============ MINNESOTA ============
q("rum","Rum River","green",[45.15,-93.85,46.10,-93.20],"MN","State water trail: Mille Lacs → Milaca → Anoka at the Mississippi.","Quiet water trail; carry-in accesses throughout.","Reliable most of the season.")
q("cannon","Cannon River","green",[44.25,-93.35,44.60,-92.55],"MN","Faribault → Northfield → Cannon Falls → Red Wing (Welch trestle country).","Non-motorized paddling water between dams.","Good all season except deep drought.")
q("root-mn","Root River (MN)","green",[43.60,-92.30,43.85,-91.25],"MN","Bluff-country classic: Chatfield → Lanesboro → Rushford beside the bike trail.","Quiet paddle water.","Reliable all season.",qn="Root River")
q("zumbro","Zumbro River","green",[44.00,-92.90,44.40,-92.00],"MN","Rochester → Zumbro Falls → Kellogg through the driftless bluffs.","No motor traffic on the river runs.","Good through July; sandy-low late summer.")
q("crowwing","Crow Wing River","green",[46.15,-94.95,46.70,-94.25],"MN","Nimrod → Crow Wing State Park: sandy, easy wilderness water trail with campsites.","Non-motorized water-trail reaches.","Steady sand-country flow all season.")
q("snake-mn","Snake River","green",[45.80,-93.40,46.20,-92.70],"MN","Mora → the St. Croix; mellow below town, whitewater up high.","Quiet water below Mora.","Best through July.",qn="Snake River")
q("kettle","Kettle River","green",[45.80,-93.00,46.55,-92.55],"MN","Banning State Park's sandstone gorge (Class II–III) and mellow water below Sandstone.","No motors — rocky gorge water.","Spring river — low by midsummer.",watch="Banning gorge rapids are intermediate+ — put in below Sandstone for the easy float.")
q("crow-mn","Crow River","green",[45.00,-94.15,45.35,-93.45],"MN","Rockford → Hanover → Dayton at the Mississippi; farm-country water trail.","Quiet water.","Good through July.",qn="Crow River")
q("missheadwaters","Mississippi Headwaters","green",[47.20,-95.25,47.55,-94.75],"MN","Itasca State Park → Bemidji: paddle the Mississippi at 20 feet wide.","Canoe-route water — no motors this small.","Floatable all season (it's spring-fed at the source).",qn="Mississippi River")
q("minnesota-r","Minnesota River","blue",[44.15,-95.00,44.95,-93.55],"MN","Big muddy prairie river: Mankato → Twin Cities.","Motorized.","Always floatable.")
q("stlouis","St. Louis River","blue",[46.55,-92.60,46.95,-92.05],"MN","Jay Cooke's gorges (expert) and the Duluth estuary.","Motorized estuary; expert whitewater above.","Always has water.",qn=["Saint Louis River","St. Louis River"])

# ============ INDIANA ============
q("sugarcreek","Sugar Creek (IN)","green",[39.85,-87.50,40.05,-86.85],"IN","THE Indiana paddle: Crawfordsville → Shades SP → Turkey Run SP covered bridges.","Riffle creek — canoe liveries, no motors.","Spring–June is prime; scrapey by late July.",qn="Sugar Creek")
q("tippecanoe","Tippecanoe River","green",[40.60,-86.90,41.25,-85.80],"IN","Winamac → Monticello: clear, lake-fed and steady ('the Tippy').","Quiet water between the lakes; motors on the lakes themselves.","Lake-fed — reliable all season.")
q("blue-in","Blue River (IN)","green",[38.10,-86.65,38.50,-86.10],"IN","Fredericksburg → Milltown → Wyandotte caves country — Indiana's first Natural & Scenic river.","Livery water — no motors.","Spring-fed enough to run most of the season.",qn="Blue River")
q("whitewater-in","Whitewater River","green",[39.25,-85.15,39.70,-84.80],"IN","Brookville tailwater → Harrison: the fastest gradient in Indiana.","Riffle water, canoe liveries.","Dam-fed — good most of the season.",qn="Whitewater River")
q("wildcat","Wildcat Creek","green",[40.40,-86.95,40.55,-86.10],"IN","Kokomo → Lafayette water trail.","Quiet creek.","Best through July.")
q("bigpine","Big Pine Creek","green",[40.35,-87.50,40.60,-87.05],"IN","Rocky canyon creek near Williamsport — Indiana's mini-whitewater.","Kayak creek.","Spring only.",qn="Big Pine Creek")
q("flatrock-in","Flatrock River","green",[39.18,-85.95,39.60,-85.40],"IN","Columbus → Edinburgh farm-and-woods float.","Quiet water.","Good through July.",qn="Flatrock River")
q("driftwood","Driftwood River","green",[39.15,-86.00,39.35,-85.85],"IN","Short, steady link: Edinburgh → Columbus (joins the East Fork White).","Quiet water.","Reliable all season.")
q("eel-in","Eel River (northern)","green",[40.70,-86.50,41.20,-85.45],"IN","Columbia City → North Manchester → Logansport water trail.","Quiet water between old mill dams.","Good most of the season.",qn="Eel River")
q("cedarck-in","Cedar Creek","green",[41.20,-85.20,41.40,-84.90],"IN","Indiana's other Natural & Scenic river: Auburn → the St. Joseph near Fort Wayne.","Narrow wooded creek.","Spring–June.",qn="Cedar Creek")
q("mississinewa","Mississinewa River","green",[40.55,-86.15,40.80,-85.40],"IN","Marion → the Mississinewa Lake tailwater near Peru.","Quiet water.","Best through July.")
q("wabash","Wabash River","blue",[40.20,-87.25,40.85,-86.25],"IN","Indiana's state river — wide water past Lafayette.","Motorized.","Always floatable.")

# ============ IOWA ============
q("upperiowa","Upper Iowa River","green",[43.30,-92.15,43.55,-91.20],"IA","Iowa's crown jewel: Kendallville → Decorah → the chimney-rock bluffs.","Canoe water — liveries, no motors.","Reliable most of the season.")
q("yellow-ia","Yellow River","green",[43.05,-91.60,43.25,-91.10],"IA","Trout-stream paddle through Effigy Mounds country.","Tiny creek — kayaks only.","Spring–June.",qn="Yellow River")
q("turkey-ia","Turkey River","green",[42.60,-91.85,43.00,-91.00],"IA","Elkader → Garber → Millville through the driftless hills.","Quiet water trail.","Good through July.",qn="Turkey River")
q("volga","Volga River","green",[42.70,-91.90,42.90,-91.20],"IA","Fayette → Volga River Rec Area → Garber.","Narrow wooded water.","Spring–June.")
q("maquoketa","Maquoketa River","green",[42.00,-91.25,42.30,-90.30],"IA","Monticello → Maquoketa caves country (Delhi dam rebuilt).","Quiet water trail.","Good through July.")
q("wapsi","Wapsipinicon River","green",[42.00,-92.00,42.60,-91.10],"IA","'The Wapsi': Independence → Anamosa (Stone City).","Quiet water; a few jon boats.","Good most of the season.")
q("boone-ia","Boone River","green",[42.05,-94.00,42.45,-93.70],"IA","Webster City canyon run to the Des Moines River.","Narrow water trail.","Spring–June.",qn="Boone River")
q("midraccoon","Middle Raccoon River","green",[41.55,-94.70,41.85,-94.10],"IA","Panora → Redfield — central Iowa's favorite quick float.","Quiet water trail.","Best through July.")
q("raccoon","Raccoon River","green",[41.55,-94.25,41.75,-93.55],"IA","Redfield → Walnut Woods → Des Moines water trail.","Quiet water.","Good through July.",qn="Raccoon River")
q("cedar-ia","Cedar River","blue",[41.85,-92.55,42.60,-91.55],"IA","Big water trail: Cedar Falls → Cedar Rapids.","Motorized ramps throughout.","Always floatable.",qn="Cedar River")
q("desmoines-r","Des Moines River","blue",[41.20,-93.90,41.80,-93.20],"IA","The capital's big river and its water trail.","Motorized.","Always floatable.",qn="Des Moines River")

# ============ MISSOURI — the Ozarks ============
q("current","Current River","green",[36.90,-91.75,37.45,-90.85],"MO","THE Ozark float: Montauk SP → Akers → Pulltite → Round Spring → Two Rivers → Van Buren → Big Spring (Ozark National Scenic Riverways).","National Riverways paddle water; jon boats increase below Round Spring — upper river is canoe country.","Spring-fed and floatable every day of the year.")
q("jacksfork","Jacks Fork","green",[37.00,-91.85,37.25,-91.20],"MO","Buck Hollow → Alley Spring → Eminence → the Current confluence at Two Rivers.","Canoe/kayak water in the National Riverways.","Lower half floats all season; above Alley Spring it's a spring-flow run.")
q("elevenpoint","Eleven Point River","green",[36.58,-91.60,36.90,-91.05],"MO","National Wild & Scenic: Thomasville → Greer Spring (doubles the flow) → Riverton.","Wild & Scenic corridor — paddle craft.","Greer Spring keeps it floatable all season below the spring.")
q("niangua","Niangua River","green",[37.45,-93.05,37.85,-92.75],"MO","Bennett Spring SP country — Missouri's livery-est river.","Livery water; the odd jon boat.","Bennett Spring keeps it running all summer.")
q("meramec","Meramec River","green",[37.90,-91.60,38.25,-90.95],"MO","Maramec Spring → Onondaga Cave → Meramec State Park.","Quiet upper river; motors appear far downstream.","Spring-fed enough for all-season floats.")
q("gasconade","Gasconade River","green",[37.60,-92.60,38.00,-92.00],"MO","Ozark hills between Hazelgreen and Jerome — bluffs and gravel bars.","Quiet water with occasional jon boats.","Reliable most of the season.")
q("bigpiney","Big Piney River","green",[37.30,-92.15,37.80,-91.95],"MO","Slabtown → Ross Bridge toward the Gasconade.","Quiet water.","Good through summer in normal years.",qn="Big Piney River")
q("huzzah","Huzzah Creek","green",[37.90,-91.25,38.05,-91.05],"MO","The Meramec's clear-water little sister (with the Courtois next door).","Narrow creek — kayaks and canoes.","Best through July; scrapey after.")
q("northfork-mo","North Fork River","green",[36.58,-92.35,36.95,-92.10],"MO","Twin Bridges → Dawt Mill; Rainbow and Hodgson springs pour in mid-run.","Clear Ozark paddle water.","Spring-fed — floats all season.",qn=["North Fork River","North Fork of the White River"])
q("missouri-r","Missouri River","blue",[38.55,-92.30,38.90,-91.30],"MO","The Big Muddy: Jefferson City → Hermann reach.","Barge and powerboat water.","Always deep; wind and wakes rule.")

# ============ v8: northern WI / N IL / lower MI majors (outfitter-qualified) ============
q("flambeau","Flambeau River (N Fork)","green",[45.50,-91.05,45.90,-90.40],"WI","The northwoods classic with island campsites, ~42 river miles: Nine Mile Creek Landing (Hwy 70) → Dix Dox (Oxbo) → Hwy W → Camp 41 → Flambeau Lodge Landing above the NF/SF forks north of Tony.","Quiet state-forest water; a few fishing boats near landings.","Dam-fed and reliable all season.",qn=["Flambeau River","North Fork Flambeau River"])
q("namekagon","Namekagon River","green",[45.75,-92.35,46.25,-91.10],"WI","St. Croix National Scenic Riverway, ~87 river miles: Cable Wayside (Hwy 63) → Hayward → Springbrook → Trego (County K) → Riverside Landing at the St. Croix confluence — NPS landings the whole way.","National Riverway paddle water.","Reliable most of the season; upper reaches thin in drought.")
q("peshtigo","Peshtigo River","green",[45.33,-88.45,45.56,-88.22],"WI","~15 mi: Goodman County Park (below Strong Falls) → McClintock Park → Farm Dam Landing (9.8 mi, Class II), then the Roaring Rapids run Farm Dam → County C (Kosir's) → WPS Landing 12 on Caldron Falls Reservoir (5.2 mi) — the Midwest's busiest raft water.","Raft/kayak water in the rapids; motors on the flowages.","Rafting runs all summer; rapids best above ~250 cfs.",watch="Roaring Rapids is Class II-IV — beginners go with the rafting outfitters. Goodman → Farm Dam is quieter Class II bring-your-own water.")
q("brule","Bois Brule River","green",[46.30,-91.80,46.80,-91.35],"WI","The fabled Brule, ~34 river miles: Stone's Bridge → Winneboujou → Bois Brule CG → Copper Range → Hwy 13 → the mouth at Lake Superior; spring-fed cedar water.","Canoe/kayak water (fly-fishing etiquette upstream).","Spring-fed and steady all season; lower ledges best with some rain.",qn=["Bois Brule River","Brule River"],watch="Hwy 13 → the mouth holds the Class II ledges — the wilder last leg.",unpinned=["Mouth of the Brule landing (Lake Superior)"])
q("nbchicago","North Branch Chicago River","green",[41.90,-87.82,42.15,-87.65],"IL","Skokie Lagoons (Tower Rd) → Willow Rd → Glenview/Morton Grove → River Park → Clark Park boathouse — Chicago's backyard paddle.","Non-motorized urban water trail.","Floatable all season (urban flow).",qn="North Branch Chicago River",watch="Portages at the Willow Rd, Beckwith Rd (Chick Evans) and Tam O'Shanter dams.",unpinned=["Blue Star Memorial Woods landing (Glenview)","Linne Woods landing (Morton Grove)"])
q("thornapple","Thornapple River","green",[42.60,-85.55,42.98,-85.15],"MI","~45 dam-broken river miles in two segments: Barry County (Charlton Park → Tyden Park, Hastings → Irving → Middleville) and Kent County (Ruehs Park → Ada). Dams at Irving, Cascade (portage Tassell Park) and Ada.","Quiet water between small dams.","Good through the season; thin late summer above Hastings.",watch="Not one continuous run — plan the Barry and Kent segments separately around the dams.")
q("flat","Flat River","green",[42.93,-85.40,43.20,-85.20],"MI","Greenville (Tower Riverside / Jackson's Landing) → Belding (dam portage W of Zahm Rd) → Whites Bridge → Fallasburg → Lowell at the Grand, ~28 mi.","Quiet water; Michigan's only state-designated Natural River in Kent Co reaches.","Good through July; low late summer.",qn="Flat River",unpinned=["Whites Bridge Rd (historic covered bridge, Smyrna)","Water St Park launch (below Belding dam)"])
q("pawpaw","Paw Paw River","green",[42.05,-86.50,42.28,-86.10],"MI","The official lower water trail, ~21 mi: Paw Paw River Campground → County Park (Watervliet) → Coloma → Bundy Rd → Riverside → Graham Ave (Benton Harbor); twisty SW-Michigan jungle water — the last 11 mi below Riverside are the quiet bring-your-own leg.","Quiet water trail.","Good most of the season; deadfall is the limiter.",qn="Paw Paw River")
q("dowagiac","Dowagiac River","green",[41.80,-86.35,42.05,-86.05],"MI","The official 19-mi Dowagiac River Water Trail: Dowagiac (Peavine St) → Dodd Park (Sumnerville) → Pucker St (former dam, removed 2019-20) → the M-139 DNR access at the St. Joseph confluence, Niles — restored coldwater stream running free to the mouth.","Quiet trout water.","Spring-fed — floats all season.",qn="Dowagiac River",watch="Sink Rd access is closed; log jams reported near Dodd Park.",unpinned=["Middle Crossing Rd access (NW of Dowagiac)"])
q("clinton","Clinton River","green",[42.55,-83.35,42.70,-82.75],"MI","The 32-mi Clinton River Water Trail: Yates Park (Dequindre Rd, Rochester Hills) → River Bends → Utica → Clinton Twp → Mt. Clemens (Shadyside) → the Harley Ensign DNR launch on Lake St. Clair — the last leg below Mt. Clemens is motorized-mouth water.","Non-motorized upstream; motors near the Lake St. Clair mouth.","Good through July; scrappy in dry spells.",qn="Clinton River")

# ---- seasonal shading (green rivers): how late the river reliably floats ----
SEASON = {
 # deep green — into Aug–Sept
 "kickapoo":"aug","badfish":"aug","mecan":"aug","crystal":"aug","mukwonago":"aug","black":"aug",
 "pecatonica":"aug","sugar":"aug","lemonweir":"aug","fox-il":"aug","fox-il2":"aug","desplaines":"aug",
 "kankakee":"aug","nippersink":"aug","peremarquette":"aug","pine-mi":"aug","platte-mi":"aug",
 "boardman":"aug","jordan-mi":"aug","white-mi":"aug","betsie":"aug","manistee-upper":"aug",
 # medium — July rivers, marginal by August
 "milwaukee":"jul","bark":"jul","wolf-upper":"jul","grant":"jul","platte-wi":"jul","lacrosse":"jul",
 "turtle":"jul","yahara":"jul","dupage":"jul","littlemanistee":"jul","rogue":"jul",
 # light — June rivers, usually done by mid-July
 "baraboo":"jun","vermilion-il":"jun","apple":"jun","kishwaukee":"jun","root":"jun",
 # --- v4 additions ---
 "mfvermilion":"jul","mackinaw":"jun","sangamon":"jul","spoon":"jul","embarras":"jul","cache-il":"aug","bigmuddy":"aug","kaskaskia":"jul","lusk":"jun",
 "ausable":"aug","rifle":"aug","sturgeon-mi":"aug","pigeon-mi":"aug","huron-mi":"aug","chippewa-mi":"aug","cass":"jul","thunderbay":"jul",
 "elkhorn":"jul","red-ky":"jun","green-ky":"aug","barren":"aug","nolin":"jul","rockcastle":"jun","licking-ky":"jul","floydsfork":"jul","gasper":"jun","rough-ky":"jul",
 "greenbrier":"jul","sbpotomac":"jul","cacapon":"jul","cheat":"jul","elk-wv":"aug","coal-wv":"aug","bluestone":"jun",
 "mohican":"aug","littlemiami":"aug","bigdarby":"jul","kokosing":"aug","mad-oh":"aug","littlebeaver":"jun","cuyahoga":"jul","grand-oh":"jul","stillwater-oh":"jul","sandusky-oh":"jul",
 "rum":"aug","cannon":"aug","root-mn":"aug","zumbro":"jul","crowwing":"aug","snake-mn":"jul","kettle":"jun","crow-mn":"jul","missheadwaters":"aug",
 "sugarcreek":"jun","tippecanoe":"aug","blue-in":"jul","whitewater-in":"jul","wildcat":"jul","bigpine":"jun","flatrock-in":"jul","driftwood":"aug","eel-in":"jul","cedarck-in":"jun","mississinewa":"jul",
 "flambeau":"aug","namekagon":"aug","peshtigo":"jul","brule":"aug","nbchicago":"aug","thornapple":"jul","flat":"jul","pawpaw":"jul","dowagiac":"jul","clinton":"jul",
 "upperiowa":"aug","yellow-ia":"jun","turkey-ia":"jul","volga":"jun","maquoketa":"jul","wapsi":"jul","boone-ia":"jun","midraccoon":"jul","raccoon":"jul",
 "current":"aug","jacksfork":"aug","elevenpoint":"aug","niangua":"aug","meramec":"aug","gasconade":"aug","bigpiney":"jul","huzzah":"jul","northfork-mo":"aug",
}
for r in R:
    r["season"] = SEASON.get(r["id"]) if r["cls"]=="green" else None
missing = [r["id"] for r in R if r["cls"]=="green" and not r["season"]]
assert not missing, f"green rivers without season: {missing}"

# ---- regional sections (WI 3-way; IL and MI 2-way), each with its own home view ----
REGION_MAP = {
 "milwaukee":"se","bark":"se","mukwonago":"se","fox-il":"se","root":"se","turtle":"se","sugar":"se","yahara":"se","badfish":"se",
 "wolf-upper":"ne","crystal":"ne","mecan":"ne",
 "kickapoo":"w","baraboo":"w","black":"w","lacrosse":"w","lemonweir":"w","grant":"w","platte-wi":"w","pecatonica":"w",
 "flambeau":"n","namekagon":"n","peshtigo":"n","brule":"n",
 # Illinois: north / south of US-24
 "kishwaukee":"il-n","nippersink":"il-n","dupage":"il-n","desplaines":"il-n","vermilion-il":"il-n","apple":"il-n","kankakee":"il-n","fox-il2":"il-n",
 "nbchicago":"il-n",
 "mfvermilion":"il-s","mackinaw":"il-s","sangamon":"il-s","spoon":"il-s","embarras":"il-s","cache-il":"il-s","bigmuddy":"il-s","kaskaskia":"il-s","lusk":"il-s",
 # Michigan: west / east Lower Peninsula
 "peremarquette":"mi-w","pine-mi":"mi-w","littlemanistee":"mi-w","platte-mi":"mi-w","betsie":"mi-w","boardman":"mi-w","jordan-mi":"mi-w","white-mi":"mi-w","rogue":"mi-w","manistee-upper":"mi-w",
 "thornapple":"mi-w","flat":"mi-w","pawpaw":"mi-w","dowagiac":"mi-w",
 "ausable":"mi-e","clinton":"mi-e","rifle":"mi-e","sturgeon-mi":"mi-e","pigeon-mi":"mi-e","huron-mi":"mi-e","chippewa-mi":"mi-e","cass":"mi-e","thunderbay":"mi-e",
}
for r in R:
    r["region"] = REGION_MAP.get(r["id"]) if r["cls"]=="green" else None
for st_code in ("WI","IL","MI"):
    missing_rg = [r["id"] for r in R if r["state"]==st_code and r["cls"]=="green" and not r["region"]]
    assert not missing_rg, f"{st_code} greens without region: {missing_rg}"

# ---- trip stats for green rivers: mapped-run miles, conservative paddle speed (mph),
#      typical seasonal flow range (spring high -> late-summer low, cfs), est=True if no gauge data ----
TRIP = {  # id: (miles, mph, flow_hi, flow_lo, est)
 "milwaukee":(68,2,600,250,False), "bark":(34,2,250,60,False), "mukwonago":(13,2,120,70,False),
 "fox-il":(51,2,600,120,False), "root":(13,2,300,35,False), "turtle":(22,2,400,90,False),
 "sugar":(62,2,200,50,False), "yahara":(17,2,500,330,False), "badfish":(10,2,150,90,False),
 "wolf-upper":(21,2.5,700,250,False), "crystal":(4,2,70,40,True), "mecan":(14,2,120,80,True),
 "kickapoo":(60,2,150,55,False), "baraboo":(64,2,600,150,False), "black":(65,2,900,300,False),
 "lacrosse":(18,2,250,140,False), "lemonweir":(24,2,400,170,False), "grant":(20,2,350,150,False),
 "platte-wi":(21,2,250,90,False), "pecatonica":(30,2,600,220,False),
 "kishwaukee":(29,2,800,300,False), "nippersink":(15,2,150,45,False), "dupage":(29,2,600,180,False),
 "desplaines":(81,2,600,50,False), "vermilion-il":(50,2.5,1800,250,False), "apple":(21,2,400,150,False),
 "kankakee":(38,2,6000,2500,False), "fox-il2":(36,2,3000,900,False),
 "peremarquette":(65,2.5,900,550,False), "pine-mi":(25,2.5,350,220,False), "littlemanistee":(20,2,250,150,False),
 "platte-mi":(14,2,220,140,False), "betsie":(17,2,300,150,True), "boardman":(26,2,250,120,False),
 "jordan-mi":(12,2.5,250,150,False), "white-mi":(25,2,400,200,False), "rogue":(12,2,350,180,True),
 "manistee-upper":(90,2.5,400,250,False),
 # --- v4 additions (all flow ranges are estimates until gauges are wired) ---
 "mfvermilion":(13.5,2,500,150,True),"mackinaw":(20,2,400,80,True),"sangamon":(25,2,800,250,True),"spoon":(55,2,500,150,True),
 "embarras":(31,2,500,120,True),"cache-il":(6,2,60,30,True),"bigmuddy":(12,2,600,150,True),"kaskaskia":(50,2,500,150,True),"lusk":(8.1,2,200,30,True),
 "ausable":(40,2.5,600,350,True),"rifle":(32,2,300,150,True),"sturgeon-mi":(17,2.5,250,180,True),"pigeon-mi":(32,2,150,90,True),
 "huron-mi":(104,2,500,200,True),"chippewa-mi":(47,2,300,120,True),"cass":(37.5,2,400,100,True),"thunderbay":(70,2,300,100,True),
 "elkhorn":(10,2,500,120,True),"red-ky":(9,2,400,60,True),"green-ky":(20,2,1500,600,True),"barren":(12,2,800,300,True),"nolin":(8,2,400,150,True),
 "rockcastle":(15,2,600,100,True),"licking-ky":(15,2,500,150,True),"floydsfork":(12,2,200,40,True),"gasper":(8,2,300,50,True),"rough-ky":(8,2,300,100,True),
 "greenbrier":(25,2,1000,200,True),"sbpotomac":(10,2,800,150,True),"cacapon":(12,2,500,100,True),"cheat":(10,2,800,200,True),
 "elk-wv":(15,2,500,150,True),"coal-wv":(10,2,400,100,True),"bluestone":(10,2,400,60,True),
 "mohican":(12,2,500,150,True),"littlemiami":(25,2,800,200,True),"bigdarby":(12,2,400,80,True),"kokosing":(14,2,400,100,True),
 "mad-oh":(10,2,300,150,True),"littlebeaver":(12,2,500,80,True),"cuyahoga":(15,2,500,150,True),"grand-oh":(12,2,500,100,True),
 "stillwater-oh":(12,2,400,80,True),"sandusky-oh":(12,2,500,100,True),
 "rum":(18,2,600,200,True),"cannon":(15,2,800,250,True),"root-mn":(18,2,700,250,True),"zumbro":(15,2,500,150,True),
 "crowwing":(20,2,500,250,True),"snake-mn":(12,2,600,150,True),"kettle":(10,2.5,800,150,True),"crow-mn":(15,2,500,150,True),"missheadwaters":(30,2,200,100,True),
 "sugarcreek":(15,2,600,80,True),"tippecanoe":(20,2,700,300,True),"blue-in":(15,2,400,80,True),"whitewater-in":(12,2,800,150,True),
 "wildcat":(12,2,400,80,True),"bigpine":(8,2,300,40,True),"flatrock-in":(12,2,300,70,True),"driftwood":(8,2,800,250,True),
 "eel-in":(15,2,400,100,True),"cedarck-in":(8,2,200,40,True),"mississinewa":(12,2,400,100,True),
 "upperiowa":(20,2,500,150,True),"yellow-ia":(10,2,200,50,True),"turkey-ia":(18,2,600,150,True),"volga":(10,2,200,40,True),
 "maquoketa":(15,2,600,150,True),"wapsi":(15,2,700,200,True),"boone-ia":(12,2,400,80,True),"midraccoon":(12,2,300,70,True),"raccoon":(15,2,500,150,True),
 "flambeau":(42,2,800,300,True),"namekagon":(87,2.5,500,200,True),"peshtigo":(15,2,600,250,True),"brule":(34,2.5,300,150,True),"nbchicago":(12,2,150,60,True),"thornapple":(45,2,400,120,True),"flat":(28,2,350,100,True),"pawpaw":(21,2,300,100,True),"dowagiac":(19,2,250,120,True),"clinton":(32,2,300,100,True),
 "current":(25,2.5,600,350,True),"jacksfork":(25,2.5,400,150,True),"elevenpoint":(19,2.5,800,400,True),"niangua":(12,2.5,400,250,True),"meramec":(20,2,800,300,True),"gasconade":(25,2,700,300,True),"bigpiney":(20,2,400,150,True),"huzzah":(8,2,250,60,True),"northfork-mo":(15,2.5,500,300,True),
}
for r in R:
    t = TRIP.get(r["id"])
    if r["cls"]=="green":
        assert t, f"green river without trip stats: {r['id']}"
        r["miles"], r["mph"], r["fhi"], r["flo"], r["fest"] = t
    else:
        r["miles"] = r["mph"] = r["fhi"] = r["flo"] = None; r["fest"] = False
GNONE = {"mecan","betsie"}   # genuinely no usable USGS gauge; others without gauge = "link coming"
for r in R:
    r["gnone"] = r["id"] in GNONE

# ---------------- LANDINGS ----------------
# type: p=put-in, t=take-out, b=both
L = [
 # Baraboo
 ["baraboo","Wonewoc Municipal Canoe Landing (Cty FF)","Wonewoc","b",43.65361,-90.22725,"https://milespaddled.com/baraboo-river-iii/"],
 ["baraboo","Hwy 136 wayside — Ableman's Gorge","Rock Springs","p",43.490594,-89.918131,"https://www.wisconsinrivertrips.com/segments/baraboo-river/rock-springs"],
 ["baraboo","North Freedom Village Park landing","North Freedom","b",43.45682,-89.86329,"https://milespaddled.com/baraboo-river-i/"],
 ["baraboo","Giese Park","West Baraboo","b",43.46813,-89.810437,"https://www.wisconsinrivertrips.com/segments/baraboo-river/giese-park"],
 ["baraboo","Haskins Park","West Baraboo","b",43.46997,-89.76158,"https://milespaddled.com/baraboo-river-ii/"],
 ["baraboo","Hwy 113 landing (Glenville)","Baraboo","b",43.45853,-89.71399,"https://milespaddled.com/baraboo-river-i/"],
 ["baraboo","Hwy 33 bridge landing","Baraboo (east)","t",43.50341,-89.63256,"https://milespaddled.com/baraboo-river-iv/"],
 # Kickapoo
 ["kickapoo","Landing 1 — Hwy 33/Cty P","Ontario","p",43.72233,-90.58747,"https://milespaddled.com/kickapoo-river-iii/"],
 ["kickapoo","Bridge 4 landing (Hwy 131)","Ontario","b",43.6978,-90.6025,"https://www.wisconsinrivertrips.com/segments/kickapoo-river/ontario"],
 ["kickapoo","Bridge 7 landing (Wildcat Mtn SP)","Ontario","b",43.67258,-90.59407,"https://www.wisconsinrivertrips.com/segments/kickapoo-river/bridge-4-to-bridge-7"],
 ["kickapoo","Landing 12 — Rockton","Rockton","b",43.6371,-90.60292,"https://milespaddled.com/kickapoo-river-i/"],
 ["kickapoo","Landing 20 — La Farge","La Farge","b",43.57481,-90.6437,"https://milespaddled.com/kickapoo-river-ii/"],
 ["kickapoo","Tourist Park landing","Readstown","b",43.44541,-90.76174,"https://www.wisconsinrivertrips.com/segments/kickapoo-river/readstown"],
 ["kickapoo","Hwy S Canoe Landing (below dam)","Gays Mills","b",43.27417,-90.84119,"https://www.wisconsinrivertrips.com/segments/kickapoo-river/gays-mills"],
 ["kickapoo","Wauzeka Boat Landing (Wisconsin R.)","Wauzeka","t",43.08471,-90.87906,"https://milespaddled.com/kickapoo-river-v/"],
 # Sugar
 ["sugar","Hwy A landing","Paoli/Belleville","b",42.90046,-89.53008,"https://www.wisconsinrivertrips.com/segments/sugar-river/hwy-a"],
 ["sugar","Belleville Community Park","Belleville","b",42.86112,-89.5357,"https://www.wisconsinrivertrips.com/segments/sugar-river/hwy-a"],
 ["sugar","Exeter Park (Hwy 92)","Belleville","b",42.82526,-89.50828,"https://www.wisconsinrivertrips.com/segments/sugar-river/belleville"],
 ["sugar","County X landing","Attica","b",42.79994,-89.48646,"https://milespaddled.com/sugar-river-v/"],
 ["sugar","County EE landing","Albany (north)","b",42.73374,-89.44287,"https://milespaddled.com/sugar-river-v/"],
 ["sugar","Bowman Park","Albany","b",42.70709,-89.43801,"https://milespaddled.com/sugar-river-vi/"],
 ["sugar","Headgates Park (Decatur Lake)","Brodhead","t",42.64437,-89.39743,"https://milespaddled.com/sugar-river-vi/"],
 ["sugar","Decatur Park (below dam)","Brodhead","p",42.64446,-89.40896,"https://milespaddled.com/sugar-river-vii/"],
 ["sugar","Avon Bottoms Landing (W Beloit-Newark Rd)","Avon","b",42.5426,-89.34146,"https://milespaddled.com/sugar-river-vii/"],
 ["sugar","Colored Sands FP launch (Haas Rd)","Shirland, IL","b",42.48399,-89.24929,"https://milespaddled.com/sugar-river-viii/"],
 ["sugar","N Meridian Rd (Pecatonica confluence)","Shirland, IL","t",42.43807,-89.17545,"https://milespaddled.com/sugar-river-viii/"],
 # Wolf upper
 ["wolf-upper","Lily landing (Hwy 52)","Lily","b",45.30768,-88.85806,"https://milespaddled.com/wolf-river-i/"],
 ["wolf-upper","Hollister landing (W Hollister Rd)","Hollister","b",45.24736,-88.80559,"https://milespaddled.com/wolf-river-i/"],
 ["wolf-upper","Langlade DNR landing (Hwy 64)","Langlade","b",45.18977,-88.73369,"https://wisconsintrailguide.com/paddle/pdf/guide-wolf4.pdf"],
 ["wolf-upper","Herb's Landing (private — ask permission)","White Lake","p",45.13412,-88.71756,"https://wisconsintrailguide.com/paddle/pdf/guide-wolf4.pdf"],
 ["wolf-upper","County M bridge DNR landing","Markton","b",45.11818,-88.6631,"https://wisconsintrailguide.com/paddle/pdf/guide-wolf4.pdf"],
 ["wolf-upper","Wild Wolf Inn landing (private)","White Lake","t",45.11729,-88.66236,"https://wisconsintrailguide.com/paddle/pdf/guide-wolf4.pdf"],
 # Black
 ["black","County K landing (below Hatfield dam)","Hatfield","p",44.40667,-90.72842,"https://milespaddled.com/black-river-ii/"],
 ["black","Hall's Creek landing (County E)","Black River Falls","b",44.35852,-90.78404,"https://wisconsintrailguide.com/paddle/pdf/guide-black1.pdf"],
 ["black","Morrison Creek landing (state forest)","Black River Falls","p",44.35449,-90.76783,"https://wisconsintrailguide.com/paddle/pdf/guide-black1.pdf"],
 ["black","Holmgreen landing (above dam)","Black River Falls","b",44.29747,-90.84354,"https://wisconsintrailguide.com/paddle/pdf/guide-black1.pdf"],
 ["black","Bruce Cormican landing (below dam)","Black River Falls","p",44.28824,-90.85101,"https://milespaddled.com/black-river-i/"],
 ["black","Hansen Memorial canoe landing","Irving","b",44.17384,-90.91371,"https://wisconsintrailguide.com/paddle/pdf/guide-black3.pdf"],
 ["black","Melrose DNR landing","Melrose","t",44.1295,-90.97765,"https://wisconsintrailguide.com/paddle/pdf/guide-black3.pdf"],
 ["black","Linde landing","Melrose","b",44.1088,-90.9872,"https://wisconsintrailguide.com/paddle/pdf/guide-black3.pdf"],
 ["black","Melrose boat launch (Hwy 71/108)","Melrose","b",44.10862,-90.99646,"https://milespaddled.com/black-river-iii/"],
 ["black","North Bend Drive landing","North Bend","t",44.08953,-91.1155,"https://milespaddled.com/black-river-iii/"],
 ["black","Hwy 35 Main Landing","Holmen","b",43.99928,-91.32705,"https://www.wisconsinrivertrips.com/segments/black-river/van-loon-forest"],
 ["black","Lytle's Landing (Van Loon Wildlife Area)","Midway/Onalaska","t",43.9593,-91.33705,"https://www.wisconsinrivertrips.com/segments/black-river/van-loon-forest"],
 # Milwaukee
 ["milwaukee","River Hill Park (below Kewaskum dam)","Kewaskum","p",43.51734,-88.22324,"https://milespaddled.com/milwaukee-river-iv/"],
 ["milwaukee","Barton above-dam take-out (Commerce St)","West Bend (Barton)","t",43.44255,-88.18135,"https://milespaddled.com/milwaukee-river-iv/"],
 ["milwaukee","Quaas Creek Park landing","West Bend","b",43.41965,-88.14603,"https://www.wisconsinrivertrips.com/segments/milwaukee-river/west-bend"],
 ["milwaukee","Fireman's Park","Newburg","b",43.43373,-88.04926,"https://milespaddled.com/milwaukee-river-i/"],
 ["milwaukee","Waubedonia Park","Waubeka/Fredonia","b",43.46838,-87.97313,"https://milespaddled.com/milwaukee-river-i/"],
 ["milwaukee","Veterans Park (above Grafton dam)","Grafton","t",43.32211,-87.94948,"https://milespaddled.com/milwaukee-river-vi/"],
 ["milwaukee","14th Ave lot (below Grafton dam)","Grafton","p",43.31673,-87.94868,"https://milespaddled.com/milwaukee-river-v/"],
 ["milwaukee","Lime Kiln Park","Grafton","b",43.30534,-87.95358,"https://milespaddled.com/milwaukee-river-iii/"],
 ["milwaukee","County T / Lakefield Rd landing","Grafton","b",43.29459,-87.94498,"https://milespaddled.com/milwaukee-river-v/"],
 ["milwaukee","Villa Grove Park","Thiensville","b",43.23439,-87.95722,"https://milespaddled.com/milwaukee-river-iii/"],
 ["milwaukee","Estabrook Park (Lincoln Park ramp nearby)","Milwaukee","p",43.09944,-87.90763,"https://milespaddled.com/milwaukee-river-ii/"],
 ["milwaukee","Bruce Street boat launch","Milwaukee","t",43.02503,-87.90403,"https://milespaddled.com/milwaukee-river-ii/"],
 # Bark
 ["bark","Merton millpond dam launch","Merton","b",43.1488,-88.30731,"https://milespaddled.com/bark-river-ii/"],
 ["bark","Hwy 83 bridge access","Hartland","b",43.08662,-88.36324,"https://milespaddled.com/bark-river-ii/"],
 ["bark","Upper Nemahbin Lake launch","Delafield","b",43.05873,-88.43185,"https://milespaddled.com/bark-river-iii/"],
 ["bark","Sugar Island Rd DNR landing","Delafield","p",43.05367,-88.43855,"https://milespaddled.com/bark-river-vi/"],
 ["bark","Atkins-Olson Memorial Park (Hwy 18)","Dousman","b",43.02104,-88.49648,"https://milespaddled.com/bark-river-vi/"],
 ["bark","County E access","Rome/Heath Mills","p",42.98432,-88.57551,"https://milespaddled.com/bark-river-v/"],
 ["bark","Hagedorn Rd access","Sullivan (Slabtown)","t",42.96096,-88.67803,"https://milespaddled.com/bark-river-v/"],
 ["bark","Burnt Village County Park","Hebron","b",42.91549,-88.77933,"https://milespaddled.com/bark-river-i/"],
 ["bark","Mechanic St boat landing","Fort Atkinson","t",42.9289,-88.83879,"https://milespaddled.com/bark-river-i/"],
 # Mukwonago
 ["mukwonago","Eagle Spring Lake DNR ramp","Eagle","b",42.85514,-88.43494,"https://boatrampguide.com/ramps/eagle-spring-lake-and-lulu-lake-town-of-eagle-wi/"],
 ["mukwonago","Lower Phantom Lake DNR carry-in","Town of Mukwonago","b",42.86092,-88.36484,"https://boatrampguide.com/ramps/lower-phantom-lake-town-of-mukwonago-wi/"],
 ["mukwonago","Below Mukwonago dam (Front St)","Mukwonago","p",42.85655,-88.32959,"https://milespaddled.com/mukwonago-river/"],
 ["mukwonago","Big Bend Village Park (on the Fox)","Big Bend","t",42.87701,-88.21143,"https://milespaddled.com/mukwonago-river/"],
 # Fox IL
 ["fox-il","Frame Park","Waukesha","b",43.0182,-88.2242,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","Fox River Sanctuary","Waukesha","b",43.0047,-88.245,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","Fox River Park","Waukesha","b",42.9634,-88.2747,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","CTH I access","Waukesha","b",42.9337,-88.2929,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","CTH ES access (Vernon Marsh)","Mukwonago","b",42.8759,-88.306,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","Center Drive access","Big Bend","b",42.8768,-88.2481,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","Big Bend Riverside Park","Big Bend","b",42.877,-88.2113,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","Fox River Greenway","Big Bend","b",42.863,-88.1981,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","Tichigan Lake public access","Waterford","b",42.8235,-88.2337,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","Village Hall Park (below Waterford dam)","Waterford","b",42.7639,-88.2131,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","Case Eagle Park South (below Rochester dam)","Rochester","b",42.7354,-88.2257,"https://fabulousfoxwatertrail.org/access-sites/"],
 ["fox-il","Riverside Park","Burlington","b",42.6818,-88.2678,"https://fabulousfoxwatertrail.org/access-sites/"],
 # Root
 ["root","Five Mile County Park (5 Mile Rd)","Caledonia","b",42.79984,-87.87081,"https://milespaddled.com/root-river/"],
 ["root","Hwy 31 / Ole Davidson Rd pull-off","Racine","b",42.78531,-87.83647,"https://www.wisconsinrivertrips.com/segments/root-river"],
 ["root","Horlick Dam landing (Rapids Ct)","Racine","t",42.7538,-87.82322,"https://milespaddled.com/root-river/"],
 ["root","Island Park kayak launches","Racine","b",42.73056,-87.80278,"https://cityofracinewi.gov/parksrec/on-the-water/"],
 # ---- Southern WI round 2 ----
 ["yahara","Veterans Memorial Park","DeForest","p",43.24963,-89.34357,"https://milespaddled.com/yahara-river-i/"],
 ["yahara","Windsor Rd bridge","Windsor","b",43.21653,-89.34963,"https://milespaddled.com/yahara-river-i/"],
 ["yahara","Yahara Heights County Park (Hwy 113)","Madison","t",43.15103,-89.40171,"https://milespaddled.com/yahara-river-ii/"],
 ["yahara","Mandt Park (below Stoughton dam)","Stoughton","p",42.91326,-89.21767,"https://milespaddled.com/yahara-river-v/"],
 ["yahara","Murwin County Park","Fulton","t",42.811,-89.12798,"https://milespaddled.com/yahara-river-vi/"],
 ["yahara","County H at Rock River confluence","Fulton","t",42.78716,-89.1289,"https://milespaddled.com/yahara-river-vi/"],
 ["badfish","Sunrise Rd bridge","Rutland/Oregon","p",42.9281,-89.32907,"https://milespaddled.com/badfish-creek-iii/"],
 ["badfish","Old Stone Rd bridge","Cooksville (N)","b",42.88009,-89.2761,"https://milespaddled.com/badfish-creek-iii/"],
 ["badfish","Old Stage Rd access","Cooksville","b",42.85299,-89.25676,"https://milespaddled.com/badfish-creek-i/"],
 ["badfish","Hwy 138 bridge","Cooksville","b",42.83958,-89.24077,"https://milespaddled.com/badfish-creek-i/"],
 ["badfish","N Casey Rd bridge","Porter","t",42.83354,-89.19133,"https://milespaddled.com/badfish-creek-i/"],
 ["badfish","Hwy 59 bridge (near Yahara confluence)","Fulton","t",42.82596,-89.17238,"https://milespaddled.com/badfish-creek-i/"],
 ["pecatonica","County G bridge","Calamine","p",42.74113,-90.16915,"https://milespaddled.com/pecatonica-river-i/"],
 ["pecatonica","Black Bridge Park (Hwy 23)","Darlington","b",42.68602,-90.12035,"https://milespaddled.com/pecatonica-river-ii/"],
 ["pecatonica","Pecatonica River Trails Park","Darlington","b",42.68074,-90.12252,"https://milespaddled.com/pecatonica-river-i/"],
 ["pecatonica","Wells Landing (Walnut Rd)","Red Rock","t",42.64239,-90.03986,"https://milespaddled.com/pecatonica-river-ii/"],
 ["pecatonica","Hwy 11 boat landing","Browntown","p",42.57971,-89.81006,"https://milespaddled.com/pecatonica-river-iii/"],
 ["pecatonica","Winslow Rd landing","Winslow, IL","t",42.49516,-89.76796,"https://milespaddled.com/pecatonica-river-iii/"],
 ["grant","Short Cut Rd bridge","Lancaster (W)","p",42.81228,-90.83308,"https://milespaddled.com/grant-river-i/"],
 ["grant","County U bridge","Beetown","b",42.76189,-90.86411,"https://milespaddled.com/grant-river-i/"],
 ["grant","Chaffie Hollow Rd bridge","Beetown/Potosi","b",42.72231,-90.8479,"https://milespaddled.com/grant-river-ii/"],
 ["grant","Potosi Point Recreation Area","Potosi","t",42.65894,-90.73325,"https://milespaddled.com/grant-river-iii/"],
 ["platte-wi","County E bridge (eastern)","Annaton","p",42.90628,-90.54686,"https://milespaddled.com/platte-river-i/"],
 ["platte-wi","Coon Hollow Rd bridge","Platteville (rural)","b",42.86086,-90.58533,"https://milespaddled.com/platte-river-ii/"],
 ["platte-wi","County A bridge","Ellenboro (N)","b",42.83946,-90.6015,"https://milespaddled.com/platte-river-i/"],
 ["platte-wi","Airport Rd bridge","Ellenboro","b",42.78357,-90.609,"https://milespaddled.com/platte-river-ii/"],
 ["platte-wi","Platte Rd bridge","Ellenboro (S)","t",42.76276,-90.61347,"https://milespaddled.com/platte-river-ii/"],
 ["platte-wi","Banfield Bridge Rec Area","Potosi","b",42.63089,-90.65307,"https://milespaddled.com/platte-river-v/"],
 ["lacrosse","Fishermen's Park","Sparta","p",43.94223,-90.80265,"https://milespaddled.com/la-crosse-river-i/"],
 ["lacrosse","Hwy 162 bridge","Bangor","t",43.90086,-90.99025,"https://milespaddled.com/la-crosse-river-i/"],
 ["lacrosse","Below Neshonoc dam (Hwy 108)","West Salem","p",43.91421,-91.07612,"https://milespaddled.com/la-crosse-river-ii/"],
 ["lacrosse","Veterans Memorial County Park","West Salem","t",43.89187,-91.11906,"https://milespaddled.com/la-crosse-river-ii/"],
 ["lemonweir","Kennedy County Park ramp","New Lisbon","p",43.9186,-90.1713,"https://thepaddlinghub.com/directory/wisconsin/kennedy-county-park"],
 ["lemonweir","19th Ave landing (Lemonweir Mills)","Mauston (SE)","b",43.78723,-90.0168,"https://milespaddled.com/lemonweir-river/"],
 ["lemonweir","Two Rivers launch (Wisconsin R.)","Lyndon Station","t",43.76149,-89.85258,"https://milespaddled.com/lemonweir-river/"],
 ["mecan","County JJ bridge","Richford/Dakota","p",43.98865,-89.35846,"https://milespaddled.com/mecan-river-i/"],
 ["mecan","Dover Ave bridge","Budsin (N)","b",43.93784,-89.31932,"https://milespaddled.com/mecan-river-iv/"],
 ["mecan","Hwy 22 bridge","Dakota (S)","b",43.91597,-89.31208,"https://milespaddled.com/mecan-river-i/"],
 ["mecan","Eagle Rd access (below Germania dam)","Germania","p",43.89336,-89.25924,"https://milespaddled.com/mecan-river-ii/"],
 ["mecan","County N / Eagle Rd bridge","Germania","b",43.89133,-89.25379,"https://milespaddled.com/mecan-river-ii/"],
 ["mecan","Lock Rd access (Fox confluence)","Princeton (SW)","t",43.82686,-89.1585,"https://milespaddled.com/mecan-river-ii/"],
 ["crystal","Main St access","Rural","b",44.31259,-89.15951,"https://milespaddled.com/crystal-river-i/"],
 ["crystal","Shadow Lake Rd bridge","Little Hope/Waupaca","t",44.31967,-89.0978,"https://milespaddled.com/crystal-river-i/"],
 ["turtle","Springs Park","Delavan","p",42.63011,-88.65232,"https://milespaddled.com/turtle-creek-iii/"],
 ["turtle","School Section Rd bridge","Delavan/Darien","b",42.63189,-88.71521,"https://milespaddled.com/turtle-creek-iii/"],
 ["turtle","County C bridge","Fairfield","p",42.6308,-88.7748,"https://milespaddled.com/turtle-creek-ii/"],
 ["turtle","S O'Riley Rd access","Clinton","b",42.59752,-88.78525,"https://milespaddled.com/turtle-creek-ii/"],
 ["turtle","Sweet-Allyn Park","Shopiere","b",42.5735,-88.93969,"https://milespaddled.com/turtle-creek-ii/"],
 ["turtle","Dickop St (Rock River confluence)","South Beloit, IL","t",42.49361,-89.03973,"https://milespaddled.com/turtle-creek-i/"],
 # ---- Illinois ----
 ["kishwaukee","County Line Rd access","Garden Prairie","p",42.25801,-88.70592,"https://milespaddled.com/kishwaukee-river-ii/"],
 ["kishwaukee","Red Horse Bend (Distillery Rd)","Belvidere","b",42.26203,-88.81697,"https://milespaddled.com/kishwaukee-river-ii/"],
 ["kishwaukee","Belvidere Park (below dam)","Belvidere","p",42.25538,-88.85263,"https://www.wisconsinrivertrips.com/segments/kishwaukee-river/belvidere"],
 ["kishwaukee","Newburg Rd bridge","Cherry Valley","t",42.25395,-88.93046,"https://www.wisconsinrivertrips.com/segments/kishwaukee-river/belvidere"],
 ["kishwaukee","Baumann Park","Cherry Valley","b",42.23215,-88.95713,"https://milespaddled.com/kishwaukee-river-i/"],
 ["kishwaukee","Atwood Park","New Milford","t",42.18279,-89.05624,"https://milespaddled.com/kishwaukee-river-i/"],
 ["nippersink","Keystone Rd landing (Glacial Park)","Richmond","p",42.41832,-88.34459,"https://milespaddled.com/nippersink-creek/"],
 ["nippersink","Pioneer Rd landing","Solon Mills","b",42.43078,-88.29249,"https://www.wisconsinrivertrips.com/segments/nippersink-creek"],
 ["nippersink","Lyle C. Thomas Memorial Park","Spring Grove","b",42.44091,-88.23348,"https://recplanet.com/il/spring-grove/lyle-c-thomas-memorial-park"],
 ["nippersink","Nippersink Canoe Base","Spring Grove","t",42.41873,-88.20666,"https://milespaddled.com/nippersink-creek/"],
 ["dupage","McDowell Grove Forest Preserve (W Branch)","Naperville","b",41.79475,-88.1834,"https://openlands.org/paddle-illinois/mcdowell-grove-to-knoch-knolls-park/"],
 ["dupage","Knoch Knolls Park launch","Naperville","b",41.7122,-88.14095,"https://napervilleparks.org/location/knochknollspark"],
 ["dupage","Eaton Preserve (135th St)","Plainfield","b",41.6368,-88.19072,"https://openlands.org/paddle-illinois/eaton-preserve-to-riverside-parkway/"],
 ["dupage","Hammel Woods Rte 59 access","Shorewood","b",41.53042,-88.19805,"https://www.reconnectwithnature.org/preserves-trails/preserves/hammel-woods"],
 ["desplaines","Russell Rd launch (Van Patten Woods)","Wadsworth","p",42.48959,-87.92459,"https://milespaddled.com/des-plaines-river/"],
 ["desplaines","Wadsworth Rd launch (Sedge Meadow)","Wadsworth","b",42.42861,-87.92977,"https://milespaddled.com/des-plaines-river/"],
 ["desplaines","Independence Grove launch","Libertyville","b",42.31492,-87.957,"https://www.lcfpd.org/things-to-do/recreation/canoe-launches/"],
 ["desplaines","Oak Spring Rd launch (Wilmot Woods)","Libertyville","b",42.28849,-87.93789,"https://www.lcfpd.org/things-to-do/recreation/canoe-launches/"],
 ["desplaines","Wright Woods launch (Rte 60)","Vernon Hills","b",42.23977,-87.9397,"https://www.lcfpd.org/things-to-do/recreation/canoe-launches/"],
 ["desplaines","Dam No. 2 Woods landing","Mount Prospect","b",42.08287,-87.89061,"https://fpdcc.com/things-to-do/boating-canoeing-kayaking/"],
 ["desplaines","Columbia Woods landing","Willow Springs","t",41.73077,-87.88983,"https://fpdcc.com/things-to-do/boating-canoeing-kayaking/"],
 ["apple","E Canyon Rd bridge (Apple River Canyon SP)","Apple River","p",42.4491,-90.05556,"https://milespaddled.com/apple-river-i-illinois/"],
 ["apple","S Apple River Rd bridge","Hanover (N)","t",42.36414,-90.15927,"https://milespaddled.com/apple-river-i-illinois/"],
 ["apple","Below Hanover dam access","Hanover","p",42.25727,-90.28662,"https://milespaddled.com/apple-river-ii-illinois/"],
 ["apple","W Whitton Rd bridge","Hanover (mouth)","t",42.20942,-90.25042,"https://milespaddled.com/apple-river-ii-illinois/"],
 ["kankakee","Cobb Park ramp (dam pool — motorized)","Kankakee","b",41.1017,-87.8466,"https://www.kankakeeriverppa.org/trips-and-distances/"],
 ["kankakee","Bird Park","Kankakee","b",41.1197,-87.8786,"https://openlands.org/paddle-illinois/bird-park-to-chippewa-boat-launch/"],
 ["kankakee","Kankakee River SP ramp (Warner Bridge)","Bourbonnais","b",41.20904,-88.0192,"https://dnr.illinois.gov/parks/park.kankakeeriver.html"],
 ["fox-il2","Bicentennial Riverfront Park / whitewater course","Yorkville","p",41.64313,-88.44305,"https://www.yorkville.il.us/facilities/facility/details/marge-cline-whitewater-course-37"],
 ["fox-il2","Silver Springs State FWA launch","Yorkville (SW)","b",41.6275,-88.5225,"https://openlands.org/paddle-illinois/yorkville-to-silver-spring-state-park/"],
 ["fox-il2","Shuh Shuh Gah canoe launch","Plano/Millbrook","b",41.6086,-88.5632,"https://openlands.org/paddle-illinois/yorkville-to-silver-spring-state-park/"],
 ["fox-il2","IL-52 bridge landing","Serena/Sheridan","b",41.48568,-88.68579,"https://milespaddled.com/fox-river-i-illinois-tributary/"],
 ["fox-il2","Ayers Landing (private, fee)","Wedron","b",41.43938,-88.76345,"https://milespaddled.com/fox-river-i-illinois-tributary/"],
 ["fox-il2","Allen Park ramp (Illinois R., below Fox mouth)","Ottawa","t",41.34105,-88.84616,"https://illinoispaddling.org/paddling-the-fox-river/"],
 # ---- Michigan ----
 ["peremarquette","M-37 Bridge Boat Launch (The Forks)","Baldwin","p",43.85737,-85.85037,"https://outdoormichigan.org/feature/5279"],
 ["peremarquette","Green Cottage access","Baldwin","b",43.8602,-85.88139,"https://www.fs.usda.gov/r09/huron-manistee/recreation/green-cottage-river-access"],
 ["peremarquette","Gleason's Landing","Baldwin","b",43.87139,-85.92167,"https://www.fs.usda.gov/r09/huron-manistee/recreation/gleasons-landing-river-access"],
 ["peremarquette","Bowman Bridge access","Baldwin","b",43.88944,-85.94011,"https://www.fs.usda.gov/r09/huron-manistee/recreation/bowman-bridge-river-access"],
 ["peremarquette","Rainbow Rapids launch","Baldwin","b",43.92278,-85.97556,"https://www.fs.usda.gov/r09/huron-manistee/recreation/rainbow-rapids-boat-launch"],
 ["peremarquette","Sulak Campground access","Branch","b",43.92378,-86.01325,"https://www.fs.usda.gov/r09/huron-manistee/recreation/sulak-campground"],
 ["peremarquette","Upper Branch Bridge access","Branch","t",43.92861,-86.02028,"https://www.fs.usda.gov/r09/huron-manistee/recreation/upper-branch-bridge-river-access"],
 ["peremarquette","Lower Branch Bridge access","Branch","b",43.93528,-86.05083,"https://www.fs.usda.gov/r09/huron-manistee/recreation/lower-branch-bridge-river-access"],
 ["peremarquette","Indian Bridge access (motor line)","Custer","b",43.93722,-86.18222,"https://www.fs.usda.gov/r09/huron-manistee/recreation/indian-bridge-river-access"],
 ["peremarquette","Custer Weir & Boat Launch (S Custer Rd)","Custer","b",43.9371,-86.21865,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=1206"],
 ["peremarquette","Scottville Riverside Park Boat Launch","Scottville","b",43.9436,-86.27753,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=1205"],
 ["peremarquette","Old US-31 Bridge Access (MDNR)","Ludington","t",43.92735,-86.41684,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=1121"],
 ["pine-mi","Edgetts Bridge launch","Luther","p",44.06568,-85.58826,"https://www.thepineriver.com/pine-river/map"],
 ["pine-mi","Skookum Bridge","Luther","b",44.08245,-85.64772,"https://www.thepineriver.com/pine-river/map"],
 ["pine-mi","Lincoln Bridge SF Campground","Luther","b",44.1328,-85.69121,"https://www.michigan.gov/recsearch/sfcampgroundsa-m/lincolnbridge"],
 ["pine-mi","Elm Flats canoe landing","Wellston","b",44.1524,-85.71224,"https://www.thepineriver.com/pine-river/map"],
 ["pine-mi","Dobson Bridge canoe landing","Wellston","b",44.18011,-85.75889,"https://www.fs.usda.gov/r09/huron-manistee/recreation/dobson-bridge-canoe-landing"],
 ["pine-mi","Peterson Bridge canoe launch","Wellston","b",44.20222,-85.7975,"https://www.fs.usda.gov/r09/huron-manistee/recreation/peterson-bridge-campground"],
 ["pine-mi","Low Bridge canoe landing","Wellston","t",44.21611,-85.9025,"https://www.fs.usda.gov/r09/huron-manistee/recreation/low-bridge-canoe-landing"],
 ["littlemanistee","Driftwood Valley Campground","Irons","p",44.13026,-85.98216,"https://www.fs.usda.gov/r09/huron-manistee/recreation/groups/little-manistee-river-national-scenic-study-river"],
 ["littlemanistee","Bear Track Campground","Irons","b",44.1475,-86.03056,"https://www.fs.usda.gov/r09/huron-manistee/recreation/bear-track-campground"],
 ["littlemanistee","Nine Mile Bridge launch","Stronach Twp","b",44.17099,-86.10359,"https://paddling.com/paddle/trips/little-manistee-river-michigan-10"],
 ["littlemanistee","Six Mile Bridge launch (USFS)","Stronach Twp","b",44.1837,-86.16743,"https://paddling.com/paddle/trips/little-manistee-river-michigan-10"],
 ["littlemanistee","Old Stronach Bridge launch","Stronach","t",44.21013,-86.24523,"https://paddling.com/paddle/trips/little-manistee-river-michigan-10"],
 ["platte-mi","Veterans Memorial SFCG canoe launch (US-31)","Honor","p",44.6593,-85.94399,"https://outdoormichigan.org/feature/6225"],
 ["platte-mi","Platte River SF Campground","Honor","b",44.64435,-85.9785,"https://outdoormichigan.org/feature/6216"],
 ["platte-mi","Platte River Park launch (Indian Hill Rd)","Honor","b",44.67075,-86.03713,"https://outdoormichigan.org/feature/15086"],
 ["platte-mi","Loon Lake access (NPS)","Honor","b",44.7089,-86.1261,"https://www.nps.gov/places/000/loon-lake-access.htm"],
 ["platte-mi","Platte River Picnic Area access (NPS)","Honor","p",44.7127,-86.1199,"https://www.nps.gov/places/000/platte-river-picnic-area-water-access.htm"],
 ["platte-mi","El Dorado access (NPS)","Honor","b",44.7265,-86.1436,"https://www.nps.gov/places/000/el-dorado-platte-river-access.htm"],
 ["platte-mi","Platte River Point (Lake Michigan)","Honor","t",44.7296,-86.1562,"https://www.nps.gov/places/000/platte-river-point-water-access.htm"],
 ["betsie","Grass Lake SFCG launch","Wallin","p",44.59158,-85.84714,"https://s21124.pcdn.co/wp-content/uploads/2024/07/MCTA_BetsieRiver_web2024update.pdf"],
 ["betsie","Homestead Dam launch (DNR, portage right)","Benzonia","b",44.59636,-86.07916,"https://s21124.pcdn.co/wp-content/uploads/2024/07/MCTA_BetsieRiver_web2024update.pdf"],
 ["betsie","US-31 DNR carry-in launch","Benzonia","b",44.60209,-86.09909,"https://outdoormichigan.org/feature/6263"],
 ["betsie","Grace Rd DNR carry-in launch","Benzonia","b",44.60623,-86.1102,"https://outdoormichigan.org/feature/6259"],
 ["betsie","River Rd launch (DNR)","Benzonia Twp","t",44.6174,-86.12254,"https://s21124.pcdn.co/wp-content/uploads/2024/07/MCTA_BetsieRiver_web2024update.pdf"],
 ["boardman","Forks SF Campground","Mayfield","p",44.67319,-85.40124,"https://natureiscalling.org/river-paddle-upper-boardman"],
 ["boardman","Scheck's Place SF Campground","Mayfield","b",44.65176,-85.45375,"https://natureiscalling.org/river-paddle-upper-boardman"],
 ["boardman","Brown Bridge Landing (Quiet Area)","Mayfield","b",44.64176,-85.51005,"https://natureiscalling.org/river-paddle-upper-boardman"],
 ["boardman","Shumsky's Landing","Blair Twp","b",44.6509,-85.59075,"https://natureiscalling.org/river-paddle-lower-boardman"],
 ["boardman","Beitner Park landing","Blair Twp","b",44.67515,-85.63033,"https://natureiscalling.org/river-paddle-lower-boardman"],
 ["boardman","Medalie Park (Boardman Lake)","Traverse City","p",44.73456,-85.61641,"https://natureiscalling.org/river-paddle-lower-boardman"],
 ["boardman","Hull Park (Boardman Lake)","Traverse City","t",44.75685,-85.61073,"https://natureiscalling.org/river-paddle-lower-boardman"],
 ["jordan-mi","Graves Crossing SFCG (M-66)","Jordan Twp","p",45.03327,-85.06414,"https://www.jvoutfitters.com/canoeing-and-kayaking"],
 ["jordan-mi","Chestonia Bridge (Old State Rd)","Chestonia Twp","b",45.06018,-85.06942,"https://www.jvoutfitters.com/canoeing-and-kayaking"],
 ["jordan-mi","Webster's Bridge (Webster Rd)","Jordan Twp","b",45.10208,-85.0977,"https://www.jvoutfitters.com/canoeing-and-kayaking"],
 ["jordan-mi","Rogers Rd bridge access","East Jordan","b",45.13265,-85.12378,"https://www.fishweb.com/maps/antrim/jordanriver/rogers/index.html"],
 ["jordan-mi","Sportsman's Park (Jordan mouth, Lake Charlevoix)","East Jordan","t",45.1515,-85.1318,"https://www.mypacer.com/parks/195209/sportsman-s-park-east-jordan"],
 ["white-mi","Hesperia dam access","Hesperia","p",43.5728,-86.04068,"https://www.michiganwatertrails.org/trail.asp?ait=cv&cid=253"],
 ["white-mi","Pines Point Campground (USFS)","Hesperia","b",43.53028,-86.11639,"https://www.fs.usda.gov/r09/huron-manistee/recreation/pines-point-campground"],
 ["white-mi","Sischo Bayou access (USFS)","Hesperia","b",43.48333,-86.14944,"https://www.fs.usda.gov/r09/huron-manistee/recreation/sischo-bayou-river-access"],
 ["white-mi","Diamond Point (USFS)","Montague","b",43.47444,-86.21167,"https://www.fs.usda.gov/r09/huron-manistee/recreation/diamond-point"],
 ["white-mi","Happy Mohawk livery (Fruitvale Rd)","Montague","b",43.4641,-86.233,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=1094"],
 ["white-mi","Goodrich Park (White Lake)","Whitehall","t",43.4097,-86.35281,"https://cityofwhitehall.org/city-hall/recreation-parks-cemetery/"],
 ["rogue","Friske Drive Boat Launch (12 Mile Rd)","Rockford (Algoma Twp)","p",43.14674,-85.60206,"https://outdoormichigan.org/feature/1916"],
 ["rogue","Summit Ave Boat Launch","Algoma Twp","b",43.14733,-85.56424,"https://outdoormichigan.org/feature/13275"],
 ["rogue","Rockford dam launch (Richardson-Sowerby Park)","Rockford","b",43.1202,-85.56151,"https://paddling.com/paddle/trips/rogue-river-michigan"],
 ["rogue","Grand Rogue Park Boat Launch (ADA)","Belmont","b",43.0627,-85.59074,"https://outdoormichigan.org/feature/15040"],
 ["rogue","Rogue River Mouth DNR ramp (Grand confluence)","Belmont","t",43.06307,-85.5851,"https://outdoormichigan.org/feature/1735"],
 # ---- v9 QC pass: Michigan ----
 ["manistee-upper","Upper Manistee River SFCG (CR-612)","Frederic","p",44.750265,-84.839361,"https://www.michigan.gov/recsearch/sfcampgroundsn-z/uppermanistee"],
 ["manistee-upper","Manistee River Bridge SFCG (M-72)","Grayling","b",44.694682,-84.847495,"https://www.michigan.gov/recsearch/sfcampgroundsa-m/ManisteeRiverBridge"],
 ["manistee-upper","CCC Bridge SF Campground","Kalkaska","b",44.612834,-84.992376,"https://www.michigan.org/property/ccc-bridge-state-forest-campground"],
 ["manistee-upper","Smithville Landing (M-66)","Fife Lake","b",44.52333,-85.17347,"https://outdoormichigan.org/feature/12668"],
 ["manistee-upper","Chippewa Landing","Manton","t",44.48763,-85.4029,"https://outdoormichigan.org/feature/12666"],
 ["ausable","Penrod's Au Sable (Grayling town put-in)","Grayling","p",44.661701,-84.709803,"https://penrodscanoe.com/"],
 ["ausable","Burton's Landing SF Campground","Grayling","b",44.662519,-84.647202,"https://www.michigan.gov/recsearch/sfcampgroundsa-m/BurtonsLanding"],
 ["ausable","Keystone Landing SF Campground","Grayling","b",44.665062,-84.625277,"https://www.michigan.gov/recsearch/sfcampgroundsa-m/KeystoneLanding"],
 ["ausable","Wakeley Bridge Landing","Grayling","b",44.658981,-84.505617,"https://ausableaccess.com/about/"],
 ["ausable","McMasters Bridge Landing","Luzerne","b",44.665015,-84.39724,"https://ausableaccess.com/about/"],
 ["ausable","Mio Dam Pond Landing","Mio","t",44.661791,-84.136091,"https://ausableaccess.com/about/"],
 ["rifle","Ranch CG Boat Launch (Rifle River Rec Area)","Lupton","p",44.39331,-84.03833,"https://outdoormichigan.org/feature/9656"],
 ["rifle","Sage Lake Rd DNR carry-in access","Lupton","b",44.36356,-84.04841,"https://outdoormichigan.org/feature/9657"],
 ["rifle","Moffatt Bridge DNR access","Sterling","b",44.14051,-84.04361,"https://outdoormichigan.org/feature/9566"],
 ["rifle","Omer Public Access (US-23)","Omer","t",44.0475198,-83.8544333,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=1751"],
 ["sturgeon-mi","Trowbridge Rd access","Wolverine","p",45.2319577,-84.5889188,"https://waterservices.usgs.gov/nwis/site/?sites=04127988&format=rdb"],
 ["sturgeon-mi","Wolverine South Village Park carry-in launch","Wolverine","b",45.27272,-84.60136,"https://outdoormichigan.org/feature/10265"],
 ["sturgeon-mi","Haakwood State Forest Campground","Wolverine","b",45.300621,-84.613474,"https://www.michigan.gov/recsearch/sfcampgroundsa-m/haakwood"],
 ["sturgeon-mi","Rondo Rd DNR carry-in access","Wolverine","b",45.32049,-84.62554,"https://outdoormichigan.org/feature/10253"],
 ["sturgeon-mi","Burt Lake State Park (Sturgeon ramp)","Indian River","t",45.4030226,-84.6216774,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=1144"],
 ["pigeon-mi","Pigeon Bridge SFCG (Sturgeon Valley Rd)","Vanderbilt","p",45.156508,-84.465173,"https://www.michigan.gov/recsearch/sfcampgroundsn-z/pigeonbridge"],
 ["pigeon-mi","Pigeon River SF Campground","Vanderbilt","b",45.176475,-84.429086,"https://www.michigan.gov/recsearch/sfcampgroundsn-z/pigeonriver"],
 ["pigeon-mi","Pine Grove SFCG (nr Webb Rd 'Red Bridge')","Wolverine","b",45.244575,-84.446042,"https://www.michigan.gov/recsearch/sfcampgroundsn-z/pinegrove"],
 ["pigeon-mi","Afton Rd DNR carry-in launch","Afton","b",45.36301,-84.50741,"https://outdoormichigan.org/feature/12969"],
 ["pigeon-mi","Andreae Nature Preserve (parking, 0.5-mi carry)","Indian River","t",45.394864,-84.535099,"https://landtrust.org/explore/agnes-s-andreae-nature-preserve/"],
 ["thunderbay","Atlanta Dam access/portage","Atlanta","b",45.00218,-84.14368,"https://outdoormichigan.org/feature/10031"],
 ["thunderbay","Emerick Park launch","Hillman","b",45.06013,-83.900861,"https://thedyrt.com/camping/michigan/michigan-emerick-park"],
 ["thunderbay","Long Rapids Twp Park carry-in (Class II below)","Long Rapids","p",45.11895,-83.72316,"https://outdoormichigan.org/feature/10134"],
 ["thunderbay","Ford Avenue Boat Launch (river mouth)","Alpena","t",45.06296755,-83.42892034,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=1757"],
 ["huron-mi","Proud Lake Rec Area (Heavner launch)","Milford","p",42.57273,-83.56421,"https://outdoormichigan.org/feature/12650"],
 ["huron-mi","Hudson Mills Metropark","Dexter","b",42.38554,-83.91178,"https://outdoormichigan.org/feature/7899"],
 ["huron-mi","Argo Park / Argo Livery","Ann Arbor","b",42.29268,-83.74404,"https://outdoormichigan.org/feature/7811"],
 ["huron-mi","Gallup Park","Ann Arbor","b",42.27645,-83.69586,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=2279"],
 ["huron-mi","Flat Rock Boat Launch (Huroc Park)","Flat Rock","t",42.0943,-83.2933,"https://outdoormichigan.org/feature/8126"],
 ["chippewa-mi","Deerfield Nature Park","Deerfield Twp","p",43.59248,-84.8949,"https://outdoormichigan.org/feature/3644"],
 ["chippewa-mi","Meridian Park","Union Twp","b",43.57982,-84.84705,"https://outdoormichigan.org/feature/3650"],
 ["chippewa-mi","Chipp-A-Waters Park","Mount Pleasant","b",43.59485,-84.79348,"https://outdoormichigan.org/feature/3686"],
 ["chippewa-mi","Island Park","Mount Pleasant","b",43.60909,-84.78242,"https://outdoormichigan.org/feature/3691"],
 ["chippewa-mi","Chippewa Nature Center launch","Midland","b",43.5943,-84.37474,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=2112"],
 ["chippewa-mi","Tridge / Chippewassee Park launch","Midland","t",43.611052,-84.248689,"https://en.wikipedia.org/wiki/The_Tridge_(Midland,_Michigan)"],
 ["cass","M-46 Cass River Roadside Park","Tuscola County","p",43.40936,-83.48882,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5295"],
 ["cass","Vassar Canoe and Kayak Launch","Vassar","b",43.3698,-83.58186,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5352"],
 ["cass","Tuscola Township Access","Tuscola","b",43.32572,-83.65242,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5356"],
 ["cass","Frankenmuth Heritage Park (dam portage)","Frankenmuth","b",43.33027,-83.73373,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=4783"],
 ["cass","Davis Park Access","Bridgeport","b",43.35547,-83.88159,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5362"],
 ["cass","M-13 Cass River Boat Launch","Saginaw","t",43.36518,-83.95523,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5364"],
 ["clinton","Yates Park (Yates Cider Mill)","Rochester Hills","p",42.67213,-83.09708,"https://outdoormichigan.org/feature/8857"],
 ["clinton","River Bends Park","Shelby Twp","b",42.65642,-83.07222,"https://outdoormichigan.org/feature/8856"],
 ["clinton","North Clinton River Park","Clinton Twp","b",42.60781,-83.02585,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=1895"],
 ["clinton","Budd Park","Clinton Twp","b",42.58851,-82.92879,"https://outdoormichigan.org/feature/8861"],
 ["clinton","Shadyside Park","Mount Clemens","b",42.58247,-82.88009,"https://outdoormichigan.org/feature/8804"],
 ["clinton","Harley Ensign DNR Boat Launch (Lake St. Clair)","Harrison Twp","t",42.59326,-82.77473,"https://outdoormichigan.org/feature/8831"],
 ["thornapple","Charlton Park Boat Launch","Hastings Twp","p",42.61788,-85.19842,"https://outdoormichigan.org/feature/2691"],
 ["thornapple","Tyden Park Boat Launch","Hastings","b",42.65152,-85.29206,"https://outdoormichigan.org/feature/2705"],
 ["thornapple","Irving Road DNR carry-in","Irving Twp","b",42.68934,-85.42512,"https://outdoormichigan.org/feature/2761"],
 ["thornapple","River Street ADA kayak launch","Middleville","b",42.71233,-85.46684,"https://outdoormichigan.org/feature/13355"],
 ["thornapple","Ruehs Park (68th St)","Caledonia/Alaska","b",42.838822,-85.478446,"https://paddling.com/paddle/locations/ruehs-park-68th-st"],
 ["thornapple","Ada Boat Launch (at Ada Dam)","Ada","t",42.94925,-85.48265,"https://lmb.org/locations/thornapple-river-ada-boat-launch/"],
 ["flat","Tower Riverside Park (below Greenville dam)","Greenville","p",43.18231,-85.25432,"https://outdoormichigan.org/feature/2937"],
 ["flat","Jackson's Landing (M-57, ADA launch)","Greenville","b",43.17668,-85.24763,"https://outdoormichigan.org/feature/2929"],
 ["flat","East Riverside Park","Belding","b",43.096737,-85.223007,"https://belding.mi.us/belding_parks.php"],
 ["flat","Fallasburg County Park Boat Launch","Lowell (Vergennes Twp)","b",42.986,-85.33208,"https://outdoormichigan.org/feature/13446"],
 ["flat","Lowell Boat Launch (ADA, above Lowell dam)","Lowell","t",42.93621,-85.33885,"https://outdoormichigan.org/feature/1911"],
 ["pawpaw","Paw Paw River Campground (private, fee)","Watervliet","p",42.207918,-86.244151,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5083"],
 ["pawpaw","Paw Paw River County Park (barrier-free)","Watervliet","b",42.19272,-86.2577,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5203"],
 ["pawpaw","Coloma Water Access","Coloma","b",42.19057,-86.30363,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5085"],
 ["pawpaw","Bundy Road Water Access","Coloma Twp","b",42.19988,-86.34279,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5092"],
 ["pawpaw","Riverside Kayak Park (universal-access dock)","Riverside","b",42.18612,-86.37326,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5115"],
 ["pawpaw","Graham Avenue launch (trail terminus)","Benton Harbor","t",42.11765,-86.46819,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5091"],
 ["dowagiac","Peavine Street Access","Dowagiac","p",41.95614,-86.18277,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=5269"],
 ["dowagiac","Arthur Dodd Memorial Park","Sumnerville","b",41.90725,-86.21734,"https://outdoormichigan.org/feature/4677"],
 ["dowagiac","Pucker Street Access / Losensky Park","Niles","b",41.86426,-86.24271,"https://www.michiganwatertrails.org/location.asp?ait=av&aid=1959"],
 ["dowagiac","MDNR access at M-139 (St. Joseph confluence)","Niles","t",41.844482,-86.262556,"https://www.michigandnr.com/publications/pdfs/ArcGISOnline/StoryMaps/fish_troutTrails/PDFs/TT2015031.pdf"],
 # ---- v9 QC pass: northern WI ----
 ["flambeau","Nine Mile Creek Landing (Hwy 70)","Fifield","p",45.8526,-90.60026,"https://milespaddled.com/flambeau-river-north-fork-ii/"],
 ["flambeau","Dix Dox Landing","Oxbo","b",45.86263,-90.70473,"https://milespaddled.com/flambeau-river-north-fork-ii/"],
 ["flambeau","Hwy W Landing","Flambeau River SF","b",45.76869,-90.76078,"https://milespaddled.com/flambeau-river-north-fork-iii/"],
 ["flambeau","Camp 41 Landing","Flambeau River SF","b",45.69208,-90.81288,"https://wisconsintrailguide.com/paddle/gpx/FLAMBEAU-FN4.gpx"],
 ["flambeau","Flambeau Lodge Landing","Tony (N)","t",45.57279,-90.94891,"https://milespaddled.com/flambeau-river-north-fork-iii/"],
 ["namekagon","Cable Wayside Landing (Hwy 63)","Cable","p",46.18825,-91.30938,"https://wisconsintrailguide.com/paddle/pdf/guide-namekagon1.pdf"],
 ["namekagon","Hayward Landing (below dam)","Hayward","b",46.0035,-91.48906,"https://wisconsintrailguide.com/paddle/gpx/NAM02.gpx"],
 ["namekagon","Springbrook Landing","Springbrook","b",45.95392,-91.68622,"https://wisconsintrailguide.com/paddle/gpx/NAM02.gpx"],
 ["namekagon","County K Landing","Trego","b",45.95314,-91.89151,"https://milespaddled.com/namekagon-river/"],
 ["namekagon","Riverside Landing (St. Croix confluence)","Danbury (Hwy 35)","t",46.07661,-92.24626,"https://milespaddled.com/namekagon-river/"],
 ["peshtigo","Goodman County Park","Silver Cliff (NW)","p",45.51799,-88.33935,"https://wisconsintrailguide.com/paddle/gpx/PESHTIGO4.gpx"],
 ["peshtigo","McClintock County Park","Silver Cliff","b",45.47758,-88.32955,"https://wisconsintrailguide.com/paddle/gpx/PESHTIGO4.gpx"],
 ["peshtigo","Farm Dam Public Landing (Roaring Rapids put-in)","Silver Cliff/Athelstane","b",45.41351,-88.34615,"https://wisconsintrailguide.com/paddle/gpx/PESHTIGO5.gpx"],
 ["peshtigo","County C bridge landing (Kosir's)","Athelstane","b",45.38766,-88.30468,"https://wisconsintrailguide.com/paddle/gpx/PESHTIGO5.gpx"],
 ["peshtigo","WPS Landing 12 (Caldron Falls Reservoir)","Athelstane","t",45.38092,-88.30101,"https://wisconsintrailguide.com/paddle/gpx/PESHTIGO5.gpx"],
 ["brule","Stone's Bridge Landing (Cty S)","Lake Nebagamon (S)","p",46.43431,-91.67486,"https://milespaddled.com/bois-brule-river-i/"],
 ["brule","Winneboujou Landing (Cty B)","Brule","b",46.5167,-91.60369,"https://wisconsin-explorer.blogspot.com/2023/04/kayaking-bois-brule-river-in-douglas.html"],
 ["brule","Bois Brule Campground Landing","Brule","b",46.54043,-91.59404,"https://milespaddled.com/bois-brule-river-i/"],
 ["brule","Copper Range Campground Landing","Brule (N)","b",46.6095,-91.58319,"https://milespaddled.com/bois-brule-river-iii/"],
 ["brule","Hwy 13 Landing","Brule (N)","t",46.67885,-91.59528,"https://milespaddled.com/bois-brule-river-iii/"],
 # ---- v9 QC pass: Illinois ----
 ["dupage","W. Seil Road access","Shorewood/Minooka","b",41.50738,-88.21053,"https://www.illinoispaddle.com/uploads/1/0/6/3/10637609/dupage_river.kml"],
 ["dupage","Shepley Road access","Channahon","b",41.4685,-88.20763,"https://www.illinoispaddle.com/uploads/1/0/6/3/10637609/dupage_river.kml"],
 ["dupage","Channahon SP / I&M Canal launch (dam portage)","Channahon","t",41.4234,-88.228,"https://www.illinoispaddle.com/uploads/1/0/6/3/10637609/dupage_river.kml"],
 ["kankakee","Momence access (Island Park area)","Momence","p",41.16635,-87.65061,"https://www.illinoispaddle.com/uploads/1/0/6/3/10637609/kankakee_river.kml"],
 ["kankakee","Potawatomi Park","Aroma Park","b",41.07605,-87.80837,"https://www.illinoispaddle.com/uploads/1/0/6/3/10637609/kankakee_river.kml"],
 ["kankakee","Wilmington Dam take-out","Wilmington","t",41.30059,-88.15151,"https://www.illinoispaddle.com/uploads/1/0/6/3/10637609/kankakee_river.kml"],
 ["vermilion-il","Hopalong Cassidy Trail canoe launch (Rt 18)","Streator","b",41.12087,-88.84558,"https://www.illinoisriverroad.org/places/united-states/illinois/streator/nature-outdoor-recreation/hopalong-cassidy-river-trail/"],
 ["vermilion-il","Lowell canoe launch (IL-178 bridge)","Lowell","b",41.25434,-89.01337,"https://www.riverfacts.com/maps/11172.html"],
 ["vermilion-il","Vermilion River Boat Ramp (Ed Hand Hwy)","Oglesby","t",41.30131,-89.03746,"https://www.riverfacts.com/maps/11172.html"],
 ["mfvermilion","Kickapoo Landing canoe launch (Kickapoo SRA)","Oakwood","t",40.1441,-87.75665,"https://www.enjoyillinois.com/explore/listing/kickapoo-landing/"],
 ["sangamon","Lake of the Woods FP canoe access","Mahomet","p",40.1962,-88.38063,"https://www.enjoyillinois.com/explore/listing/lake-of-the-woods-forest-preserve/"],
 ["spoon","Riverside Park boat ramp","London Mills","p",40.71324,-90.26621,"https://www.localopal.org/riverside-park-london-mills.html"],
 ["spoon","Bernadotte Public Park (portage dam)","Bernadotte","b",40.40212,-90.32214,"https://www.localopal.org/bernadotte-park-bernadotte.html"],
 ["spoon","Havana Riverfront Park ramp (Illinois R.)","Havana","t",40.30015,-90.06685,"https://www.waymarking.com/waymarks/WMK8WZ_Illinois_River_Boat_Ramp_Riverfront_Park_Havana_IL"],
 ["embarras","Lake Charleston side-channel access (below dam)","Charleston","p",39.45977,-88.14656,"https://paddling.com/paddle/locations/lake-charleston"],
 ["embarras","Fox Ridge State Park canoe launch","Charleston","b",39.4,-88.15,"https://marinas.com/view/ramp/jxcyd8_Embarras_River_Fox_Ridge_State_Park_Ramp_Charleston_IL_United_States"],
 ["embarras","Cumberland County Covered Bridge (informal)","Greenup","t",39.23857,-88.1878,"https://www.hmdb.org/m.asp?m=152477"],
 ["cache-il","Lower Cache River Access (Perks Rd)","Ullin/Perks","p",37.29732,-89.05306,"https://milespaddled.com/cache-river/"],
 ["cache-il","Cache Bayou Outfitters landing (Dean Ln, fee)","Ullin","t",37.29091,-89.08417,"https://www.enjoyillinois.com/explore/listing/cache-bayou-outfitters/"],
 ["bigmuddy","Big Muddy Boat Launch (Turkey Bayou CG, USFS)","Gorham","t",37.685,-89.41139,"https://www.fs.usda.gov/r09/shawnee/recreation/oakwood-bottoms-turkey-bayou-campground"],
 ["lusk","Saltpeter Cave crossing (Trail 481, 1.5-mi carry)","Eddyville","p",37.53557,-88.54647,"https://milespaddled.com/lusk-creek/"],
 ["lusk","Lusk Creek Access (Eddyville Blacktop, USFS)","Eddyville","t",37.47259,-88.54769,"https://milespaddled.com/lusk-creek/"],
 ["kaskaskia","Spillway Rec Area ramp (below Shelbyville dam)","Shelbyville","p",39.40694,-88.77972,"https://thedyrt.com/camping/illinois/spillway"],
 ["nbchicago","Tower Road Boat Launch (Skokie Lagoons)","Winnetka","p",42.1135,-87.77477,"https://naturalatlas.com/boat-launches/tower-road-2239478"],
 ["nbchicago","Willow Road dam launch","Northfield","b",42.10197,-87.75884,"https://milespaddled.com/chicago-river-north-branch/"],
 ["nbchicago","River Park launch (N Shore Channel confluence)","Chicago","b",41.97304,-87.70419,"https://www.atly.com/location/River-Park-KayakCanoe-Boat-Launch"],
 ["nbchicago","Clark (Richard) Park / WMS Boathouse","Chicago","t",41.94336,-87.69515,"https://www.chicagoparkdistrict.com/parks-facilities/clark-richard-boat-launch"],
]


# ---- backup SPINES: hand-traced course through the documented run (upstream -> downstream).
#      QC guarantee: every river with <2 pinned landings still highlights instantly. ----
SPINE = {
 "mfvermilion":[[40.32,-87.78],[40.21,-87.74],[40.14,-87.71],[40.10,-87.66]],
 "mackinaw":[[40.63,-89.05],[40.62,-89.20],[40.55,-89.35],[40.50,-89.55],[40.49,-89.72]],
 "sangamon":[[40.20,-88.38],[40.16,-88.44],[40.10,-88.52],[40.03,-88.57]],
 "spoon":[[40.71,-90.27],[40.60,-90.33],[40.44,-90.44],[40.36,-90.25],[40.30,-90.07]],
 "embarras":[[39.46,-88.147],[39.40,-88.15],[39.32,-88.15],[39.24,-88.188]],
 "cache-il":[[37.33,-89.08],[37.32,-89.00],[37.30,-88.93]],
 "bigmuddy":[[37.76,-89.34],[37.70,-89.40],[37.63,-89.44]],
 "kaskaskia":[[39.40,-88.78],[39.25,-88.90],[39.10,-89.00],[38.97,-89.11]],
 "lusk":[[37.52,-88.57],[37.46,-88.54],[37.41,-88.50]],
 "vermilion-il":[[40.88,-88.63],[41.00,-88.75],[41.12,-88.83],[41.26,-89.00],[41.29,-89.06]],
 "ausable":[[44.66,-84.71],[44.66,-84.55],[44.65,-84.40],[44.63,-84.30],[44.66,-84.13]],
 "rifle":[[44.42,-84.02],[44.31,-84.05],[44.15,-84.03],[44.05,-83.98],[44.05,-83.86]],
 "sturgeon-mi":[[45.23,-84.59],[45.27,-84.60],[45.30,-84.61],[45.32,-84.63],[45.40,-84.62]],
 "pigeon-mi":[[45.16,-84.47],[45.24,-84.45],[45.30,-84.46],[45.36,-84.51],[45.39,-84.54]],
 "huron-mi":[[42.57,-83.53],[42.52,-83.65],[42.42,-83.77],[42.31,-83.79],[42.28,-83.73],[42.24,-83.62],[42.20,-83.50],[42.09,-83.29],[42.08,-83.19]],
 "chippewa-mi":[[43.59,-84.89],[43.58,-84.85],[43.60,-84.78],[43.60,-84.55],[43.59,-84.37],[43.61,-84.25]],
 "cass":[[43.41,-83.49],[43.37,-83.58],[43.33,-83.73],[43.33,-83.80],[43.36,-83.88],[43.37,-83.96]],
 "thunderbay":[[45.00,-84.14],[45.06,-83.90],[45.12,-83.72],[45.09,-83.50],[45.06,-83.43]],
 "manistee-upper":[[44.77,-84.85],[44.75,-84.84],[44.69,-84.85],[44.61,-84.99],[44.55,-85.06],[44.52,-85.17],[44.49,-85.40]],
 "rogue":[[43.23,-85.52],[43.12,-85.56],[43.08,-85.60],[43.03,-85.62]],
 "elkhorn":[[38.19,-84.79],[38.26,-84.83],[38.30,-84.85],[38.34,-84.87]],
 "red-ky":[[37.79,-83.50],[37.82,-83.58],[37.84,-83.68],[37.82,-83.78]],
 "green-ky":[[37.20,-86.03],[37.18,-86.11],[37.22,-86.24],[37.24,-86.33]],
 "barren":[[36.89,-86.13],[36.95,-86.30],[36.99,-86.44],[37.03,-86.55]],
 "nolin":[[37.28,-86.25],[37.26,-86.15],[37.23,-86.07]],
 "rockcastle":[[37.30,-84.22],[37.20,-84.20],[37.05,-84.25],[36.98,-84.33]],
 "licking-ky":[[38.12,-83.53],[38.20,-83.45],[38.30,-83.35]],
 "floydsfork":[[38.22,-85.45],[38.15,-85.48],[38.08,-85.52],[38.03,-85.55]],
 "gasper":[[36.95,-86.60],[36.98,-86.70],[37.00,-86.80]],
 "rough-ky":[[37.61,-86.50],[37.60,-86.42],[37.63,-86.25],[37.65,-86.12]],
 "greenbrier":[[38.22,-80.09],[38.13,-80.18],[38.05,-80.30],[37.93,-80.45],[37.72,-80.64]],
 "sbpotomac":[[38.90,-79.25],[38.99,-79.13],[39.06,-78.97],[39.20,-78.85],[39.34,-78.75],[39.45,-78.65]],
 "cacapon":[[39.06,-78.59],[39.18,-78.52],[39.30,-78.44],[39.48,-78.35],[39.62,-78.29]],
 "cheat":[[39.09,-79.68],[39.20,-79.65],[39.35,-79.67],[39.49,-79.64]],
 "elk-wv":[[38.48,-80.41],[38.66,-80.71],[38.46,-81.08],[38.49,-81.35],[38.35,-81.63]],
 "coal-wv":[[38.25,-81.68],[38.32,-81.75],[38.39,-81.83]],
 "bluestone":[[37.44,-81.01],[37.52,-80.95],[37.62,-80.93]],
 "mohican":[[40.65,-82.28],[40.61,-82.20],[40.55,-82.15],[40.47,-82.10]],
 "littlemiami":[[39.75,-83.93],[39.53,-84.09],[39.35,-84.12],[39.27,-84.26],[39.17,-84.29]],
 "bigdarby":[[40.05,-83.25],[39.95,-83.22],[39.87,-83.20],[39.76,-83.18]],
 "kokosing":[[40.39,-82.47],[40.37,-82.38],[40.39,-82.30],[40.36,-82.20]],
 "mad-oh":[[40.05,-83.80],[39.92,-83.83],[39.85,-83.95],[39.80,-84.03]],
 "littlebeaver":[[40.80,-80.68],[40.73,-80.61],[40.70,-80.52]],
 "cuyahoga":[[41.15,-81.36],[41.13,-81.48],[41.24,-81.55],[41.32,-81.59],[41.40,-81.60]],
 "grand-oh":[[41.76,-80.95],[41.72,-81.05],[41.72,-81.24]],
 "stillwater-oh":[[40.12,-84.35],[39.96,-84.33],[39.87,-84.30]],
 "sandusky-oh":[[40.83,-83.28],[41.00,-83.20],[41.11,-83.18],[41.35,-83.12]],
 "rum":[[46.07,-93.67],[45.76,-93.65],[45.57,-93.58],[45.56,-93.35],[45.40,-93.38],[45.20,-93.39]],
 "cannon":[[44.29,-93.27],[44.46,-93.16],[44.51,-92.90],[44.57,-92.74],[44.56,-92.62]],
 "root-mn":[[43.84,-92.18],[43.72,-91.97],[43.80,-91.76],[43.76,-91.56],[43.73,-91.30]],
 "zumbro":[[44.03,-92.46],[44.28,-92.42],[44.24,-92.30],[44.31,-92.00]],
 "crowwing":[[46.63,-94.88],[46.45,-94.75],[46.33,-94.64],[46.33,-94.47],[46.27,-94.33]],
 "snake-mn":[[45.88,-93.29],[45.85,-93.10],[45.82,-92.90],[45.82,-92.76]],
 "kettle":[[46.45,-92.90],[46.17,-92.85],[46.12,-92.87],[45.95,-92.82],[45.84,-92.75]],
 "crow-mn":[[45.09,-93.73],[45.16,-93.66],[45.24,-93.51]],
 "missheadwaters":[[47.24,-95.20],[47.28,-95.14],[47.35,-95.10],[47.45,-94.95],[47.47,-94.88]],
 "sugarcreek":[[40.04,-86.90],[39.94,-87.09],[39.88,-87.20],[39.87,-87.32],[39.91,-87.45]],
 "tippecanoe":[[41.20,-85.90],[41.10,-86.30],[41.05,-86.61],[40.90,-86.75],[40.74,-86.77]],
 "blue-in":[[38.43,-86.19],[38.34,-86.28],[38.22,-86.36],[38.15,-86.42]],
 "whitewater-in":[[39.42,-85.01],[39.35,-84.94],[39.28,-84.87]],
 "wildcat":[[40.47,-86.18],[40.45,-86.45],[40.44,-86.70],[40.44,-86.85]],
 "bigpine":[[40.55,-87.20],[40.45,-87.30],[40.37,-87.42]],
 "flatrock-in":[[39.55,-85.45],[39.43,-85.63],[39.30,-85.80],[39.21,-85.90]],
 "driftwood":[[39.35,-85.96],[39.28,-85.94],[39.22,-85.91]],
 "eel-in":[[41.16,-85.48],[41.08,-85.63],[41.00,-85.77],[40.91,-85.92],[40.75,-86.36]],
 "cedarck-in":[[41.35,-85.08],[41.28,-85.04],[41.22,-85.00]],
 "mississinewa":[[40.56,-85.66],[40.62,-85.80],[40.71,-85.95],[40.75,-86.07]],
 "upperiowa":[[43.36,-92.00],[43.41,-91.90],[43.31,-91.79],[43.38,-91.60],[43.44,-91.40],[43.49,-91.26]],
 "yellow-ia":[[43.11,-91.50],[43.10,-91.35],[43.09,-91.18]],
 "turkey-ia":[[42.85,-91.40],[42.74,-91.26],[42.71,-91.08],[42.72,-91.02]],
 "volga":[[42.84,-91.80],[42.80,-91.55],[42.75,-91.40],[42.74,-91.26]],
 "maquoketa":[[42.24,-91.18],[42.17,-90.95],[42.07,-90.66],[42.10,-90.45],[42.14,-90.34]],
 "wapsi":[[42.47,-91.90],[42.39,-91.76],[42.25,-91.60],[42.11,-91.28]],
 "boone-ia":[[42.44,-93.82],[42.30,-93.88],[42.15,-93.92],[42.06,-93.95]],
 "midraccoon":[[41.69,-94.36],[41.64,-94.28],[41.59,-94.20]],
 "raccoon":[[41.59,-94.19],[41.61,-94.02],[41.53,-93.95],[41.55,-93.75],[41.58,-93.65]],
 "flambeau":[[45.853,-90.600],[45.863,-90.705],[45.769,-90.761],[45.692,-90.813],[45.573,-90.949]],
 "namekagon":[[46.19,-91.31],[46.01,-91.48],[45.89,-91.87],[45.94,-92.10],[46.05,-92.27]],
 "peshtigo":[[45.518,-88.339],[45.478,-88.330],[45.414,-88.346],[45.388,-88.305],[45.381,-88.301]],
 "brule":[[46.38,-91.68],[46.48,-91.62],[46.56,-91.58],[46.67,-91.55],[46.74,-91.53]],
 "nbchicago":[[42.10,-87.76],[42.03,-87.74],[41.97,-87.70],[41.93,-87.68]],
 "thornapple":[[42.62,-85.20],[42.64,-85.29],[42.71,-85.46],[42.83,-85.48],[42.95,-85.49]],
 "flat":[[43.18,-85.25],[43.10,-85.23],[43.00,-85.29],[42.94,-85.34]],
 "pawpaw":[[42.22,-86.18],[42.21,-86.24],[42.19,-86.26],[42.19,-86.30],[42.20,-86.34],[42.19,-86.37],[42.12,-86.47]],
 "dowagiac":[[41.98,-86.13],[41.89,-86.20],[41.84,-86.25]],
 "clinton":[[42.67,-83.10],[42.66,-83.07],[42.61,-83.03],[42.59,-82.93],[42.58,-82.88],[42.59,-82.78]],
 "stlouis":[[46.72,-92.46],[46.65,-92.35],[46.66,-92.28],[46.74,-92.10]],
 "current":[[37.40,-91.67],[37.37,-91.55],[37.28,-91.41],[37.18,-91.25],[37.05,-91.10],[36.96,-91.00]],
 "jacksfork":[[37.08,-91.78],[37.12,-91.60],[37.15,-91.44],[37.15,-91.35],[37.18,-91.25]],
 "elevenpoint":[[36.79,-91.53],[36.78,-91.40],[36.70,-91.30],[36.63,-91.18]],
 "niangua":[[37.55,-92.95],[37.65,-92.90],[37.72,-92.86],[37.80,-92.88]],
 "meramec":[[37.95,-91.55],[38.05,-91.30],[38.13,-91.18],[38.22,-91.09]],
 "gasconade":[[37.65,-92.55],[37.75,-92.35],[37.85,-92.20],[37.95,-92.10]],
 "bigpiney":[[37.35,-92.05],[37.55,-92.05],[37.70,-92.03],[37.78,-92.02]],
 "huzzah":[[37.92,-91.20],[37.97,-91.13],[38.02,-91.08]],
 "northfork-mo":[[36.92,-92.25],[36.80,-92.22],[36.70,-92.18],[36.60,-92.16]],
}
for r in R:
    r["spine"] = SPINE.get(r["id"])
# QC: every river must have an offline highlight path (>=2 landings OR spine OR NE key)
NE_IDS = {"wisconsin","rock","chippewa","fox-lower","wolf-lower","stcroix","menominee","rock-il","fox-chain",
 "illinois-r","desplaines","kankakee","manistee","muskegon","grand-mi","kalamazoo","stjoseph","kentucky-r",
 "cumberland-ky","ohio-r","new-wv","kanawha","maumee","muskingum","minnesota-r","wabash","cedar-ia","desmoines-r","green-ky","licking-ky","missouri-r"}
land_count = {}
for l in L: land_count[l[0]] = land_count.get(l[0],0)+1
uncovered = [r["id"] for r in R if land_count.get(r["id"],0)<2 and not r["spine"] and r["id"] not in NE_IDS]
assert not uncovered, f"RIVERS WITH NO OFFLINE HIGHLIGHT PATH: {uncovered}"
# spines must fit their river bbox
for r in R:
    if r["spine"]:
        s,w,n,e = r["bbox"]
        for lat,lon in r["spine"]:
            assert s-0.02<=lat<=n+0.02 and w-0.02<=lon<=e+0.02, f"spine point outside bbox: {r['id']} {lat},{lon}"


# ---- outfitters (kayak rentals, max 3, user-confirmed) + campgrounds (max 3) ----
OUTFIT = {
 "peremarquette":[["Baldwin Canoe Rental","https://baldwincanoe.com/pere-marquette-river/"],
                  ["Henry's Landing","http://www.henryslanding.com/kayak-rental.html"],
                  ["Ivan's Canoe Rental","https://ivansmichigan.com/"]],
 "pine-mi":[["Pine River Paddlesports Center","https://www.thepineriver.com/pine-river"],
            ["Horina's Canoe & Kayak Rental","https://www.horinasprcanoe.com/thepineriver"],
            ["The Sportsman's Port","https://www.thesportsmansport.com/"]],
}
CAMPS = {
 "peremarquette":[["Ivan's Campground & Cabins","https://ivansmichigan.com/"],
                  ["Henry's Landing Campground","http://www.henryslanding.com/camping.html"],
                  ["Sulak Campground (USFS)","https://www.fs.usda.gov/r09/huron-manistee/recreation/sulak-campground"]],
 "pine-mi":[["Peterson Bridge Campground (USFS)","https://www.fs.usda.gov/r09/huron-manistee/recreation/peterson-bridge-campground"],
            ["Lincoln Bridge SF Campground","https://www.michigan.gov/recsearch/sfcampgroundsa-m/lincolnbridge"],
            ["The Sportsman's Port Campground","https://www.thesportsmansport.com/"]],
}
for r in R:
    r["outfitters"] = OUTFIT.get(r["id"], [])[:3]
    r["camps"] = CAMPS.get(r["id"], [])[:3]


# ---- greens where motors are genuinely common (hidden with the big-river toggle OFF) ----
MOTOROK = {"black","kankakee","barren","bigmuddy","green-ky","licking-ky","wapsi"}
for r in R:
    r["motorok"] = r["id"] in MOTOROK

# ---- big-river traversible sections (upstream -> downstream; danger: 0 ok, 1 not-advised/gray, 2 dangerous/red) ----
SECTIONS = {
 "rock":[["Watertown → Jefferson",0,[[43.19,-88.72],[43.05,-88.77],[43.00,-88.78]]],["Fort Atkinson → Janesville",0,[[42.93,-88.84],[42.85,-88.95],[42.75,-89.03],[42.68,-89.02]]],["Janesville → Beloit",0,[[42.68,-89.02],[42.60,-89.03],[42.50,-89.03]]]],
 "rock-il":[["Rockton → Rockford",0,[[42.45,-89.07],[42.35,-89.05],[42.27,-89.09]]],["Byron → Oregon",0,[[42.13,-89.26],[42.05,-89.33],[42.01,-89.33]]],["Oregon → Dixon",0,[[42.01,-89.33],[41.93,-89.36],[41.84,-89.48]]]],
 "wisconsin":[["Sauk City → Spring Green",0,[[43.27,-89.72],[43.20,-89.90],[43.17,-90.07]]],["Spring Green → Boscobel",0,[[43.17,-90.07],[43.10,-90.30],[43.13,-90.70]]],["Boscobel → Wyalusing",0,[[43.13,-90.70],[43.05,-90.88],[42.97,-91.10]]]],
 "chippewa":[["Eau Claire → Caryville",0,[[44.80,-91.50],[44.75,-91.65],[44.72,-91.77]]],["Durand → the Mississippi",0,[[44.63,-91.96],[44.55,-92.00],[44.43,-92.08]]]],
 "fox-lower":[["Princeton → Berlin",0,[[43.85,-89.12],[43.90,-89.05],[43.97,-88.94]]],["De Pere → Green Bay",0,[[44.45,-88.06],[44.50,-88.02],[44.54,-88.00]]]],
 "wolf-lower":[["Shawano → Shiocton (Dragonfly water)",0,[[44.78,-88.60],[44.60,-88.55],[44.44,-88.58]]],["New London → Fremont",0,[[44.39,-88.74],[44.30,-88.80],[44.26,-88.86]]]],
 "stcroix":[["Riverside → St. Croix Falls",0,[[45.77,-92.62],[45.60,-92.65],[45.41,-92.65]]],["Osceola → Stillwater",0,[[45.32,-92.70],[45.20,-92.76],[45.06,-92.80]]]],
 "menominee":[["Piers Gorge (expert whitewater)",1,[[45.72,-87.98],[45.70,-87.96],[45.68,-87.95]]],["Menominee → the mouth",0,[[45.15,-87.62],[45.11,-87.60],[45.09,-87.59]]]],
 "fox-chain":[["McHenry → Algonquin",0,[[42.33,-88.27],[42.24,-88.28],[42.16,-88.29]]],["St. Charles → Aurora",0,[[41.91,-88.31],[41.82,-88.31],[41.76,-88.32]]]],
 "illinois-r":[["Morris → Ottawa",0,[[41.35,-88.42],[41.33,-88.60],[41.34,-88.84]]],["Ottawa → Starved Rock",0,[[41.34,-88.84],[41.32,-88.92],[41.32,-88.99]]]],
 "manistee":[["Tippy Dam → High Bridge",0,[[44.26,-85.94],[44.26,-86.00],[44.25,-86.06]]],["High Bridge → Manistee Lake",0,[[44.25,-86.06],[44.24,-86.15],[44.25,-86.25]]]],
 "muskegon":[["Croton → Newaygo",0,[[43.44,-85.66],[43.42,-85.73],[43.42,-85.80]]],["Newaygo → Bridgeton",0,[[43.42,-85.80],[43.38,-85.88],[43.33,-85.95]]]],
 "grand-mi":[["Grand Rapids → Eastmanville",0,[[42.97,-85.68],[43.00,-85.80],[43.02,-85.95]]],["Eastmanville → Grand Haven",0,[[43.02,-85.95],[43.04,-86.10],[43.06,-86.22]]]],
 "kalamazoo":[["Allegan → New Richmond",0,[[42.53,-85.85],[42.58,-86.00],[42.65,-86.10]]],["New Richmond → Saugatuck",0,[[42.65,-86.10],[42.66,-86.15],[42.66,-86.20]]]],
 "stjoseph":[["Niles → Berrien Springs",0,[[41.83,-86.25],[41.90,-86.30],[41.95,-86.34]]],["Berrien Springs → St. Joseph",0,[[41.95,-86.34],[42.03,-86.42],[42.10,-86.48]]]],
 "kentucky-r":[["The Palisades: Camp Nelson → Clays Ferry",0,[[37.78,-84.60],[37.82,-84.50],[37.88,-84.45]]],["Frankfort pool",0,[[38.15,-84.87],[38.20,-84.87],[38.27,-84.83]]]],
 "cumberland-ky":[["Below Cumberland Falls (guided rafts)",1,[[36.84,-84.34],[36.86,-84.40],[36.87,-84.45]]],["Wolf Creek tailwater (Burkesville float)",0,[[36.87,-85.15],[36.83,-85.25],[36.80,-85.35]]]],
 "ohio-r":[["Louisville pool",0,[[38.28,-85.75],[38.28,-85.80],[38.26,-85.85]]],["Cincinnati pool",0,[[39.09,-84.50],[39.07,-84.60],[39.05,-84.70]]]],
 "new-wv":[["Sandstone → Thurmond (Upper Gorge)",1,[[37.76,-80.90],[37.85,-81.00],[37.95,-81.07]]],["Lower Gorge: Thurmond → Fayette (expert rafting)",1,[[37.95,-81.07],[38.02,-81.08],[38.07,-81.08]]]],
 "kanawha":[["Kanawha Falls → Charleston",0,[[38.14,-81.21],[38.20,-81.50],[38.35,-81.63]]]],
 "maumee":[["Grand Rapids → Waterville",0,[[41.42,-83.86],[41.47,-83.75],[41.50,-83.72]]],["Side Cut → Toledo",0,[[41.55,-83.65],[41.60,-83.58],[41.65,-83.53]]]],
 "muskingum":[["Zanesville → McConnelsville",0,[[39.94,-82.01],[39.80,-81.90],[39.65,-81.85]]],["Stockport → Marietta",0,[[39.55,-81.79],[39.48,-81.65],[39.42,-81.45]]]],
 "minnesota-r":[["Mankato → St. Peter",0,[[44.16,-94.00],[44.25,-93.96],[44.32,-93.96]]],["St. Peter → Henderson",0,[[44.32,-93.96],[44.45,-93.93],[44.53,-93.91]]]],
 "stlouis":[["Jay Cooke canyon — DANGEROUS, no watercraft",2,[[46.66,-92.36],[46.65,-92.30],[46.66,-92.26]]],["Estuary: Boy Scout Landing → Duluth",0,[[46.68,-92.20],[46.71,-92.15],[46.74,-92.10]]]],
 "wabash":[["Delphi → Lafayette",0,[[40.59,-86.68],[40.50,-86.78],[40.42,-86.90]]],["Lafayette → Attica",0,[[40.42,-86.90],[40.35,-87.10],[40.29,-87.24]]]],
 "cedar-ia":[["Cedar Falls → Waterloo",0,[[42.53,-92.44],[42.50,-92.38],[42.49,-92.33]]],["Vinton → Cedar Rapids",0,[[42.17,-92.02],[42.08,-91.85],[41.98,-91.66]]]],
 "desmoines-r":[["Downtown Des Moines water trail",0,[[41.63,-93.65],[41.58,-93.60],[41.54,-93.55]]],["Red Rock reach",0,[[41.45,-93.40],[41.40,-93.30],[41.37,-93.25]]]],
 "missouri-r":[["Jefferson City → Hermann",0,[[38.58,-92.17],[38.65,-91.80],[38.70,-91.44]]],["Hermann eastward",0,[[38.70,-91.44],[38.72,-91.35],[38.75,-91.32]]]],
}
for r in R:
    r["sections"] = SECTIONS.get(r["id"]) if r["cls"]=="blue" else None
blues_no_sec = [r["id"] for r in R if r["cls"]=="blue" and not r["sections"]]
assert not blues_no_sec, f"blues without sections: {blues_no_sec}"


# ---- permit-required water: red outline on the map ----
PERMIT = {"peremarquette","pine-mi"}   # USFS watercraft permit Memorial Day wknd - Labor Day
for r in R:
    r["permit"] = r["id"] in PERMIT
    if r["id"]=="wolf-upper":
        r["permit_seg"] = [[45.118,-88.663],[45.05,-88.68],[44.98,-88.70],[44.93,-88.65],[44.88,-88.63]]
        r["permit_seg_label"] = "Menominee Reservation stretch — tribal permit required (Otter Slide → Big Smokey Falls → Keshena)"
    else:
        r["permit_seg"] = None

# ---- draft outfitter candidates (visual flag only; names live in the Excel roadmap, not the HTML) ----
from outfitters_data import CAND
for r in R:
    r["outcand"] = r["id"] in CAND

# ---- outfitter-covered "core" box [S,W,N,E] for outfitted rivers whose full run extends
#      beyond livery water: the line outside the core fades to the BYO dot-dash style ----
CORE = {
 "peremarquette":[43.80,-86.30,44.00,-85.70],   # livery water M-37 -> Scottville; fade to Ludington
 "kickapoo":[43.55,-90.95,43.85,-90.40],        # Ontario -> La Farge; fade below to Wauzeka
 "sugar":[42.60,-89.75,43.05,-89.25],           # Belleville -> Brodhead; fade into IL
 "milwaukee":[43.02,-88.06,43.65,-87.85],       # Newburg -> harbor; fade Kewaskum -> West Bend
 "black":[44.03,-90.90,44.46,-90.60],           # Hatfield -> North Bend; fade Van Loon leg
 "peshtigo":[45.33,-88.45,45.42,-88.22],        # Roaring Rapids; fade Goodman -> Farm Dam
 "brule":[46.30,-91.80,46.69,-91.35],           # Stone's -> Hwy 13; fade the ledges to the mouth
 "huron-mi":[42.22,-83.95,42.65,-83.55],        # Proud Lake -> Ypsilanti; fade to Lake Erie
 "clinton":[42.55,-83.35,42.70,-82.87],         # Yates -> Mt. Clemens; fade to Lake St. Clair
 "betsie":[44.45,-86.115,44.70,-85.75],         # livery firm to Grace Rd; fade to Betsie Bay
 "pawpaw":[42.05,-86.385,42.28,-86.10],         # trail to Riverside; fade last 11 mi to Benton Harbor
 "thornapple":[42.60,-85.55,42.72,-85.15],      # Barry Co segment; fade the Kent segment
 "vermilion-il":[41.24,-89.10,41.35,-88.55],    # rafting water Lowell -> Oglesby; fade Pontiac -> Streator
 "kishwaukee":[42.15,-89.02,42.31,-88.60],      # to Atwood Park; fade the mouth reach
 "kankakee":[41.05,-88.10,41.25,-87.75],        # livery water around the SP; fade Momence + Wilmington ends
 "dupage":[41.51,-88.35,41.85,-88.05],          # Knoch Knolls -> Hammel; fade to the confluence
}
for r in R:
    r["core"] = CORE.get(r["id"])
    if r["core"]:
        assert r["outcand"] or r["outfitters"], f"core box on non-outfitted river: {r['id']}"
        cs,cw,cn,ce = r["core"]; s,w,n,e = r["bbox"]
        assert s<=cs<cn<=n and w<=cw<ce<=e, f"core box outside bbox: {r['id']}"

data = {"rivers":R,"landings":L,"ne":json.load(open("/tmp/ne_fallback.json")),"states":json.load(open("/tmp/states.json"))}
js = json.dumps(data,separators=(",",":"))
open("/home/claude/rivermap/data.json","w").write(js)
print("rivers:",len(R)," landings:",len(L)," bytes:",len(js))
# sanity: all landings reference valid river ids and are inside their river bbox
ids={r["id"]:r for r in R}
bad=0
for l in L:
    rid,name,_,typ,lat,lon,_=l
    assert rid in ids, name
    s,w,n,e=ids[rid]["bbox"]
    if not(s<=lat<=n and w<=lon<=e):
        print("OUT OF BBOX:",rid,name,lat,lon); bad+=1
    if typ not in "ptb": print("BAD TYPE",name); bad+=1
print("bbox violations:",bad)
