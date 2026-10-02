#!/usr/bin/env python3
"""
INDIAN CUISINE.EXE - cyberpunk x student-notes website generator.
Run:  python indian_cuisine_site.py
Output: indian_cuisine.html (opens in browser)
 - 10 Chrome-style tabs on top (one per section)
 - each section = 2 fixed A4 pages  ->  Ctrl+P prints exactly 20 A4 pages
   (print tip: enable "Background graphics", margins = None, scale 100%)
"""
import html, webbrowser, pathlib

# key, tab label, icon, tagline, [2 paragraphs], [3 facts], [5 (dish, desc)], student tip
S = [
("intro", "Boot Up", "⚡", "Welcome to the flavour mainframe",
 ["India's cuisine is not one cuisine but hundreds of regional food systems, shaped by geography, religion, climate and trade. A meal in Punjab, Kerala and Nagaland can feel like three different countries on one plate.",
  "This guide is a study pack: history, regions, spices, street food, student budget hacks and sweets. Each tab is two A4 pages, so you can read it on screen or print the whole thing as a 20-page revision booklet."],
 ["1.4 billion people, 28 states, 700+ dialects, countless recipes", "Roughly 30-40% of Indians follow a vegetarian diet, the highest share in the world", "Staple grains: wheat in the north, rice in the south and east, millets in the dry west"],
 [("Dal-Chawal", "Lentils with rice: the everyday comfort meal"), ("Roti / Chapati", "Flat whole-wheat bread cooked on a tawa"), ("Sabzi", "Seasonal vegetables cooked dry or in light gravy"), ("Raita", "Spiced yogurt that cools the heat"), ("Chai", "Milky spiced tea, the national drink")],
 "Think of a thali as a balanced plate: grain + dal + veg + curd + pickle."),
("history", "History.log", "📜", "5000 years of recipes, compiled",
 ["Indus Valley people ate wheat, barley, lentils and dairy over 4,000 years ago. Ancient texts like the Ayurvedic works describe food by taste, season and effect on the body.",
  "Later waves reshaped the kitchen: Persian and Central Asian rulers brought dum cooking, kebabs and dried fruit; the Portuguese brought chillies, potatoes, tomatoes and vinegar; the British gave tea culture and 'curry' as a label."],
 ["Black pepper from Kerala was traded to Rome and Egypt for centuries", "Chillies arrived only in the 1500s, before that heat came from pepper and ginger", "The Mughal court merged Persian technique with Indian spice to create rich gravies"],
 [("Khichdi", "Ancient rice and lentil porridge, still a healing food"), ("Biryani", "Mughal layered rice, now a national obsession"), ("Vindaloo", "Goan dish from Portuguese carne de vinha d'alhos"), ("Samosa", "Central Asian pastry made Indian with potato and peas"), ("Jalebi", "Persian-origin sweet, fried and soaked in syrup")],
 "Exam angle: link every famous dish to a trade route or empire."),
("north", "North.exe", "🏔️", "Tandoor, ghee and big flavours",
 ["North Indian food (Punjab, Delhi, Uttar Pradesh, Kashmir) is known for wheat breads, dairy, paneer and the clay tandoor oven. Gravies are thick, creamy and built on onion, tomato, ginger and garam masala.",
  "Punjabi dhabas serve hearty food for truck drivers, while Awadhi cuisine of Lucknow is slow-cooked and delicate. Kashmiri food uses fennel, dry ginger and saffron instead of onion and garlic."],
 ["Tandoor temperatures can reach about 480°C", "Lassi, a yogurt drink, originated in Punjab", "Kashmiri wazwan is a feast of up to 36 courses"],
 [("Butter Chicken", "Tandoori chicken in tomato-butter gravy"), ("Rajma Chawal", "Kidney beans with rice, a Sunday classic"), ("Chole Bhature", "Spicy chickpeas with fluffy fried bread"), ("Sarson da Saag", "Mustard greens with makki di roti"), ("Galouti Kebab", "Melt-in-mouth Lucknowi minced meat patty")],
 "Cheap win: rajma chawal gives protein plus carbs for a very low price."),
("south", "South.exe", "🌴", "Rice, coconut, tamarind, curry leaf",
 ["South Indian cuisine covers Tamil Nadu, Kerala, Karnataka, Andhra Pradesh and Telangana. Rice and lentils are fermented into idli and dosa, and meals are tempered with mustard seeds, curry leaves and dried red chillies.",
  "Kerala loves coconut, seafood and banana-leaf sadhya feasts. Andhra and Chettinad cooking are famously fiery, while Karnataka balances sweet, sour and spicy in the same meal."],
 ["Idli and dosa batter is naturally fermented, which aids digestion", "Sambar is a lentil-vegetable stew thickened with tamarind", "A sadhya can have 20+ dishes served on one banana leaf"],
 [("Masala Dosa", "Crisp crepe stuffed with spiced potato"), ("Idli-Sambar", "Steamed rice cakes with lentil stew"), ("Hyderabadi Biryani", "Dum-cooked saffron rice with marinated meat"), ("Appam-Stew", "Lacy rice pancake with coconut milk stew"), ("Rasam", "Peppery tamarind soup, also a cold remedy")],
 "Dosa joints are open late and filling, and a classic student hangout."),
("east", "East.exe", "🐟", "Mustard oil, fish and gentle sweetness",
 ["Eastern India (Bengal, Odisha, Assam, Bihar, the North-East) uses mustard oil, panch phoron five-spice mix and a lot of fresh fish and rice. Flavours are subtle, with sharp mustard and sweetness balancing each other.",
  "Bengali meals follow a sequence from bitter to sweet. North-Eastern food is lighter, with fermented bamboo shoots, smoked meats, local herbs and very little oil."],
 ["Bengal is famous for rasgulla, though Odisha disputes its origin", "Panch phoron: fenugreek, nigella, mustard, cumin, fennel seeds", "Assam produces more than half of India's tea"],
 [("Macher Jhol", "Light Bengali fish curry with potato"), ("Litti Chokha", "Roasted wheat balls with mashed smoky veg"), ("Momos", "Steamed dumplings from the Himalayan belt"), ("Pakhala", "Fermented rice, a cooling summer meal in Odisha"), ("Mishti Doi", "Sweetened caramel yogurt set in clay pots")],
 "Litti chokha is cheap, filling and travels well, great for hostel life."),
("west", "West.exe", "🌶️", "Sweet-spicy thalis and coastal fire",
 ["Western India spans Gujarat, Maharashtra, Goa and Rajasthan. Gujarati food leans sweet and vegetarian, Maharashtrian food is bold with peanuts and kokum, and Goan food mixes Portuguese and coastal influences.",
  "Rajasthan's dry desert shaped a cuisine of dried beans, gram flour, ghee and long shelf life, because fresh vegetables and water were scarce."],
 ["Gujarati dishes often add jaggery for a sweet-sour balance", "Dal baati churma is baked in cow-dung embers in villages", "Goa's vinegar and toddy are legacy of Portuguese rule"],
 [("Vada Pav", "Mumbai's spicy potato fritter burger"), ("Dhokla", "Steamed fermented gram-flour cake"), ("Dal Baati Churma", "Rajasthani trio of lentils, baked wheat balls and sweet crumble"), ("Pav Bhaji", "Buttery mashed vegetable curry with soft rolls"), ("Fish Curry Rice", "Goan coconut-chilli curry, the coastal staple")],
 "Vada pav is a famously cheap Mumbai meal, so a good budget benchmark."),
("spice", "Spice.dll", "🧪", "The chemistry set of every kitchen",
 ["Indian cooking is applied chemistry. Whole spices are bloomed in hot oil (tadka or tempering) to release fat-soluble flavour, while ground spices are added later so they don't burn.",
  "Many spices also have traditional medicinal uses: turmeric for its curcumin, ginger for digestion, cumin and ajwain for gas relief. The masala dabba, a round steel box of seven spices, is the heart of every home kitchen."],
 ["India produces and consumes more spice than any other country", "Black pepper is nicknamed 'black gold'", "Garam masala differs in every household; there is no single recipe"],
 [("Turmeric (Haldi)", "Earthy, yellow, antiseptic; used in almost every curry"), ("Cumin (Jeera)", "Smoky seeds that start countless dals"), ("Coriander (Dhania)", "Citrusy seeds and fresh leaves, the base spice"), ("Cardamom (Elaichi)", "Queen of spices, used in chai and sweets"), ("Asafoetida (Hing)", "Pungent resin that mimics onion and garlic")],
 "Starter kit for hostel cooking: turmeric, red chilli, cumin, salt, garam masala."),
("street", "Street.bat", "🛺", "Chaat, fried things and legendary carts",
 ["Street food is India's real fast food, serving millions daily. Chaat is built around contrasts: crunchy, soft, sweet, sour, spicy and cool all in one bite, thanks to chutneys, yogurt and sev.",
  "Every city has its own signature: Delhi's chaat, Kolkata's kathi rolls, Mumbai's pav bhaji, Lucknow's tunday kebabs, Varanasi's tamatar chaat. Look for crowded stalls with high turnover for fresher food."],
 ["Pani puri has many names: golgappa, puchka, gupchup", "Chaat roughly means 'to lick', as in finger-licking good", "Street vendors form a huge part of India's informal economy"],
 [("Pani Puri", "Hollow crisp shells filled with spiced water"), ("Aloo Tikki", "Crisp spiced potato patties with chutneys"), ("Kathi Roll", "Egg-coated paratha wrapped around kebab or paneer"), ("Bhel Puri", "Puffed rice tossed with onion, tomato and tamarind"), ("Kachori", "Flaky fried pastry filled with spiced lentils")],
 "Safety: pick busy stalls, hot-fried items and bottled water."),
("student", "Hostel.hack", "🎒", "Eat well on a broke-student budget",
 ["A hostel kitchen needs only a pressure cooker and a stove. Dal, rice, khichdi, poha and upma can each be cooked in under 30 minutes for a few rupees per serving, and they are far more nutritious than instant noodles.",
  "Meal-prep tip: cook a big batch of dal and sabzi, refrigerate in boxes and pair with fresh roti or rice. Sprouts, eggs, curd, peanuts and soya chunks are cheap, high-protein add-ons."],
 ["Pressure cookers cut cooking time and fuel use by up to 70%", "Peanuts offer protein comparable to many pricier snacks", "Mess tip: a banana and curd can be a fast, balanced breakfast"],
 [("Poha", "Flattened rice with onion, peanuts and lemon, 10 minutes"), ("Egg Bhurji", "Spiced scrambled eggs, a high-protein quickie"), ("Veg Khichdi", "One-pot rice, lentils and vegetables"), ("Maggi Masala Upgrade", "Add veggies and an egg to level up"), ("Besan Chilla", "Savoury gram-flour pancake, protein-rich")],
 "Budget rule: buy lentils and rice in bulk, vegetables by season."),
("sweet", "Dessert.zip", "🍯", "Mithai, kulfi and chai culture",
 ["Indian sweets are tied to festivals and celebrations. Diwali has barfi and ladoo, Holi has gujiya, Eid has sheer khurma, and Onam has payasam. Sugar, milk, ghee, nuts and cardamom are the core building blocks.",
  "Beyond sweets, drinks define social life. Chai is brewed with milk, ginger and cardamom; lassi cools summer heat; nimbu pani and jaljeera refresh the afternoon, and filter coffee rules the south."],
 ["India is the world's largest milk producer", "Chai wallahs serve hundreds of cups daily at railway stations", "Kulfi is denser and creamier than ice cream as it isn't whipped"],
 [("Gulab Jamun", "Milk-solid dumplings in rose-cardamom syrup"), ("Rasmalai", "Soft cheese discs in saffron milk"), ("Kulfi", "Traditional frozen dessert with pistachio"), ("Masala Chai", "Spiced milk tea, fuel of every study session"), ("Filter Kaapi", "Strong south Indian decoction coffee with frothy milk")],
 "Final boss: keep exploring a new regional dish every month."),
]

