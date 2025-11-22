import streamlit as st

pages = {
    "Main": [
        st.Page("app.py", title="Summarizer"),
        st.Page("df.py", title="Data Frame's"),
        ],
    "Full": [
        st.Page("full.py", title="Full Streamlit Components"),
        st.Page("animations.py", title="Full Streamlit animations"),
        
        ]
}

pg = st.navigation(pages)
pg.run()