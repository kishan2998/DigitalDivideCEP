import streamlit as st


def apply_styles():

    st.markdown(
        """
        <style>

        /* Main content */
        .block-container {
            max-width: 1100px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* Headings */
        h1 {
            font-size: 2.4rem;
        }

        h2 {
            font-size: 1.8rem;
        }

        h3 {
            font-size: 1.3rem;
        }

        /* Buttons */
        .stButton > button,
        .stLinkButton > a {
            border-radius: 8px;
            font-weight: 600;
            min-height: 42px;
        }

        /* Input fields */
        .stTextInput input,
        .stTextArea textarea {
            border-radius: 8px;
        }

        /* Containers/cards */
        [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 12px;
        }

        /* Mobile-friendly layout */
        @media (max-width: 768px) {

            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 1rem;
            }

            h1 {
                font-size: 1.9rem;
            }

            h2 {
                font-size: 1.5rem;
            }

            h3 {
                font-size: 1.2rem;
            }

            .stButton > button,
            .stLinkButton > a {
                width: 100%;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )