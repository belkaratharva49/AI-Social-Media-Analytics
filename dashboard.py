import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# PAGE CONFIG
st.set_page_config(
    page_title="AI Social Media Command Center",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# LOAD DATA
df = pd.read_csv("analytics.csv")   

# -------------------------------
# EXTRA CALCULATIONS
# -------------------------------

df["engagement_rate"] = (
    (
        df["likes"]
        + df["comments"]
        + df["shares"]
        + df["saves"]
    )
    / df["reach"]
) * 100

df["viral_score"] = (
    df["shares"] * 2
    + df["saves"] * 3
)

df["follower_gain"] = (
    df["followers"].diff().fillna(0)
)

# TOTALS
total_reach = df["reach"].sum()
total_likes = df["likes"].sum()
total_comments = df["comments"].sum()
total_shares = df["shares"].sum()
total_saves = df["saves"].sum()

latest_followers = df["followers"].iloc[-1]

engagement_rate = df["engagement_rate"].mean()

# PLATFORM HEALTH
health_score = min(
    int(engagement_rate * 10),
    100
)

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.title("🚀 AI Command Center")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Audience Intelligence",
        "Engagement Analytics",
        "Growth Prediction",
        "AI Insights",
        "Content Intelligence",
        "Virality Center",
        "Audience Mood",
        "Posting Intelligence"
    ]
)

st.sidebar.markdown("---")

st.sidebar.metric(
    "Platform Health",
    f"{health_score}/100"
)

st.sidebar.success(
    "System Status: Active"
    
)

# -------------------------------
# HEADER
# -------------------------------

st.title("🚀 AI Social Media Command Center")

st.caption(
    "Enterprise Instagram Intelligence Platform"
)

st.markdown("---")

# -------------------------------
# KPI CARDS
# -------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "📈 Reach",
    f"{total_reach:,}",
    "+18%"
)

col2.metric(
    "❤️ Likes",
    f"{total_likes:,}",
    "+24%"
)

col3.metric(
    "💬 Comments",
    f"{total_comments:,}",
    "+11%"
)

col4.metric(
    "👥 Followers",
    f"{latest_followers:,}",
    "+31%"
)

col5.metric(
    "⚡ Engagement",
    f"{engagement_rate:.2f}%",
    "+8%"
)

st.markdown("---")

# =====================================================
# EXECUTIVE OVERVIEW
# =====================================================

if page == "Executive Overview":

    st.subheader("📊 Reach Performance")

    fig1 = px.area(
        df,
        x="date",
        y="reach"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.subheader("🔥 Followers Growth")

    fig2 = px.line(
        df,
        x="date",
        y="followers",
        markers=True
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader("📌 Engagement Distribution")

    pie_data = pd.DataFrame({
        "Metric": [
            "Likes",
            "Comments",
            "Shares",
            "Saves"
        ],
        "Value": [
            total_likes,
            total_comments,
            total_shares,
            total_saves
        ]
    })

    fig3 = px.pie(
        pie_data,
        names="Metric",
        values="Value"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# =====================================================
# AUDIENCE INTELLIGENCE
# =====================================================

elif page == "Audience Intelligence":

    st.subheader("👀 Profile View Intelligence")

    fig4 = px.bar(
        df,
        x="date",
        y="profile_views"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.subheader("📈 Audience Growth Velocity")

    fig5 = px.line(
        df,
        x="date",
        y="follower_gain",
        markers=True
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# =====================================================
# ENGAGEMENT ANALYTICS
# =====================================================

elif page == "Engagement Analytics":

    st.subheader("❤️ Engagement Performance")

    fig6 = go.Figure()

    fig6.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["likes"],
            mode="lines+markers",
            name="Likes"
        )
    )

    fig6.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["comments"],
            mode="lines+markers",
            name="Comments"
        )
    )

    fig6.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["shares"],
            mode="lines+markers",
            name="Shares"
        )
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

    st.subheader("⚡ Engagement Rate")

    fig7 = px.line(
        df,
        x="date",
        y="engagement_rate",
        markers=True
    )

    st.plotly_chart(
        fig7,
        use_container_width=True
    )

# =====================================================
# GROWTH PREDICTION
# =====================================================

