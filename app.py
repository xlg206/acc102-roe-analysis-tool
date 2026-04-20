import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ACC102 ROE Analysis Tool", layout="wide")

st.title("Listed Company ROE Comparison Tool")
st.markdown("""
### For Who: Business students, retail investors
### What it does: Compare ROE and revenue trends of Apple and Microsoft
### Data Source: Sample financial data (2020-2023)
""")

@st.cache_data
def load_data():
    df = pd.read_csv("finance_data.csv")
    return df

df = load_data()

st.sidebar.header("Filter Settings")
selected_company = st.sidebar.multiselect(
    "Select Companies",
    options=df["company"].unique(),
    default=df["company"].unique()
)
selected_year = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df["year"].min()),
    max_value=int(df["year"].max()),
    value=(2020, 2023)
)

df_filtered = df[
    (df["company"].isin(selected_company)) &
    (df["year"] >= selected_year[0]) &
    (df["year"] <= selected_year[1])
]

st.subheader("Core Financial Data")
st.dataframe(df_filtered, use_container_width=True)

st.subheader("ROE Trend Comparison")
fig_roe = px.line(
    df_filtered,
    x="year",
    y="roe",
    color="company",
    markers=True,
    title="ROE Trend (2020-2023)",
    labels={"roe": "ROE (Return on Equity)", "year": "Year"}
)
st.plotly_chart(fig_roe, use_container_width=True)

st.subheader("Revenue Trend Comparison")
fig_revenue = px.bar(
    df_filtered,
    x="year",
    y="revenue",
    color="company",
    barmode="group",
    title="Revenue Trend (2020-2023)",
    labels={"revenue": "Revenue (USD Millions)", "year": "Year"}
)
st.plotly_chart(fig_revenue, use_container_width=True)

st.subheader("Key Insights")
avg_roe = df_filtered.groupby("company")["roe"].mean().sort_values(ascending=False)
st.markdown(f"""
1. The company with the highest average ROE is **{avg_roe.index[0]}**, with an average ROE of {avg_roe.iloc[0]:.2%}
2. Both companies' revenue showed an overall upward trend from {selected_year[0]} to {selected_year[1]}
""")