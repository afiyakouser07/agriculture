import streamlit as st

from utils.data_loader import load_data

df = load_data()

st.title("📊 Dataset Overview")

st.subheader("First 20 Records")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.subheader("Dataset Shape")

st.write(df.shape)

st.subheader("Missing Values")

st.dataframe(
    df.isnull().sum(),
    use_container_width=True
)

st.subheader("Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)
