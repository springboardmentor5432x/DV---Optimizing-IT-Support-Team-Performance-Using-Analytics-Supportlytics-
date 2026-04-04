import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Supportlytics", layout="wide")

# basic dark card style for the KPI metrics at the top
st.markdown("""
<style>
    .metric-card {
        background: #1e2130;
        border: 1px solid #3a3f55;
        border-radius: 10px;
        padding: 18px;
        text-align: center;
    }
    .metric-value { font-size: 2rem; font-weight: 700; color: #fff; }
    .metric-label { font-size: 0.8rem; color: #9ea3b8; margin-top: 4px; }
</style>
""", unsafe_allow_html=True)

# constants used across charts
PRIORITY_ORDER  = ["Low", "Medium", "High", "Critical"]
PRIORITY_COLORS = {"Low": "#4ade80", "Medium": "#facc15", "High": "#fb923c", "Critical": "#f87171"}
TEMPLATE        = "plotly_dark"

# reused layout settings for every plotly chart so we dont repeat it each time
DARK_BG = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    title_font_color="#a5b4fc"
)


@st.cache_data
def load_data():
    df = pd.read_csv("customer_support_tickets_cleaned_milestone1.csv")
    df.columns = df.columns.str.strip()

    # calculate how long each ticket took to resolve (in hours)
    if "resolution_duration" in df.columns:
        df["Resolution_Hours"] = pd.to_numeric(df["resolution_duration"], errors="coerce")
    elif "Time_to_Resolution" in df.columns:
        df["Resolution_Hours"] = (
            pd.to_datetime(df["Time_to_Resolution"], errors="coerce") -
            pd.to_datetime(df["First_Response_Time"], errors="coerce")
        ).dt.total_seconds() / 3600

    df["Date_of_Purchase"] = pd.to_datetime(df["Date_of_Purchase"], errors="coerce")
    df["Month"] = df["Date_of_Purchase"].dt.to_period("M").astype(str)
    df["Year"]  = df["Date_of_Purchase"].dt.year

    # handle two different ways priority can exist in the csv
    if "Ticket_Priority" in df.columns:
        df["Ticket_Priority"] = df["Ticket_Priority"].str.strip().str.capitalize()
    elif "priority_score" in df.columns:
        df["Ticket_Priority"] = df["priority_score"].map({1: "Low", 2: "Medium", 3: "High", 4: "Critical"})

    df["Ticket_Status"] = df["Ticket_Status"].str.strip()
    return df


df = load_data()

# sidebar filters
with st.sidebar:
    st.title("Supportlytics")
    st.markdown("---")

    sel_priority = st.multiselect("Priority",
                                  [p for p in PRIORITY_ORDER if p in df["Ticket_Priority"].unique()],
                                  default=df["Ticket_Priority"].dropna().unique().tolist())

    sel_type    = st.multiselect("Ticket Type",  df["Ticket_Type"].dropna().unique().tolist(),
                                 default=df["Ticket_Type"].dropna().unique().tolist())

    sel_channel = st.multiselect("Channel",      df["Ticket_Channel"].dropna().unique().tolist(),
                                 default=df["Ticket_Channel"].dropna().unique().tolist())

    sel_status  = st.multiselect("Status",       df["Ticket_Status"].dropna().unique().tolist(),
                                 default=df["Ticket_Status"].dropna().unique().tolist())

    min_yr, max_yr = int(df["Year"].min()), int(df["Year"].max())
    year_range = st.slider("Year Range", min_yr, max_yr, (min_yr, max_yr))

# apply all filters in one shot
fdf = df[
    df["Ticket_Priority"].isin(sel_priority) &
    df["Ticket_Type"].isin(sel_type) &
    df["Ticket_Channel"].isin(sel_channel) &
    df["Ticket_Status"].isin(sel_status) &
    df["Year"].between(*year_range)
]

st.title("IT Support Performance Dashboard")
st.caption(f"Showing {len(fdf):,} of {len(df):,} tickets")
st.markdown("---")

# top-level numbers
total    = len(fdf)
closed   = (fdf["Ticket_Status"] == "Closed").sum()
open_    = (fdf["Ticket_Status"] == "Open").sum()
avg_res  = fdf["Resolution_Hours"].mean()
critical = (fdf["Ticket_Priority"] == "Critical").sum()
avg_sat  = fdf["Customer_Satisfaction_Rating"].mean() if "Customer_Satisfaction_Rating" in fdf.columns else None


