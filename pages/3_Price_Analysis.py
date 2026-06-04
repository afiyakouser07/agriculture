import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
df = pd.read_csv("data/data_season.csv")

st.set_page_config(
    page_title="Price Analysis",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Crop Price Analysis Dashboard")

# Average Price by Crop
st.subheader("Average Crop Price")

price_data = (
    df.groupby("Crops")["price"]
    .mean()
    .reset_index()
    .sort_values("price", ascending=False)
)

fig = px.bar(
    price_data,
    x="Crops",
    y="price",
    color="price",
    title="Average Price by Crop"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Price Distribution
st.subheader("Price Distribution")

fig = px.histogram(
    df,
    x="price",
    nbins=30,
    title="Distribution of Crop Prices"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Season vs Price
st.subheader("Season vs Price")

fig = px.box(
    df,
    x="Season",
    y="price",
    color="Season",
    title="Crop Prices Across Seasons"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Crop vs Season Price
st.subheader("Crop Price by Season")

season_price = (
    df.groupby(["Season", "Crops"])["price"]
    .mean()
    .reset_index()
)

fig = px.bar(
    season_price,
    x="Season",
    y="price",
    color="Crops",
    barmode="group",
    title="Average Crop Price by Season"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Top 10 Expensive Crops
st.subheader("Top 10 Highest Priced Crops")

top_price = (
    df.groupby("Crops")["price"]
    .mean()
    .reset_index()
    .sort_values("price", ascending=False)
    .head(10)
)

st.dataframe(
    top_price,
    use_container_width=True
)
