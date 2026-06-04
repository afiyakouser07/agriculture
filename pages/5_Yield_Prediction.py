import streamlit as st

from utils.data_loader import load_data
from utils.model import build_model

st.title("🤖 Yield Prediction")

df = load_data()

X = df.drop(
    "yeilds",
    axis=1
)

y = df["yeilds"]

model = build_model()

model.fit(X, y)

st.success("Yield Prediction Model Trained")

st.write(
    "Random Forest Regression model is trained on the dataset."
)

feature_data = X.head()

st.subheader("Sample Training Data")

st.dataframe(
    feature_data,
    use_container_width=True
)
