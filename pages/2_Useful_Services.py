import streamlit as st
from database import supabase
from style import apply_styles

st.set_page_config(
    page_title="Digital Skills",
    page_icon="📚"
)

apply_styles()

st.title("🏛️ Useful Services")

st.write(
    "Find useful government, education, employment, "
    "and digital services."
)

st.divider()

# Get services from Supabase
response = (
    supabase
    .table("services")
    .select("*")
    .execute()
)

services = response.data

if not services:
    st.info("No services available yet.")

else:

    # Search
    search = st.text_input(
        "🔎 Search services",
        placeholder="Try: education, jobs, government..."
    )

    # Categories
    categories = sorted(
        set(service["category"] for service in services)
    )

    selected_category = st.selectbox(
        "Category",
        ["All"] + categories
    )

    # Filter
    filtered_services = services

    if search:
        filtered_services = [
            service
            for service in filtered_services
            if search.lower() in (
                service["name"] + " " +
                service["description"] + " " +
                service["category"]
            ).lower()
        ]

    if selected_category != "All":
        filtered_services = [
            service
            for service in filtered_services
            if service["category"] == selected_category
        ]

    st.divider()

    st.write(
        f"**{len(filtered_services)} service(s) found**"
    )

    if not filtered_services:

        st.warning(
            "No services match your search or filter."
        )

    else:

        for service in filtered_services:

            with st.container(border=True):

                st.subheader(service["name"])

                st.write(service["description"])

                st.write(
                    f"**Category:** {service['category']}"
                )

                if service["url"]:
                    st.link_button(
                        "Visit Service",
                        service["url"]
                    )