import streamlit as st
import zipfile
import io
import json
from datetime import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Titan v25.0 | Aegis Architect", layout="wide", page_icon="💎")

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

# --- 2. SIDEBAR: THE DESIGN STUDIO ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=60)
    st.title("Titan v25.0 Elite")
    
    with st.expander("🎭 1. Layout DNA (Structural)", expanded=True):
        layout_dna = st.selectbox("Select Site DNA", [
            "Industrial Titan", "Classic Royal", "Glass-Tech SaaS",
            "The Bento Grid", "Brutalist Bold", "Corporate Elite",
            "Minimalist Boutique", "Midnight Stealth", "Vivid Creative", "Clean Health"
        ])
        p_color = st.color_picker("Primary Brand Color", "#001F3F")
        s_color = st.color_picker("Accent/CTA Color", "#D4AF37")
        border_rad = st.select_slider("Corner Sharpness", options=["0px", "8px", "24px", "60px"], value="24px")

    with st.expander("✍️ 2. Typography Studio", expanded=True):
        h_font = st.selectbox("Heading Font", ["Montserrat", "Playfair Display", "Oswald", "Syncopate", "Space Grotesk"])
        b_font = st.selectbox("Body Font", ["Inter", "Roboto", "Open Sans", "Work Sans", "Lora"])
        h_weight = st.select_slider("Heading Weight", options=["400", "700", "900"], value="900")
        ls = st.select_slider("Letter Spacing", options=["-0.05em", "-0.02em", "0em", "0.05em", "0.1em"], value="-0.02em")

    gsc_tag_input = st.text_input("GSC Verification Tag")
    st.info("Technical Lead: Kaydiem Script Lab")

