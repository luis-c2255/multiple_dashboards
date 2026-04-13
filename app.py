import streamlit as st
from utils.theme import Components


st.set_page_config(
    page_title=f"Multiple Dataset Analysis",
    page_icon="📊",
    layout="wide"
    )

try:
    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

st.markdown(Components.page_header("📊 Multiple Dataset Analysis"), unsafe_allow_html=True)


st.markdown("""
<div style='text-align: center; color: #666; font-size: 1.8rem;'>
    <p><strong>Use the buttons to navigate to the different dashboards created with datasets analysis of several topics.</strong></p>
</div>
""", unsafe_allow_html=True)


st.markdown("   ")
st.markdown("   ")

with st.container(height="content", width="stretch", horizontal_alignment="center"):
    st.image("image.svg")
    
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("Dashboard Number 1",
    "https://analytics-1-trjcz7qln7bv2sskobjeua.streamlit.app/",
    icon="1️⃣", icon_position="left", width="stretch"
    )
with col2:
    st.link_button("Dashboard Number 2",
    "https://analytics2.streamlit.app/",
    icon="2️⃣", icon_position="left", width="stretch"
    )
with col3:
    st.link_button("Dashboard Number 3",
    "https://analytics3-bm439rd2y4n9b2xlst9gvb.streamlit.app/",
    icon="3️⃣", icon_position="left", width="stretch"
    )
    
col4, col5 = st.columns(2)
with col4:
    st.link_button("Dashboard Number 4",
    "https://analytics4-0.streamlit.app/",
    icon="4️⃣", icon_position="left", width="stretch"
    )
with col5:
    st.link_button("Dashboard Number 5",
    "https://analytics5-2.streamlit.app/",
    icon="5️⃣", icon_position="left", width="stretch"
    )
    
# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>📊 Multiple Analysis Dashboard</strong></p>
    <p>Multiple Dashboards from several datasets analyzed</p>
    <p style='font-size: 0.9rem;'>Navigate using the buttons</p>
</div>
""", unsafe_allow_html=True)