def kpi_card(col, value, label):
    col.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>""", unsafe_allow_html=True)


cols = st.columns(6)
kpi_card(cols[0], f"{total:,}",    "Total Tickets")
kpi_card(cols[1], f"{closed:,}",   "Closed")
kpi_card(cols[2], f"{open_:,}",    "Open")
kpi_card(cols[3], f"{avg_res:.1f}h" if avg_res and not np.isnan(avg_res) else "N/A", "Avg Resolution")
kpi_card(cols[4], f"{critical:,}", "Critical")
kpi_card(cols[5], f"{avg_sat:.2f}" if avg_sat and not np.isnan(avg_sat) else "N/A", "Avg Satisfaction")

st.markdown("<br>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Performance", "Geographic", "Deep Dive"])


# --- Overview ---
with tab1:
    c1, c2 = st.columns(2)

    with c1:
        data = fdf["Ticket_Type"].value_counts().reset_index()
        data.columns = ["Type", "Count"]
        fig = px.bar(data, x="Type", y="Count", color="Count",
                     color_continuous_scale="Viridis", title="Tickets by Type",
                     template=TEMPLATE, text="Count")
        fig.update_traces(textposition="outside")
        fig.update_layout(**DARK_BG, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        data = fdf["Ticket_Priority"].value_counts().reset_index()
        data.columns = ["Priority", "Count"]
        fig = px.pie(data, values="Count", names="Priority", hole=0.45,
                     color="Priority", color_discrete_map=PRIORITY_COLORS,
                     title="Tickets by Priority", template=TEMPLATE)
        fig.update_layout(**DARK_BG)
        st.plotly_chart(fig, use_container_width=True)

    c3, c4 = st.columns(2)

    with c3:
        data = fdf["Ticket_Channel"].value_counts().reset_index()
        data.columns = ["Channel", "Count"]
        fig = px.bar(data, x="Count", y="Channel", orientation="h",
                     color="Count", color_continuous_scale="Blues",
                     title="Tickets by Channel", template=TEMPLATE, text="Count")
        fig.update_traces(textposition="outside")
        fig.update_layout(**DARK_BG, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

    with c4:
        data = fdf["Ticket_Status"].value_counts().reset_index()
        data.columns = ["Status", "Count"]
        fig = px.pie(data, values="Count", names="Status", hole=0.4,
                     title="Ticket Status", template=TEMPLATE)
        fig.update_layout(**DARK_BG)
        st.plotly_chart(fig, use_container_width=True)

    # heatmap showing how many tickets fall into each priority + type combo
    pivot = fdf.groupby(["Ticket_Priority", "Ticket_Type"]).size().unstack(fill_value=0)
    pivot = pivot.reindex([p for p in PRIORITY_ORDER if p in pivot.index])
    fig = px.imshow(pivot, color_continuous_scale="RdYlGn_r", text_auto=True,
                    title="Priority vs Type Heatmap", template=TEMPLATE, aspect="auto")
    fig.update_layout(**DARK_BG)
    st.plotly_chart(fig, use_container_width=True)


# --- Performance ---
with tab2:
    # only look at rows where we actually have a valid resolution time
    res_df = fdf[fdf["Resolution_Hours"].notna() & (fdf["Resolution_Hours"] > 0)]

    c1, c2 = st.columns(2)

    with c1:
        if not res_df.empty:
            data = res_df.groupby("Ticket_Priority")["Resolution_Hours"].mean().reset_index()
            data.columns = ["Priority", "Avg_Hours"]
            fig = px.bar(data, x="Priority", y="Avg_Hours", color="Priority",
                         color_discrete_map=PRIORITY_COLORS, title="Avg Resolution Time by Priority",
                         template=TEMPLATE, text=data["Avg_Hours"].round(1))
            fig.update_traces(textposition="outside")
            fig.update_layout(**DARK_BG, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    with c2:
        if not res_df.empty:
            data = res_df.groupby("Ticket_Type")["Resolution_Hours"].mean().reset_index()
            data.columns = ["Type", "Avg_Hours"]
            data = data.sort_values("Avg_Hours")
            fig = px.bar(data, x="Avg_Hours", y="Type", orientation="h",
                         color="Avg_Hours", color_continuous_scale="Oranges",
                         title="Avg Resolution Time by Type", template=TEMPLATE,
                         text=data["Avg_Hours"].round(1))
            fig.update_traces(textposition="outside")
            fig.update_layout(**DARK_BG, coloraxis_showscale=False)
            st.plotly_chart(fig, use_container_width=True)

    if not res_df.empty:
        fig = px.box(res_df, x="Ticket_Priority", y="Resolution_Hours",
                     color="Ticket_Priority", color_discrete_map=PRIORITY_COLORS,
                     category_orders={"Ticket_Priority": PRIORITY_ORDER},
                     title="Resolution Time Distribution by Priority",
                     template=TEMPLATE, points="outliers")
        fig.update_layout(**DARK_BG, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    if "Customer_Satisfaction_Rating" in fdf.columns:
        sat_df = fdf.dropna(subset=["Customer_Satisfaction_Rating"])
        c1, c2 = st.columns(2)

        with c1:
            data = sat_df.groupby("Ticket_Priority")["Customer_Satisfaction_Rating"].mean().reset_index()
            data.columns = ["Priority", "Avg"]
            fig = px.bar(data, x="Priority", y="Avg", color="Priority",
                         color_discrete_map=PRIORITY_COLORS, title="Avg Satisfaction by Priority",
                         template=TEMPLATE, text=data["Avg"].round(2))
            fig.update_traces(textposition="outside")
            fig.update_layout(**DARK_BG, showlegend=False, yaxis=dict(range=[0, 5.5]))
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            data = sat_df.groupby("Ticket_Type")["Customer_Satisfaction_Rating"].mean().reset_index()
            data.columns = ["Type", "Avg"]
            data = data.sort_values("Avg")
            fig = px.bar(data, x="Avg", y="Type", orientation="h",
                         color="Avg", color_continuous_scale="RdYlGn",
                         title="Avg Satisfaction by Ticket Type", template=TEMPLATE,
                         text=data["Avg"].round(2))
            fig.update_traces(textposition="outside")
            fig.update_layout(**DARK_BG, coloraxis_showscale=False, xaxis=dict(range=[0, 5.5]))
            st.plotly_chart(fig, use_container_width=True)


# --- Geographic ---
with tab3:
    # check which geographic column exists in this dataset
    geo_col = next((c for c in ["Country", "State", "Location", "Region"] if c in fdf.columns), None)

    if geo_col:
        data = fdf[geo_col].value_counts().reset_index()
        data.columns = [geo_col, "Count"]
        mode = "country names" if "country" in geo_col.lower() else "USA-states"
        fig = px.choropleth(data, locations=geo_col, locationmode=mode, color="Count",
                            color_continuous_scale="Viridis", title=f"Tickets by {geo_col}",
                            template=TEMPLATE)
        fig.update_layout(**DARK_BG, geo=dict(bgcolor="rgba(0,0,0,0)"))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No geographic column found in the data.")

    if "Product_Purchased" in fdf.columns:
        prod_counts = fdf["Product_Purchased"].value_counts().head(15).reset_index()
        prod_counts.columns = ["Product", "Count"]
        c1, c2 = st.columns(2)

        with c1:
            fig = px.bar(prod_counts.sort_values("Count"), x="Count", y="Product",
                         orientation="h", color="Count", color_continuous_scale="Purples",
                         title="Top 15 Products by Ticket Volume", template=TEMPLATE, text="Count")
            fig.update_traces(textposition="outside")
            fig.update_layout(**DARK_BG, coloraxis_showscale=False)
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            if "Customer_Satisfaction_Rating" in fdf.columns:
                data = (fdf.dropna(subset=["Customer_Satisfaction_Rating"])
                           .groupby("Product_Purchased")["Customer_Satisfaction_Rating"]
                           .mean().reset_index())
                data.columns = ["Product", "Avg"]
                data = data.sort_values("Avg").tail(15)
                fig = px.bar(data, x="Avg", y="Product", orientation="h",
                             color="Avg", color_continuous_scale="RdYlGn",
                             title="Avg Satisfaction by Product", template=TEMPLATE,
                             text=data["Avg"].round(2))
                fig.update_traces(textposition="outside")
                fig.update_layout(**DARK_BG, coloraxis_showscale=False, xaxis=dict(range=[0, 5.5]))
                st.plotly_chart(fig, use_container_width=True)

        # bubble chart — bigger bubble means more tickets for that product/priority combo
        bubble = fdf.groupby(["Product_Purchased", "Ticket_Priority"]).size().reset_index(name="Count")
        bubble = bubble[bubble["Product_Purchased"].isin(prod_counts["Product"])]
        fig = px.scatter(bubble, x="Product_Purchased", y="Ticket_Priority", size="Count",
                         color="Ticket_Priority", color_discrete_map=PRIORITY_COLORS,
                         size_max=45, title="Product vs Priority Bubble Chart",
                         template=TEMPLATE, category_orders={"Ticket_Priority": PRIORITY_ORDER})
        fig.update_layout(**DARK_BG, showlegend=False, xaxis_tickangle=-40)
        st.plotly_chart(fig, use_container_width=True)


# --- Deep Dive ---
with tab4:
    if "Ticket_Subject" in fdf.columns:
        c1, c2 = st.columns(2)

        with c1:
            data = fdf["Ticket_Subject"].value_counts().head(12).reset_index()
            data.columns = ["Subject", "Count"]
            fig = px.bar(data.sort_values("Count"), x="Count", y="Subject",
                         orientation="h", color="Count", color_continuous_scale="Teal",
                         title="Top Ticket Subjects", template=TEMPLATE, text="Count")
            fig.update_traces(textposition="outside")
            fig.update_layout(**DARK_BG, coloraxis_showscale=False)
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            top_subj = fdf["Ticket_Subject"].value_counts().head(8).index
            data = (fdf[fdf["Ticket_Subject"].isin(top_subj)]
                      .groupby(["Ticket_Subject", "Ticket_Status"]).size()
                      .reset_index(name="Count"))
            fig = px.bar(data, x="Count", y="Ticket_Subject", color="Ticket_Status",
                         orientation="h", barmode="stack",
                         title="Subject vs Status", template=TEMPLATE)
            fig.update_layout(**DARK_BG)
            st.plotly_chart(fig, use_container_width=True)

    if "Customer_Age" in fdf.columns:
        fdf = fdf.copy()
        fdf["Age_Group"] = pd.cut(fdf["Customer_Age"],
                                  bins=[0, 25, 35, 45, 55, 65, 100],
                                  labels=["<25", "25-35", "35-45", "45-55", "55-65", "65+"])
        c1, c2 = st.columns(2)

        with c1:
            data = fdf["Age_Group"].value_counts().sort_index().reset_index()
            data.columns = ["Age_Group", "Count"]
            fig = px.bar(data, x="Age_Group", y="Count", color="Count",
                         color_continuous_scale="Blues", title="Tickets by Age Group",
                         template=TEMPLATE, text="Count")
            fig.update_traces(textposition="outside")
            fig.update_layout(**DARK_BG, coloraxis_showscale=False)
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            if "Customer_Gender" in fdf.columns:
                data = fdf["Customer_Gender"].value_counts().reset_index()
                data.columns = ["Gender", "Count"]
                fig = px.pie(data, values="Count", names="Gender", hole=0.4,
                             title="Tickets by Gender", template=TEMPLATE)
                fig.update_layout(**DARK_BG)
                st.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        data = fdf.groupby(["Ticket_Type", "Ticket_Channel"]).size().reset_index(name="Count")
        fig = px.bar(data, x="Ticket_Type", y="Count", color="Ticket_Channel",
                     barmode="group", title="Ticket Type vs Channel", template=TEMPLATE,
                     color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_layout(**DARK_BG, xaxis_tickangle=-20)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Raw Data")
    n = st.slider("Rows to show", 5, 100, 20, step=5)
    wanted_cols = ["Ticket_ID", "Customer_Name", "Ticket_Type", "Ticket_Priority",
                   "Ticket_Status", "Ticket_Channel", "Resolution_Hours",
                   "Customer_Satisfaction_Rating", "Product_Purchased"]
    show_cols = [c for c in wanted_cols if c in fdf.columns]
    st.dataframe(fdf[show_cols].head(n).reset_index(drop=True), use_container_width=True)

st.markdown("---")
st.caption("Supportlytics — IT Support Dashboard")