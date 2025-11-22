import streamlit as st
import time
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="Streamlit Animations", page_icon="✨")

st.title("✨ Streamlit Animations & Transitions")
st.markdown("This script demonstrates loading states, visual effects, and live data updates.")

# -----------------------------------------------------------------------------
# SECTION 1: CELEBRATION EFFECTS
# -----------------------------------------------------------------------------
st.header("1. Celebration Effects")
st.write("Built-in visual effects for successful tasks.")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎈 Balloons"):
        st.balloons()
    st.code("st.balloons()")

with col2:
    if st.button("❄️ Snow"):
        st.snow()
    st.code("st.snow()")

with col3:
    if st.button("🍞 Toast Notification"):
        st.toast("Task completed successfully!", icon="✅")
    st.code('st.toast("Message", icon="✅")')

st.divider()

# -----------------------------------------------------------------------------
# SECTION 2: PROGRESS & SPINNERS
# -----------------------------------------------------------------------------
st.header("2. Loading States")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Progress Bar")
    start_btn = st.button("Start Progress")
    
    progress_bar = st.progress(0)
    status_text = st.empty()

    if start_btn:
        for i in range(100):
            # Update progress bar
            progress_bar.progress(i + 1)
            status_text.text(f"Processing... {i+1}%")
            time.sleep(0.02) # Sleep to simulate work
        status_text.text("Done!")

    st.code("""
my_bar = st.progress(0)
for i in range(100):
    my_bar.progress(i + 1)
    time.sleep(0.01)
    """)

with col_b:
    st.subheader("Spinner")
    
    if st.button("Run Long Task"):
        with st.spinner("Wait for it..."):
            time.sleep(2.5) # Simulate a 2.5s task
        st.success("Task finished!")

    st.code("""
with st.spinner("Wait for it..."):
    time.sleep(3)
st.success("Done!")
    """)

st.divider()

# -----------------------------------------------------------------------------
# SECTION 3: ADVANCED STATUS CONTAINER
# -----------------------------------------------------------------------------
st.header("3. Status Container")
st.write("`st.status` allows you to show a multi-step process and collapse it when done.")

if st.button("Start Multi-step Process"):
    with st.status("Initializing...", expanded=True) as status:
        st.write("⚡ Connecting to server...")
        time.sleep(1)
        
        st.write("💾 Downloading data...")
        time.sleep(1)
        
        st.write("⚙️ Processing configuration...")
        time.sleep(1)
        
        status.update(label="Process Complete!", state="complete", expanded=False)
    
    st.button("Reset")

st.code("""
with st.status("Initializing...", expanded=True) as status:
    st.write("Step 1...")
    time.sleep(1)
    st.write("Step 2...")
    time.sleep(1)
    status.update(label="Done!", state="complete", expanded=False)
""")

st.divider()

# -----------------------------------------------------------------------------
# SECTION 4: LIVE CHART UPDATES
# -----------------------------------------------------------------------------
st.header("4. Streaming Data")
st.write("You can animate charts by adding rows in real-time using `add_rows`.")

if st.button("Start Data Stream"):
    # Initialize data
    data = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
    
    # Create the chart element
    chart = st.line_chart(data)
    
    # Stream new data
    for _ in range(50):
        # Create a tiny bit of new data
        new_data = pd.DataFrame(np.random.randn(1, 2), columns=['A', 'B'])
        
        # Update the chart
        chart.add_rows(new_data)
        
        # Sleep to make the animation visible
        time.sleep(0.05)

st.code("""
chart = st.line_chart(initial_data)

for i in range(50):
    new_rows = get_new_data()
    chart.add_rows(new_rows)
    time.sleep(0.05)
""")