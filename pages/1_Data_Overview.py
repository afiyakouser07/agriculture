import streamlit as st
import pandas as pd

# Load Dataset
df = pd.read_csv("data/data_season.csv")

st.set_page_config(
    page_title="Data Overview",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Agriculture Dataset Overview")

# Dataset Shape
col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.divider()

# First Records
st.subheader("First 20 Records")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.divider()

# Column Information
st.subheader("Column Information")

info_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(
    info_df,
    use_container_width=True
)

st.divider()

# Missing Values
st.subheader("Missing Values")

missing_df = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values
})

st.dataframe(
    missing_df,
    use_container_width=True
)

st.divider()

# Statistical Summary
st.subheader("Statistical Summary")

st.dataframe(
    df.describe(include="all"),
    use_container_width=True
)

st.divider()

# Unique Values
st.subheader("Unique Values per Column")

unique_df = pd.DataFrame({
    "Column": df.columns,
    "Unique Values": [df[col].nunique() for col in df.columns]
})

st.dataframe(
    unique_df,
    use_container_width=True
)
