import streamlit as st
import zipfile
import io
import json
from datetime import datetime

# --- 1. APP CONFIGURATION ---
# Sets the browser tab title, favicon, and wide-screen layout
st.set_page_config(
    page_title="Kaydiem Titan v25.0 | Sovereign Architect",
    layout="wide",
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# ---- LIGHT THEME ADMIN CSS (Professional / Minimal) ----
st.markdown(
    """
    <style>
    /* Root and container sizing */
    :root{
        --bg: #f8fafc;
        --card: #ffffff;
        --muted: #64748b;
        --accent: #0f172a;
        --accent-2: #0ea5a6;
        --radius: 12px;
        --glass: rgba(15,23,42,0.04);
    }

    /* Page background & main container */
    body, .main {
        background: var(--bg) !important;
        color: var(--accent) !important;
        font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    /* Block container width for better reading */
    .block-container {
        max-width: 1100px;
        padding-top: 28px;
        padding-bottom: 48px;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%) !important;
        border-right: 1px solid #e6eef5;
        box-shadow: 0 6px 24px rgba(16,24,40,0.06);
        padding: 20px 18px;
        width: 320px;
    }
    [data-testid="stSidebar"] .stImage {
        margin-bottom: 8px;
    }
    .stSidebar .stButton>button {
        border-radius: 10px;
    }

    /* Card / expander polish */
    .stExpander {
        background: var(--card) !important;
        border: 1px solid #eef4f8 !important;
        box-shadow: 0 6px 18px rgba(16,24,40,0.04);
        border-radius: var(--radius) !important;
        padding: 12px !important;
    }

    /* Inputs (text, textarea, select) */
    input, textarea, select {
        background: #ffffff !important;
        color: var(--accent) !important;
        border: 1px solid #e6eef5 !important;
        padding: 12px !important;
        border-radius: 8px !important;
        box-shadow: none !important;
        font-size: 15px !important;
    }
    textarea {
        min-height: 120px !important;
    }
    .stTextInput>div>label, .stTextArea>div>label, .stSelectbox>div>label {
        color: var(--accent) !important;
        font-weight: 600;
        margin-bottom: 6px;
        display:block;
    }

    /* Buttons (primary) */
    .stButton>button {
        background: linear-gradient(90deg, var(--accent) 0%, var(--accent-2) 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 1.2rem !important;
        border-radius: 12px !important;
        font-weight: 700;
        box-shadow: 0 8px 24px rgba(14,165,166,0.12) !important;
        transition: transform .12s ease;
    }
    .stButton>button:hover { transform: translateY(-3px); }

    /* Checkbox / slider adjustments */
    .stCheckbox, .stRadio {
        margin-top: 6px;
        color: var(--muted);
    }

    /* Tabs styling (the big horizontal tabs) */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; margin-bottom: 16px; }
    .stTabs [data-baseweb="tab"] {
        background: #ffffff;
        border-radius: 10px;
        padding: 8px 14px;
        border: 1px solid #eef4f8;
        color: var(--muted);
        font-weight: 700;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #ecfdfd 0%, #ffffff 100%);
        color: var(--accent) !important;
        box-shadow: 0 6px 18px rgba(14,165,166,0.06);
        border: 1px solid rgba(14,165,166,0.12);
    }

    /* Form sections: cards */
    .card {
        background: var(--card);
        border-radius: 14px;
        padding: 18px;
        border: 1px solid #eef4f8;
        box-shadow: 0 6px 20px rgba(16,24,40,0.04);
        margin-bottom: 18px;
    }

    /* Headings */
    h1, h2, h3 { color: var(--accent); font-weight: 800; }
    .subtle { color: var(--muted); font-weight: 500; }

    /* Small helper info boxes */
    .helper {
        background: #f1fbfb;
        border-left: 3px solid rgba(14,165,166,0.12);
        color: #0f4660;
        padding: 10px 12px;
        border-radius: 8px;
    }

    /* Make Streamlit components consistent spacing */
    .stMarkdown, .stText, .stHeader {
        margin-bottom: 10px;
    }

    /* Compact the sidebar form controls a bit */
    [data-testid="stSidebar"] .stTextInput, [data-testid="stSidebar"] .stSelectbox, [data-testid="stSidebar"] .stColorPicker {
        margin-bottom: 12px !important;
    }

    /* Make the preview embed area visually lighter */
    .stComponents iframe {
        border-radius: 12px;
        border: 1px solid #eef4f8;
        box-shadow: 0 10px 30px rgba(16,24,40,0.06);
    }

    /* Responsive tweaks */
    @media (max-width: 900px) {
        .block-container { padding-left: 20px; padding-right: 20px; }
        [data-testid="stSidebar"] { width: 100% !important; position: relative; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 2. SIDEBAR: THE DESIGN STUDIO ---
with st.sidebar:
    # Laboratory Branding
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=56)
    st.title("Titan v25.0 Studio")
    st.caption("Fulfilling 1,000+ Assets Daily")
    st.divider()

    # Pillar 1: Layout & DNA (Structural Branching)
    with st.expander("🎭 1. Architecture DNA", expanded=True):
        layout_dna = st.selectbox("Select Site DNA", [
            "Industrial Titan", "Classic Royal", "Glass-Tech SaaS",
            "The Bento Grid", "Brutalist Bold", "Corporate Elite",
            "Minimalist Boutique", "Midnight Stealth", "Vivid Creative", "Clean Health"
        ], help="This changes the actual HTML structure of the generated asset.")

        col1, col2 = st.columns(2)
        with col1:
            p_color = st.color_picker("Primary Color", "#0f172a")
        with col2:
            s_color = st.color_picker("Accent (CTA)", "#0ea5a6")

        # Fixed Slider: Value '24px' matches the options list
        border_rad = st.select_slider(
            "Corner Sharpness",
            options=["0px", "4px", "12px", "24px", "40px", "60px"],
            value="24px"
        )

    # Pillar 2: Typography Studio (Pairing Logic)
    with st.expander("✍️ 2. Typography Studio", expanded=True):
        h_font = st.selectbox("Heading Font",
            ["Montserrat", "Playfair Display", "Oswald", "Syncopate", "Space Grotesk"],
            index=0)

        b_font = st.selectbox("Body Text Font",
            ["Inter", "Roboto", "Open Sans", "Work Sans", "Lora"],
            index=0)

        h_weight = st.select_slider(
            "Heading Weight",
            options=["300", "400", "700", "900"],
            value="900"
        )

        ls = st.select_slider(
            "Letter Spacing (Tracking)",
            options=["-0.05em", "-0.02em", "0em", "0.05em", "0.1em"],
            value="-0.02em"
        )

    # Pillar 3: Technical SEO Tags
    with st.expander("⚙️ 3. Technical Verification"):
        gsc_tag_input = st.text_input("GSC Meta Tag Content", placeholder="google-site-verification=...")
        canonical_check = st.checkbox("Force Canonical Mapping", value=True)

    st.divider()
    st.info("Technical Lead: Kiran Deb Mondal\nwww.kaydiemscriptlab.com")

# --- 3. DATA COLLECTION ---
st.title("🏗️ Kaydiem Titan Supreme Engine v25.0")
st.caption("Precision Engineering for Local SEO Dominance")

# Create the 6 Pillars of Onboarding
tabs = st.tabs(["📍 Identity", "🏗️ Content & SEO", "🖼️ Assets", "⚡ Live E-com", "🌟 Social Proof", "⚖️ Legal"])

with tabs[0]:
    st.subheader("Core Business Identity (NAP Compliance)")
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            biz_name = st.text_input("Business Name", "Red Hippo (The Planners)", help="Must match Google Maps exactly.")
            biz_phone = st.text_input("Verified Phone", "+91 84540 02711", help="Include country code.")
            biz_email = st.text_input("Business Email", "events@redhippoplanners.in")
        with c2:
            biz_cat = st.text_input("Primary Category", "Luxury Wedding Planner")
            biz_hours = st.text_input("Operating Hours", "Mon-Sun: 10:00 - 19:00")
            prod_url = st.text_input("Production URL", "https://kani201012.github.io/site/", help="The final live link.")

    biz_logo = st.text_input("Logo Image URL", help="Direct link to a PNG/SVG file.")
    biz_addr = st.text_area("Full Maps Physical Address", help="Point #8: Crawlable NAP data.")
    biz_areas = st.text_area("Service Areas (Comma separated)", "Vasant Kunj, Chhatarpur, South Delhi, Riyadh", help="Used for Geo-Schema Injection.")
    map_iframe = st.text_area("Map Embed HTML Code", placeholder="Paste the <iframe> from Google Maps here.")

with tabs[1]:
    st.subheader("AI-Search Content & Meta Layer")
    hero_h = st.text_input("Main Hero Headline", "Crafting Dream Weddings: New Delhi's Premier Luxury Decorators")
    seo_d = st.text_input("Meta Description (160 Chars)", "Verified 2026 AI-Ready Industrial Assets.", help="Point #11: Technical Meta Precision.")
    biz_key = st.text_input("Target SEO Keywords", help="Separate by commas.")

    col_s1, col_s2 = st.columns([2,1])
    with col_s1:
        biz_serv = st.text_area("Services Listing (One per line)", "Floral Decor\nThematic Lighting\nVenue Sourcing")
    with col_s2:
        st.markdown('<div class="helper">💡 Pro Tip: Every service listed here is wrapped in H3 Semantic Tags for Googlebot clarity.</div>', unsafe_allow_html=True)

    about_txt = st.text_area("Our Authority Story (E-E-A-T Content)", height=350,
                             placeholder="Write 800+ words here to satisfy Google's Trust Audit (Point #9).")

with tabs[2]:
    st.header("📸 High-Ticket Asset Manager")
    st.write("Ensure your site is visually 'Full' to build trust.")
    custom_hero = st.text_input("Hero Background URL", placeholder="Industrial/Luxury high-res image.")
    custom_feat = st.text_input("Feature Section Image URL", placeholder="Fleet/Office/Equipment image.")
    custom_gall = st.text_input("About Section Image URL", placeholder="Team/History/Factory image.")

with tabs[3]:
    st.header("🛒 Headless E-commerce Bridge")
    st.info("Update your prices from your phone. Publish your Google Sheet as CSV and paste below.")
    sheet_url = st.text_input("Published CSV Link", placeholder="https://docs.google.com/spreadsheets/d/.../pub?output=csv")
    st.warning("Ensure your sheet columns are: Name | Price | Description | Img1 | Img2 | Img3")

with tabs[4]:
    st.header("🌟 Trust & Social Proof")
    testi_raw = st.text_area("Testimonials (Name | Quote)", "Aramco | Reliable Partner.\nNEOM | Best in class.")
    faq_raw = st.text_area("F.A.Q. (Question? ? Answer)", "Are you certified? ? Yes, we are ISO 2026 compliant.")

with tabs[5]:
    st.header("⚖️ Authoritative Legal Hub")
    priv_body = st.text_area("Full Privacy Policy Content", height=250)
    terms_body = st.text_area("Full Terms & Conditions Content", height=250)

# --- 4. GLOBAL DATA SYNCHRONIZATION (The "Zero-Defect" Layer) ---

# 4.1 Process WhatsApp Link
wa_clean = biz_phone.replace(" ", "").replace("+", "")
wa_final_url = f"https://wa.me/{wa_clean}?text=Hello%20{biz_name.replace(' ', '%20')}"

# 4.2 Process Geo-Areas for JSON-LD Schema
area_list = [a.strip() for a in biz_areas.split(",") if a.strip()]
s_areas_json = json.dumps(area_list)

# 4.3 Setup High-Resolution Image Fallbacks
img_h = custom_hero if custom_hero else "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&q=80&w=1600"
img_f = custom_feat if custom_feat else "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&q=80&w=800"
img_g = custom_gall if custom_gall else "https://images.unsplash.com/photo-1532712938310-34cb3982ef74?auto=format&fit=crop&q=80&w=1600"

# 4.4 Logo Logic
logo_html = f'<img src="{biz_logo}" alt="{biz_name}" class="h-10 md:h-16 w-auto object-contain">' if biz_logo else f'<span class="text-xl md:text-3xl font-black tracking-tighter uppercase" style="color:var(--p)">{biz_name}</span>'

# --- 5.1 THE CSS MASTER STYLE (Every brace {{ }} is double-escaped for stability) ---
master_css = f"""
:root {{
    --p: {p_color}; --s: {s_color}; --radius: {border_rad};
    --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif;
    --h-weight: {h_weight}; --ls: {ls};
}}
* {{ box-sizing: border-box; -webkit-font-smoothing: antialiased; }}
html, body {{ margin: 0; padding: 0; width: 100%; overflow-x: hidden; scroll-behavior: smooth; }}
body {{ font-family: var(--b-font); color: #0f172a; line-height: 1.7; background: #fff; }}
h1, h2, h3 {{ font-family: var(--h-font); font-weight: var(--h-weight); letter-spacing: var(--ls); text-transform: uppercase; line-height: 1.1; }}

/* ... (your existing master site CSS kept as-is for asset generation) ... */
.hero-title {{ font-size: clamp(2rem, 8vw, 100px); text-shadow: 0 4px 20px rgba(0,0,0,0.04); }}
.section-title {{ font-size: clamp(1.8rem, 6vw, 75px); color: var(--p); text-align: center; margin-bottom: 3rem; }}
.btn-accent {{ background: var(--s); color: white !important; padding: 1.1rem 2.8rem; border-radius: var(--radius); font-weight: 900; transition: 0.4s; display: inline-block; text-align: center; border:none; text-decoration:none; cursor: pointer; box-shadow: 0 10px 20px -5px var(--s); }}
.btn-accent:hover {{ transform: translateY(-3px); filter: brightness(1.1); box-shadow: 0 15px 30px -5px var(--s); }}
.hero-mask {{ background: linear-gradient(rgba(0,0,0,0.06), rgba(0,0,0,0.03)), url('{img_h}'); background-size: cover; background-position: center; min-height: 60vh; display: flex; align-items: center; justify-content: center; width: 100%; padding: 80px 20px 40px 20px; }}
.legal-text {{ white-space: pre-wrap; font-size: 1.05rem; color: #334155; line-height: 1.9; }}
#modal {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.65); z-index: 100000; padding: 1rem; align-items: center; justify-content: center; overflow-y: auto; }}
.modal-content {{ background: white; max-width: 1000px; width: 100%; border-radius: var(--radius); overflow: hidden; }}
"""

def build_sovereign_html(page_title, page_desc, content_body, is_home=False):
    v_tag = f'<meta name="google-site-verification" content="{gsc_tag_input}">' if (is_home and gsc_tag_input) else ""

    dyn_script = ""
    if is_home and sheet_url:
        dyn_script = f\"\"\"
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
                            <img src="${{p.img1}}" class="w-full h-56 object-cover mb-6 rounded-[2rem] bg-slate-50" onerror="this.src='{img_f}'">
                            <div>
                                <h3 class="text-2xl font-black mb-2 uppercase" style="color:var(--p)">${{p.name}}</h3>
                                <p class="font-black text-2xl mb-4 text-s" style="color:var(--s)">${{p.price}}</p>
                                <p class="text-slate-400 text-[10px] font-black uppercase tracking-widest italic underline decoration-slate-100 underline-offset-4">Click to Open →</p>
                            </div>
                        </div>`;
                    }}
                }});
            }} catch (e) {{ console.log("Fail", e); }}
        }}
        function openProduct(id) {{
            const p = currentProducts[id];
            document.getElementById('m-title').innerText = p.name;
            document.getElementById('m-price').innerText = p.price;
            document.getElementById('m-desc').innerText = p.desc;
            document.getElementById('m-img-1').src = p.img1;
            document.getElementById('m-wa').href = "{wa_final_url}" + encodeURIComponent(" (Interest in " + p.name + ")");
            document.getElementById('modal').style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }}
        function closeModal() {{ document.getElementById('modal').style.display='none'; document.body.style.overflow='auto'; }}
        window.onload = fetchLiveData;
        </script>
        \"\"\"

    c_badges = "".join([f'<span class="bg-slate-800 text-[10px] px-3 py-1 rounded-full uppercase font-bold text-white border border-slate-700 tracking-widest">{a}</span>' for a in area_list])

    return f\"\"\"<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    {v_tag}<title>{page_title} | {biz_name}</title><meta name="description" content="{page_desc}">
    <link rel="canonical" href="{prod_url}"><script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@700;900&family={b_font.replace(' ', '+')}:wght@400;700&display=swap" rel="stylesheet">
    <style>{master_css}</style>
    <script type="application/ld+json">
    {{ "@context": "https://schema.org", "@type": "LocalBusiness", "name": "{biz_name}", "address": {{ "@type": "PostalAddress", "streetAddress": "{biz_addr}" }}, "telephone": "{biz_phone}", "areaServed": {s_areas_json} }}
    </script>
</head>
<body class="bg-white flex flex-col min-h-screen text-slate-900">
    <nav class="glass-nav p-4 md:p-6 shadow-sm"><div class="max-w-[1440px] mx-auto flex justify-between items-center"><a href="index.html" class="no-underline">{logo_html}</a>
    <div class="hidden md:flex space-x-12 text-[10px] md:text-xs font-black uppercase tracking-widest text-slate-600"><a href="index.html" class="no-underline hover:text-blue-600">Home</a> <a href="about.html" class="no-underline hover:text-blue-600">About</a> <a href="contact.html" class="no-underline hover:text-blue-600">Contact</a></div>
    <a href="tel:{biz_phone}" class="btn-accent" style="padding: 0.5rem 1.5rem; font-size: 10px;">CALL NOW</a></div></nav>
    <main class="flex-grow pt-24 md:pt-0">{content_body}</main>

    <div id="modal" onclick="if(event.target == this) closeModal()"><div class="modal-content shadow-2xl animate-in zoom-in duration-300">
    <div class="grid md:grid-cols-2"><div class="p-6 bg-slate-50 flex items-center justify-center"><img id="m-img-1" class="w-full h-auto rounded-[3rem] shadow-xl border-4 border-white"></div>
    <div class="p-12 flex flex-col justify-center text-left"><h2 id="m-title" class="text-4xl font-black mb-4 uppercase" style="color:var(--p)"></h2><p id="m-price" class="text-3xl font-black mb-8 text-s" style="color:var(--s)"></p>
    <p id="m-desc" class="text-slate-600 mb-10 text-lg legal-text"></p><a id="m-wa" href="#" target="_blank" class="btn-accent w-full uppercase shadow-2xl">Confirm Booking</a>
    <button onclick="closeModal()" class="text-xs font-black uppercase mt-8 underline no-underline opacity-30 text-center w-full">Close Window</button></div></div></div></div>

    <a href="https://wa.me/{wa_clean}" class="wa-float" target="_blank"><svg style="width:38px;height:38px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.10-.8-.30-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.10-.45-1.08-.62-1.48c-.16-.40-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></svg></a>

    <footer class="bg-slate-950 text-slate-500 py-32 px-10 border-t border-slate-900"><div class="max-w-[1440px] mx-auto grid md:grid-cols-4 gap-16 text-left">
    <div class="col-span-2"><h4 class="text-white text-3xl font-black mb-8 uppercase tracking-tighter uppercase leading-none">{biz_name}</h4><p class="text-sm leading-relaxed mb-10 max-w-md opacity-80">{biz_addr}</p><div class="flex flex-wrap gap-2">{c_badges}</div></div>
    <div><h4 class="text-white font-bold mb-8 uppercase text-xs tracking-widest">Company Hub</h4><ul class="space-y-4 text-sm font-bold uppercase list-none p-0"><li><a href="privacy.html" class="no-underline">Privacy Policy</a></li><li><a href="terms.html" class="no-underline">Terms & Conditions</a></li></ul></div>
    <div class="md:text-right"><h4 class="text-white font-bold mb-8 uppercase text-xs text-brand tracking-widest underline decoration-blue-600 decoration-4 underline-offset-8 uppercase tracking-widest" style="color:var(--s)">Direct Connect</h4><p class="text-xl mt-4 font-black text-white">{biz_phone}</p><p class="text-xs mt-2">{biz_email}</p></div></div>
    <div class="text-center mt-20 opacity-20 text-[10px] uppercase font-black tracking-widest italic tracking-widest underline decoration-white underline-offset-8 text-white text-decoration-none">Architected By <a href="https://www.kaydiemscriptlab.com" class="text-white underline">Kaydiem Script Lab</a></div></footer>{dyn_script}
</body></html>\"\"\"

# --- 5.2 STRUCTURAL DNA SWITCH (same logic as before) ---
s_cards_html = "".join([f'<div class="bg-slate-50 p-12 rounded-[2.5rem] border border-slate-100 shadow-xl hover:scale-[1.02] transition-transform"><h3 class="text-2xl font-black mb-4 uppercase" style="color:var(--p)">{s.strip()}</h3><p class="text-slate-500 text-sm font-bold uppercase tracking-tight italic text-left">Verified technical solution.</p></div>' for s in biz_serv.splitlines() if s.strip()])
t_html = "".join([f'<div class="p-10 bg-slate-50 rounded-[3rem] border border-slate-100 italic text-xl shadow-inner mb-8" style="color:var(--p)">"{t.split("|")[1].strip()}"<br><span class="font-black not-italic text-sm block mt-6 uppercase tracking-widest text-brand" style="color:var(--p)">— {t.split("|")[0].strip()} <span class="text-emerald-500 font-black ml-2 text-xs">● Verified Partner</span></span></div>' for t in testi_raw.splitlines() if "|" in t])
f_html = "".join([f'<details class="mb-6 bg-white p-6 rounded-2xl border border-slate-100 cursor-pointer shadow-sm"><summary class="font-black text-lg uppercase tracking-tight">{f.split("?")[0].strip()}?</summary><p class="mt-4 text-slate-600 leading-relaxed font-medium text-sm">{f.split("?")[1].strip()}</p></details>' for f in faq_raw.splitlines() if "?" in f])

if layout_dna == "Industrial Titan":
    idx_content = f\"\"\"
    <section class="hero-mask px-6 text-center text-white"><div class="max-w-[1200px] mx-auto"><h1 class="hero-title mb-10 uppercase tracking-tighter leading-none font-black">{hero_h}</h1><p class="text-lg md:text-3xl font-light mb-16 max-w-4xl mx-auto opacity-90 leading-tight">{seo_d}</p><a href="#inventory" class="btn-accent uppercase tracking-[0.4em] text-[10px] md:text-sm shadow-2xl" style="background:var(--p)">Direct Booking</a></div></section>
    <section class="max-w-[1440px] mx-auto py-24 px-6 grid md:grid-cols-2 gap-24 items-center border-b text-left"><img src="{img_f}" class="shadow-2xl rounded-[var(--radius)] border-8 border-slate-50"><div><h2 class="section-title mb-12 uppercase tracking-tighter leading-none" style="color:var(--p); text-align:left;">Our Expertise</h2><div class="grid gap-6 text-left">{s_cards_html}</div><a href="about.html" class="btn-p mt-10 no-underline" style="background:var(--p); color:white; padding:1.2rem 3rem; border-radius:var(--radius);">Read History</a></div></section>
    <section id="inventory" class="py-32 px-6 max-w-[1440px] mx-auto text-center border-b"><h2 class="section-title mb-20 uppercase tracking-tighter">Live Inventory</h2><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-4 gap-10 text-left"><p class="p-20 text-center text-slate-400 font-bold animate-pulse uppercase tracking-widest">Opening Data Hub...</p></div></section>
    <section class="py-32 px-6 max-w-7xl mx-auto text-center"><div class="grid md:grid-cols-2 gap-24 text-left"><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Success</h2>{t_html}</div><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Insights</h2>{f_html}</div></div></section>
    \"\"\"
elif layout_dna == "Classic Royal":
    idx_content = f\"\"\"
    <section class="hero-mask px-6 text-center text-white"><div class="max-w-[1200px] mx-auto"><h1 class="hero-title mb-10 tracking-tighter leading-none font-serif normal-case italic" style="font-family: 'Playfair Display', serif;">{hero_h}</h1><p class="text-lg md:text-3xl mb-16 italic opacity-80 leading-tight">{seo_d}</p><a href="#inventory" class="btn-accent tracking-widest text-[10px] md:text-sm shadow-2xl">Enter Showroom</a></div></section>
    <section class="bg-white py-40 px-6 text-center border-b"><div class="max-w-4xl mx-auto"><h2 class="section-title mb-20 font-serif normal-case italic underline decoration-blue-600 underline-offset-8" style="color:var(--p)">Proven Reputation</h2>{t_html}</div></section>
    <section id="inventory" class="py-40 px-6 max-w-[1440px] mx-auto text-center border-b"><h2 class="section-title mb-24 font-serif normal-case italic" style="color:var(--p)">The Collection</h2><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-3 gap-20"></div></section>
    <section class="max-w-[1440px] mx-auto py-24 px-6 grid md:grid-cols-2 gap-24 items-center border-t border-slate-100 text-left"><div class="order-2 md:order-1"><h2 class="section-title mb-12" style="text-align:left;">Elite Expertise</h2><div class="grid gap-6">{s_cards_html}</div><a href="about.html" class="btn-p mt-10 no-underline" style="background:var(--p); color:white; padding:1.2rem 3rem; border-radius:var(--radius);">Read Our Legacy</a></div><img src="{img_f}" class="order-1 md:order-2 shadow-2xl rounded-[var(--radius)]"></section>
    \"\"\"
else:
    idx_content = f\"\"\"
    <section class="hero-mask px-6 text-center text-white"><div class="max-w-[1200px] mx-auto"><h1 class="hero-title mb-10">{hero_h}</h1><p class="mb-10 opacity-70">{seo_d}</p><a href="#inventory" class="btn-accent shadow-2xl">Access Data Hub</a></div></section>
    <section class="p-10 max-w-[1440px] mx-auto grid md:grid-cols-3 gap-8 text-left">
        <div class="md:col-span-2 bg-slate-900 p-20 rounded-[4rem] text-white flex flex-col justify-center shadow-2xl"><h2 class="text-7xl font-black mb-8 tracking-tighter uppercase leading-none">Authority Heritage</h2><p class="text-xl opacity-60 mb-10 italic">"Transforming industrial and luxury landscapes since inception."</p><a href="about.html" class="btn-p w-fit no-underline" style="background:var(--p); color:white; padding:1.2rem 3rem; border-radius:var(--radius);">Full Story</a></div>
        <div class="bg-slate-50 p-12 rounded-[4rem] border shadow-xl flex flex-col justify-center"><p class="text-xs uppercase font-black tracking-widest opacity-30 mb-4 tracking-widest">Direct Contact</p><p class="text-4xl font-black leading-none mb-10" style="color:var(--p)">{biz_phone}</p><a href="tel:{biz_phone}" class="btn-accent w-full no-underline uppercase tracking-widest font-black shadow-2xl">Voice Connect</a></div>
    </section>
    <section id="inventory" class="py-40 px-6 max-w-[1440px] mx-auto text-center border-t border-slate-100"><h2 class="section-title mb-24 uppercase tracking-tighter">Exclusive Offers</h2><div id="live-data-container" class="grid grid-cols-1 md:grid-cols-4 gap-12 text-left"></div></section>
    <section class="p-20 text-center"><h2 class="section-title mb-20 uppercase tracking-tighter">Technical Capabilities</h2><div class="grid md:grid-cols-3 gap-10 text-left">{s_cards_html}</div></section>
    <section class="py-32 px-6 bg-slate-50 border-y"><div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-24 text-left"><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Partners</h2>{t_html}</div><div><h2 class="text-4xl font-black mb-16 uppercase tracking-tighter" style="color:var(--p)">Insights</h2>{f_html}</div></div></section>
    \"\"\"

# --- 6. PREVIEW & ZIP PACKAGING ---
st.header("⚡ Live Technical Preview (v25.0)")
full_asset_html = build_sovereign_html("Home", seo_d, idx_content, True)

if st.checkbox("Activate Full Live Site Preview"):
    st.components.v1.html(full_asset_html, height=800, scrolling=True)

if st.button("🚀 DEPLOY & DOWNLOAD THE WORLD'S BEST BUSINESS ASSET"):
    z_b = io.BytesIO()
    with zipfile.ZipFile(z_b, "w", zipfile.ZIP_DEFLATED) as z_f:
        z_f.writestr("index.html", build_sovereign_html("Home", seo_d, idx_content, True))
        z_f.writestr("about.html", build_sovereign_html("About Us", "History", f"<section class='max-w-7xl mx-auto py-40 px-10'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>About Our Heritage</h1><div class='text-xl md:text-2xl leading-relaxed text-slate-700 legal-text'>{about_txt}</div><img src='{img_g}' class='mt-20 w-full h-[600px] object-cover shadow-2xl' style='border-radius: var(--radius)'></section>"))
        z_f.writestr("contact.html", build_sovereign_html("Contact", "Location", f"<section class='max-w-[1440px] mx-auto py-32 px-6 text-center'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>Technical Hub</h1><div class='grid md:grid-cols-2 gap-16 text-left'><div class='bg-slate-950 p-12 md:p-24 text-white' style='border-radius: var(--radius)'><p class='text-4xl font-black mb-8 text-white'>{biz_phone}</p><p class='text-2xl mb-12 opacity-80 text-white'>{biz_addr}</p><a href='tel:{biz_phone}' class='btn-accent w-full no-underline uppercase tracking-widest font-black shadow-2xl'>Book Consultation</a></div><div class='rounded-[3rem] overflow-hidden border shadow-2xl bg-slate-100' style='min-height:300px'>{map_iframe}</div></div></section>"))
        z_f.writestr("privacy.html", build_sovereign_html("Privacy", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>Privacy Policy</h1><div class='text-lg legal-text'>{priv_body}</div></div>"))
        z_f.writestr("terms.html", build_sovereign_html("Terms", "Legal", f"<div class='max-w-4xl mx-auto py-32 px-10'><h1 class='legal-bold-title uppercase tracking-tighter text-brand' style='color:var(--p)'>Terms & Conditions</h1><div class='text-lg legal-text'>{terms_body}</div></div>"))
        z_f.writestr("404.html", build_sovereign_html("404", "Not Found", "<div class='py-64 text-center'><h1 class='text-[150px] font-black uppercase text-slate-200 tracking-widest leading-none'>404</h1><p class='text-2xl font-black uppercase -mt-10 opacity-30'>Not Found</p><a href='index.html' class='btn-accent mt-20 no-underline'>Return Home</a></div>"))
        z_f.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}sitemap.xml")
        z_f.writestr("sitemap.xml", f"<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'><url><loc>{prod_url}index.html</loc></url><url><loc>{prod_url}about.html</loc></url></urlset>")

    st.success("💎 TITAN SOVEREIGN v25.0 DEPLOYED. Zero Defects Confirmed.")
    st.download_button("📥 DOWNLOAD PLATINUM ASSET", z_b.getvalue(), file_name=f"{biz_name.lower().replace(' ', '_')}_final.zip")
