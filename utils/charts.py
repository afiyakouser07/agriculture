import plotly.express as px

def yield_distribution(df):
    fig = px.histogram(
        df,
        x="yeilds",
        nbins=30,
        title="Yield Distribution"
    )
    return fig

def crop_yield(df):
    crop_data = (
        df.groupby("Crops")["yeilds"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        crop_data,
        x="Crops",
        y="yeilds",
        title="Average Yield by Crop"
    )

    return fig

def rainfall_vs_yield(df):
    return px.scatter(
        df,
        x="Rainfall",
        y="yeilds",
        color="Season",
        title="Rainfall vs Yield"
    )

def temperature_vs_yield(df):
    return px.scatter(
        df,
        x="Temperature",
        y="yeilds",
        color="Crops",
        title="Temperature vs Yield"
    )

def humidity_vs_yield(df):
    return px.scatter(
        df,
        x="Humidity",
        y="yeilds",
        color="Season",
        title="Humidity vs Yield"
    )
