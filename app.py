import streamlit as st
import zipfile
import io
import json
from datetime import datetime

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Kaydiem Titan v13.1 | Full-Site Integrity", layout="wide", page_icon="🏗️")

st.markdown("""
    <style>
    .main { background: #020617; color: white; }
    .stTabs [data-baseweb="tab"] { color: white; font-weight: bold; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4em; 
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%); 
        color: white; font-weight: 900; border: none; font-size: 1.4rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: DESIGN STUDIO ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/business_profile_96dp.png", width=50)
    st.title("Titan v13.1 Studio")
    
    with st.expander("🎨 Brand DNA", expanded=True):
        layout_dna = st.selectbox("Design Style", ["Industrial Titan", "Royal Luxury", "Soft-UI", "Brutalist"])
        p_color = st.color_picker("Primary Color", "#001F3F")
        s_color = st.color_picker("Accent Color", "#FFD700")
        border_rad = st.select_slider("Corner Roundness", options=["0px", "8px", "16px", "40px"], value="16px")

    with st.expander("✍️ Typography", expanded=True):
        h_font = st.selectbox("Heading Font", ["Oswald", "Playfair Display", "Montserrat"])
        b_font = st.selectbox("Body Font", ["Inter", "Roboto", "Open Sans"])

    gsc_tag = st.text_input("GSC Verification Tag")
    st.info("Certified Build: Kaydiem Script Lab")

st.title("🏗️ Kaydiem Titan Supreme v13.1")
st.info("Generating a 5-Page W3C Compliant Industrial Asset with Zero Repetitive AI Copy.")

# --- 2. DATA COLLECTION TABS ---
tabs = st.tabs(["📍 Identity", "🏗️ Services & Story", "🖼️ Images", "🌟 Trust & Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name (NAP)", "Al-Mashael Sulai Boom Truck")
        biz_phone = st.text_input("Verified Phone", "+966 50 000 0000")
        biz_email = st.text_input("Business Email", "info@almashael-rentals.sa")
    with c2:
        biz_cat = st.text_input("Category", "Industrial Equipment Rental")
        biz_hours = st.text_input("Hours", "Sat-Thu: 08:00 - 18:00")
        prod_url = st.text_input("Production URL", "https://kani201012.github.io/site/")
    biz_addr = st.text_area("Full Physical Address")
    map_iframe = st.text_area("Google Map Embed HTML (iframe)")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", "Precision Lifting for Riyadh's Heavy Industry")
    seo_d = st.text_input("Meta Description (160 Chars)")
    # SERVICE INPUTS (Now with unique descriptions to beat the roast)
    st.subheader("Service Breakdown (Unique Descriptions)")
    s1_n = st.text_input("Service 1 Name", "Boom Truck Rental")
    s1_d = st.text_area("Service 1 Description", "High-capacity lifting solutions for construction and logistics.")
    s2_n = st.text_input("Service 2 Name", "Scissor Lift Services")
    s2_d = st.text_area("Service 2 Description", "Vertical access platforms for safe warehouse and facility maintenance.")
    s3_n = st.text_input("Service 3 Name", "Mobile Crane Hire")
    s3_d = st.text_area("Service 3 Description", "Flexible crane operations for tight urban sites and heavy lifting.")
    about_txt = st.text_area("Our Full History (E-E-A-T Content)", height=250)

with tabs[2]:
    hero_img = st.text_input("Hero Image URL", "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?q=80&w=1600")
    feat_img = st.text_input("About Image URL", "https://images.unsplash.com/photo-1581094288338-2314dddb7ecb?q=80&w=1600")

with tabs[3]:
    testi = st.text_area("Testimonials (Name | Role | Quote)", "Eng. Ahmed | Project Manager | Reliable fleet.")
    faqs = st.text_area("FAQ (Question? ? Answer)")
    priv_body = st.text_area("Privacy Policy")
    terms_body = st.text_area("Terms of Service")

# --- 3. THE SUPREME ENGINE V13.1 ---

if st.button("🚀 DEPLOY AUDIT-PROOF 5-PAGE SITE"):
    
    wa_url = f"https://wa.me/{biz_phone.replace(' ', '').replace('+', '')}"
    
    theme_css = f"""
    :root {{ --p: {p_color}; --s: {s_color}; --radius: {border_rad}; }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; padding: 0; width: 100%; overflow-x: hidden; scroll-behavior: smooth; }}
    body {{ font-family: '{b_font}', sans-serif; color: #1e293b; line-height: 1.8; background: #fff; }}
    h1, h2, h3 {{ font-family: '{h_font}', sans-serif; text-transform: uppercase; line-height: 1.1; }}
    .btn-accent {{ background: var(--s); color: #000 !important; padding: 1.2rem 3rem; border-radius: var(--radius); font-weight: 900; transition: 0.3s; display: inline-block; text-decoration:none; text-align:center; }}
    .glass-nav {{ background: rgba(255, 255, 255, 0.98); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.1); position: fixed; top: 0; width: 100%; z-index: 9999; }}
    .hero-mask {{ background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.5)), url('{hero_img}'); background-size: cover; background-position: center; min-height: 80vh; display: flex; align-items: center; justify-content: center; padding-top: 100px; color: white; }}
    .legal-text {{ white-space: pre-wrap; color: #475569; }}
    """

    def get_layout(title, desc, content, is_h=False):
        v_tag = f'<meta name="google-site-verification" content="{gsc_tag}">' if (is_h and gsc_tag) else ""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    {v_tag}
    <title>{title} | {b
