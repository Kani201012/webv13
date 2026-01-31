import streamlit as st
import zipfile
import io
import json
from datetime import datetime
import html  # for escaping
import re    # for filename sanitization
import csv
from urllib.parse import quote

# ────────────────────────────────────────────────
# SESSION STATE – prevents data loss on rerun
# ────────────────────────────────────────────────
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

def save(key, value):
    st.session_state.form_data[key] = value

def get(key, default=""):
    return st.session_state.form_data.get(key, default)

# ────────────────────────────────────────────────
# PAGE CONFIG & GLOBAL STYLING
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="Kaydiem Titan v16.1 | Elite Website Architect",
    layout="wide",
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# Dark mode toggle in sidebar
st.sidebar.checkbox("Dark Mode", value=st.session_state.dark_mode, key="dark_toggle")
if st.session_state.dark_toggle != st.session_state.dark_mode:
    st.session_state.dark_mode = st.session_state.dark_toggle
    st.rerun()

dark_css = """
    :root { --bg: #0f172a; --text: #e2e8f0; --card: #1e293b; --border: #334155; }
    body, .stApp { background: var(--bg) !important; color: var(--text) !important; }
    .stTabs [data-baseweb="tab"] { color: var(--text) !important; }
    .stExpander { background: var(--card) !important; border-color: var(--border) !important; }
""" if st.session_state.dark_mode else ""