CSS = """
:root{--bg:#07050f;--panel:#110b24;--cyan:#00f0ff;--pink:#ff2e97;--yellow:#fcee0a;--ink:#e8e6ff;--mut:#9a93c9}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#050309;color:var(--ink);font-family:'Segoe UI',Tahoma,sans-serif}
.browser{position:sticky;top:0;z-index:10;background:#1a1033;padding:8px 12px 0;border-bottom:2px solid var(--cyan);box-shadow:0 0 18px #00f0ff55}
.dots{display:flex;gap:6px;margin:0 0 6px 4px;align-items:center}.dots i{width:11px;height:11px;border-radius:50%;display:block}
.dots b{margin-left:12px;color:var(--mut);font:12px Consolas,monospace;font-weight:400}
.tabs{display:flex;gap:2px;overflow-x:auto;scrollbar-width:thin}
.tab{flex:0 1 150px;min-width:96px;padding:9px 14px;background:#120a26;color:var(--mut);border:0;border-radius:12px 12px 0 0;
 font:13px Consolas,monospace;cursor:pointer;white-space:nowrap;text-overflow:ellipsis;overflow:hidden;position:relative;transition:.15s}
.tab:hover{background:#241547;color:var(--cyan)}
.tab.active{background:var(--bg);color:var(--cyan);box-shadow:0 -2px 0 var(--pink) inset,0 0 12px #00f0ff44;z-index:2;text-shadow:0 0 8px var(--cyan)}
.bar{display:flex;gap:8px;align-items:center;padding:8px 4px;background:var(--bg);margin:0 -12px;padding-left:16px;font:12px Consolas,monospace;color:var(--mut)}
.url{flex:1;background:#150d2e;border-radius:16px;padding:5px 14px;color:var(--cyan)}
.bar button{background:var(--pink);color:#fff;border:0;border-radius:6px;padding:6px 12px;cursor:pointer;font:bold 12px Consolas,monospace}
.stage{padding:24px 0;display:flex;flex-direction:column;align-items:center;gap:24px}
.section{display:none}.section.active{display:flex;flex-direction:column;align-items:center;gap:24px}
.page{width:210mm;height:297mm;padding:16mm 15mm 14mm;background:
 linear-gradient(transparent 95%,#00f0ff0d 95%) 0 0/100% 8mm,var(--bg);position:relative;overflow:hidden;
 border:1px solid #2b1d55;box-shadow:0 0 30px #ff2e9733;display:flex;flex-direction:column;gap:6mm}
.page:before{content:"";position:absolute;top:0;right:0;width:46mm;height:46mm;background:linear-gradient(225deg,var(--pink),transparent 55%);opacity:.35}
.tag{font:11pt Consolas,monospace;color:var(--yellow);letter-spacing:2px}
h1{font-size:34pt;line-height:1.05;color:var(--cyan);text-shadow:2px 2px 0 var(--pink),0 0 18px #00f0ff77;text-transform:uppercase}
h2{font-size:20pt;color:var(--pink);border-left:5px solid var(--yellow);padding-left:10px}
.sub{font:italic 14pt Georgia,serif;color:var(--mut)}
p{font-size:13.5pt;line-height:1.6}
.note{background:var(--panel);border:1px dashed var(--yellow);border-radius:6px;padding:5mm;transform:rotate(-.4deg)}
.note h3{font:bold 13pt Consolas,monospace;color:var(--yellow);margin-bottom:3mm}
.note li{font-size:12.5pt;line-height:1.6;margin-left:5mm}
.hl{background:linear-gradient(transparent 60%,#fcee0a55 60%)}
.big{font-size:80pt;position:absolute;right:12mm;top:20mm;opacity:.9;filter:drop-shadow(0 0 14px var(--pink))}
.card{display:flex;gap:5mm;align-items:center;background:var(--panel);border:1px solid var(--cyan);border-radius:8px;padding:5mm;box-shadow:4px 4px 0 var(--pink)}
.card .n{font:bold 26pt Consolas,monospace;color:var(--yellow);min-width:14mm}
.card h3{font-size:16pt;color:var(--cyan)}.card span{font-size:12.5pt;color:var(--ink);line-height:1.45}
.tip{margin-top:auto;background:var(--yellow);color:#111;font:bold 13pt Consolas,monospace;padding:5mm;border-radius:6px;box-shadow:5px 5px 0 var(--pink)}
.foot{display:flex;justify-content:space-between;font:10pt Consolas,monospace;color:var(--mut);border-top:1px solid #2b1d55;padding-top:3mm}
@page{size:A4;margin:0}
@media print{
 html,body{background:#000;-webkit-print-color-adjust:exact;print-color-adjust:exact}
 .browser{display:none}.stage{padding:0;gap:0;display:block}
 .section,.section.active{display:block!important}
 .page{page-break-after:always;break-after:page;border:0;box-shadow:none;margin:0}
}
"""

