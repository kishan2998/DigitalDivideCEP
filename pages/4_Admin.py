import streamlit as st
from database import supabase
from style import apply_styles

st.set_page_config(
    page_title="Digital Skills",
    page_icon="📚"
)

apply_styles()
st.title("🔐 Digital Bridge Admin Dashboard")

st.write("Manage learning resources, useful services, and community resources.")

st.divider()


# =========================================================
# DASHBOARD STATISTICS
# =========================================================

resources_response = (
    supabase
    .table("resources")
    .select("*")
    .execute()
)

services_response = (
    supabase
    .table("services")
    .select("*")
    .execute()
)

community_response = (
    supabase
    .table("community_resources")
    .select("*")
    .execute()
)

resources = resources_response.data or []
services = services_response.data or []
community_resources = community_response.data or []


st.subheader("📊 Dashboard Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📚 Learning Resources",
        len(resources)
    )

with col2:
    st.metric(
        "🏛️ Useful Services",
        len(services)
    )

with col3:
    st.metric(
        "🏘️ Community Resources",
        len(community_resources)
    )


st.divider()


# =========================================================
# ADD LEARNING RESOURCE
# =========================================================

st.subheader("📚 Add Learning Resource")

with st.form("add_resource_form"):

    title = st.text_input(
        "Resource Title",
        placeholder="Example: WhatsApp Basics"
    )

    description = st.text_area(
        "Description",
        placeholder="Describe what users will learn..."
    )

    category = st.selectbox(
        "Category",
        [
            "Smartphone",
            "Internet",
            "Digital Payments",
            "Cyber Safety",
            "Email",
            "Online Services",
            "Other"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    url = st.text_input(
        "Resource URL",
        placeholder="https://example.com"
    )

    submitted = st.form_submit_button(
        "➕ Add Learning Resource"
    )

    if submitted:

        if not title or not description:
            st.error(
                "Please enter both a title and description."
            )

        else:

            try:

                supabase.table("resources").insert({
                    "title": title,
                    "description": description,
                    "category": category,
                    "difficulty": difficulty,
                    "url": url
                }).execute()

                st.success(
                    f"✅ '{title}' was added successfully!"
                )

                st.rerun()

            except Exception as e:

                st.error(
                    f"Could not add resource: {e}"
                )


st.divider()


# =========================================================
# EXISTING LEARNING RESOURCES
# =========================================================

st.subheader("📖 Existing Learning Resources")

if not resources:

    st.info("No learning resources available.")

else:

    for resource in resources:

        with st.container(border=True):

            st.subheader(resource["title"])

            st.write(resource["description"])

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(
                    f"**Category:** {resource['category']}"
                )

            with col2:
                st.write(
                    f"**Difficulty:** {resource['difficulty']}"
                )

            with col3:

                if resource["url"]:
                    st.link_button(
                        "🔗 Open Resource",
                        resource["url"]
                    )

            edit_col, delete_col = st.columns(2)

            with edit_col:

                if st.button(
                    "✏️ Edit",
                    key=f"edit_resource_{resource['id']}"
                ):

                    st.session_state[
                        "editing_resource"
                    ] = resource["id"]

                    st.rerun()

            with delete_col:

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_resource_{resource['id']}"
                ):

                    try:

                        supabase.table(
                            "resources"
                        ).delete().eq(
                            "id",
                            resource["id"]
                        ).execute()

                        st.success(
                            "Resource deleted successfully."
                        )

                        st.rerun()

                    except Exception as e:

                        st.error(
                            f"Could not delete resource: {e}"
                        )


# =========================================================
# EDIT LEARNING RESOURCE
# =========================================================

if "editing_resource" in st.session_state:

    resource_id = st.session_state[
        "editing_resource"
    ]

    resource_to_edit = next(
        (
            r for r in resources
            if r["id"] == resource_id
        ),
        None
    )

    if resource_to_edit:

        st.divider()

        st.subheader("✏️ Edit Learning Resource")

        with st.form("edit_resource_form"):

            new_title = st.text_input(
                "Resource Title",
                value=resource_to_edit["title"]
            )

            new_description = st.text_area(
                "Description",
                value=resource_to_edit["description"]
            )

            categories = [
                "Smartphone",
                "Internet",
                "Digital Payments",
                "Cyber Safety",
                "Email",
                "Online Services",
                "Other"
            ]

            current_category = resource_to_edit["category"]

            category_index = (
                categories.index(current_category)
                if current_category in categories
                else 0
            )

            new_category = st.selectbox(
                "Category",
                categories,
                index=category_index
            )

            difficulties = [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]

            current_difficulty = resource_to_edit["difficulty"]

            difficulty_index = (
                difficulties.index(current_difficulty)
                if current_difficulty in difficulties
                else 0
            )

            new_difficulty = st.selectbox(
                "Difficulty",
                difficulties,
                index=difficulty_index
            )

            new_url = st.text_input(
                "Resource URL",
                value=resource_to_edit["url"] or ""
            )

            save = st.form_submit_button(
                "💾 Save Changes"
            )

            cancel = st.form_submit_button(
                "Cancel"
            )

            if save:

                try:

                    supabase.table(
                        "resources"
                    ).update({
                        "title": new_title,
                        "description": new_description,
                        "category": new_category,
                        "difficulty": new_difficulty,
                        "url": new_url
                    }).eq(
                        "id",
                        resource_id
                    ).execute()

                    st.success(
                        "✅ Resource updated successfully."
                    )

                    del st.session_state[
                        "editing_resource"
                    ]

                    st.rerun()

                except Exception as e:

                    st.error(
                        f"Could not update resource: {e}"
                    )

            if cancel:

                del st.session_state[
                    "editing_resource"
                ]

                st.rerun()


st.divider()


# =========================================================
# ADD USEFUL SERVICE
# =========================================================

st.subheader("🏛️ Add Useful Service")

with st.form("add_service_form"):

    service_name = st.text_input(
        "Service Name",
        placeholder="Example: National Career Service"
    )

    service_description = st.text_area(
        "Description",
        placeholder="Describe what this service provides..."
    )

    service_category = st.selectbox(
        "Category",
        [
            "Government",
            "Education",
            "Employment",
            "Healthcare",
            "Digital Services",
            "Other"
        ],
        key="service_category"
    )

    service_url = st.text_input(
        "Service URL",
        placeholder="https://example.com"
    )

    add_service = st.form_submit_button(
        "➕ Add Service"
    )

    if add_service:

        if not service_name or not service_description:
            st.error(
                "Please enter both the service name and description."
            )

        else:

            try:

                supabase.table("services").insert({
                    "name": service_name,
                    "description": service_description,
                    "category": service_category,
                    "url": service_url
                }).execute()

                st.success(
                    f"✅ '{service_name}' was added successfully!"
                )

                st.rerun()

            except Exception as e:

                st.error(
                    f"Could not add service: {e}"
                )


# =========================================================
# SHOW SERVICES
# =========================================================

st.subheader("📋 Existing Services")

if not services:

    st.info("No services available.")

else:

    for service in services:

        with st.container(border=True):

            st.subheader(service["name"])

            st.write(service["description"])

            st.write(
                f"**Category:** {service['category']}"
            )

            if service["url"]:

                st.link_button(
                    "🔗 Visit Service",
                    service["url"]
                )


st.divider()


# =========================================================
# ADD COMMUNITY RESOURCE
# =========================================================

st.subheader("🏘️ Add Community Resource")

with st.form("add_community_resource_form"):

    resource_name = st.text_input(
        "Resource Name",
        placeholder="Example: Community Digital Learning Center"
    )

    resource_description = st.text_area(
        "Description",
        placeholder="Describe this community resource..."
    )

    resource_location = st.text_input(
        "Location",
        placeholder="Example: Community Center"
    )

    resource_contact = st.text_input(
        "Contact",
        placeholder="Example: Contact community coordinator"
    )

    resource_type = st.selectbox(
        "Type",
        [
            "Learning Center",
            "Internet Access",
            "Digital Assistance",
            "Community Center",
            "Other"
        ],
        key="community_resource_type"
    )

    add_community_resource = st.form_submit_button(
        "➕ Add Community Resource"
    )

    if add_community_resource:

        if not resource_name or not resource_description:
            st.error(
                "Please enter both the resource name and description."
            )

        else:

            try:

                supabase.table(
                    "community_resources"
                ).insert({
                    "name": resource_name,
                    "description": resource_description,
                    "location": resource_location,
                    "contact": resource_contact,
                    "type": resource_type
                }).execute()

                st.success(
                    f"✅ '{resource_name}' was added successfully!"
                )

                st.rerun()

            except Exception as e:

                st.error(
                    f"Could not add community resource: {e}"
                )


# =========================================================
# SHOW COMMUNITY RESOURCES
# =========================================================

st.subheader("📍 Existing Community Resources")

if not community_resources:

    st.info(
        "No community resources available."
    )

else:

    for resource in community_resources:

        with st.container(border=True):

            st.subheader(resource["name"])

            st.write(resource["description"])

            st.write(
                f"**📍 Location:** {resource['location']}"
            )

            st.write(
                f"**📞 Contact:** {resource['contact']}"
            )

            st.write(
                f"**📌 Type:** {resource['type']}"
            )


st.divider()

st.info(
    "🔐 Admin authentication will be added before public deployment."
)