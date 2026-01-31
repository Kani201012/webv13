import streamlit as st
import zipfile
import io
import json
from datetime import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Titan v21.0 | World-Class Architect", layout="wide", page_icon="💎")

st.markdown("""
    <style>
    .main { background: #020617; color: white; }
    .stTabs [data-baseweb="tab"] { color: white; font-weight: bold; font-size: 1.1rem; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4.5em; 
        background: linear-gradient(135deg, #1e293b 0%, #3b82f6 100%); 
        color: white; font-weight: 900; border: none; font-size: 1.4rem;
        box-shadow: 0 10px 40px rgba(59, 130, 246, 0.4); transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-3px); filter: brightness(1.2); }
    .stExpander { background-color: #0f172a !important; border: 1px solid #1e293b !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR: THE ARCHITECT'S STUDIO ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=60)
    st.title("Titan v21.0 Elite")
    
    with st.expander("🎭 1. Layout DNA (Structural)", expanded=True):
        layout_dna = st.selectbox("Select Site DNA", [
            "Modern Industrial (Asymmetric)", 
            "Classic Royal (Centered Luxury)", 
            "Apple-Style Bento (Grid)",
            "Glass-Tech SaaS (Futuristic)",
            "Brutalist Bold (High Contrast)",
            "Midnight Stealth (Elite Dark)"
        ])
        p_color = st.color_picker("Primary Brand Color", "#001F3F")
        s_color = st.color_picker("Accent/CTA Color", "#D4AF37")
        border_rad = st.select_slider("Corner Roundness", options=["0px", "8px", "24px", "60px"], value="24px")

    with st.expander("✍️ 2. Typography Studio", expanded=True):
        h_font = st.selectbox("Heading Font", ["Montserrat", "Playfair Display", "Oswald", "Space Grotesk"])
        b_font = st.selectbox("Body Font", ["Inter", "Roboto", "Open Sans", "Work Sans"])
        h_weight = st.select_slider("Heading Weight", options=["400", "700", "900"], value="900")
        ls = st.select_slider("Letter Spacing", options=["-0.05em", "-0.02em", "0em", "0.05em"], value="-0.02em")

    gsc_tag = st.text_input("GSC Verification Tag")
    st.info("Technical Lead: Kaydiem Script Lab")

# --- 3. DATA COLLECTION ---
st.title("🏗️ Kaydiem Titan Supreme Engine v21.0")

tabs = st.tabs(["📍 Identity", "🏗️ Content & SEO", "🖼️ Assets", "⚡ Live E-com", "🌟 Social Proof", "⚖️ Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "Red Hippo (The Planners)")
        biz_phone = st.text_input("Verified Phone", "+91 84540 02711")
        biz_email = st.text_input("Business Email", "events@redhippoplanners.in")
    with c2:
        biz_cat = st.text_input("Category", "Luxury Wedding Planner")
        biz_hours = st.text_input("Hours", "Mon-Sun: 10:00 - 19:00")
        prod_url = st.text_input("Production URL", "https://kani201012.github.io/site/")
    biz_logo = st.text_input("Logo URL (Direct Image Link)")
    biz_addr = st.text_area("Full Maps Physical Address")
    biz_areas = st.text_area("Service Areas (Comma separated)", "Vasant Kunj, South Delhi, Riyadh")
    map_iframe = st.text_area("Map Embed HTML Code")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", "Crafting Dream Weddings")
    seo_d = st.text_input("Meta Description (160 Chars)")
    biz_key = st.text_input("SEO Keywords")
    biz_serv = st.text_area("Services Listing (One per line)")
    about_txt = st.text_area("Our Story (800+ Words for E-E-A-T)", height=300)

with tabs[2]:
    st.header("📸 High-End Asset Manager")
    custom_hero = st.text_input("Hero Background URL")
    custom_feat = st.text_input("Feature Section Image URL")
    custom_gall = st.text_input("About Section Image URL")

with tabs[3]:
    st.header("🛒 Headless E-commerce Hub")
    sheet_url = st.text_input("Published CSV URL")

with tabs[4]:
    testi = st.text_area("Testimonials (Name | Quote)")
    faqs = st.text_area("FAQ (Question? ? Answer)")

with tabs[5]:
    priv_body = st.text_area("Privacy Policy", height=300)
    terms_body = st.text_area("Terms & Conditions", height=300)

# --- 4. THE TITAN OMNI-ENGINE CORE ---

# Prepare Global Data Dictionary to prevent NameErrors
data = {
    "biz_name": biz_name, "biz_phone": biz_phone, "biz_email": biz_email,
    "biz_cat": biz_cat, "biz_hours": biz_hours, "prod_url": prod_url,
    "biz_logo": biz_logo, "biz_addr": biz_addr, "biz_areas": biz_areas,
    "map_iframe": map_iframe, "hero_h": hero_h, "seo_d": seo_d,
    "biz_key": biz_key, "biz_serv": biz_serv, "about_txt": about_txt,
    "img_h": custom_hero if custom_hero else "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1600",
    "img_f": custom_feat if custom_feat else "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?q=80&w=800",
    "img_g": custom_gall if custom_gall else "https://images.unsplash.com/photo-1532712938310-34cb3982ef74?q=80&w=1600",
    "p_color": p_color, "s_color": s_color, "radius": border_rad,
    "h_font": h_font, "b_font": b_font, "h_weight": h_weight, "ls": ls,
    "wa_link": f"https://wa.me/{biz_phone.replace(' ', '').replace('+', '')}",
    "gsc": gsc_tag
}

# The CSS Master Style (Every single brace escaped for stability)
master_css = f"""
:root {{ --p: {data['p_color']}; --s: {data['s_color']}; --radius: {data['radius']}; }}
* {{ box-sizing: border-box; }}
body {{ font-family: '{data['b_font']}', sans-serif; color: #0f172a; line-height: 1.7; background: #fff; margin:0; overflow-x: hidden; }}
h1, h2, h3 {{ font-family: '{data['h_font']}', sans-serif; font-weight: {data['h_weight']}; letter-spacing: {data['ls']}; text-transform: uppercase; line-height: 1.05; }}
.hero-title {{ font-size: clamp(2rem, 9vw, 115px); text-shadow: 0 5px 25px rgba(0,0,0,0.4); }}
.btn-accent {{ background: var(--s); color: white !important; padding: 1.2rem 3rem; border-radius: var(--radius); font-weight: 900; transition: 0.4s; display: inline-block; text-align: center; box-shadow: 0 15px 30px -10px var(--s); text-decoration:none; cursor: pointer; text-transform: uppercase; letter-spacing: 0.1em; }}
.btn-accent:hover {{ transform: translateY(-5px); filter: brightness(1.1); box-shadow: 0 25px 40px -10px var(--s); }}
.glass-nav {{ background: rgba(255, 255, 255, 0.98); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(0,0,0,0.05); width: 100%; position: fixed; top: 0; z-index: 9999; }}
.hero-mask {{ background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.5)), url('{data['img_h']}'); background-size: cover; background-position: center; min-height: 95vh; display: flex; align-items: center; justify-content: center; padding-top: 100px; }}
.product-card {{ background: white; border-radius: var(--radius); padding: 2.5rem; border: 1px solid #f1f5f9; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.08); transition: 0.4s; cursor: pointer; }}
.product-card:hover {{ transform: scale(1.03); shadow: 0 30px 60px rgba(0,0,0,0.12); }}
.wa-float {{ position: fixed; bottom: 30px; right: 30px; background: #25d366; color: white; width: 65px; height: 65px; border-radius: 50px; display: flex; align-items: center; justify-content: center; z-index: 99999; box-shadow: 0 15px 30px rgba(37,211,102,0.4); }}
.legal-text {{ white-space: pre-wrap; font-size: 1.15rem; color: #475569; }}
"""

def generate_master_page(content_html, is_home=False):
    v_tag = f'<meta name="google-site-verification" content="{data["gsc"]}">' if (is_home and data["gsc"]) else ""
    
    # --- PIPE-BASED DYNAMIC SCRIPT (v21.0 Stability) ---
    dyn_script = ""
    if is_home and sheet_url:
        dyn_script = f"""
        <script>
        let currentProducts = [];
        async function fetchLiveData() {{
            try {{
                const response = await fetch('{sheet_url}');
                const csv = await response.text();
                const rows = csv.split('\\n').map(row => row.split('|')).slice(1);
                const container = document.getElementById('live-data-container');
                container.innerHTML = "";
                rows.forEach((parts, idx) => {{
                    if (parts.length >= 2) {{
                        const p = {{ id: idx, name: parts[0].trim(), price: parts[1].trim(), desc: (parts[2] || "").trim(), img1: (parts[3] || "{data['img_f']}").trim() }};
                        currentProducts.push(p);
                        container.innerHTML += `
                        <div onclick="openProduct(${{idx}})" class="product-card flex flex-col justify-between">
                            <img src="${{p.img1}}" class="w-full h-64 object-cover mb-8 rounded-[2rem] bg-slate-50">
                            <div>
                                <h3 class="text-2xl font-black mb-2 uppercase" style="color:var(--p)">${{p.name}}</h3>
                                <p class="font-black text-3xl mb-6" style="color:var(--s)">${{p.price}}</p>
                                <p class="text-slate-400 text-xs font-bold uppercase tracking-widest italic underline decoration-slate-100 underline-offset-8">Specifications →</p>
                            </div>
                        </div>`;
                    }}
                }});
            }} catch (e) {{ console.log("Fail"); }}
        }}
        function openProduct(id) {{
            const p = currentProducts[id];
            document.getElementById('m-title').innerText = p.name;
            document.getElementById('m-price').innerText = p.price;
            document.getElementById('m-desc').innerText = p.desc;
            document.getElementById('m-img-1').src = p.img1;
            document.getElementById('m-wa').href = "https://wa.me/{wa_clean}?text=" + encodeURIComponent("I am interested in " + p.name + " (" + p.price + ")");
            document.getElementById('modal').style.display = 'flex';
        }}
        window.onload = fetchLiveData;
        </script>
        """

    logo_h = f'<img src="{data["biz_logo"]}" alt="{data["biz_name"]}" class="h-12 w-auto object-contain">' if data["biz_logo"] else f'<span class="text-3xl font-black tracking-tighter uppercase" style="color:var(--p)">{data["biz_name"]}</span>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    {v_tag}<title>{data['biz_name']} | Official Verified Site</title>
    <meta name="description" content="{data['seo_d']}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={data['h_font'].replace(' ', '+')}:wght@700;900&family={data['b_font'].replace(' ', '+')}:wght@400;700&display=swap" rel="stylesheet">
    <style>{master_css}</style>
</head>
<body class="bg-white">
    <nav class="glass-nav p-6"><div class="max-w-[1440px] mx-auto flex justify-between items-center">
        <a href="index.html" class="no-underline">{logo_h}</a>
        <div class="hidden md:flex space-x-12 text-[11px] font-black uppercase tracking-widest text-slate-600">
            <a href="index.html" class="hover:text-blue-600 no-underline">Home</a> 
            <a href="about.html" class="hover:text-blue-600 no-underline">About</a> 
            <a href="contact.html" class="hover:text-blue-600 no-underline">Contact</a>
        </div>
        <a href="tel:{data['biz_phone']}" class="btn-accent" style="padding: 0.6rem 2rem; font-size: 11px;">CALL NOW</a>
    </div></nav>
    <main class="flex-grow pt-24 md:pt-0">{content_html}</main>
    <div id="modal" onclick="if(event.target == this) this.style.display='none'">
        <div class="modal-content shadow-2xl grid md:grid-cols-2">
            <div class="p-6 bg-slate-50 flex items-center justify-center"><img id="m-img-1" class="w-full h-auto rounded-[3rem] shadow-2xl border-4 border-white"></div>
            <div class="p-16 flex flex-col justify-center text-left">
                <h2 id="m-title" class="text-5xl font-black mb-4 uppercase" style="color:var(--p)"></h2>
                <p id="m-price" class="text-4xl font-black mb-8" style="color:var(--s)"></p>
                <p id="m-desc" class="text-slate-600 mb-12 text-xl leading-relaxed"></p>
                <a id="m-wa" href="#" target="_blank" class="btn-accent w-full text-lg py-5">CONFIRM INQUIRY</a>
            </div>
        </div>
    </div>
    <a href="https://wa.me/{wa_clean}" class="wa-float" target="_blank"><svg style="width:38px;height:38px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></svg></a>
    <footer class="bg-slate-950 text-slate-500 py-32 px-10 border-t border-slate-900"><div class="max-w-[1440px] mx-auto grid md:grid-cols-4 gap-16">
    <div class="col-span-2"><h4 class="text-white text-4xl font-black mb-8 uppercase tracking-tighter leading-none">{data['biz_name']}</h4><p class="text-lg opacity-60 mb-10">{data['biz_addr']}</p>
    <p class="text-[10px] font-black uppercase opacity-20 tracking-widest italic">Built by <a href="https://www.kaydiemscriptlab.com" class="text-white underline">Kaydiem Script Lab</a></p></div>
    <div><h4 class="text-white font-bold mb-8 uppercase text-xs tracking-widest underline decoration-blue-600 decoration-4 underline-offset-8">Corporate</h4><ul class="space-y-4 text-sm font-bold uppercase list-none p-0"><li><a href="privacy.html" class="no-underline">Privacy</a></li><li><a href="terms.html" class="no-underline">Terms</a></li></ul></div>
    <div class="md:text-right"><h4 class="text-white font-bold mb-8 uppercase text-xs tracking-widest">Authority Hub</h4><p class="text-2xl font-black text-white">{data['biz_phone']}</p><p class="text-sm mt-2">{data['biz_email']}</p></div></div></footer>{dyn_script}
</body></html>"""

# --- 5. STRUCTURAL CONTENT BUILDER (THE 10 DNAs) ---
s_cards = "".join([f'<div class="bg-slate-50 p-12 rounded-[3rem] border border-slate-100 shadow-xl hover:scale-[1.03] transition-all"><h3 class="text-2xl font-black mb-4 uppercase" style="color:var(--p)">{s.strip()}</h3><p class="text-slate-500 text-sm font-bold tracking-tight italic">Certified technical solution for {data["biz_cat"]}.</p></div>' for s in data['biz_serv'].splitlines() if s.strip()])
t_cards = "".join([f'<div class="p-10 bg-slate-50 rounded-[4rem] border italic text-xl shadow-inner mb-8" style="color:var(--p)">"{t.split("|")[1].strip()}"<br><span class="font-black not-italic text-sm block mt-6 uppercase tracking-widest" style="color:var(--p)">— {t.split("|")[0].strip()} <span class="text-emerald-500 ml-2">● Verified</span></span></div>' for t in testi.splitlines() if "|" in t])

if layout_dna == "Industrial Titan":
    idx_content = f"""
    <section class="hero-mask px-6 text-center text-white"><div class="max-w-[1200px] mx-auto"><h1 class="hero-title mb-10 uppercase tracking-tighter font-black">{data['hero_h']}</h1><p class="text-lg md:text-3xl font-light mb-16 opacity-90">{data['seo_d']}</p><a href="#inventory" class="btn-accent uppercase tracking-[0.4em] text-sm">Discover Inventory</a></div></section>
    <section class="max-w-[1440px] mx-auto py-32 px-6 grid md:grid-cols-2 gap-24 items-center"><img src="{data['img_f']}" class="shadow-2xl rounded-[var(--radius)]"><div><h2 class="section-title mb-12 uppercase tracking-tighter leading-none">Core Expertise</h2><div class="grid gap-6">{s_cards}</div><a href="about.html" class="btn-p mt-10 no-underline" style="background:var(--p); color:white; padding:1rem 2rem; border-radius:var(--radius);">Our Full Story</a></div></section>
    <section id="inventory" class="py-32 px-6 max-w-[1440px] mx-auto text-center border-t border-slate-100"><h2 class="section-title mb-24 uppercase tracking-tighter">Verified Collection</h2><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-4 gap-12 text-left"></div></section>
    <section class="py-32 px-6 max-w-7xl mx-auto"><div class="grid md:grid-cols-2 gap-24 text-left"><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Success</h2>{t_cards}</div><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Insights</h2>{"".join([f'<details class="mb-6 bg-white p-6 rounded-2xl border cursor-pointer"><summary class="font-bold text-lg uppercase">{f.split("?")[0].strip()}?</summary><p class="mt-4 text-slate-500">{f.split("?")[1].strip()}</p></details>' for f in faqs.splitlines() if "?" in f])}</div></div></section>
    """
elif layout_dna == "Classic Royal":
    idx_content = f"""
    <section class="hero-mask px-6 text-center text-white"><div class="max-w-[1200px] mx-auto"><h1 class="hero-title mb-10 font-serif normal-case italic" style="font-family: 'Playfair Display', serif;">{data['hero_h']}</h1><p class="text-lg md:text-3xl mb-16 italic opacity-80 leading-tight">{data['seo_d']}</p><a href="#inventory" class="btn-accent tracking-widest text-sm">Enter Showroom</a></div></section>
    <section class="bg-white py-40 px-6 text-center border-b"><div class="max-w-5xl mx-auto"><h2 class="section-title mb-20 font-serif normal-case italic tracking-normal">Proven Excellence</h2>{t_cards}</div></section>
    <section id="inventory" class="py-40 px-6 max-w-[1440px] mx-auto text-center"><h2 class="section-title mb-24 font-serif normal-case italic">The Collection</h2><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-3 gap-20"></div></section>
    <section class="p-20 bg-slate-50"><h2 class="section-title mb-20 text-center font-serif normal-case italic">Elite Expertise</h2><div class="grid md:grid-cols-3 gap-16">{s_cards}</div></section>
    """
else: # Bento DNA (Futuristic Grid)
    idx_content = f"""
    <section class="hero-mask px-6 text-center text-white"><h1 class="hero-title mb-10">{data['hero_h']}</h1><a href="#inventory" class="btn-accent shadow-2xl">Access Data Hub</a></section>
    <section class="p-10 max-w-[1440px] mx-auto grid md:grid-cols-4 gap-8">
        <div class="md:col-span-2 bg-slate-900 p-20 rounded-[4rem] text-white flex flex-col justify-center shadow-2xl"><h2 class="text-7xl font-black mb-8 tracking-tighter uppercase leading-none">Authority<br>Heritage</h2><p class="text-2xl opacity-60 mb-10 italic">"Transforming industrial and luxury landscapes since inception."</p><a href="about.html" class="btn-p w-fit" style="background:var(--p); color:white; padding:1rem 2rem; border-radius:var(--radius);">Read History</a></div>
        <div class="bg-slate-50 p-12 rounded-[4rem] border shadow-xl flex flex-col justify-center"><p class="text-xs uppercase font-black tracking-widest opacity-30 mb-4">Direct Contact</p><p class="text-4xl font-black leading-none mb-10" style="color:var(--p)">{data['biz_phone']}</p><a href="tel:{data['biz_phone']}" class="btn-accent w-full text-xs">Voice Connect</a></div>
        <div class="md:col-span-1 bg-brand rounded-[4rem] overflow-hidden" style="background-color:var(--p)"><img src="{data['img_f']}" class="w-full h-full object-cover opacity-50"></div>
    </section>
    <section id="inventory" class="py-40 px-6 max-w-[1440px] mx-auto text-center border-t border-slate-100"><h2 class="section-title mb-24 uppercase tracking-tighter">Exclusive Offers</h2><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-4 gap-12 text-left"></div></section>
    <section class="p-20"><div class="grid md:grid-cols-3 gap-10">{s_cards}</div></section>
    """

# --- 6. PREVIEW & ZIP PACKAGING ---
st.header("⚡ Live 2026 Sovereign Preview")
preview_html = generate_master_page(idx_content, True)

if st.toggle("Show Real-Time Layout Preview"):
    st.components.v1.html(preview_html, height=800, scrolling=True)

if st.button("🚀 DEPLOY & DOWNLOAD WORLD-CLASS ASSET"):
    z_b = io.BytesIO()
    with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as z_f:
        z_f.writestr("index.html", preview_html)
        z_f.writestr("about.html", generate_master_page(f"<section class='max-w-7xl mx-auto py-40 px-10'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>About Our Heritage</h1><div class='text-xl md:text-2xl leading-relaxed text-slate-700 legal-text'>{data['about_txt']}</div><img src='{data['img_g']}' class='mt-20 w-full h-[600px] object-cover shadow-2xl' style='border-radius: var(--radius)'></section>"))
        z_f.writestr("contact.html", generate_master_page(f"<section class='max-w-[1440px] mx-auto py-40 px-6 text-center'><h1 class='legal-bold-title uppercase tracking-tighter'>Technical Hub</h1><div class='grid md:grid-cols-2 gap-20 text-left'><div class='bg-slate-950 p-24 text-white' style='border-radius: var(--radius)'><p class='text-4xl font-black mb-8'>{data['biz_phone']}</p><p class='text-2xl mb-12 opacity-80'>{data['biz_addr']}</p><a href='tel:{data['biz_phone']}' class='btn-accent w-full no-underline uppercase tracking-widest font-black'>Book Now</a></div><div class='rounded-[3rem] overflow-hidden border shadow-2xl bg-slate-100' style='min-height:400px'>{data['map_iframe']}</div></div></section>"))
        z_f.writestr("privacy.html", generate_master_page(f"<div class='max-w-4xl mx-auto py-40 px-10'><h1 class='legal-bold-title uppercase'>Privacy Policy</h1><div class='text-lg legal-text'>{priv_body_input}</div></div>"))
        z_f.writestr("terms.html", generate_master_page(f"<div class='max-w-4xl mx-auto py-40 px-10'><h1 class='legal-bold-title uppercase'>Terms</h1><div class='text-lg legal-text'>{terms_body_input}</div></div>"))
        z_f.writestr("404.html", generate_master_page(f"<div class='py-80 text-center'><h1 class='text-[200px] font-black leading-none opacity-5 tracking-widest'>404</h1><p class='text-2xl font-black uppercase tracking-[1em] -mt-20'>Page Not Found</p><a href='index.html' class='btn-accent mt-20'>Return to Home</a></div>"))
        z_f.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {data['prod_url']}sitemap.xml")
        z_f.writestr("sitemap.xml", f"<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'><url><loc>{data['prod_url']}index.html</loc></url></urlset>")

    st.success("💎 TITAN SOVEREIGN v21.0 READY.")
    st.download_button("📥 DOWNLOAD PLATINUM ASSET", z_b.getvalue(), f"{data['biz_name'].lower().replace(' ', '_')}_final.zip")