JS = """
const tabs=[...document.querySelectorAll('.tab')],secs=[...document.querySelectorAll('.section')];
function show(k){tabs.forEach(t=>t.classList.toggle('active',t.dataset.k===k));
 secs.forEach(s=>s.classList.toggle('active',s.id===k));
 document.getElementById('url').textContent='https://indian-cuisine.exe/'+k;
 document.title=tabs.find(t=>t.dataset.k===k).textContent.trim();window.scrollTo(0,0);}
tabs.forEach(t=>t.onclick=()=>show(t.dataset.k));
document.addEventListener('keydown',e=>{if(e.altKey&&e.key>='1'&&e.key<='9'){const t=tabs[e.key-1];t&&show(t.dataset.k)}});
show('intro');
"""

def page(num, inner, label):
    return (f'<div class="page">{inner}<div class="foot"><span>INDIAN_CUISINE.EXE // {label}</span>'
            f'<span>PAGE {num:02d} / 20</span></div></div>')

def build():
    e = html.escape
    tabs, secs, n = [], [], 0
    for k, label, icon, tag, paras, facts, dishes, tip in S:
        tabs.append(f'<button class="tab" data-k="{k}">{icon} {e(label)}</button>')
        n += 1
        p1 = (f'<div class="big">{icon}</div><div class="tag">&gt; SECTION_{n:02d} // {e(label.upper())}</div>'
              f'<h1>{e(tag)}</h1><div class="sub">Study notes, part 1: the big picture</div>'
              + "".join(f"<p>{e(x)}</p>" for x in paras)
              + '<div class="note"><h3>📌 KEY FACTS</h3><ul>' + "".join(f'<li><span class="hl">{e(f)}</span></li>' for f in facts) + '</ul></div>')
        p1 = page(n * 2 - 1, p1, label)
        cards = "".join(f'<div class="card"><div class="n">{i+1:02d}</div><div><h3>{e(d)}</h3><span>{e(s)}</span></div></div>'
                        for i, (d, s) in enumerate(dishes))
        p2 = (f'<div class="tag">&gt; SECTION_{n:02d} // DATABASE</div><h2>Must-try dishes &amp; items</h2>'
              f'<div class="sub">Part 2: your revision checklist</div>{cards}<div class="tip">💡 STUDENT TIP: {e(tip)}</div>')
        p2 = page(n * 2, p2, label)
        secs.append(f'<section class="section" id="{k}">{p1}{p2}</section>')
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Indian Cuisine.exe</title>'
            f'<meta name="viewport" content="width=device-width,initial-scale=1"><style>{CSS}</style></head><body>'
            f'<div class="browser"><div class="dots"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i>'
            f'<i style="background:#28c840"></i><b>CYBER-THALI BROWSER v2.077</b></div><div class="tabs">{"".join(tabs)}</div>'
            f'<div class="bar"><span id="url" class="url"></span><button onclick="window.print()">🖨 PRINT 20 PAGES</button></div></div>'
            f'<main class="stage">{"".join(secs)}</main><script>{JS}</script></body></html>')

if __name__ == "__main__":
    out = pathlib.Path(__file__).with_name("indian_cuisine.html")
    out.write_text(build(), encoding="utf-8")
    print(f"Created {out}  (10 tabs x 2 A4 pages = 20 pages)")
    webbrowser.open(out.as_uri())
