import streamlit as st

from utils.data_loader import load_data
from utils.charts import *

df = load_data()

st.title("🌾 Crop Analytics")

st.plotly_chart(
    crop_yield(df),
    use_container_width=True
)

st.plotly_chart(
    rainfall_vs_yield(df),
    use_container_width=True
)

st.plotly_chart(
    temperature_vs_yield(df),
    use_container_width=True
)

st.plotly_chart(
    humidity_vs_yield(df),
    use_container_width=True
)
