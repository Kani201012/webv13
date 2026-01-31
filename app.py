import streamlit as st
import zipfile
import io
import json
from datetime import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Titan v15.2 | Elite Architect", layout="wide", page_icon="💎")

st.markdown("""
    <style>
    .main { background: #020617; color: white; }
    .stTabs [data-baseweb="tab"] { color: white; font-weight: bold; font-size: 1.1rem; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4.5em; 
        background: linear-gradient(135deg, #1e293b 0%, #2563eb 100%); 
        color: white; font-weight: 900; border: none; font-size: 1.4rem;
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: DESIGN STUDIO ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=50)
    st.title("Titan v15.2 Studio")
    
    with st.expander("🎭 1. Layout DNA (Structural)", expanded=True):
        layout_dna = st.selectbox("Select Site Architecture", [
            "Industrial Titan (Rugged)", 
            "Classic Royal (Luxury)", 
            "Glass-Tech (SaaS)",
            "The Bento Grid (Modern)",
            "Brutalist (Bold & Sharp)"
        ])
        p_color = st.color_picker("Primary Color", "#001F3F")
        s_color = st.color_picker("Accent/CTA Color", "#D4AF37")
        border_rad = st.select_slider("Corner Roundness", options=["0px", "12px", "24px", "60px"], value="12px")

    with st.expander("✍️ 2. Typography Studio", expanded=True):
        h_font = st.selectbox("Heading Font", ["Montserrat", "Playfair Display", "Oswald", "Syncopate"])
        b_font = st.selectbox("Body Font", ["Inter", "Roboto", "Open Sans", "Work Sans"])
        h_weight = st.select_slider("Weight", options=["400", "700", "900"], value="900")

    gsc_tag = st.text_input("GSC Verification Tag")
    st.info("Technical Lead: Kaydiem Script Lab")

st.title("🏗️ Kaydiem Titan Supreme v15.2")

# --- 2. MULTI-TAB DATA COLLECTION ---
tabs = st.tabs(["📍 Identity", "🏗️ Content & SEO", "🖼️ Photo Manager", "⚡ Live E-com", "🌟 Social Proof", "⚖️ Legal"])

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
    st.warning("NEW: Engine now handles BOTH Pipe (|) and Comma (,) automatically.")
    sheet_url = st.text_input("Published CSV URL")

with tabs[4]:
    testi = st.text_area("Testimonials (Name | Quote)")
    faqs = st.text_area("FAQ (Question? ? Answer)")

with tabs[5]:
    priv_body = st.text_area("Privacy Policy", height=300)
    terms_body = st.text_area("Terms & Conditions", height=300)

# --- 3. THE SUPREME ENGINE V15.2 ---

if st.button("🚀 DEPLOY 1st CLASS ELITE ARCHITECTURE"):
    
    # SETUP GLOBAL VARIABLES
    wa_clean = biz_phone.replace(" ", "").replace("+", "")
    wa_url = f"https://wa.me/{wa_clean}?text=Hello%20{biz_name.replace(' ', '%20')}"
    area_list = [a.strip() for a in biz_areas.split(",")]
    s_areas_json = json.dumps(area_list)

    img_h = custom_hero if custom_hero else "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&q=80&w=1600"
    img_f = custom_feat if custom_feat else "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&q=80&w=800"
    img_g = custom_gall if custom_gall else "https://images.unsplash.com/photo-1532712938310-34cb3982ef74?auto=format&fit=crop&q=80&w=1600"

    logo_html = f'<img src="{biz_logo}" alt="{biz_name}" class="h-10 md:h-14 w-auto object-contain">' if biz_logo else f'<span class="text-xl md:text-3xl font-black tracking-tighter uppercase" style="color:var(--p)">{biz_name}</span>'

    theme_css = f"""
    :root {{ --p: {p_color}; --s: {s_color}; --radius: {border_rad}; }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; padding: 0; width: 100%; overflow-x: hidden; scroll-behavior: smooth; }}
    body {{ font-family: '{b_font}', sans-serif; color: #0f172a; line-height: 1.7; background: #fff; }}
    h1, h2, h3 {{ font-family: '{h_font}', sans-serif; font-weight: {h_weight}; letter-spacing: -0.02em; text-transform: uppercase; line-height: 1.1; overflow-wrap: break-word; }}
    
    .hero-title {{ font-size: clamp(1.8rem, 8vw, 100px); text-shadow: 0 4px 20px rgba(0,0,0,0.4); line-height: 0.95; }}
    .btn-p {{ background: var(--p); color: white !important; padding: 0.9rem 2.2rem; border-radius: var(--radius); font-weight: 900; display: inline-block; text-align: center; text-decoration:none; text-transform: uppercase; font-size: 11px; }}
    .btn-accent {{ background: var(--s); color: white !important; padding: 1.1rem 2.8rem; border-radius: var(--radius); font-weight: 900; transition: all 0.4s; display: inline-block; text-align: center; border:none; box-shadow: 0 10px 20px -5px var(--s); text-decoration:none; cursor: pointer; }}
    .btn-accent:hover {{ transform: translateY(-3px); filter: brightness(1.1); box-shadow: 0 20px 40px -5px var(--s); }}
    
    .glass-nav {{ background: rgba(255, 255, 255, 0.98); backdrop-filter: blur(15px); border-bottom: 1px solid rgba(0,0,0,0.05); width: 100%; z-index: 9999; position: fixed; top: 0; left: 0; }}
    .hero-mask {{ background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.5)), url('{img_h}'); background-size: cover; background-position: center; min-height: 92vh; display: flex; align-items: center; justify-content: center; width: 100%; margin: 0; padding: 140px 20px 60px 20px; }}
    
    #modal {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 100000; padding: 1rem; align-items: center; justify-content: center; overflow-y: auto; }}
    .modal-content {{ background: white; max-width: 1000px; width: 100%; border-radius: var(--radius); overflow: hidden; position: relative; }}
    .wa-float {{ position: fixed; bottom: 30px; right: 30px; background: #25d366; color: white; width: 65px; height: 65px; border-radius: 50px; display: flex; align-items: center; justify-content: center; z-index: 99999; box-shadow: 0 10px 25px rgba(37,211,102,0.4); transition: 0.3s; }}
    """

    def get_layout(page_title, page_desc, content_body, is_home=False):
        v_tag = f'<meta name="google-site-verification" content="{gsc_tag}">' if (is_home and gsc_tag) else ""
        
        # --- SMART DYNAMIC E-COM PARSER (Handles Pipe and Comma) ---
        dyn_script = ""
        if is_home and sheet_url:
            dyn_script = f"""
            <script>
            let currentProducts = [];
            async function fetchLiveData() {{
                try {{
                    const response = await fetch('{sheet_url}');
                    const csv = await response.text();
                    if (csv.includes("<!DOCTYPE")) return;
                    
                    const rows = csv.split('\\n').slice(1);
                    const container = document.getElementById('live-data-container');
                    container.innerHTML = "";
                    
                    rows.forEach((line, idx) => {{
                        if (!line.trim()) return;
                        // Robust Splitter: Try Pipe first, then Comma
                        let parts = line.split('|');
                        if (parts.length < 2) parts = line.split(',');
                        
                        if (parts.length >= 2) {{
                            const p = {{ id: idx, name: parts[0].trim(), price: parts[1].trim(), desc: (parts[2] || "").trim(), img1: (parts[3] || "{img_f}").trim() }};
                            currentProducts.push(p);
                            container.innerHTML += `
                            <div onclick="openProduct(${{idx}})" class="bg-white p-8 rounded-[2.5rem] border shadow-xl cursor-pointer hover:scale-105 transition-all">
                                <img src="${{p.img1}}" class="w-full h-48 object-cover mb-6 rounded-3xl bg-slate-50" onerror="this.src='{img_f}'">
                                <h3 class="text-xl font-black mb-2 uppercase" style="color:var(--p)">${{p.name}}</h3>
                                <p class="text-blue-600 font-black text-2xl">${{p.price}}</p>
                            </div>`;
                        }
                    }});
                }} catch (e) {{ console.log("Fail"); }}
            }}
            function openProduct(id) {{
                const p = currentProducts[id];
                document.getElementById('m-title').innerText = p.name;
                document.getElementById('m-price').innerText = p.price;
                document.getElementById('m-desc').innerText = p.desc;
                document.getElementById('m-img').src = p.img1;
                document.getElementById('m-wa').href = "https://wa.me/{wa_clean}?text=" + encodeURIComponent("I am interested in " + p.name);
                document.getElementById('modal').style.display = 'flex';
            }}
            window.onload = fetchLiveData;
            </script>
            """

        coverage_badges = "".join([f'<span class="bg-slate-800 text-[10px] px-3 py-1 rounded-full uppercase font-bold text-white tracking-widest border border-slate-700">{a}</span>' for a in area_list])

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    {v_tag}
    <title>{page_title} | {biz_name}</title>
    <meta name="description" content="{page_desc}">
    <link rel="canonical" href="{prod_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@700;900&family={b_font.replace(' ', '+')}:wght@400;700&display=swap" rel="stylesheet">
    <style>{theme_css}</style>
    <script type="application/ld+json">
    {{ "@context": "https://schema.org", "@type": "LocalBusiness", "name": "{biz_name}", "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_addr}" }}, "telephone": "{biz_phone}", "areaServed": {s_areas_json} }}
    </script>
</head>
<body class="bg-white flex flex-col min-h-screen text-slate-900">
    <nav class="glass-nav p-4 md:p-6 shadow-sm">
        <div class="max-w-[1440px] mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
            <a href="index.html" class="no-underline">{logo_html}</a>
            <div class="flex items-center space-x-6 md:space-x-12 text-[10px] md:text-xs font-black uppercase tracking-widest text-slate-600">
                <a href="index.html">Home</a> <a href="about.html">About</a> <a href="contact.html">Contact</a>
                <a href="tel:{biz_phone}" class="btn-accent" style="padding: 0.5rem 1.5rem; font-size: 10px;">CALL NOW</a>
            </div>
        </div>
    </nav>
    <main class="flex-grow pt-24 md:pt-0">{content_body}</main>
    <div id="modal" onclick="if(event.target == this) this.style.display='none'">
        <div class="modal-content shadow-2xl animate-in zoom-in duration-300">
            <div class="grid md:grid-cols-2">
                <img id="m-img" class="w-full h-full object-cover">
                <div class="p-12">
                    <h2 id="m-title" class="text-4xl font-black mb-4 uppercase"></h2>
                    <p id="m-price" class="text-3xl font-black mb-8 text-blue-600"></p>
                    <p id="m-desc" class="text-slate-600 mb-10 leading-relaxed"></p>
                    <a id="m-wa" href="#" target="_blank" class="btn-accent w-full uppercase">Secure Booking</a>
                </div>
            </div>
        </div>
    </div>
    <a href="{wa_url}" class="wa-float" target="_blank"><svg style="width:38px;height:38px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></svg></a>
    <footer class="bg-slate-950 text-slate-400 py-24 px-10 border-t border-slate-900">
        <div class="max-w-[1440px] mx-auto grid md:grid-cols-4 gap-16 text-left">
            <div class="col-span-2">
                <h4 class="text-white text-3xl font-black mb-8 uppercase tracking-tighter uppercase">{biz_name}</h4>
                <p class="text-sm leading-relaxed mb-10 max-w-md opacity-80">{biz_addr}</p>
                <div class="bg-slate-900/50 p-6 border border-slate-800 rounded-3xl">
                    <h5 class="text-white text-[10px] font-black uppercase tracking-widest mb-4 opacity-50">Verified Service Coverage</h5>
                    <div class="flex flex-wrap gap-2">{coverage_badges}</div>
                </div>
                <p class="text-[10px] mt-10 opacity-30 uppercase font-black tracking-widest italic tracking-widest underline decoration-white underline-offset-8 decoration-2 text-white text-decoration-none">Architected By Kaydiem Script Lab</p>
            </div>
            <div><h4 class="text-white font-bold mb-8 uppercase text-xs tracking-widest">Policy Hub</h4><ul class="space-y-4 text-sm font-bold uppercase list-none p-0"><li><a href="privacy.html" class="hover:text-white transition no-underline">Privacy</a></li><li><a href="terms.html" class="hover:text-white transition no-underline">Terms</a></li></ul></div>
            <div><h4 class="text-white font-bold mb-8 uppercase text-xs text-brand tracking-widest" style="color:var(--s)">Direct Connect</h4><p class="text-lg font-bold text-white leading-loose underline decoration-blue-600 decoration-4 underline-offset-8 uppercase tracking-widest">Technical Support</p><p class="text-xl mt-4" style="white-space:nowrap; color:white; font-weight:900;">{biz_phone}</p><p class="text-xs mt-2">{biz_email}</p></div>
        </div>
    </footer>
    {dyn_script}
</body></html>"""

    # --- ARCHITECTURE DNA SWITCH (TRUE LAYOUTS) ---
    if layout_dna == "Industrial Titan (Rugged)":
        idx_content = f"""
        <section class="hero-mask px-6 text-center text-white">
            <div class="max-w-[1200px] mx-auto">
                <h1 class="hero-title mb-10 uppercase tracking-tighter leading-none">{hero_h}</h1>
                <p class="text-lg md:text-3xl font-light mb-16 max-w-4xl mx-auto opacity-90 leading-tight">{seo_d}</p>
                <a href="#inventory" class="btn-accent uppercase tracking-[0.4em] text-[10px] md:text-sm shadow-2xl">Discover Packages</a>
            </div>
        </section>
        <section class="max-w-[1440px] mx-auto py-24 px-6 grid md:grid-cols-2 gap-24 items-center">
            <img src="{img_f}" class="shadow-2xl rounded-[var(--radius)]">
            <div>
                <h2 class="text-5xl font-black mb-12 uppercase tracking-tighter leading-none" style="color:var(--p)">Our Expertise</h2>
                <div class="grid gap-6">{"".join([f'<div class="flex items-center gap-4 bg-slate-50 p-6 rounded-xl border"><span class="text-blue-600 font-bold">✔</span><h3 class="font-bold">{s.strip()}</h3></div>' for s in biz_serv.splitlines()])}</div>
                <a href="about.html" class="btn-p mt-10 no-underline">Read Full Story</a>
            </div>
        </section>
        <section id="inventory" class="py-32 px-6 max-w-[1440px] mx-auto text-center border-t border-slate-100">
            <h2 class="section-title mb-20 uppercase tracking-tighter">Exclusive Offers</h2>
            <div id="live-data-container" class="grid grid-cols-1 md:grid-cols-4 gap-10 text-left"></div>
        </section>
        """
    elif layout_dna == "Classic Royal (Luxury)":
        idx_content = f"""
        <section class="hero-mask px-6 text-center text-white">
            <div class="max-w-[1200px] mx-auto">
                <h1 class="hero-title mb-10 tracking-tighter leading-none font-serif normal-case italic" style="font-family: 'Playfair Display', serif;">{hero_h}</h1>
                <p class="text-lg md:text-3xl mb-16 italic opacity-80 leading-tight">{seo_d}</p>
                <a href="#inventory" class="btn-accent tracking-widest text-[10px] md:text-sm">Enter Showroom</a>
            </div>
        </section>
        <section class="bg-white py-32 px-6 text-center border-b">
            <div class="max-w-4xl mx-auto">
                <h2 class="section-title mb-20 font-serif normal-case italic">Proven Reputation</h2>
                <p class="text-2xl text-slate-600 leading-relaxed italic border-l-8 pl-10 border-brand" style="border-color:var(--p)">"Transforming high-end landscapes since inception. Technical precision meets royal aesthetics."</p>
            </div>
        </section>
        <section id="inventory" class="py-32 px-6 max-w-[1440px] mx-auto text-center"><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-3 gap-16 text-center"></div></section>
        """
    else: # Fallback Bento
        idx_content = f"""
        <section class="hero-mask px-6 text-center text-white"><h1 class="hero-title mb-10">{hero_h}</h1><a href="#inventory" class="btn-accent shadow-2xl">Enter Hub</a></section>
        <section id="inventory" class="p-10 max-w-[1440px] mx-auto"><div id="live-data-container" class="grid md:grid-cols-4 gap-6"></div></section>
        <section class="p-20"><div class="grid md:grid-cols-3 gap-10">{"".join([f'<div class="bg-slate-100 p-10 rounded-3xl h-64 flex items-center justify-center text-center font-black uppercase tracking-widest"><h3>{s}</h3></div>' for s in biz_serv.splitlines()])}</div></section>
        """

    # --- ZIP OUTPUT ---
    z_b = io.BytesIO()
    with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as z_f:
        z_f.writestr("index.html", get_layout("Home", seo_d, idx_content, True))
        z_f.writestr("about.html", get_layout("About Us", "History", f"<section class='max-w-7xl mx-auto py-32 px-6'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>About Our Heritage</h1><div class='text-xl md:text-2xl leading-relaxed text-slate-700 legal-text'>{about_txt}</div><img src='{img_g}' class='mt-20 w-full h-[600px] object-cover shadow-2xl' style='border-radius: var(--radius)'></section>"))
        z_f.writestr("contact.html", get_layout("Contact", "Location", f"<section class='max-w-[1440px] mx-auto py-32 px-6 text-center'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>Technical Hub</h1><div class='grid md:grid-cols-2 gap-16 text-left'><div class='bg-slate-950 p-12 md:p-24 text-white' style='border-radius: var(--radius)'><p class='text-4xl font-black mb-8 text-white'>{biz_phone}</p><p class='text-2xl mb-12 opacity-80'>{biz_addr}</p><a href='tel:{biz_phone}' class='btn-accent w-full no-underline uppercase tracking-widest font-black'>Book Consultation</a></div><div class='rounded-[3rem] overflow-hidden border shadow-2xl bg-slate-100' style='min-height:300px'>{map_iframe}</div></div></section>"))
        z_f.writestr("privacy.html", get_layout("Privacy", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>Privacy Policy</h1><div class='text-lg legal-text'>{priv_body}</div></div>"))
        z_f.writestr("terms.html", get_layout("Terms", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>Terms & Conditions</h1><div class='text-lg legal-text'>{terms_body}</div></div>"))
        z_f.writestr("404.html", get_layout("404", "Not Found", "<div class='py-64 text-center'><h1 class='text-[120px] font-black uppercase text-slate-200 tracking-widest'>404</h1></div>"))
        z_f.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}sitemap.xml")
        z_f.writestr("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{prod_url}index.html</loc></url><url><loc>{prod_url}about.html</loc></url></urlset>')

    st.success("💎 TITAN ELITE v15.1 DEPLOYED. Multi-DNA and Error synchronization locked.")
    st.download_button("📥 DOWNLOAD COMPLETE BIZ PACKAGE", z_b.getvalue(), f"{biz_name.lower().replace(' ', '_')}_v15_1.zip")
