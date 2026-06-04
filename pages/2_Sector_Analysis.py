import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

st.title("🏭 Sector Analysis")

df = load_data()

sector_df = (
    df.groupby("business_sector")
    .agg(
        Market_Cap=("market_cap", "sum"),
        Companies=("company_name", "count")
    )
    .reset_index()
)

st.dataframe(sector_df)

fig = px.sunburst(
    sector_df,
    path=["business_sector"],
    values="Market_Cap",
    title="Sector Contribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
