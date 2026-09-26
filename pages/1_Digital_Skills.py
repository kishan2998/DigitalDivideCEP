import streamlit as st
from database import supabase
from style import apply_styles

st.set_page_config(
    page_title="Digital Skills",
    page_icon="📚"
)

apply_styles()
st.title("📚 Digital Skills")

st.write(
    "Learn useful digital skills through simple resources."
)

st.divider()

# Get resources from Supabase
response = (
    supabase
    .table("resources")
    .select("*")
    .execute()
)

resources = response.data

if not resources:
    st.info("No learning resources available yet.")

else:

    # -----------------------------
    # SEARCH
    # -----------------------------

    search = st.text_input(
        "🔎 Search resources",
        placeholder="Try: smartphone, internet, safety..."
    )

    # -----------------------------
    # FILTERS
    # -----------------------------

    categories = sorted(
        set(resource["category"] for resource in resources)
    )

    difficulties = sorted(
        set(resource["difficulty"] for resource in resources)
        if any(resource["difficulty"] for resource in resources)
        else []
    )

    col1, col2 = st.columns(2)

    with col1:
        selected_category = st.selectbox(
            "Category",
            ["All"] + categories
        )

    with col2:
        selected_difficulty = st.selectbox(
            "Difficulty",
            ["All"] + difficulties
        )

    # -----------------------------
    # FILTER DATA
    # -----------------------------

    filtered_resources = resources

    if search:
        filtered_resources = [
            resource
            for resource in filtered_resources
            if search.lower() in (
                resource["title"] + " " +
                resource["description"] + " " +
                resource["category"]
            ).lower()
        ]

    if selected_category != "All":
        filtered_resources = [
            resource
            for resource in filtered_resources
            if resource["category"] == selected_category
        ]

    if selected_difficulty != "All":
        filtered_resources = [
            resource
            for resource in filtered_resources
            if resource["difficulty"] == selected_difficulty
        ]

    st.divider()

    # -----------------------------
    # DISPLAY RESULTS
    # -----------------------------

    st.write(
        f"**{len(filtered_resources)} resource(s) found**"
    )

    if not filtered_resources:

        st.warning(
            "No resources match your search or filters."
        )

    else:

        for resource in filtered_resources:

            with st.container(border=True):

                st.subheader(resource["title"])

                st.write(resource["description"])

                col1, col2 = st.columns(2)

                with col1:
                    st.write(
                        f"**Category:** {resource['category']}"
                    )

                with col2:
                    st.write(
                        f"**Level:** {resource['difficulty']}"
                    )

                if resource["url"]:
                    st.link_button(
                        "Open Resource",
                        resource["url"]
                    )