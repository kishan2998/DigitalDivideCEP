import streamlit as st
from database import supabase
from style import apply_styles

st.set_page_config(
    page_title="Digital Skills",
    page_icon="📚"
)

apply_styles()

st.title("🏘️ Community Resources")

st.write(
    "Find places and resources that can provide digital access "
    "and support within the community."
)

st.divider()

response = (
    supabase
    .table("community_resources")
    .select("*")
    .execute()
)

resources = response.data

if not resources:
    st.info("No community resources available yet.")

else:
    for resource in resources:

        with st.container(border=True):

            st.subheader(resource["name"])

            st.write(resource["description"])

            col1, col2 = st.columns(2)

            with col1:
                st.write(
                    f"**📍 Location:** {resource['location']}"
                )

            with col2:
                st.write(
                    f"**📌 Type:** {resource['type']}"
                )

            st.write(
                f"**📞 Contact:** {resource['contact']}"
            )