import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
df = pd.read_csv("data/data_season.csv")

st.set_page_config(
    page_title="Crop Analytics
