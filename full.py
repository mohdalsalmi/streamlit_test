import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, time as dt_time

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Streamlit Component & Code Showcase",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Streamlit Component Showcase")
st.markdown("Explore Streamlit components. The **code to generate each element** is displayed directly below it.")

# -----------------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------------
with st.sidebar:
    st.header("Sidebar")
    st.write("Content here is pinned to the left.")
    st.code("""
with st.sidebar:
    st.write("Content here...")
    """)
    
    st.divider()
    
    st.button("Sidebar Button")
    st.code('st.sidebar.button("Button")')

# -----------------------------------------------------------------------------
# TABS SETUP
# -----------------------------------------------------------------------------
tabs = st.tabs([
    "📝 Text", 
    "🎛️ Inputs", 
    "📊 Data", 
    "📈 Charts", 
    "🖼️ Media", 
    "📐 Layouts", 
    "🚦 Status",
    "💬 Chat"
])

# -----------------------------------------------------------------------------
# TAB 1: TEXT ELEMENTS
# -----------------------------------------------------------------------------
with tabs[0]:
    st.header("Text Elements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.title("This is a Title")
        st.code('st.title("This is a Title")')
        
        st.header("This is a Header")
        st.code('st.header("This is a Header")')
        
        st.subheader("This is a Subheader")
        st.code('st.subheader("This is a Subheader")')
        
        st.text("This is preformatted text.")
        st.code('st.text("This is preformatted text.")')

    with col2:
        st.markdown("This is **Markdown** with *styling*.")
        st.code('st.markdown("This is **Markdown** with *styling*.")')
        
        st.caption("This is a caption (small text).")
        st.code('st.caption("This is a caption (small text).")')
        
        st.latex(r''' e^{i\pi} + 1 = 0 ''')
        st.code(r"st.latex(r''' e^{i\pi} + 1 = 0 ''')")
        
        st.divider()
        st.code('st.divider()')

# -----------------------------------------------------------------------------
# TAB 2: INPUT WIDGETS
# -----------------------------------------------------------------------------
with tabs[1]:
    st.header("Input Widgets")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.button("Click Me")
        st.code('st.button("Click Me")')
        
        st.checkbox("Check Me")
        st.code('st.checkbox("Check Me")')
        
        st.toggle("Toggle Me")
        st.code('st.toggle("Toggle Me")')

    with c2:
        st.radio("Pick one", ["Cat", "Dog"])
        st.code('st.radio("Pick one", ["Cat", "Dog"])')
        
        st.selectbox("Select one", ["Red", "Green", "Blue"])
        st.code('st.selectbox("Select one", ["Red", "Green", "Blue"])')
        
        st.multiselect("Select multiple", ["A", "B", "C"])
        st.code('st.multiselect("Select multiple", ["A", "B", "C"])')

    with c3:
        st.slider("Slide me", 0, 100, 50)
        st.code('st.slider("Slide me", 0, 100, 50)')
        
        st.text_input("Type something")
        st.code('st.text_input("Type something")')
        
        st.number_input("Pick a number", 0, 10)
        st.code('st.number_input("Pick a number", 0, 10)')

    st.divider()
    c4, c5 = st.columns(2)
    with c4:
        st.date_input("Pick a date", datetime.now())
        st.code('st.date_input("Pick a date", datetime.now())')
        
        st.file_uploader("Upload a file")
        st.code('st.file_uploader("Upload a file")')
        
    with c5:
        st.color_picker("Pick a color", "#FF0000")
        st.code('st.color_picker("Pick a color", "#FF0000")')
        
        st.camera_input("Camera (Disabled for demo)", disabled=True)
        st.code('st.camera_input("Camera", disabled=True)')

# -----------------------------------------------------------------------------
# TAB 3: DATA DISPLAY
# -----------------------------------------------------------------------------
with tabs[2]:
    st.header("Data Display")
    
    df = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
    
    st.write("### DataFrame (Interactive)")
    st.dataframe(df, use_container_width=True)
    st.code('st.dataframe(df, use_container_width=True)')
    
    st.write("### Table (Static)")
    st.table(df.head(2))
    st.code('st.table(df.head(2))')
    
    st.write("### Data Editor (Editable)")
    st.data_editor(df, num_rows="dynamic", key="editor")
    st.code('st.data_editor(df, num_rows="dynamic")')
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Revenue", value="$1M", delta="+5%")
        st.code('st.metric(label="Revenue", value="$1M", delta="+5%")')
        
    with col2:
        st.json({"key": "value", "list": [1, 2, 3]})
        st.code('st.json({"key": "value", "list": [1, 2, 3]})')

# -----------------------------------------------------------------------------
# TAB 4: CHARTS
# -----------------------------------------------------------------------------
with tabs[3]:
    st.header("Charts")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    
    c1, c2 = st.columns(2)
    with c1:
        st.line_chart(chart_data)
        st.code('st.line_chart(chart_data)')
        
        st.area_chart(chart_data)
        st.code('st.area_chart(chart_data)')
        
    with c2:
        st.bar_chart(chart_data)
        st.code('st.bar_chart(chart_data)')
        
        st.scatter_chart(chart_data)
        st.code('st.scatter_chart(chart_data)')

    st.map(pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon']))
    st.code("""
# Data requires lat/lon columns
st.map(map_data)
    """)

# -----------------------------------------------------------------------------
# TAB 5: MEDIA
# -----------------------------------------------------------------------------
with tabs[4]:
    st.header("Media")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
        st.code('st.image("url_or_path", width=150)')
        
    with c2:
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        st.code('st.audio("url_or_path")')
        
    with c3:
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
        st.code('st.video("url_or_path")')

# -----------------------------------------------------------------------------
# TAB 6: LAYOUTS
# -----------------------------------------------------------------------------
with tabs[5]:
    st.header("Layouts")

    st.write("### Columns")
    c1, c2 = st.columns([1, 2])
    with c1:
        st.info("Column 1")
    with c2:
        st.warning("Column 2")
    
    st.code("""
c1, c2 = st.columns([1, 2])
with c1:
    st.info("Column 1")
with c2:
    st.warning("Column 2")
    """)

    st.write("### Expander")
    with st.expander("Open to see details"):
        st.write("Hidden content!")
    st.code("""
with st.expander("Open to see details"):
    st.write("Hidden content!")
    """)

    st.write("### Container (Border)")
    with st.container(border=True):
        st.write("Inside a box.")
    st.code("""
with st.container(border=True):
    st.write("Inside a box.")
    """)
    
    st.write("### Popover")
    with st.popover("Click for Popover"):
        st.write("Hello!")
    st.code("""
with st.popover("Click for Popover"):
    st.write("Hello!")
    """)

# -----------------------------------------------------------------------------
# TAB 7: STATUS
# -----------------------------------------------------------------------------
with tabs[6]:
    st.header("Status & Feedback")
    
    st.success("Success Message")
    st.code('st.success("Success Message")')
    
    st.info("Info Message")
    st.code('st.info("Info Message")')
    
    st.warning("Warning Message")
    st.code('st.warning("Warning Message")')
    
    st.error("Error Message")
    st.code('st.error("Error Message")')

    if st.button("Show Spinner & Progress"):
        with st.spinner("Processing..."):
            time.sleep(1)
        st.toast("Done!")
    
    st.code("""
with st.spinner("Processing..."):
    time.sleep(1)
st.toast("Done!")
    """)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Balloons"):
            st.balloons()
        st.code("st.balloons()")
    with c2:
        if st.button("Snow"):
            st.snow()
        st.code("st.snow()")

# -----------------------------------------------------------------------------
# TAB 8: CHAT
# -----------------------------------------------------------------------------
with tabs[7]:
    st.header("Chat Interface")
    
    with st.chat_message("user"):
        st.write("Hello AI!")
    st.code("""
with st.chat_message("user"):
    st.write("Hello AI!")
    """)
    
    with st.chat_message("assistant"):
        st.write("Hello Human.")
    st.code("""
with st.chat_message("assistant"):
    st.write("Hello Human.")
    """)

    st.chat_input("Type a message...")
    st.code('prompt = st.chat_input("Type a message...")')