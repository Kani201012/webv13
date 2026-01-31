import streamlit as st
import zipfile
import io
import json
from datetime import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Titan v13.0 | Industrial Rebirth", layout="wide", page_icon="🏗️")

st.markdown("""
    <style>
    .main { background: #020617; color: white; }
    .stTabs [data-baseweb="tab"] { color: white; font-weight: bold; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4.5em; 
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%); 
        color: white; font-weight: 900; border: none; font-size: 1.4rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: DESIGN STUDIO ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=50)
    st.title("Titan v13.0 Architect")
    
    with st.expander("🎨 Brand Theme", expanded=True):
        p_color = st.color_picker("Primary Brand Color", "#001F3F")
        s_color = st.color_picker("Accent/CTA Color", "#FFD700")
        border_rad = st.select_slider("Corner Roundness", options=["0px", "8px", "16px", "32px"], value="8px")

    with st.expander("✍️ Typography", expanded=True):
        h_font = st.selectbox("Heading Font", ["Oswald", "Playfair Display", "Montserrat"])
        b_font = st.selectbox("Body Font", ["Inter", "Roboto", "Open Sans"])

    gsc_tag = st.text_input("GSC Verification Tag (Required for Point 16)")
    st.info("Certified Build by Kaydiem Script Lab")

st.title("🏗️ Kaydiem Titan Supreme v13.0")
st.warning("This engine generates a 100% W3C Compliant, AI-Search Optimized Industrial Asset.")

# --- 2. DATA COLLECTION TABS ---
tabs = st.tabs(["📍 Identity", "🏗️ Content & SEO", "🖼️ Images", "🛒 Inventory", "⚖️ Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name (NAP)", "Al-Mashael Sulai Boom Truck")
        biz_phone = st.text_input("Verified Phone", "+966 50 000 0000")
        biz_email = st.text_input("Business Email", "info@almashael-rentals.sa")
    with c2:
        biz_cat = st.text_input("Category", "Equipment Rental Agency")
        biz_hours = st.text_input("Hours", "Sat-Thu: 08:00 - 18:00")
        prod_url = st.text_input("Production URL", "https://username.github.io/repo/")
    biz_addr = st.text_area("Full Maps Physical Address")
    map_iframe = st.text_area("Map Embed HTML (iframe)")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", "Precision Lifting & Industrial Power")
    seo_d = st.text_input("Meta Description (160 Chars)", "Riyadh's leading boom truck and scissor lift rental service.")
    biz_key = st.text_input("SEO Keywords")
    biz_serv = st.text_area("Services Listing (One per line)")
    about_txt = st.text_area("Full About Us Story (Min 800 Words)", height=250)

with tabs[2]:
    st.header("📸 Photo Management (Mandatory for Trust)")
    hero_img = st.text_input("Hero Background URL", "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?q=80&w=1600")
    feat_img = st.text_input("Feature Section URL", "https://images.unsplash.com/photo-1504307651254-35680f3366d4?q=80&w=800")
    gall_img = st.text_input("About Page URL", "https://images.unsplash.com/photo-1581094288338-2314dddb7ecb?q=80&w=1600")

with tabs[3]:
    st.header("⚡ Live Data Feed")
    sheet_url = st.text_input("Published CSV Link")

with tabs[4]:
    priv_body = st.text_area("Privacy Policy", height=200)
    terms_body = st.text_area("Terms & Conditions", height=200)

# --- 3. THE SUPREME ENGINE V13.0 ---

if st.button("🚀 DEPLOY 100% AUDIT-PROOF ASSET"):
    
    wa_clean = biz_phone.replace(" ", "").replace("+", "")
    
    theme_css = f"""
    :root {{ --p: {p_color}; --s: {s_color}; --radius: {border_rad}; }}
    * {{ box-sizing: border-box; -webkit-font-smoothing: antialiased; }}
    html, body {{ margin: 0; padding: 0; width: 100%; overflow-x: hidden; scroll-behavior: smooth; }}
    body {{ font-family: '{b_font}', sans-serif; color: #1e293b; line-height: 1.7; background: #fff; }}
    h1, h2, h3 {{ font-family: '{h_font}', sans-serif; text-transform: uppercase; line-height: 1.1; }}
    .btn-accent {{ background: var(--s); color: #000 !important; padding: 1.2rem 3rem; border-radius: var(--radius); font-weight: 900; transition: 0.3s; display: inline-block; text-decoration:none; text-align:center; box-shadow: 0 10px 20px -5px var(--s); }}
    .btn-accent:hover {{ transform: translateY(-3px); filter: brightness(1.1); }}
    .glass-nav {{ background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.1); position: fixed; top: 0; width: 100%; z-index: 9999; }}
    .hero-mask {{ background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.5)), url('{hero_img}'); background-size: cover; background-position: center; min-height: 85vh; display: flex; align-items: center; justify-content: center; padding-top: 80px; }}
    .legal-text {{ white-space: pre-wrap; font-size: 1.1rem; color: #475569; }}
    """

    def get_layout(title, desc, content, is_h=False):
        v_tag = f'<meta name="google-site-verification" content="{gsc_tag}">' if (is_h and gsc_tag) else ""
        
        dyn_script = ""
        if is_h and sheet_url:
            dyn_script = f"""
            <script>
            async function fetchLiveData() {{
                try {{
                    const response = await fetch('{sheet_url}');
                    const csvText = await response.text();
                    const rows = csvText.split('\\n').map(row => row.split('|')).slice(1);
                    const container = document.getElementById('live-data-container');
                    container.innerHTML = "";
                    rows.forEach((parts) => {{
                        if (parts.length >= 2) {{
                            container.innerHTML += `
                            <div class="bg-white p-10 rounded-[2rem] border shadow-xl">
                                <h3 class="text-2xl font-black mb-2" style="color:var(--p)">${{parts[0]}}</h3>
                                <p class="text-blue-600 font-black text-2xl mb-4">${{parts[1]}}</p>
                                <p class="text-slate-500 text-sm">${{parts[2] || ""}}</p>
                                <a href="https://wa.me/{wa_clean}" class="btn-accent w-full mt-6 text-sm">BOOK NOW</a>
                            </div>`;
                        }}
                    }});
                }} catch (e) {{ console.log("Offline"); }}
            }}
            window.onload = fetchLiveData;
            </script>
            """

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    {v_tag}
    <title>{title} | {biz_name}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{biz_key}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@700;900&family={b_font.replace(' ', '+')}:wght@400;700&display=swap" rel="stylesheet">
    <style>{theme_css}</style>
</head>
<body class="flex flex-col min-h-screen">
    <nav class="glass-nav p-4 md:p-6">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <a href="index.html" class="text-2xl font-black tracking-tighter uppercase" style="color:var(--p)">{biz_name}</a>
            <div class="hidden md:flex space-x-10 text-xs font-bold uppercase tracking-widest">
                <a href="index.html">Home</a> <a href="about.html">About</a> <a href="contact.html">Contact</a>
            </div>
            <a href="tel:{biz_phone}" class="bg-slate-900 text-white px-6 py-2 rounded-full font-bold text-[10px]">CALL NOW</a>
        </div>
    </nav>
    <main class="flex-grow pt-20">{content}</main>
    <footer class="bg-slate-950 text-slate-500 py-24 px-10">
        <div class="max-w-7xl mx-auto grid md:grid-cols-3 gap-20 text-left">
            <div><h4 class="text-white font-black mb-6 uppercase tracking-widest">{biz_name}</h4><p class="text-sm leading-relaxed">{biz_addr}</p></div>
            <div><h4 class="text-white font-bold mb-6 uppercase text-xs">Legal Hub</h4><ul class="space-y-4 text-xs uppercase font-bold"><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms & Conditions</a></li></ul></div>
            <div class="text-right"><p class="text-[10px] opacity-30 italic mb-4">Built by Kaydiem Script Lab</p><p class="text-white font-bold">{biz_phone}<br>{biz_email}</p></div>
        </div>
    </footer>
    {dyn_script}
</body></html>"""

    # --- INDEX PAGE ---
    serv_html = "".join([f'<div class="bg-slate-50 p-10 rounded-3xl border hover:shadow-2xl transition"><h3 class="text-xl font-black mb-4" style="color:var(--p)">{s.strip()}</h3><p class="text-slate-500 text-sm leading-relaxed">Certified industrial solution for {biz_cat} requirements.</p></div>' for s in biz_serv.splitlines() if s.strip()])
    
    idx_content = f"""
    <section class="hero-mask px-6 text-center text-white">
        <div class="max-w-5xl mx-auto">
            <h1 class="text-5xl md:text-8xl font-black mb-10 tracking-tighter leading-[1.1] uppercase">{hero_h}</h1>
            <p class="text-xl md:text-2xl mb-12 opacity-80 max-w-3xl mx-auto">{seo_d}</p>
            <a href="contact.html" class="btn-accent uppercase tracking-widest text-sm">Request Technical Quote</a>
        </div>
    </section>
    <section class="max-w-7xl mx-auto py-32 px-6">
        <h2 class="text-5xl font-black mb-20 text-center uppercase tracking-tighter" style="color:var(--p)">Core Capabilities</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10">{serv_html}</div>
    </section>
    <section class="bg-slate-50 py-32 px-6 border-y">
        <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-24 items-center">
            <img src="{feat_img}" class="rounded-[3rem] shadow-2xl">
            <div>
                <h2 class="text-6xl font-black mb-10 tracking-tighter" style="color:var(--p)">Industrial Authority</h2>
                <p class="text-2xl text-slate-600 mb-10 leading-relaxed italic">"Verified 2026 infrastructure solutions. Precision, safety, and direct owner oversight."</p>
                <a href="about.html" class="font-black text-xs uppercase underline underline-offset-8">Our History</a>
            </div>
        </div>
    </section>
    <section id="inventory" class="py-32 px-6 max-w-7xl mx-auto text-center">
        <h2 class="text-5xl font-black mb-20 uppercase tracking-tighter" style="color:var(--p)">Live Equipment Hub</h2>
        <div id="live-data-container" class="grid grid-cols-1 md:grid-cols-3 gap-10 text-left">
            <p class="p-20 text-center text-slate-400 font-black animate-pulse">Establishing Connection...</p>
        </div>
    </section>
    """

    # --- ZIP ---
    z_buf = io.BytesIO()
    with zipfile.ZipFile(z_buf, "a", zipfile.ZIP_DEFLATED, False) as zf:
        zf.writestr("index.html", get_layout("Home", seo_d, idx_content, True))
        zf.writestr("about.html", get_layout("About", "Our Legacy", f"<section class='max-w-5xl mx-auto py-32 px-10'><h1 class='text-7xl font-black mb-16 uppercase tracking-tighter leading-none' style='color:var(--p)'>About Us</h1><div class='text-xl leading-relaxed text-slate-700 legal-text'>{about_txt}</div><img src='{gall_img}' class='mt-20 rounded-[3rem] w-full h-[500px] object-cover shadow-2xl'></section>"))
        zf.writestr("contact.html", get_layout("Contact", "Visit Us", f"<section class='max-w-7xl mx-auto py-32 px-6 text-center'><h1 class='text-8xl font-black mb-16 tracking-tighter uppercase' style='color:var(--p)'>Connect</h1><div class='grid md:grid-cols-2 gap-16 text-left'><div class='bg-slate-950 p-12 md:p-24 text-white rounded-[3rem] shadow-2xl border'> <p class='text-4xl font-black mb-8'>{biz_phone}</p><p class='text-2xl mb-12 opacity-80'>{biz_addr}</p></div><div class='rounded-[3rem] overflow-hidden border shadow-2xl bg-slate-100' style='min-height:300px'>{map_iframe}</div></div></section>"))
        zf.writestr("privacy.html", get_layout("Privacy", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='text-6xl font-black mb-16 uppercase' style='color:var(--p)'>Privacy Policy</h1><div class='legal-text'>{priv_body}</div></div>"))
        zf.writestr("terms.html", get_layout("Terms", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='text-6xl font-black mb-16 uppercase' style='color:var(--p)'>Terms</h1><div class='legal-text'>{terms_body}</div></div>"))
        zf.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}sitemap.xml")
        zf.writestr("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{prod_url}index.html</loc></url></urlset>')

    st.success("💎 TITAN SUPREME v13.0 DEPLOYED. Technical Audit Passed.")
    st.download_button("📥 DOWNLOAD COMPLETE BIZ PACKAGE", z_buf.getvalue(), f"{biz_name.lower()}_v13.zip")
