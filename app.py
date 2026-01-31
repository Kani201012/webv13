import streamlit as st
import zipfile
import io
import json
from datetime import datetime

# --- 1. DESIGN STUDIO CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Titan v14.0 | Global Web Architect", layout="wide", page_icon="🏗️")

st.markdown("""
    <style>
    .main { background: #020617; color: white; }
    .stTabs [data-baseweb="tab"] { color: white; font-weight: bold; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4.5em; 
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); 
        color: white; font-weight: 900; border: none; font-size: 1.3rem;
        box-shadow: 0 10px 30px rgba(79, 70, 229, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: THE ARCHITECT'S TOOLS ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=50)
    st.title("Titan v14.0 Studio")
    
    with st.expander("🎭 1. Architecture DNA", expanded=True):
        layout_dna = st.selectbox("Choose Layout Strategy", [
            "Industrial Titan (Rugged)", 
            "Classic Royal (Luxury)", 
            "Soft-UI (Modern Clean)", 
            "Glass-Tech (Futuristic)",
            "Brutalist (Bold & Sharp)", 
            "Corporate Elite (Global Standard)",
            "Minimalist Boutique",
            "Midnight Stealth (Dark)",
            "Vivid Creative (Gradients)",
            "The Bento Grid (Modern)"
        ])
        p_color = st.color_picker("Primary Brand Color", "#4F46E5")
        s_color = st.color_picker("Accent/CTA Color", "#10B981")
        border_rad = st.select_slider("Corner Roundness", options=["0px", "4px", "12px", "24px", "50px"], value="12px")

    with st.expander("✍️ 2. Typography Studio", expanded=True):
        h_font = st.selectbox("Heading Font", ["Oswald", "Playfair Display", "Montserrat", "Syncopate", "Inter", "Space Grotesk"])
        b_font = st.selectbox("Body Font", ["Inter", "Roboto", "Open Sans", "Lora", "Work Sans"])
        h_weight = st.select_slider("Heading Weight", options=["400", "700", "900"], value="900")
        ls = st.select_slider("Letter Spacing", options=["-0.05em", "-0.02em", "0em", "0.05em"], value="-0.02em")

    gsc_tag = st.text_input("GSC Verification Tag")
    st.info("By www.kaydiemscriptlab.com")

st.title("🏗️ Kaydiem Titan Supreme v14.0")

# --- 2. MULTI-TAB DATA COLLECTION ---
tabs = st.tabs(["📍 Identity", "🏗️ Content & SEO", "🖼️ Photo Manager", "⚡ Live E-com", "🌟 Social Proof", "⚖️ Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name (NAP)", "Al-Mashael Sulai Boom Truck")
        biz_phone = st.text_input("Verified Phone", "+966 50 000 0000")
        biz_email = st.text_input("Business Email", "info@almashael.sa")
    with c2:
        biz_cat = st.text_input("Category", "Heavy Equipment Rental")
        biz_hours = st.text_input("Hours", "Sat-Thu: 08:00 - 18:00")
        prod_url = st.text_input("Live URL", "https://kani201012.github.io/site/")
    biz_logo = st.text_input("Logo URL (Direct Image Link)")
    biz_addr = st.text_area("Full Maps Physical Address")
    map_iframe = st.text_area("Map Embed HTML (iframe)")

with tabs[1]:
    hero_h = st.text_input("Main Hero Headline", "Dominating the Industrial Horizon")
    seo_d = st.text_input("Meta Description", "Riyadh's premier verified heavy equipment solutions.")
    biz_key = st.text_input("SEO Keywords (Comma Separated)")
    biz_serv = st.text_area("Services Listing (One per line)")
    about_txt = st.text_area("Our Authority Story (800+ Words)", height=300)

with tabs[2]:
    st.header("📸 High-Ticket Asset Manager")
    custom_hero = st.text_input("Hero Image URL")
    custom_feat = st.text_input("Feature Image URL")
    custom_gall = st.text_input("About Section Image URL")

with tabs[3]:
    st.header("🛒 Headless E-commerce Bridge")
    sheet_url = st.text_input("Published CSV Link (Pipe | Separator)")

with tabs[4]:
    testi = st.text_area("Testimonials (Name | Quote)")
    faqs = st.text_area("FAQ (Question? ? Answer)")

with tabs[5]:
    priv_body = st.text_area("Privacy Policy", height=200)
    terms_body = st.text_area("Terms Content", height=200)

# --- 3. THE SUPREME TITAN ENGINE CORE ---

if st.button("🚀 DEPLOY WORLD-CLASS ARCHITECTURE"):
    
    # 3.1 Setup Assets
    img_h = custom_hero if custom_hero else "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?auto=format&fit=crop&q=80&w=1600"
    img_f = custom_feat if custom_feat else "https://images.unsplash.com/photo-1504307651254-35680f3366d4?auto=format&fit=crop&q=80&w=800"
    img_g = custom_gall if custom_gall else "https://images.unsplash.com/photo-1581094288338-2314dddb7ecb?auto=format&fit=crop&q=80&w=1600"
    
    logo_html = f'<img src="{biz_logo}" alt="{biz_name}" class="h-10 md:h-16 w-auto object-contain">' if biz_logo else f'<span class="text-xl md:text-3xl font-black tracking-tighter" style="color:var(--p)">{biz_name}</span>'
    wa_clean = biz_phone.replace(" ", "").replace("+", "")

    # 3.2 Dynamic Architecture Logic
    layout_styles = {
        "Industrial Titan (Rugged)": "bg-white",
        "Classic Royal (Luxury)": "bg-slate-50",
        "Soft-UI (Modern Clean)": "bg-gray-50",
        "Glass-Tech (Futuristic)": "bg-slate-900",
        "Brutalist (Bold & Sharp)": "bg-white",
        "Corporate Elite (Global Standard)": "bg-white",
        "Minimalist Boutique": "bg-white",
        "Midnight Stealth (Dark)": "bg-black text-white",
        "Vivid Creative (Gradients)": "bg-white",
        "The Bento Grid (Modern)": "bg-slate-50"
    }
    
    bg_class = layout_styles[layout_dna]

    theme_css = f"""
    :root {{ --p: {p_color}; --s: {s_color}; --radius: {border_rad}; --ls: {ls}; --weight: {h_weight}; }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; padding: 0; width: 100%; overflow-x: hidden; scroll-behavior: smooth; font-family: '{b_font}', sans-serif; }}
    body {{ color: #1e293b; background: #fff; line-height: 1.7; }}
    h1, h2, h3 {{ font-family: '{h_font}', sans-serif; font-weight: var(--weight); letter-spacing: var(--ls); text-transform: uppercase; line-height: 1.1; overflow-wrap: break-word; }}
    .btn-accent {{ background: var(--s); color: #000 !important; padding: 1.2rem 3rem; border-radius: var(--radius); font-weight: 900; transition: 0.3s; display: inline-block; text-decoration:none; text-align:center; box-shadow: 0 10px 20px -5px var(--s); }}
    .btn-accent:hover {{ transform: translateY(-3px); filter: brightness(1.1); }}
    .glass-nav {{ background: rgba(255, 255, 255, 0.98); backdrop-filter: blur(15px); border-bottom: 1px solid rgba(0,0,0,0.05); position: fixed; top: 0; width: 100%; z-index: 9999; }}
    .hero-mask {{ background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.5)), url('{img_h}'); background-size: cover; background-position: center; min-height: 90vh; display: flex; align-items: center; justify-content: center; width: 100%; }}
    .legal-text {{ white-space: pre-wrap; word-wrap: break-word; font-size: 1.1rem; color: #475569; }}
    #modal {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 100000; padding: 1rem; align-items: center; justify-content: center; }}
    .modal-content {{ background: white; max-width: 1000px; width: 100%; border-radius: var(--radius); overflow: hidden; }}
    """

    def get_layout(page_title, page_desc, content_body, is_home=False):
        v_tag = f'<meta name="google-site-verification" content="{gsc_tag}">' if (is_home and gsc_tag) else ""
        
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
                            const p = {{ id: idx, name: parts[0], price: parts[1], desc: parts[2]||"", img1: parts[3]||"{img_f}" }};
                            currentProducts.push(p);
                            container.innerHTML += `
                            <div onclick="openProduct(${{idx}})" class="bg-white p-8 rounded-[2.5rem] border shadow-xl cursor-pointer hover:scale-105 transition-all">
                                <img src="${{p.img1}}" class="w-full h-48 object-cover mb-6 rounded-3xl bg-slate-50">
                                <h3 class="text-xl font-black mb-2" style="color:var(--p)">${{p.name}}</h3>
                                <p class="text-blue-600 font-black text-2xl">${{p.price}}</p>
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
                document.getElementById('m-img').src = p.img1;
                document.getElementById('m-wa').href = "https://wa.me/{wa_clean}?text=" + encodeURIComponent("I am interested in " + p.name);
                document.getElementById('modal').style.display = 'flex';
            }}
            window.onload = fetchLiveData;
            </script>
            """

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    {v_tag}
    <title>{page_title} | {biz_name}</title>
    <meta name="description" content="{page_desc}"><meta name="keywords" content="{biz_key}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@700;900&family={b_font.replace(' ', '+')}:wght@400;700&display=swap" rel="stylesheet">
    <style>{theme_css}</style>
</head>
<body class="{bg_class} flex flex-col min-h-screen">
    <nav class="glass-nav p-4 md:p-6">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <a href="index.html">{logo_html}</a>
            <div class="hidden md:flex space-x-10 text-[11px] font-black uppercase tracking-[0.2em] text-slate-500">
                <a href="index.html">Home</a> <a href="about.html">About</a> <a href="contact.html">Contact</a>
            </div>
            <a href="tel:{biz_phone}" class="bg-slate-900 text-white px-8 py-2 rounded-full font-bold text-[10px]">CALL NOW</a>
        </div>
    </nav>
    <main class="flex-grow pt-24">{content_body}</main>
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
    <footer class="bg-slate-950 text-slate-500 py-32 px-10">
        <div class="max-w-7xl mx-auto grid md:grid-cols-3 gap-20">
            <div><h4 class="text-white font-black mb-6 uppercase tracking-widest">{biz_name}</h4><p class="text-sm leading-relaxed">{biz_addr}</p></div>
            <div class="text-center">{logo_html.replace('h-10 md:h-16', 'h-8 opacity-50 mb-4')}<p class="text-[10px] uppercase">Built by <a href="https://www.kaydiemscriptlab.com" class="text-white underline">Kaydiem Script Lab</a></p></div>
            <div class="text-right"><h4 class="text-white font-bold mb-4 uppercase text-xs">Direct Support</h4><p class="text-white font-bold">{biz_phone}<br>{biz_email}</p></div>
        </div>
    </footer>
    {dyn_script}
</body></html>"""

    # --- INDEX ---
    serv_h = "".join([f'<div class="bg-slate-50 p-12 rounded-[2.5rem] border border-slate-100 shadow-sm hover:shadow-2xl transition-all"><h3 class="text-2xl font-black mb-4 uppercase" style="color:var(--p)">{s.strip()}</h3><p class="text-slate-500 text-sm leading-relaxed italic">Verified 2026 industrial technical solution.</p></div>' for s in biz_serv.splitlines() if s.strip()])
    
    idx_content = f"""
    <section class="hero-mask px-6 text-center text-white">
        <div class="max-w-7xl mx-auto">
            <h1 class="hero-title mb-10 uppercase tracking-tighter leading-none">{hero_h}</h1>
            <p class="text-lg md:text-3xl font-light mb-16 max-w-4xl mx-auto opacity-80 leading-tight">{seo_d}</p>
            <a href="contact.html" class="btn-accent uppercase tracking-widest text-[10px] md:text-sm">Get Enterprise Quote</a>
        </div>
    </section>
    <section class="max-w-7xl mx-auto py-40 px-6">
        <h2 class="text-5xl font-black mb-20 text-center uppercase tracking-tighter" style="color:var(--p)">Core Capabilities</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10">{serv_h}</div>
    </section>
    <section id="inventory" class="py-32 px-6 max-w-7xl mx-auto text-center border-t">
        <h2 class="text-5xl font-black mb-20 uppercase tracking-tighter">Live Equipment Data</h2>
        <div id="live-data-container" class="grid grid-cols-1 md:grid-cols-4 gap-10 text-left">
            <p class="p-20 text-center text-slate-400 font-bold animate-pulse">Establishing Connection...</p>
        </div>
    </section>
    <section class="bg-slate-50 py-32 px-6 border-y text-left">
        <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-24 items-center">
            <img src="{img_f}" class="shadow-2xl" style="border-radius: var(--radius)">
            <div>
                <h2 class="text-5xl font-black mb-12 uppercase tracking-tighter leading-none" style="color:var(--p)">Industrial Authority</h2>
                <p class="text-2xl text-slate-600 mb-12 leading-relaxed italic">"Providing the technical and engineering foundation for the 2026 urban landscape. Precision mixing, certified safety, and direct quality oversight."</p>
                <a href="about.html" class="font-black text-xs uppercase underline decoration-p decoration-4 underline-offset-8">Our History</a>
            </div>
        </div>
    </section>
    """

    # --- ZIP OUTPUT ---
    z_b = io.BytesIO()
    with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as z_f:
        z_f.writestr("index.html", get_layout("Home", seo_d, idx_content, True))
        z_f.writestr("about.html", get_layout("About", "History", f"<section class='max-w-7xl mx-auto py-32 px-6'><h1 class='text-7xl font-black mb-16 uppercase tracking-tighter leading-none' style='color:var(--p)'>About Our Heritage</h1><div class='text-xl md:text-2xl leading-relaxed text-slate-700 legal-text'>{about_txt}</div><img src='{img_g}' class='mt-20 w-full h-[600px] object-cover shadow-2xl' style='border-radius: var(--radius)'></section>"))
        z_f.writestr("contact.html", get_layout("Contact", "Location", f"<section class='max-w-7xl mx-auto py-32 px-6 text-center'><h1 class='text-8xl font-black mb-16 tracking-tighter uppercase' style='color:var(--p)'>Connect</h1><div class='grid md:grid-cols-2 gap-16 text-left'><div class='bg-slate-950 p-12 md:p-24 text-white' style='border-radius: var(--radius)'><p class='text-4xl font-black mb-8 text-white'>{biz_phone}</p><p class='text-2xl mb-12 opacity-80'>{biz_addr}</p></div><div class='rounded-[3rem] overflow-hidden border shadow-2xl bg-slate-100' style='min-height:300px'>{map_iframe}</div></div></section>"))
        z_f.writestr("privacy.html", get_layout("Privacy", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='text-6xl font-black mb-16 uppercase' style='color:var(--p)'>Privacy Policy</h1><div class='text-lg legal-text'>{priv_body}</div></div>"))
        z_f.writestr("terms.html", get_layout("Terms", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='text-6xl font-black mb-16 uppercase' style='color:var(--p)'>Terms</h1><div class='text-lg legal-text'>{terms_body}</div></div>"))
        z_f.writestr("404.html", get_layout("404", "Not Found", "<div class='py-64 text-center'><h1 class='text-[120px] font-black uppercase text-slate-200 tracking-widest'>404</h1></div>"))
        z_f.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}sitemap.xml")
        z_f.writestr("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{prod_url}index.html</loc></url><url><loc>{prod_url}about.html</loc></url></urlset>')

    st.success("💎 TITAN SUPREME v14.0 DEPLOYED. World-Class Build Confirmed.")
    st.download_button("📥 DOWNLOAD COMPLETE BIZ PACKAGE", z_b.getvalue(), f"{biz_name.lower().replace(' ', '_')}_v14_0.zip")
