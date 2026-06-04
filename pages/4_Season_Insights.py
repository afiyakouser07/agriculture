import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("🍂 Seasonal Insights")

fig = px.box(
    df,
    x="Season",
    y="yeilds",
    color="Season",
    title="Seasonal Yield Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

season_data = (
    df.groupby("Season")["yeilds"]
    .mean()
    .reset_index()
)

fig = px.bar(
    season_data,
    x="Season",
    y="yeilds",
    title="Average Yield by Season"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