elif page == "Growth Prediction":

    st.subheader("🔮 AI Growth Prediction")

    avg_growth = int(
        df["followers"].diff().mean()
    )

    next_followers = (
        latest_followers
        + avg_growth * 7
    )

    st.info(
        f"""
        Predicted Followers
        in next 7 days:

        {next_followers}
        """
    )

    prediction_dates = list(range(1, 8))

    predictions = [
        latest_followers
        + avg_growth * x
        for x in prediction_dates
    ]

    pred_df = pd.DataFrame({
        "Day": prediction_dates,
        "Predicted Followers": predictions
    })

    fig8 = px.line(
        pred_df,
        x="Day",
        y="Predicted Followers",
        markers=True
    )

    st.plotly_chart(
        fig8,
        use_container_width=True
    )

# =====================================================
# AI INSIGHTS
# =====================================================

elif page == "AI Insights":

    st.subheader("🤖 AI Content Intelligence")

    best_day = df.loc[
        df["reach"].idxmax()
    ]

    worst_day = df.loc[
        df["reach"].idxmin()
    ]

    st.success(
        f"""
        🚀 Best Performing Day:

        {best_day['date']}

        Reach: {best_day['reach']}
        """
    )

    st.warning(
        f"""
        ⚠ Lowest Performing Day:

        {worst_day['date']}

        Reach: {worst_day['reach']}
        """
    )

    virality_score = min(
        int(
            (
                total_shares
                + total_saves
            ) / total_reach * 1000
        ),
        100
    )

    st.metric(
        "🔥 Virality Score",
        f"{virality_score}/100"
    )

    st.subheader("🧠 AI Recommendations")

    recommendations = [
        "Post more reels during high engagement days.",
        "Increase carousel posts for better saves.",
        "Use emotional captions for more shares.",
        "Post consistently at night hours.",
        "Increase short-form video content."
    ]

    for rec in recommendations:

        st.info(rec)

# =====================================================
# CONTENT INTELLIGENCE
# =====================================================

elif page == "Content Intelligence":

    st.subheader("🎬 Content Type Performance")

    content_data = pd.DataFrame({
        "Content Type": [
            "Reels",
            "Carousel",
            "Stories",
            "Static Posts"
        ],
        "Reach": [
            45000,
            30000,
            15000,
            12000
        ]
    })

    fig9 = px.bar(
        content_data,
        x="Content Type",
        y="Reach"
    )

    st.plotly_chart(
        fig9,
        use_container_width=True
    )

    st.subheader("🎨 Caption Style Analysis")

    caption_data = pd.DataFrame({
        "Caption Style": [
            "Emotional",
            "Luxury",
            "Funny",
            "Minimal"
        ],
        "Engagement": [
            92,
            80,
            70,
            65
        ]
    })

    fig10 = px.pie(
        caption_data,
        names="Caption Style",
        values="Engagement"
    )

    st.plotly_chart(
        fig10,
        use_container_width=True
    )

# =====================================================
# VIRALITY CENTER
# =====================================================

elif page == "Virality Center":

    st.subheader("🔥 Viral Content Detection")

    fig11 = px.line(
        df,
        x="date",
        y="viral_score",
        markers=True
    )

    st.plotly_chart(
        fig11,
        use_container_width=True
    )

    top_viral = df.loc[
        df["viral_score"].idxmax()
    ]

    st.success(
        f"""
        🚀 Most Viral Day:

        {top_viral['date']}

        Viral Score:
        {top_viral['viral_score']}
        """
    )

# =====================================================
# AUDIENCE MOOD
# =====================================================

elif page == "Audience Mood":

    st.subheader("😊 Audience Sentiment Analysis")

    mood_data = pd.DataFrame({
        "Mood": [
            "Positive",
            "Neutral",
            "Negative"
        ],
        "Percentage": [
            72,
            20,
            8
        ]
    })

    fig12 = px.pie(
        mood_data,
        names="Mood",
        values="Percentage"
    )

    st.plotly_chart(
        fig12,
        use_container_width=True
    )

    st.success(
        "Audience sentiment is strongly positive."
    )

# =====================================================
# POSTING INTELLIGENCE
# =====================================================

elif page == "Posting Intelligence":

    st.subheader("⏰ Best Posting Time Intelligence")

    post_data = pd.DataFrame({
        "Hour": [
            "9 AM",
            "12 PM",
            "6 PM",
            "9 PM"
        ],
        "Engagement": [
            40,
            65,
            88,
            95
        ]
    })

    fig13 = px.bar(
        post_data,
        x="Hour",
        y="Engagement"
    )

    st.plotly_chart(
        fig13,  
        use_container_width=True
    )

    st.success(
        "Best posting time detected: 9 PM"
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Powered by Python • Streamlit • Plotly • AI Intelligence"
)

#=======================================================
# THIS IS BASICALLY A MOCKUP DASHBOARD WITH GENERATED DATA AND INSIGHTS
#========================================================