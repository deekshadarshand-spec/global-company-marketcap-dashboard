import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

st.title("🌍 Country Analysis")

df = load_data()

country_df = (
    df.groupby("headquarter")
    .agg(
        Total_Market_Cap=("market_cap", "sum"),
        Companies=("company_name", "count")
    )
    .reset_index()
)

country_df = country_df.sort_values(
    "Total_Market_Cap",
    ascending=False
)

st.dataframe(country_df)

fig = px.scatter(
    country_df,
    x="Companies",
    y="Total_Market_Cap",
    size="Total_Market_Cap",
    color="headquarter",
    title="Country Market Cap Analysis"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
