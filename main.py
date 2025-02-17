import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Eden Care Claims Follow-Up",
    page_icon=Image.open("logo.png"),
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load logo
logo_url = 'EC_logo.png'
st.sidebar.image(logo_url, use_column_width=True)

# Define custom CSS for styled tabs and content
st.markdown("""
<style>
    .tab {
        font-size: 1.5em;
        font-weight: bold;
        color: #e66c37;
        text-align: center;
        margin: 10px;
        padding: 10px;
        border-radius: 10px;
        background-color: #f8f9fa;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        text-decoration: none;
        display: inline-block;
        width: 100%;
    }
    .tab:hover {
        background-color: #e66c37;
        color: white;
        cursor: pointer;
    }
    .text {
            font-size: 1.1rem;
            color: #333;
            padding: 10px;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
    .separator {
            margin: 2rem 0;
            border-bottom: 2px solid #ddd;
        }
</style>
""", unsafe_allow_html=True)
st.markdown('<h1 class="main-title" style="text-align: center; color: #009DAE;">Eden Care Combined Claims Dashboard</h1>', unsafe_allow_html=True)
# Introduction
st.markdown("""
<div class="text" style="font-size: 1.2em; color: #333; text-align: center;">
   Use the tabs below to navigate to the Executive, Managers, or Operations dashboards depending on your role.
    <strong>Note: ALL</strong> dashboards require authentication and don't forget to click the login button twice
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# Dynamically get the base URL of the app
base_url = st.experimental_get_query_params().get("_", [""])[0]  # Default to empty string if no base URL

# Construct absolute URLs for each dashboard
exec_url = f"{base_url}/exec" if base_url else "https://dorcas-001-claims-for-executives-claims-wjpsbm.streamlit.app/"
managers_url = f"{base_url}/managers" if base_url else "https://dorcas-001-claims-for-managers-claims-wokkfu.streamlit.app/"
operations_url = f"{base_url}/operations" if base_url else "https://dorcas-001-claims-for-operators-claims-mb8flj.streamlit.app/"

# Create tabs for redirection
tab_titles = ["Executive Dashboard", "Managers Dashboard", "Operations Dashboard"]
tabs = st.tabs(tab_titles)

# Main Title

st.image("Tiny doctor giving health insurance.jpg", caption='Eden Care Medical', use_column_width=True)







with tabs[0]:  # Executive Dashboard Tab
    st.markdown(f'<div class="tab"><a href="{exec_url}" target="_self">Executive Dashboard</a></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.2em; color: #333; text-align: center;">The Executive Dashboard provides high-level insights into claims management performance.</p>', unsafe_allow_html=True)

with tabs[1]:  # Managers Dashboard Tab
    st.markdown(f'<div class="tab"><a href="{managers_url}" target="_self">Managers Dashboard</a></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.2em; color: #333; text-align: center;">The Managers Dashboard offers detailed analysis of claims by product, provider, and client.</p>', unsafe_allow_html=True)

with tabs[2]:  # Operations Dashboard Tab
    st.markdown(f'<div class="tab"><a href="{operations_url}" target="_self">Operations Dashboard</a></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 1.2em; color: #333; text-align: center;">The Operations Dashboard focuses on operational efficiency and day-to-day activities.</p>', unsafe_allow_html=True)