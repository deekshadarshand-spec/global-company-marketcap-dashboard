import plotly.express as px


def top_companies_chart(df):

    top20 = df.nlargest(20, "market_cap")

    fig = px.bar(
        top20,
        x="company_name",
        y="market_cap",
        color="market_cap",
        title="Top 20 Companies by Market Cap"
    )

    return fig


def country_marketcap_chart(df):

    country_df = (
        df.groupby("headquarter")["market_cap"]
        .sum()
        .reset_index()
        .sort_values(
            "market_cap",
            ascending=False
        )
        .head(15)
    )

    fig = px.bar(
        country_df,
        x="headquarter",
        y="market_cap",
        color="market_cap",
        title="Top Countries by Market Cap"
    )

    return fig


def sector_chart(df):

    sector_df = (
        df.groupby("business_sector")["market_cap"]
        .sum()
        .reset_index()
    )

    fig = px.treemap(
        sector_df,
        path=["business_sector"],
        values="market_cap",
        title="Sector Wise Market Cap"
    )

    return fig