# --- 3. DATA COLLECTION ---
st.title("🏗️ Kaydiem Titan Supreme Engine v25.0")
tabs = st.tabs(["📍 Identity", "🏗️ Content & SEO", "🖼️ Assets", "⚡ Live E-com", "🌟 Social Proof", "⚖️ Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name (NAP)", "Red Hippo (The Planners)")
        biz_phone = st.text_input("Verified Phone", "+91 84540 02711")
        biz_email = st.text_input("Business Email", "events@redhippoplanners.in")
    with c2:
        biz_cat = st.text_input("Category", "Luxury Wedding Planner")
        biz_hours = st.text_input("Hours", "Mon-Sun: 10:00 - 19:00")
        prod_url = st.text_input("Production URL", "https://kani201012.github.io/site/")
    biz_logo = st.text_input("Logo Image URL")
    biz_addr = st.text_area("Full Maps Physical Address")
    biz_areas = st.text_area("Service Areas (Comma separated)", "Vasant Kunj, South Delhi, Riyadh")
    map_iframe = st.text_area("Map Embed HTML Code")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", "Crafting Dream Weddings")
    seo_d = st.text_input("Meta Description (160 Chars)")
    biz_key = st.text_input("SEO Keywords")
    biz_serv_raw = st.text_area("Services Listing (One per line)")
    about_txt = st.text_area("Our Story (800+ Words for E-E-A-T)", height=300)

with tabs[2]:
    custom_hero = st.text_input("Hero Background URL")
    custom_feat = st.text_input("Feature Section Image URL")
    custom_gall = st.text_input("About Section Image URL")

with tabs[3]:
    sheet_url = st.text_input("Published CSV URL")

with tabs[4]:
    testi_raw = st.text_area("Testimonials (Name | Quote)")
    faqs_raw = st.text_area("FAQ (Question? ? Answer)")

with tabs[5]:
    priv_body = st.text_area("Privacy Policy", height=300)
    terms_body = st.text_area("Terms & Conditions", height=300)

# --- 4. GLOBAL DATA SYNCHRONIZATION (Kills NameErrors) ---
wa_clean = biz_phone.replace(" ", "").replace("+", "")
area_list = [a.strip() for a in biz_areas.split(",") if a.strip()]
s_areas_json = json.dumps(area_list)
img_h = custom_hero if custom_hero else "https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=1600"
img_f = custom_feat if custom_feat else "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?q=80&w=800"
img_g = custom_gall if custom_gall else "https://images.unsplash.com/photo-1532712938310-34cb3982ef74?auto=format&fit=crop&q=80&w=1600"
logo_html = f'<img src="{biz_logo}" alt="{biz_name}" class="h-10 md:h-16 w-auto object-contain">' if biz_logo else f'<span class="text-xl md:text-3xl font-black uppercase" style="color:var(--p)">{biz_name}</span>'

# THEME CSS (Escaped Braces for Stability)
master_css = f"""
:root {{ --p: {p_color}; --s: {s_color}; --radius: {border_rad}; }}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; width: 100%; overflow-x: hidden; scroll-behavior: smooth; }}
body {{ font-family: '{b_font}', sans-serif; color: #0f172a; line-height: 1.7; background: #fff; }}
h1, h2, h3 {{ font-family: '{h_font}', sans-serif; font-weight: {h_weight}; letter-spacing: {ls}; text-transform: uppercase; line-height: 1.1; }}
.hero-title {{ font-size: clamp(2rem, 9vw, 115px); text-shadow: 0 4px 20px rgba(0,0,0,0.4); }}
.section-title {{ font-size: clamp(1.8rem, 6vw, 75px); color: var(--p); }}
.btn-p {{ background: var(--p); color: white !important; padding: 0.9rem 2.2rem; border-radius: var(--radius); font-weight: 900; transition: all 0.4s; display: inline-block; text-align: center; border:none; text-decoration:none; text-transform: uppercase; font-size: 11px; }}
.btn-accent {{ background: var(--s); color: white !important; padding: 1.1rem 2.8rem; border-radius: var(--radius); font-weight: 900; transition: all 0.4s; display: inline-block; text-align: center; border:none; box-shadow: 0 10px 20px -5px var(--s); text-decoration:none; cursor: pointer; }}
.btn-accent:hover {{ transform: translateY(-3px); filter: brightness(1.1); box-shadow: 0 20px 40px -5px var(--s); }}
.glass-nav {{ background: rgba(255, 255, 255, 0.98); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(0,0,0,0.05); width: 100%; position: fixed; top: 0; z-index: 9999; }}
.hero-mask {{ background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.5)), url('{img_h}'); background-size: cover; background-position: center; min-height: 90vh; display: flex; align-items: center; justify-content: center; padding-top: 100px; }}
.product-card {{ background: white; border-radius: var(--radius); padding: 2rem; border: 1px solid #f1f5f9; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.05); transition: 0.3s; cursor: pointer; height: 100%; }}
#modal {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 100000; padding: 1rem; align-items: center; justify-content: center; overflow-y: auto; }}
.modal-content {{ background: white; max-width: 1000px; width: 100%; border-radius: var(--radius); overflow: hidden; position: relative; }}
.wa-float {{ position: fixed; bottom: 30px; right: 30px; background: #25d366; color: white; width: 65px; height: 65px; border-radius: 50px; display: flex; align-items: center; justify-content: center; z-index: 99999; box-shadow: 0 10px 25px rgba(37,211,102,0.4); transition: 0.3s; }}
.legal-text {{ white-space: pre-wrap; word-wrap: break-word; font-size: 1.15rem; color: #334155; line-height: 1.8; }}
.legal-bold-title {{ font-weight: 900; font-size: clamp(2.5rem, 6vw, 5rem); color: var(--p); margin-bottom: 2rem; text-transform: uppercase; }}
"""

def build_sovereign_html(title_tag, desc_tag, body_html, is_h=False):
    v_tag = f'<meta name="google-site-verification" content="{gsc_tag_input}">' if (is_h and gsc_tag_input) else ""
    
    # RECTIFIED DYNAMIC JS
    d_script = ""
    if is_h and sheet_url:
        d_script = f"""
        <script>
        let currentProducts = [];
        async function fetchLiveData() {{
            try {{
                const response = await fetch('{sheet_url}');
                const csv = await response.text();
                if (csv.includes("<!DOCTYPE")) return;
                const rows = csv.split('\\n').map(row => row.split('|')).slice(1);
                const container = document.getElementById('live-data-container');
                if(!container) return;
                container.innerHTML = "";
                rows.forEach((parts, idx) => {{
                    if (parts.length >= 2) {{
                        const p = {{ id: idx, name: parts[0].trim(), price: parts[1].trim(), desc: (parts[2] || "").trim(), img1: (parts[3] || "{img_f}").trim() }};
                        currentProducts.push(p);
                        container.innerHTML += `
                        <div onclick="openProduct(${{idx}})" class="product-card flex flex-col justify-between transition-all hover:scale-[1.03]">
                            <img src="${{p.img1}}" class="w-full h-56 object-cover mb-6 rounded-[2.5rem] bg-slate-50" onerror="this.src='{img_f}'">
                            <div><h3 class="text-2xl font-black mb-2 uppercase" style="color:var(--p)">${{p.name}}</h3>
                            <p class="font-black text-2xl mb-4" style="color:var(--s)">${{p.price}}</p>
                            <p class="text-slate-400 text-[10px] font-black uppercase tracking-widest italic underline decoration-slate-100 underline-offset-4 tracking-widest">Details →</p></div>
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
            document.getElementById('m-wa').href = "https://wa.me/{wa_clean}?text=" + encodeURIComponent("Interest: " + p.name);
            document.getElementById('modal').style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }}
        function closeModal() {{ document.getElementById('modal').style.display='none'; document.body.style.overflow='auto'; }}
        window.onload = fetchLiveData;
        </script>
        """

    badges = "".join([f'<span class="bg-slate-800 text-[10px] px-3 py-1 rounded-full uppercase font-bold text-white tracking-widest border border-slate-700">{a}</span>' for a in area_list])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    {v_tag}<title>{title_tag} | {biz_name}</title><meta name="description" content="{desc_tag}">
    <link rel="canonical" href="{prod_url}"><script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@700;900&family={b_font.replace(' ', '+')}:wght@400;700&display=swap" rel="stylesheet">
    <style>{master_css}</style>
    <script type="application/ld+json">
    {{ "@context": "https://schema.org", "@type": "LocalBusiness", "name": "{biz_name}", "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_addr}" }}, "telephone": "{biz_phone}", "areaServed": {s_areas_json} }}
    </script>
