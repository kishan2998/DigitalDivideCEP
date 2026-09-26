import streamlit as st
from database import supabase
from style import apply_styles

st.set_page_config(
    page_title="Digital Skills",
    page_icon="📚"
)

apply_styles()

st.title("ℹ️ About Digital Bridge")

st.write(
    """
    Digital Bridge is a community-focused platform created to help
    bridge the digital divide in underserved urban communities.
    """
)

st.divider()

st.header("🎯 Our Goal")

st.write(
    """
    The goal of Digital Bridge is to make digital learning,
    online services, and community resources easier to discover
    and access.
    """
)

st.header("📚 What We Provide")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("📱 Digital Skills")

    st.write(
        "Simple resources for learning smartphone, internet, "
        "email, online safety, and other digital skills."
    )

with col2:

    st.subheader("🏛️ Useful Services")

    st.write(
        "Information about useful government, education, "
        "employment, and digital services."
    )

with col3:

    st.subheader("🏘️ Community Resources")

    st.write(
        "Information about places that may provide digital "
        "access, learning, or assistance."
    )

st.divider()

st.header("💡 Why This Matters")

st.write(
    """
    Access to technology is not only about having a device.
    People also need digital skills, reliable information,
    and support to use online services confidently.
    """
)

st.info(
    "🌐 Digital Bridge aims to make technology more accessible, "
    "useful, and easier to understand."
)

st.divider()

st.caption(
    "Digital Bridge — Bridging the Digital Divide in Urban Slum Communities"
)