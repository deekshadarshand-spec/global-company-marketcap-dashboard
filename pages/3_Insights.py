import streamlit as st

from utils.data_loader import load_data

st.title("📈 Business Insights")

df = load_data()

top_company = df.loc[
    df["market_cap"].idxmax()
]

st.success(
    f"""
    Largest Company:
    {top_company['company_name']}
    """
)

top_country = (
    df.groupby("headquarter")["market_cap"]
    .sum()
    .idxmax()
)

st.info(
    f"""
    Country with highest market cap:
    {top_country}
    """
)

top_sector = (
    df.groupby("business_sector")["market_cap"]
    .sum()
    .idxmax()
)

st.warning(
    f"""
    Highest Value Sector:
    {top_sector}
    """
)

st.subheader("Key Findings")

st.markdown("""
### Insights

- Top companies dominate global market capitalization.
- Few countries contribute most of the total market value.
- Technology and Finance sectors generally lead.
- Market cap distribution is highly skewed.
- Most companies fall into lower market-cap ranges.
""")
