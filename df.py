import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.title("Data Frame's")


st.markdown("This page contains some data frame's created using ***Pandas*** and ***Streamlit***")

st.divider()

st.subheader("Scatter chart")

df = pd.DataFrame(
    rng(0).standard_normal((20, 3)), columns=["a", "b", "c"],
)

st.scatter_chart(df)


st.subheader("Line chart")
st.line_chart(df)
