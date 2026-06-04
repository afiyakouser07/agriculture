import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.charts import *

st.set_page_config(
    page_title="Crop Analytics Dashboard",
    page_icon="🌾",
    layout="wide"
)

df = load_data()

st.title("🌾 Smart Agriculture Analytics Dashboard")

# SIDEBAR

st.sidebar.header("Filters")

crop_filter = st.sidebar.multiselect(
    "Select Crop",
    options=df["Crops"].unique(),
    default=df["Crops"].unique()
)

season_filter = st.sidebar.multiselect(
    "Select Season",
    options=df["Season"].unique(),
    default=df["Season"].unique()
)

df = df[
    (df["Crops"].isin(crop_filter)) &
    (df["Season"].isin(season_filter))
]

# KPI CARDS

c1,c2,c3,c4,c5,c6 = st.columns(6)

c1.metric("Records", len(df))

c2.metric(
    "Avg Yield",
    round(df["yeilds"].mean(),2)
)

c3.metric(
    "Avg Price",
    round(df["price"].mean(),2)
)

c4.metric(
    "Avg Rainfall",
    round(df["Rainfall"].mean(),2)
)

c5.metric(
    "Avg Temperature",
    round(df["Temperature"].mean(),2)
)

c6.metric(
    "Crop Types",
    df["Crops"].nunique()
)

st.divider()

left,right = st.columns(2)

with left:
    st.plotly_chart(
        yield_distribution(df),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        crop_yield(df),
        use_container_width=True
    )

st.divider()

st.subheader("Correlation Heatmap")

corr = df.select_dtypes(
    include="number"
).corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
