import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/company_data.csv")

    df["market_cap"] = (
        df["market cap(Billion USD)"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    df["world_rank"] = pd.to_numeric(
        df["world_rank"],
        errors="coerce"
    )

    return df
