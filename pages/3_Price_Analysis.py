import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("💰 Price Analysis")

price_data = (
    df.groupby("Crops")["price"]
    .mean()
    .reset_index()
)

fig = px.bar(
    price_data,
    x="Crops",
    y="price",
    title="Average Crop Price"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.box(
    df,
    x="Season",
    y="price",
    color="Season",
    title="Season vs Price"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