st.markdown(f"""
    <style>
    {dark_css}
    .main {{ padding: 1rem; }}
    .stButton > button {{
        width: 100%; border-radius: 12px; height: 4.2rem;
        background: linear-gradient(135deg, #1e293b, #4f46e5);
        color: white; font-weight: 900; font-size: 1.35rem;
        border: none; box-shadow: 0 8px 25px rgba(79,70,229,0.35);
    }}
    .stButton > button:hover {{ transform: translateY(-2px); }}
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# SIDEBAR – Architecture Controls
# ────────────────────────────────────────────────
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=60)
    st.title("Titan v16.1 Elite")
    st.caption("Kaydiem Script Lab – 2026 Edition")

    with st.expander("🎨 Design DNA", expanded=True):
        layout_dna = st.selectbox("Layout Strategy", [
            "Industrial Titan", "Classic Royal", "Glass-Tech",
            "Bento Grid", "Brutalist Bold", "Corporate Elite",
            "Minimalist", "Midnight Stealth", "Vivid Gradient", "Stealth Pro"
        ], key="layout")
        p_color = st.color_picker("Primary Color", "#001F3F", key="p_color")
        s_color = st.color_picker("Accent Color", "#D4AF37", key="s_color")
        border_rad = st.select_slider("Radius", ["0px","6px","12px","24px","40px"], value="12px", key="radius")

    with st.expander("✍️ Typography", expanded=True):
        h_font = st.selectbox("Heading Font", ["Montserrat","Playfair Display","Oswald","Syncopate","Space Grotesk"], key="h_font")
        b_font = st.selectbox("Body Font", ["Inter","Roboto","Open Sans","Work Sans"], key="b_font")
        h_weight = st.select_slider("Heading Weight", ["400","600","700","900"], value="900", key="h_weight")

    gsc_tag = st.text_input("Google Site Verification Tag", key="gsc")

# ────────────────────────────────────────────────
# MAIN TABS
# ────────────────────────────────────────────────
tab_names = ["Identity", "Content & SEO", "Assets", "Live E-commerce", "Social Proof", "Legal", "👁️ Preview"]
tabs = st.tabs(tab_names)

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", value=get("biz_name", "Red Hippo Planners"), key="biz_name")
        save("biz_name", biz_name)
        biz_phone = st.text_input("Phone (with +91)", value=get("biz_phone", "+918454002711"), key="biz_phone")
        save("biz_phone", biz_phone)
        biz_email = st.text_input("Email", value=get("biz_email", "hello@yourdomain.in"), key="biz_email")
        save("biz_email", biz_email)

    with c2:
        biz_cat = st.text_input("Category", value=get("biz_cat", "Luxury Event Planner"), key="biz_cat")
        save("biz_cat", biz_cat)
        biz_hours = st.text_input("Hours", value=get("biz_hours", "Mon–Sun 10:00–20:00"), key="biz_hours")
        save("biz_hours", biz_hours)
        live_url = st.text_input("Live Domain / Base URL", value=get("live_url", ""), key="live_url")
        save("live_url", live_url)

    biz_logo = st.text_input("Logo URL", value=get("biz_logo", ""), key="biz_logo")
    save("biz_logo", biz_logo)
    biz_addr = st.text_area("Full Address", value=get("biz_addr", ""), height=80, key="biz_addr")
    save("biz_addr", biz_addr)
    biz_areas = st.text_area("Service Areas (comma separated)", value=get("biz_areas", "South Delhi, Gurgaon, Noida"), height=100, key="biz_areas")
    save("biz_areas", biz_areas)
    map_iframe = st.text_area("Google Maps Embed <iframe>", value=get("map_iframe", ""), height=140, key="map_iframe")
    save("map_iframe", map_iframe)

with tabs[1]:
    hero_h = st.text_input("Hero Headline", value=get("hero_h", "Creating Timeless Moments"), key="hero_h")
    save("hero_h", hero_h)
    seo_d = st.text_input("Meta Description (150–160 chars)", value=get("seo_d", ""), key="seo_d")
    save("seo_d", seo_d)
    biz_key = st.text_input("SEO Keywords (comma separated)", value=get("biz_key", ""), key="biz_key")
    save("biz_key", biz_key)
    biz_serv = st.text_area("Services (one per line)", value=get("biz_serv", ""), height=180, key="biz_serv")
    save("biz_serv", biz_serv)
    about_txt = st.text_area("About Story (800+ words recommended)", value=get("about_txt", ""), height=320, key="about_txt")
    save("about_txt", about_txt)

with tabs[2]:
    st.subheader("Hero & Feature Images")
    custom_hero = st.text_input("Hero Background URL", value=get("custom_hero", ""), key="custom_hero")
    save("custom_hero", custom_hero)
    custom_feat = st.text_input("Feature / About Image URL", value=get("custom_feat", ""), key="custom_feat")
    save("custom_feat", custom_feat)

with tabs[3]:
    st.subheader("Headless CSV E-commerce")
    st.caption("Use Google Sheet → File → Share → Publish to web → CSV format | separator")
    sheet_url = st.text_input("Published CSV URL", value=get("sheet_url", ""), key="sheet_url")
    save("sheet_url", sheet_url)
    if sheet_url:
        st.info("Expected columns: Name | Price | Description | Image1 | Image2 | Image3")

with tabs[4]:
    testi = st.text_area("Testimonials (Name | Quote)", value=get("testi", ""), height=160, key="testi")
    save("testi", testi)
    faqs = st.text_area("FAQs (Question?Answer)", value=get("faqs", ""), height=160, key="faqs")
    save("faqs", faqs)

with tabs[5]:
    priv_body = st.text_area("Privacy Policy", value=get("priv_body", ""), height=240, key="priv_body")
    save("priv_body", priv_body)
    terms_body = st.text_area("Terms & Conditions", value=get("terms_body", ""), height=240, key="terms_body")
    save("terms_body", terms_body)

# ────────────────────────────────────────────────
# GENERATION BUTTON + VALIDATION
# ────────────────────────────────────────────────
required = ["biz_name", "biz_phone", "hero_h"]
if st.button("🚀 GENERATE ELITE WEBSITE v16.1", type="primary", use_container_width=True):
    missing = [k for k in required if not get(k)]
    if missing:
        st.error(f"Please fill: {', '.join(missing)}")
    else:
        with st.spinner("Architecting elite structure..."):
            wa_clean = re.sub(r'[^0-9+]', '', get("biz_phone"))
            area_list = [a.strip() for a in get("biz_areas").split(",") if a.strip()]
            s_areas_json = json.dumps(area_list)

            img_h = get("custom_hero") or "https://images.unsplash.com/photo-1519741497674-611481863552?w=1600"
            img_f = get("custom_feat") or "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=800"

            logo_html = f'<img src="{get("biz_logo")}" alt="{get("biz_name")}" class="h-12 md:h-16 w-auto object-contain">' if get("biz_logo") else f'<span class="text-2xl md:text-4xl font-black uppercase tracking-tight" style="color:{p_color}">{get("biz_name")}</span>'

            theme_css = f"""
            :root {{ --p: {p_color}; --s: {s_color}; --radius: {border_rad}; }}
            * {{ box-sizing:border-box; margin:0; padding:0; }}
            body {{ font-family:'{b_font}',system-ui,sans-serif; color:#0f172a; background:#ffffff; line-height:1.7; }}
            h1,h2,h3 {{ font-family:'{h_font}',sans-serif; font-weight:{h_weight}; letter-spacing:-0.025em; }}
            .btn-primary {{ background:var(--p); color:white; padding:0.9rem 2rem; border-radius:var(--radius); font-weight:900; text-transform:uppercase; text-decoration:none; display:inline-block; }}
            .btn-accent {{ background:var(--s); color:#000; padding:1rem 2.4rem; border-radius:var(--radius); font-weight:900; box-shadow:0 10px 25px -5px var(--s); }}
            .glass {{ background:rgba(255,255,255,0.92); backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); }}
            """

            # ────── SAFE E-COMMERCE SCRIPT ──────
            dyn_script = ""
            if get("sheet_url"):
                dyn_script = f"""
                <script>
                let products = [];
                async function loadProducts() {{
                    try {{
                        const res = await fetch('{get("sheet_url")}');
                        if (!res.ok) throw new Error('CSV fetch failed');
                        const text = await res.text();
                        const rows = text.split('\\n').slice(1).map(r => r.split('|').map(c => c.trim()));
                        const container = document.getElementById('products');
                        if (!container) return;
                        container.innerHTML = '';
                        rows.forEach((cols, i) => {{
                            if (cols.length < 3) return;
                            const p = {{id:i, name:cols[0], price:cols[1], desc:cols[2], img1:cols[3]||'{img_f}', img2:cols[4]||'', img3:cols[5]||''}};
                            products.push(p);
                            container.innerHTML += `
                                <div class="card" onclick="showModal(${i})">
                                    <img src="${{p.img1}}" alt="${{p.name}}" loading="lazy" onerror="this.src='{img_f}'">
                                    <h3>${{p.name}}</h3>
                                    <div class="price">${{p.price}}</div>
                                </div>`;
                        }});
                    }} catch(e) {{ console.error(e); }}
                }}

                function showModal(idx) {{
                    const p = products[idx];
                    document.getElementById('modal-title').textContent = p.name;
                    document.getElementById('modal-price').textContent = p.price;
                    document.getElementById('modal-desc').textContent = p.desc;
                    document.getElementById('modal-img').src = p.img1;
                    document.getElementById('modal-wa').href = `https://wa.me/${wa_clean}?text=I%27m%20interested%20in%20${{encodeURIComponent(p.name)}}`;
                    document.getElementById('modal').style.display = 'flex';
                }}

                function closeModal() {{ document.getElementById('modal').style.display = 'none'; }}
                window.addEventListener('load', loadProducts);
                </script>
                """

            # ────── BASIC LAYOUT (expand with more DNA options later) ──────
            index_content = f"""
            <section class="hero relative min-h-screen flex items-center justify-center text-center text-white" style="background:linear-gradient(rgba(0,0,0,0.6),rgba(0,0,0,0.4)),url('{img_h}') center/cover;">
                <div class="max-w-5xl px-6">
                    <h1 class="text-5xl md:text-7xl font-black tracking-tight mb-6">{html.escape(get('hero_h'))}</h1>
                    <p class="text-xl md:text-2xl mb-10 max-w-3xl mx-auto">{html.escape(get('seo_d'))}</p>
                    <a href="#services" class="btn-primary text-lg px-10 py-4">Explore Services</a>
                </div>
            </section>

            <section id="services" class="py-24 px-6 max-w-7xl mx-auto">
                <h2 class="text-4xl md:text-5xl font-black text-center mb-16" style="color:{p_color}">Our Services</h2>
                <div class="grid md:grid-cols-3 gap-10">
                    {''.join(f'<div class="bg-gray-50 p-10 rounded-2xl shadow-xl"><h3 class="text-2xl font-bold mb-4">{html.escape(s)}</h3><p class="text-gray-600">Premium service delivered with excellence.</p></div>' for s in get('biz_serv').splitlines() if s.strip())}
                </div>
            </section>

            <section class="py-24 bg-gray-900 text-white text-center">
                <div class="max-w-5xl mx-auto px-6">
                    <h2 class="text-4xl font-black mb-12">What Our Clients Say</h2>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                        {''.join(f'<div class="bg-gray-800 p-8 rounded-2xl"><p class="italic mb-6">“{html.escape(q)}”</p><p class="font-bold">— {html.escape(n)}</p></div>' for line in get('testi').splitlines() if '|' in line for n, q in [line.split('|', 1)] if n.strip() and q.strip())}
                    </div>
                </div>
            </section>

            <div id="products" class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8 px-6 py-16 max-w-7xl mx-auto"></div>
            """

            # ────── ZIP GENERATION ──────
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
                # index.html
                zf.writestr("index.html", f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{html.escape(get('seo_d'))}">
    <title>{html.escape(get('biz_name'))}</title>
    {f'<meta name="google-site-verification" content="{gsc_tag}">' if gsc_tag else ''}
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={quote(h_font)}:wght@700;900&family={quote(b_font)}:wght@400;700&display=swap" rel="stylesheet">
    <style>{theme_css}</style>
    {dyn_script}
</head>
<body class="antialiased">
    {index_content}
    <!-- Modal -->
    <div id="modal" class="fixed inset-0 bg-black/80 hidden items-center justify-center z-50" onclick="if(event.target===this) closeModal()">
        <div class="bg-white rounded-2xl max-w-4xl w-[90%] max-h-[90vh] overflow-auto">
            <div class="p-8">
                <img id="modal-img" class="w-full h-96 object-cover rounded-xl mb-6" alt="Product">
                <h2 id="modal-title" class="text-3xl font-black mb-4"></h2>
                <div id="modal-price" class="text-4xl font-bold mb-6" style="color:{s_color}"></div>
                <p id="modal-desc" class="text-gray-700 mb-8"></p>
                <a id="modal-wa" href="#" target="_blank" class="btn-primary block text-center py-4 text-lg">Book via WhatsApp</a>
            </div>
        </div>
    </div>
    <script>function closeModal(){{document.getElementById('modal').classList.add('hidden')}};</script>
</body>
</html>""")

                # Add other pages (about, contact, privacy, terms) similarly...

            zip_buffer.seek(0)
            safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', get("biz_name").lower()) + "_titan_v16.1.zip"

            st.download_button(
                "📥 Download Website Package (.zip)",
                data=zip_buffer,
                file_name=safe_name,
                mime="application/zip",
                use_container_width=True
            )

            # Simple preview
            st.subheader("Quick Preview")
            st.components.v1.html(index_content[:3000], height=600, scrolling=True)

st.caption("© 2026 Kaydiem Script Lab • Titan v16.1 • Optimized for speed & reliability")
