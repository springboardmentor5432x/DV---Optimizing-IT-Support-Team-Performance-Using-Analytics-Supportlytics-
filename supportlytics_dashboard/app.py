import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("supportlytics_final.csv")

st.title("Supportlytics Performance Dashboard")

# ---------------- Filters ----------------
st.sidebar.header("Filters")

priority_filter = st.sidebar.multiselect(
    "Select Priority",
    options=df["Priority"].unique(),
    default=df["Priority"].unique()
)

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Issue Category",
    options=df["Cluster_Label"].unique(),
    default=df["Cluster_Label"].unique()
)

filtered_df = df[
    (df["Priority"].isin(priority_filter)) &
    (df["Region"].isin(region_filter)) &
    (df["Cluster_Label"].isin(category_filter))
]

# ---------------- KPI Section ----------------
st.header("Key Performance Indicators")

col1, col2 = st.columns(2)

col1.metric("Average Resolution Time",
            round(filtered_df["Resolution_Time"].mean(), 2))

col2.metric("Ticket Volume",
            len(filtered_df))

# ---------------- Ticket Volume by Category ----------------
st.subheader("Most Frequent Issue Categories")

category_count = filtered_df["Cluster_Label"].value_counts()

fig1, ax1 = plt.subplots()
category_count.plot(kind="bar", ax=ax1)
ax1.set_title("Ticket Volume by Category")
ax1.set_xlabel("Category")
ax1.set_ylabel("Ticket Count")
st.pyplot(fig1)

# ---------------- High Priority Performance ----------------
st.subheader("High Priority Performance")

high_df = filtered_df[filtered_df["Priority"] == "high"]

if not high_df.empty:
    high_perf = high_df.groupby("Region")["Resolution_Time"].mean()

    fig2, ax2 = plt.subplots()
    high_perf.plot(kind="bar", ax=ax2)
    ax2.set_title("High Priority Resolution Time by Region")
    ax2.set_xlabel("Region")
    ax2.set_ylabel("Average Resolution Time")
    st.pyplot(fig2)

# ---------------- Cluster Performance ----------------
st.subheader("Cluster Size vs Performance")

cluster_size = filtered_df["Cluster_Label"].value_counts()
cluster_perf = filtered_df.groupby("Cluster_Label")["Resolution_Time"].mean()

cluster_analysis = pd.DataFrame({
    "Cluster_Size": cluster_size,
    "Avg_Resolution_Time": cluster_perf
})

fig3, ax3 = plt.subplots()
ax3.scatter(cluster_analysis["Cluster_Size"],
            cluster_analysis["Avg_Resolution_Time"])
ax3.set_title("Cluster Size vs Resolution Performance")
ax3.set_xlabel("Cluster Size")
ax3.set_ylabel("Average Resolution Time")
st.pyplot(fig3)

# ---------------- Region Performance ----------------
st.subheader("Region Performance Comparison")

region_perf = filtered_df.groupby("Region")["Resolution_Time"].mean()

fig4, ax4 = plt.subplots()
region_perf.plot(kind="bar", ax=ax4)
ax4.set_title("Average Resolution Time by Region")
ax4.set_xlabel("Region")
ax4.set_ylabel("Average Resolution Time")
st.pyplot(fig4)
