import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
df = pd.read_csv("data/agriculture_data.csv")

st.set_page_config(
    page_title="Crop Analytics",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Crop Analytics Dashboard")

# Crop Yield Analysis

st.subheader("Average Yield by Crop")

crop_data = (
    df.groupby("Crops")["yeilds"]
    .mean()
    .reset_index()
)

fig = px.bar(
    crop_data,
    x="Crops",
    y="yeilds",
    color="yeilds",
    title="Average Yield by Crop"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Rainfall vs Yield

st.subheader("Rainfall vs Yield")

fig = px.scatter(
    df,
    x="Rainfall",
    y="yeilds",
    color="Season",
    hover_data=["Crops"],
    title="Impact of Rainfall on Yield"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Temperature vs Yield

st.subheader("Temperature vs Yield")

fig = px.scatter(
    df,
    x="Temperature",
    y="yeilds",
    color="Crops",
    title="Temperature Impact on Yield"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Humidity vs Yield

st.subheader("Humidity vs Yield")

fig = px.scatter(
    df,
    x="Humidity",
    y="yeilds",
    color="Season",
    title="Humidity Impact on Yield"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Soil Type Analysis

st.subheader("Yield by Soil Type")

soil_data = (
    df.groupby("Soil type")["yeilds"]
    .mean()
    .reset_index()
)

fig = px.bar(
    soil_data,
    x="Soil type",
    y="yeilds",
    color="yeilds",
    title="Average Yield by Soil Type"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Irrigation Analysis

st.subheader("Yield by Irrigation Type")

irrigation_data = (
    df.groupby("Irrigation")["yeilds"]
    .mean()
    .reset_index()
)

fig = px.bar(
    irrigation_data,
    x="Irrigation",
    y="yeilds",
    color="yeilds",
    title="Average Yield by Irrigation Method"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
