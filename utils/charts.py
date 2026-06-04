import plotly.express as px
import plotly.graph_objects as go


# --------------------------------------------------
# Top Companies by Market Cap
# --------------------------------------------------
def top_companies_chart(df, top_n=20):

    top_df = df.nlargest(top_n, "market_cap")

    fig = px.bar(
        top_df,
        x="company_name",
        y="market_cap",
        color="market_cap",
        title=f"Top {top_n} Companies by Market Cap",
        text_auto=".2s"
    )

    fig.update_layout(
        xaxis_title="Company",
        yaxis_title="Market Cap (Billion USD)",
        height=600
    )

    return fig


# --------------------------------------------------
# Country Wise Market Cap
# --------------------------------------------------
def country_marketcap_chart(df):

    country_df = (
        df.groupby("headquarter")["market_cap"]
        .sum()
        .reset_index()
        .sort_values(
            by="market_cap",
            ascending=False
        )
        .head(15)
    )

    fig = px.bar(
        country_df,
        x="headquarter",
        y="market_cap",
        color="market_cap",
        title="Top 15 Countries by Market Cap"
    )

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Total Market Cap"
    )

    return fig


# --------------------------------------------------
# Sector Analysis Treemap
# --------------------------------------------------
def sector_treemap(df):

    sector_df = (
        df.groupby("business_sector")["market_cap"]
        .sum()
        .reset_index()
    )

    fig = px.treemap(
        sector_df,
        path=["business_sector"],
        values="market_cap",
        title="Business Sector Market Cap Distribution"
    )

    return fig


# --------------------------------------------------
# Market Cap Distribution
# --------------------------------------------------
def marketcap_distribution(df):

    fig = px.histogram(
        df,
        x="market_cap",
        nbins=50,
        title="Market Cap Distribution"
    )

    fig.update_layout(
        xaxis_title="Market Cap",
        yaxis_title="Number of Companies"
    )

    return fig


# --------------------------------------------------
# Country Pie Chart
# --------------------------------------------------
def country_pie_chart(df):

    country_df = (
        df.groupby("headquarter")["market_cap"]
        .sum()
        .reset_index()
        .sort_values(
            by="market_cap",
            ascending=False
        )
        .head(10)
    )

    fig = px.pie(
        country_df,
        names="headquarter",
        values="market_cap",
        title="Top 10 Countries Market Share"
    )

    return fig


# --------------------------------------------------
# Sector Pie Chart
# --------------------------------------------------
def sector_pie_chart(df):

    sector_df = (
        df.groupby("business_sector")["market_cap"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        sector_df,
        names="business_sector",
        values="market_cap",
        title="Sector-wise Market Share"
    )

    return fig


# --------------------------------------------------
# Rank vs Market Cap
# --------------------------------------------------
def rank_vs_marketcap(df):

    fig = px.scatter(
        df,
        x="world_rank",
        y="market_cap",
        color="business_sector",
        hover_name="company_name",
        title="World Rank vs Market Cap"
    )

    fig.update_layout(
        xaxis_title="World Rank",
        yaxis_title="Market Cap"
    )

    return fig


# --------------------------------------------------
# Box Plot
# --------------------------------------------------
def marketcap_boxplot(df):

    fig = px.box(
        df,
        y="market_cap",
        title="Market Cap Outlier Analysis"
    )

    return fig


# --------------------------------------------------
# Top Sectors
# --------------------------------------------------
def top_sectors_chart(df):

    sector_df = (
        df.groupby("business_sector")["market_cap"]
        .sum()
        .reset_index()
        .sort_values(
            by="market_cap",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        sector_df,
        x="business_sector",
        y="market_cap",
        color="market_cap",
        title="Top 10 Business Sectors"
    )

    return fig