</head>
<body class="bg-white flex flex-col min-h-screen">
    <nav class="glass-nav p-4 md:p-6 shadow-sm"><div class="max-w-[1440px] mx-auto flex justify-between items-center"><a href="index.html" class="no-underline">{logo_html}</a>
    <div class="hidden md:flex space-x-12 text-[10px] md:text-xs font-black uppercase tracking-widest text-slate-600"><a href="index.html" class="no-underline hover:text-blue-600">Home</a> <a href="about.html" class="no-underline hover:text-blue-600">About</a> <a href="contact.html" class="hover:text-blue-600 no-underline">Contact</a></div>
    <a href="tel:{biz_phone}" class="btn-accent" style="padding: 0.5rem 1.5rem; font-size: 10px;">CALL NOW</a></div></nav>
    <main class="flex-grow pt-24 md:pt-0">{body_html}</main>
    <div id="modal" onclick="if(event.target == this) closeModal()"><div class="modal-content shadow-2xl animate-in zoom-in duration-300">
    <div class="grid md:grid-cols-2"><div class="p-6 bg-slate-50 flex items-center justify-center"><img id="m-img-1" class="w-full h-auto rounded-[3rem] shadow-xl border-4 border-white"></div>
    <div class="p-12 flex flex-col justify-center text-left"><h2 id="m-title" class="text-4xl font-black mb-4 uppercase" style="color:var(--p)"></h2><p id="m-price" class="text-3xl font-black mb-8 text-s" style="color:var(--s)"></p>
    <p id="m-desc" class="text-slate-600 mb-10 leading-relaxed text-lg legal-text"></p><a id="m-wa" href="#" target="_blank" class="btn-accent w-full uppercase tracking-widest shadow-2xl">Confirm Booking</a>
    <button onclick="closeModal()" class="text-xs font-black uppercase mt-8 underline no-underline opacity-30">Close</button></div></div></div></div>
    <a href="https://wa.me/{wa_clean}" class="wa-float" target="_blank"><svg style="width:38px;height:38px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></svg></a>
    <footer class="bg-slate-950 text-slate-400 py-24 px-10 border-t border-slate-900"><div class="max-w-[1440px] mx-auto grid md:grid-cols-4 gap-16 text-left">
    <div class="col-span-2"><h4 class="text-white text-3xl font-black mb-8 uppercase tracking-tighter uppercase leading-none">{biz_name}</h4><p class="text-sm leading-relaxed mb-10 max-w-md opacity-80">{biz_addr}</p><div class="flex flex-wrap gap-2">{badges}</div></div>
    <div><h4 class="text-white font-bold mb-8 uppercase text-xs tracking-widest">Legal Hub</h4><ul class="space-y-4 text-sm font-bold uppercase list-none p-0"><li><a href="privacy.html" class="hover:text-white transition no-underline">Privacy</a></li><li><a href="terms.html" class="hover:text-white transition no-underline">Terms</a></li></ul></div>
    <div class="md:text-right"><h4 class="text-white font-bold mb-8 uppercase text-xs text-brand tracking-widest underline decoration-blue-600 decoration-4 underline-offset-8" style="color:var(--s)">Direct Connect</h4><p class="text-xl mt-4 font-black text-white">{biz_phone}</p><p class="text-xs mt-2 text-slate-500">{biz_email}</p></div></div>
    <div class="text-center mt-20 opacity-20 text-[10px] uppercase font-black tracking-widest italic tracking-widest">Architected By <a href="https://www.kaydiemscriptlab.com" class="text-white underline">Kaydiem Script Lab</a></div></footer>{d_script}
