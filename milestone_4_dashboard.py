import pandas as pd
import plotly.express as px
import streamlit as st

# Set page config
st.set_page_config(page_title="Supportlytics Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('cleaned_Supportlytics.csv')

df = load_data()

st.title("🚀 Supportlytics: IT Support Performance Dashboard")
st.markdown("### Data-Driven Optimization of IT Support Team Performance")

# Sidebar filters
st.sidebar.header("Filters")
country_filter = st.sidebar.multiselect("Select Country", options=df['Country'].unique(), default=df['Country'].unique())
priority_filter = st.sidebar.multiselect("Select Priority", options=df['Priority'].unique(), default=df['Priority'].unique())

filtered_df = df[(df['Country'].isin(country_filter)) & (df['Priority'].isin(priority_filter))]

# Top level KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Tickets", len(filtered_df))
col2.metric("Avg Resolution Time", f"{filtered_df['Resolution_Duration'].mean():.2f}h")
col3.metric("Avg Satisfaction", f"{filtered_df['Survey_Results'].mean():.2f}/5")
col4.metric("SLA Compliance", f"{(filtered_df['Resolution_Gap'] >= 0).mean()*100:.1f}%")

# Main Dashboard Layout
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Ticket Distribution by Category")
    fig_cat = px.pie(filtered_df, names='Category', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_cat, use_container_width=True)

with row1_col2:
    st.subheader("Resolution Efficiency by Priority")
    fig_res = px.box(filtered_df, x='Priority', y='Resolution_Duration', color='Priority')
    st.plotly_chart(fig_res, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Performance Bucket vs Similarity Score")
    cluster_perf = filtered_df.groupby('Performance_Bucket')['Similarity_Score'].mean().reset_index()
    fig_cluster = px.bar(cluster_perf, x='Performance_Bucket', y='Similarity_Score', color='Similarity_Score')
    st.plotly_chart(fig_cluster, use_container_width=True)

with row2_col2:
    st.subheader("Geographical Ticket Concentration")
    fig_geo = px.scatter_geo(filtered_df, lat='Latitude', lon='Longitude', color='Priority', size='Agent_interactions')
    st.plotly_chart(fig_geo, use_container_width=True)

st.markdown("---")
st.subheader("Performance Insights & Recommendations")
st.info("""
- **Optimize Resource Allocation**: High-priority tickets in 'Security' category show longer resolution times. Consider reallocating senior agents to this queue.
- **Training Opportunities**: Clusters with low Similarity Scores indicate a need for better documentation or training for those specific issue types.
- **Regional Focus**: USA and India show the highest ticket volumes; consider expanding support teams in these time zones.
""")
