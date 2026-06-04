import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.charts import (
    top_companies_chart,
    country_marketcap_chart,
    sector_chart
)

st.set_page_config(
    page_title="Market Cap Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Global Company Market Cap Dashboard")

df = load_data()

# Sidebar Filters

st.sidebar.header("Filters")

selected_country = st.sidebar.multiselect(
    "Country",
    sorted(df["headquarter"].unique())
)

selected_sector = st.sidebar.multiselect(
    "Business Sector",
    sorted(df["business_sector"].unique())
)

filtered_df = df.copy()

if selected_country:
    filtered_df = filtered_df[
        filtered_df["headquarter"].isin(selected_country)
    ]

if selected_sector:
    filtered_df = filtered_df[
        filtered_df["business_sector"].isin(selected_sector)
    ]

# KPI Cards

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Companies",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Countries",
        filtered_df["headquarter"].nunique()
    )

with col3:
    st.metric(
        "Sectors",
        filtered_df["business_sector"].nunique()
    )

with col4:
    st.metric(
        "Total Market Cap",
        f"{filtered_df['market_cap'].sum():,.0f} B"
    )

st.divider()

# Charts

st.plotly_chart(
    top_companies_chart(filtered_df),
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        country_marketcap_chart(filtered_df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        sector_chart(filtered_df),
        use_container_width=True
    )

st.divider()

st.subheader("Market Cap Distribution")

hist = px.histogram(
    filtered_df,
    x="market_cap",
    nbins=50,
    title="Distribution of Market Cap"
)

st.plotly_chart(
    hist,
    use_container_width=True
)

st.subheader("Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)