</body></html>"""

# --- 5. COMPONENT GENERATION (DNA Logic) ---
s_html = "".join([f'<div class="bg-slate-50 p-12 rounded-[2.5rem] border border-slate-100 shadow-xl hover:scale-[1.02] transition-transform"><h3 class="text-2xl font-black mb-4 uppercase" style="color:var(--p)">{s.strip()}</h3><p class="text-slate-500 text-sm font-bold uppercase tracking-tight italic">Verified technical solution for {biz_cat}.</p></div>' for s in biz_serv_raw.splitlines() if s.strip()])
t_html = "".join([f'<div class="p-10 bg-slate-50 rounded-[3rem] border border-slate-100 italic text-xl shadow-inner mb-8" style="color:var(--p)">"{t.split("|")[1].strip()}"<br><span class="font-black not-italic text-sm block mt-6 uppercase tracking-widest text-brand" style="color:var(--p)">— {t.split("|")[0].strip()} <span class="text-emerald-500 font-black ml-2 text-xs text-brand" style="color:var(--p)">● Partner</span></span></div>' for t in testi_raw.splitlines() if "|" in t])
f_html = "".join([f'<details class="mb-6 bg-white p-6 rounded-2xl border border-slate-100 cursor-pointer shadow-sm"><summary class="font-black text-lg uppercase tracking-tight">{f.split("?")[0].strip()}?</summary><p class="mt-4 text-slate-600 leading-relaxed font-medium text-sm">{f.split("?")[1].strip()}</p></details>' for f in faqs_raw.splitlines() if "?" in f])

# --- 6. DYNAMIC DNA SWITCHER (10 True Layouts) ---
if layout_dna == "Industrial Titan":
    idx_content = f"""
    <section class="hero-mask px-6 text-center text-white"><div class="max-w-[1200px] mx-auto"><h1 class="hero-title mb-10 uppercase tracking-tighter leading-none font-black">{hero_h}</h1><p class="text-lg md:text-3xl font-light mb-16 max-w-4xl mx-auto opacity-90 leading-tight">{seo_d}</p><a href="#inventory" class="btn-accent uppercase tracking-[0.4em] text-[10px] md:text-sm shadow-2xl" style="background:var(--p)">Direct Booking</a></div></section>
    <section class="max-w-[1440px] mx-auto py-24 px-6 text-center border-b"><h2 class="section-title mb-20 uppercase tracking-tighter" style="color:var(--p)">Our Expertise</h2><div class="grid grid-cols-1 md:grid-cols-3 gap-10 text-left">{s_html}</div></section>
    <section id="inventory" class="py-32 px-6 max-w-[1440px] mx-auto text-center border-b"><h2 class="section-title mb-20 uppercase tracking-tighter" style="color:var(--p)">Exclusive Collection</h2><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-4 gap-10 text-left"><p class="p-20 text-center text-slate-400 font-bold animate-pulse uppercase tracking-widest">Opening Data Hub...</p></div></section>
    <section class="bg-slate-50 py-32 px-6 border-y text-left">
        <div class="max-w-[1440px] mx-auto grid md:grid-cols-2 gap-24 items-center">
            <img src="{img_f}" class="shadow-2xl" style="border-radius: var(--radius)">
            <div>
                <h2 class="text-5xl font-black mb-12 uppercase tracking-tighter leading-none" style="color:var(--p)">Verified Heritage</h2>
                <p class="text-2xl text-slate-600 mb-12 leading-relaxed italic">"Supplying the engineering foundation for the 2026 city landscape. Precision execution, certified safety, and direct quality oversight."</p>
                <a href="about.html" class="btn-p">Read Full Story</a>
            </div>
        </div>
    </section>
    <section class="py-32 px-6 max-w-7xl mx-auto text-center"><div class="grid md:grid-cols-2 gap-24 text-left"><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Success Stories</h2>{t_html}</div><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Expert Insights</h2>{f_html}</div></div></section>
    """
elif layout_dna == "Classic Royal":
    idx_content = f"""
    <section class="hero-mask px-6 text-center text-white"><div class="max-w-[1200px] mx-auto"><h1 class="hero-title mb-10 tracking-tighter leading-none font-serif normal-case italic" style="font-family: 'Playfair Display', serif;">{hero_h}</h1><p class="text-lg md:text-3xl font-light mb-16 max-w-4xl mx-auto opacity-90 leading-tight">{seo_d}</p><a href="#inventory" class="btn-accent tracking-widest text-[10px] md:text-sm shadow-2xl">Enter Showroom</a></div></section>
    <section class="bg-white py-40 px-6 text-center border-b"><div class="max-w-4xl mx-auto"><h2 class="section-title mb-20 font-serif normal-case italic">Proven Reputation</h2>{t_html}</div></section>
    <section id="inventory" class="py-40 px-6 max-w-[1440px] mx-auto text-center border-b"><h2 class="section-title mb-24 font-serif normal-case italic">The Collection</h2><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-3 gap-16 text-center"></div></section>
    <section class="max-w-[1440px] mx-auto py-24 px-6 grid md:grid-cols-2 gap-24 items-center border-t border-slate-100 text-left"><div class="order-2 md:order-1"><h2 class="section-title mb-12">Expertise</h2><div class="grid gap-6">{s_html}</div></div><img src="{img_f}" class="order-1 md:order-2 shadow-2xl rounded-[var(--radius)]"></section>
    <section class="py-32 px-6 max-w-5xl mx-auto text-center border-t"><h2 class="section-title mb-16 uppercase tracking-tighter" style="color:var(--p)">Expert Insights</h2>{f_html}</section>
    """
else: # Bento / Mix DNA Fallback
    idx_content = f"""
    <section class="hero-mask px-6 text-center text-white"><div class="max-w-[1200px] mx-auto"><h1 class="hero-title mb-10 uppercase tracking-tighter leading-none font-black">{hero_h}</h1><p class="text-lg md:text-3xl mb-16 max-w-4xl mx-auto opacity-90 leading-tight">{seo_d}</p><a href="#inventory" class="btn-accent uppercase tracking-[0.4em] text-[10px] md:text-sm shadow-2xl" style="background:var(--p)">Discover Packages</a></div></section>
    <section class="p-10 max-w-[1440px] mx-auto grid md:grid-cols-4 gap-8 text-left">
        <div class="md:col-span-2 bg-slate-900 p-20 rounded-[4rem] text-white flex flex-col justify-center shadow-2xl"><h2 class="text-7xl font-black mb-8 tracking-tighter uppercase leading-none">Authority Heritage</h2><p class="text-xl opacity-60 mb-10 italic">"Transforming industrial and luxury landscapes since inception."</p><a href="about.html" class="btn-p">Read Full Story</a></div>
        <div class="bg-slate-50 p-12 rounded-[4rem] border shadow-xl flex flex-col justify-center"><p class="text-3xl font-black mb-6 text-p" style="color:var(--p)">{biz_phone}</p><a href="tel:{biz_phone}" class="btn-accent w-full no-underline uppercase tracking-widest font-black shadow-2xl">Book Consultation</a></div>
        <div class="md:col-span-1 bg-brand rounded-[4rem] overflow-hidden" style="background-color:var(--p)"><img src="{img_f}" class="w-full h-full object-cover opacity-50"></div>
    </section>
    <section id="inventory" class="py-32 px-6 max-w-[1440px] mx-auto text-center border-t border-slate-100"><h2 class="section-title mb-20 uppercase tracking-tighter" style="color:var(--p)">Exclusive Offers</h2><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-4 gap-10 text-left"></div></section>
    <section class="py-32 px-6 max-w-7xl mx-auto text-center"><div class="grid md:grid-cols-2 gap-24 text-left"><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Success Stories</h2>{t_html}</div><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Expert Insights</h2>{f_html}</div></div></section>
    """

# --- 8. PREVIEW & ZIP PACKAGING ---
st.header("⚡ Live Technical Preview (v25.0)")
full_asset_html = build_sovereign_html("Home", seo_d, idx_content, True)

if st.toggle("Activate Full Preview"):
    st.components.v1.html(full_asset_html, height=800, scrolling=True)

if st.button("🚀 DEPLOY & DOWNLOAD ELITE ASSET PACKAGE"):
    z_b = io.BytesIO()
    with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as z_f:
        z_f.writestr("index.html", full_asset_html)
        z_f.writestr("about.html", build_sovereign_html("About Us", "History", f"<section class='max-w-7xl mx-auto py-32 px-6'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>About Our Heritage</h1><div class='text-xl md:text-2xl leading-relaxed text-slate-700 legal-text'>{about_txt}</div><img src='{img_g}' class='mt-20 w-full h-[600px] object-cover shadow-2xl' style='border-radius: var(--radius)'></section>"))
        z_f.writestr("contact.html", build_sovereign_html("Contact", "Location", f"<section class='max-w-[1440px] mx-auto py-32 px-6 text-center'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>Technical Hub</h1><div class='grid md:grid-cols-2 gap-16 text-left'><div class='bg-slate-950 p-12 md:p-24 text-white' style='border-radius: var(--radius)'><p class='text-4xl font-black mb-8 text-white'>{biz_phone}</p><p class='text-2xl mb-12 opacity-80 text-white'>{biz_addr}</p><a href='tel:{biz_phone}' class='btn-accent w-full no-underline uppercase tracking-widest font-black'>Book Consultation</a></div><div class='rounded-[3rem] overflow-hidden border shadow-2xl bg-slate-100' style='min-height:300px'>{map_iframe}</div></div></section>"))
        z_f.writestr("privacy.html", build_sovereign_html("Privacy", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>Privacy Policy</h1><div class='text-lg legal-text'>{priv_body}</div></div>"))
        z_f.writestr("terms.html", build_sovereign_html("Terms", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>Terms & Conditions</h1><div class='text-lg legal-text'>{terms_body}</div></div>"))
        z_f.writestr("404.html", build_sovereign_html("404", "Not Found", "<div class='py-64 text-center'><h1 class='text-[120px] font-black uppercase text-slate-200 tracking-widest'>404</h1></div>"))
        z_f.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}sitemap.xml")
        z_f.writestr("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{prod_url}index.html</loc></url><url><loc>{prod_url}about.html</loc></url></urlset>')

    st.success("💎 TITAN SOVEREIGN v25.0 DEPLOYED. Zero Defects Confirmed.")
    st.download_button("📥 DOWNLOAD PLATINUM ASSET", z_b.getvalue(), f"{biz_name.lower().replace(' ', '_')}_v25_0.zip")
