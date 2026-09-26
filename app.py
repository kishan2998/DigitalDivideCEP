import streamlit as st
from style import apply_styles

st.set_page_config(
    page_title="Digital Bridge",
    page_icon="🌐",
    layout="wide"
)

apply_styles()
# -----------------------------
# HEADER
# -----------------------------

st.title("🌐 Digital Bridge")

st.subheader(
    "Bridging the Digital Divide in Urban Slum Communities"
)

st.write(
    """
    Digital Bridge is a community-focused platform designed to make
    digital learning, online services, and useful community resources
    easier to discover and access.
    """
)

st.divider()


# -----------------------------
# QUICK ACCESS
# -----------------------------

st.header("🚀 Explore Digital Bridge")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("📚 Learn Digital Skills")

    st.write(
        "Learn smartphone, internet, email, online safety, "
        "and other useful digital skills."
    )

    st.page_link(
        "pages/1_Digital_Skills.py",
        label="Explore Skills →"
    )


with col2:

    st.subheader("🏛️ Useful Services")

    st.write(
        "Discover government, education, employment, "
        "and other useful online services."
    )

    st.page_link(
        "pages/2_Useful_Services.py",
        label="Explore Services →"
    )


with col3:

    st.subheader("🏘️ Community Resources")

    st.write(
        "Find community locations that may provide "
        "digital access and assistance."
    )

    st.page_link(
        "pages/3_Community_Resources.py",
        label="Explore Community →"
    )


st.divider()


# -----------------------------
# WHY DIGITAL SKILLS MATTER
# -----------------------------

st.header("💡 Why Digital Skills Matter")

col1, col2 = st.columns(2)

with col1:

    st.write(
        """
        Digital technology is increasingly important for education,
        employment, communication, government services, and everyday life.
        """
    )

    st.write(
        """
        However, access to technology is not only about having a
        smartphone or computer. People also need knowledge,
        confidence, and support to use digital tools effectively.
        """)


with col2:

    st.info(
        """
        🌐 **Digital Bridge focuses on three areas:**

        📚 Digital learning

        🏛️ Access to useful online services

        🏘️ Community-based digital support
        """
    )


st.divider()


# -----------------------------
# PROJECT GOAL
# -----------------------------

st.header("🎯 Project Goal")

st.write(
    """
    The goal of Digital Bridge is to help reduce barriers to
    digital participation by making useful information,
    learning resources, and community support easier to find.
    """
)


st.divider()


# -----------------------------
# FOOTER
# -----------------------------

st.caption(
    "Digital Bridge | Community Engagement Project"
)