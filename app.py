# ==========================================================
# Nassau Candy Distributor Dashboard
# Factory Reallocation & Shipping Optimization
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Nassau Candy Dashboard",
    page_icon="🍬",
    layout="wide"
)

# ----------------------------------------------------------
# Load CSS
# ----------------------------------------------------------

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------------------------------------------
# Load Datasets
# ----------------------------------------------------------

orders = pd.read_csv("datasets/orders.csv")
processed_orders = pd.read_csv("datasets/processed_orders.csv")
recommendations = pd.read_csv("datasets/factory_recommendations.csv")
kpi_summary = pd.read_csv("datasets/kpi_summary.csv")

model = joblib.load("best_lead_time_model.pkl")

# ----------------------------------------------------------
# Header
# ----------------------------------------------------------

st.markdown("""
<div class='main-header'>
<h1>🍬 Nassau Candy Distributor</h1>
<h3>Factory Reallocation & Shipping Optimization Recommendation System</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Sidebar Filters
# ==========================================================

st.sidebar.title("⚙ Dashboard Filters")

product = st.sidebar.selectbox(
    "Select Product",
    sorted(processed_orders["Product Name"].unique())
)

region = st.sidebar.selectbox(
    "Select Region",
    sorted(processed_orders["Region"].unique())
)

ship_mode = st.sidebar.selectbox(
    "Ship Mode",
    sorted(processed_orders["Ship Mode"].unique())
)

priority = st.sidebar.slider(
    "Optimization Priority",
    0,
    100,
    50
)

st.sidebar.markdown("---")

st.sidebar.success("Filters Applied")
# ==========================================================
# KPI Calculations
# ==========================================================

total_orders = len(orders)

avg_lead_time = processed_orders["Lead Time"].mean()

avg_profit = processed_orders["Gross Profit"].mean()

total_recommendations = len(recommendations)

# ==========================================================
# KPI Cards
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📦 Total Orders",
        f"{total_orders:,}"
    )

with col2:

    st.metric(
        "🚚 Avg Lead Time",
        f"{avg_lead_time:.2f} Days"
    )

with col3:

    st.metric(
        "💰 Avg Gross Profit",
        f"${avg_profit:.2f}"
    )

with col4:

    st.metric(
        "🏭 Recommendations",
        f"{total_recommendations:,}"
    )

st.markdown("---")
# ==========================================================
# Executive Summary
# ==========================================================

st.subheader("📊 Executive Summary")

left, right = st.columns([2,1])

with left:

    st.write("""
This dashboard provides decision support for Nassau Candy Distributor by
analyzing shipping performance, factory assignments, and recommendation
scenarios.

Use the filters in the sidebar to explore product-wise and region-wise
performance.
""")

with right:

    st.info(
"""
✔ Predict Lead Time

✔ Recommend Best Factory

✔ Compare Scenarios

✔ Analyze Business Impact
"""
)
# ==========================================================
# Executive Dashboard
# ==========================================================

st.subheader("📊 Executive Dashboard")

col1, col2 = st.columns(2)    
with col1:

    factory_orders = (
        processed_orders["Factory"]
        .value_counts()
        .reset_index()
    )

    factory_orders.columns = ["Factory", "Orders"]

    fig = px.bar(
        factory_orders,
        x="Factory",
        y="Orders",
        color="Orders",
        text="Orders",
        title="Factory-wise Order Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
with col2:

    fig = px.histogram(
        processed_orders,
        x="Lead Time",
        nbins=20,
        color_discrete_sequence=["#1f77b4"],
        title="Lead Time Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)    
col3, col4 = st.columns(2)  
with col3:

    fig = px.histogram(
        processed_orders,
        x="Gross Profit",
        nbins=20,
        color_discrete_sequence=["green"],
        title="Gross Profit Distribution"
    )

    st.plotly_chart(fig, use_container_width=True) 
with col4:

    recommendation_count = (
        recommendations["Recommendation"]
        .value_counts()
        .reset_index()
    )

    recommendation_count.columns = [
        "Recommendation",
        "Count"
    ]

    fig = px.pie(
        recommendation_count,
        names="Recommendation",
        values="Count",
        title="Recommendation Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)   
st.subheader("🏭 Factory Performance Comparison")

factory_performance = (

    processed_orders
    .groupby("Factory")[["Lead Time", "Gross Profit"]]
    .mean()
    .reset_index()

)

fig = px.scatter(

    factory_performance,

    x="Lead Time",

    y="Gross Profit",

    color="Factory",

    size="Gross Profit",

    hover_name="Factory",

    title="Average Lead Time vs Gross Profit"

)

st.plotly_chart(fig, use_container_width=True)      
st.markdown("---")
# ==========================================================
# Factory Optimization Simulator
# ==========================================================

st.header("🏭 Factory Optimization Simulator")

selected_product = st.selectbox(
    "Select Product",
    sorted(recommendations["Product Name"].unique())
)
product_data = recommendations[
    recommendations["Product Name"] == selected_product
].iloc[0]
col1, col2 = st.columns(2)

with col1:

    st.subheader("Current Factory")

    st.success(product_data["Current Factory"])

    st.metric(
        "Current Lead Time",
        f"{product_data['Lead Time']:.2f} Days"
    )

with col2:

    st.subheader("Recommended Factory")

    st.info(product_data["Simulated Factory"])

    st.metric(
        "Predicted Lead Time",
        f"{product_data['Predicted Lead Time']:.2f} Days"
    )
col3, col4, col5 = st.columns(3)

with col3:

    st.metric(
        "Lead Time Improvement",
        f"{product_data['Lead Time Improvement']:.2f} Days"
    )

with col4:

    st.metric(
        "Shipping Cost Savings",
        f"${product_data['Shipping Cost Savings']:.2f}"
    )

with col5:

    st.metric(
        "Profit Impact",
        f"${product_data['Profit Impact']:.2f}"
    )
st.markdown("### Recommendation")

if product_data["Recommendation"] == "Reallocate":

    st.success(
        f"""
Move production from

**{product_data['Current Factory']}**

to

**{product_data['Simulated Factory']}**
"""
    )

else:

    st.info("Current Factory is already optimal.")        
priority = product_data["Priority"]

if priority == "High":

    st.error(f"Priority : {priority}")

elif priority == "Medium":

    st.warning(f"Priority : {priority}")

else:

    st.success(f"Priority : {priority}")    
st.markdown("---")
st.header("🔄 What-If Scenario Analysis")

st.write("Compare the current factory assignment with the recommended assignment.")

comparison = pd.DataFrame({

    "Metric":[
        "Current Factory",
        "Recommended Factory",
        "Current Lead Time (Days)",
        "Predicted Lead Time (Days)",
        "Lead Time Improvement",
        "Shipping Cost Savings ($)",
        "Profit Impact ($)"
    ],

    "Current":[

        product_data["Current Factory"],

        "-",

        round(product_data["Lead Time"],2),

        "-",

        "-",

        "-",

        "-"

    ],

    "Recommended":[

        "-",

        product_data["Simulated Factory"],

        "-",

        round(product_data["Predicted Lead Time"],2),

        round(product_data["Lead Time Improvement"],2),

        round(product_data["Shipping Cost Savings"],2),

        round(product_data["Profit Impact"],2)

    ]

})

st.dataframe(comparison,use_container_width=True)  
st.markdown("---")
st.header("⭐ Recommendation Dashboard")

search_order = st.text_input(
    "Search Order ID"
)

recommendation_table = recommendations.copy()

if search_order:

    recommendation_table = recommendation_table[
        recommendation_table["Order ID"].astype(str).str.contains(search_order)
    ]

st.dataframe(
    recommendation_table,
    use_container_width=True,
    height=500
)  
csv = recommendation_table.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📥 Download Recommendation Report",

    data=csv,

    file_name="factory_recommendations.csv",

    mime="text/csv"

)
st.markdown("---")
st.header("⚠ Risk & Impact Panel")
priority_count = (

    recommendations["Priority"]

    .value_counts()

    .reset_index()

)

priority_count.columns=["Priority","Count"]

fig = px.bar(

    priority_count,

    x="Priority",

    y="Count",

    color="Priority",

    text="Count",

    title="Priority Distribution"

)

st.plotly_chart(fig,use_container_width=True)
fig = px.histogram(

    recommendations,

    x="Profit Impact",

    nbins=25,

    title="Profit Impact Distribution"

)

st.plotly_chart(fig,use_container_width=True)
fig = px.histogram(

    recommendations,

    x="Scenario Confidence Score",

    nbins=20,

    title="Scenario Confidence Score"

)

st.plotly_chart(fig,use_container_width=True)
st.subheader("🚨 High Priority Reallocations")

high_priority = recommendations[

    recommendations["Priority"]=="High"

]

st.dataframe(

    high_priority,

    use_container_width=True,

    height=300

)
st.markdown("---")

st.header("📈 KPI Summary")

st.dataframe(

    kpi_summary,

    use_container_width=True

)
st.markdown("---")

st.header("🏭 Factory Performance Summary")

factory_summary = (

    processed_orders

    .groupby("Factory")

    .agg({

        "Lead Time":"mean",

        "Gross Profit":"mean",

        "Estimated Shipping Cost":"mean",

        "Order ID":"count"

    })

    .reset_index()

)

factory_summary.columns=[

    "Factory",

    "Average Lead Time",

    "Average Gross Profit",

    "Average Shipping Cost",

    "Orders"

]

st.dataframe(

    factory_summary,

    use_container_width=True

)
st.markdown("---")

st.header("ℹ Project Information")

st.info("""

### Factory Reallocation & Shipping Optimization Recommendation System

This dashboard was developed to assist Nassau Candy Distributor in improving
factory assignment decisions using Machine Learning and Data Analytics.

Features Included

• Lead Time Prediction

• Factory Reallocation Recommendation

• Shipping Optimization

• KPI Dashboard

• Risk Assessment

• Recommendation Analytics

• Interactive What-If Scenario Analysis

""")
st.markdown("---")

st.markdown("""

<div style="text-align:center;color:gray;">

Developed using ❤️ with Streamlit

Factory Reallocation & Shipping Optimization Recommendation System

</div>

""",unsafe_allow_html=True)