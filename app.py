import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
# Change filename if needed:
# data/data_season.csv
# OR
# data/agriculture_data.csv

df = pd.read_csv("data/data_season.csv")

st.set_page_config(
    page_title="Smart Agriculture Dashboard",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Smart Agriculture Analytics Dashboard")

# ======================
# SIDEBAR FILTERS
# ======================

st.sidebar.header("Filters")

crop_filter = st.sidebar.multiselect(
    "Select Crop",
    options=sorted(df["Crops"].unique()),
    default=sorted(df["Crops"].unique())
)

season_filter = st.sidebar.multiselect(
    "Select Season",
    options=sorted(df["Season"].unique()),
    default=sorted(df["Season"].unique())
)

location_filter = st.sidebar.multiselect(
    "Select Location",
    options=sorted(df["Location"].unique()),
    default=sorted(df["Location"].unique())
)

df = df[
    (df["Crops"].isin(crop_filter)) &
    (df["Season"].isin(season_filter)) &
    (df["Location"].isin(location_filter))
]

# ======================
# KPI CARDS
# ======================

st.subheader("Dashboard Overview")

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric("Records", len(df))

c2.metric(
    "Avg Yield",
    round(df["yeilds"].mean(), 2)
)

c3.metric(
    "Avg Price",
    round(df["price"].mean(), 2)
)

c4.metric(
    "Avg Rainfall",
    round(df["Rainfall"].mean(), 2)
)

c5.metric(
    "Avg Temp",
    round(df["Temperature"].mean(), 2)
)

c6.metric(
    "Crop Types",
    df["Crops"].nunique()
)

st.divider()

# ======================
# YIELD DISTRIBUTION
# ======================

left, right = st.columns(2)

with left:

    fig = px.histogram(
        df,
        x="yeilds",
        nbins=30,
        title="Yield Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    crop_data = (
        df.groupby("Crops")["yeilds"]
        .mean()
        .reset_index()
        .sort_values("yeilds", ascending=False)
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

st.divider()

# ======================
# RAINFALL VS YIELD
# ======================

fig = px.scatter(
    df,
    x="Rainfall",
    y="yeilds",
    color="Season",
    hover_data=["Crops"],
    title="Rainfall vs Yield"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================
# TEMPERATURE VS YIELD
# ======================

fig = px.scatter(
    df,
    x="Temperature",
    y="yeilds",
    color="Crops",
    title="Temperature vs Yield"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================
# CORRELATION HEATMAP
# ======================

st.subheader("Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

corr = numeric_df.corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Matrix"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================
# DATA PREVIEW
# ======================

st.subheader("Dataset Preview")

st.dataframe(
    df.head(50),
    use_container_width=True
)
