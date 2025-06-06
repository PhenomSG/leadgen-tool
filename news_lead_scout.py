import streamlit as st
import pandas as pd
import numpy as np
from textblob import TextBlob
import random
from datetime import datetime, timedelta

# Initialize session state for persistent data
if 'news_data' not in st.session_state:
    st.session_state.news_data = pd.DataFrame()

# Page configuration
st.set_page_config(page_title="NewsLead Scout", layout="wide")
st.title("NewsLead Scout - AI-Powered Lead Generation")
st.caption("Identify high-potential leads from news analysis")

# --------------------------
# Step 2: Synthetic Data Generation
# --------------------------
def news_scraped(num_articles=50):
    companies = [
        "TechNova", "CloudForge", "DataSphere", "QuantumLeap", "CyberShield",
        "AI Dynamics", "ByteCraft", "NexaTech", "FutureSystems", "DigitalPulse",
        "SecureNet", "VisionAI", "RoboWorks", "BioTech Innovations", "EcoSolutions"
    ]
    
    industries = ["AI/ML", "Cybersecurity", "Biotech", "Fintech", "Clean Energy", "SaaS", "IoT"]
    
    news_types = {
        "funding": ("raised $XX million", "secured funding", "closed Series X"),
        "product": ("launched new platform", "introduced breakthrough", "released innovative"),
        "hire": ("appointed new CEO", "hired industry veteran", "expanded leadership team"),
        "layoff": ("announced layoffs", "downsizing workforce", "restructuring operations"),
        "scandal": ("facing investigation", "controversy over", "accused of"),
        "neutral": ("partnered with", "expanded to", "won award for")
    }
    
    news = []
    for _ in range(num_articles):
        company = random.choice(companies)
        date = datetime.now() - timedelta(days=random.randint(0, 30))
        industry = random.choice(industries)
        news_type, phrases = random.choice(list(news_types.items()))
        headline = f"{company} {random.choice(phrases)} in {industry} sector"
        
        news.append({
            "date": date.strftime("%Y-%m-%d"),
            "company": company,
            "headline": headline,
            "news_type": news_type,
            "industry": industry
        })
    
    return pd.DataFrame(news)

# --------------------------
# Step 3: Analysis Functions
# --------------------------
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def calculate_lead_score(row):
    score_map = {
        "funding": 3,
        "product": 2,
        "hire": 1,
        "layoff": -2,
        "scandal": -2,
        "neutral": 0
    }
    base_score = score_map[row['news_type']]
    sentiment_boost = row['sentiment'] * 0.5
    return base_score + sentiment_boost

# --------------------------
# Main App Execution
# --------------------------
if st.button("Scrape News Data") or not st.session_state.news_data.empty:
    if st.session_state.news_data.empty:
        st.session_state.news_data = news_scraped(100)
    
    # Add analysis columns
    st.session_state.news_data['sentiment'] = st.session_state.news_data['headline'].apply(analyze_sentiment)
    st.session_state.news_data['lead_score'] = st.session_state.news_data.apply(calculate_lead_score, axis=1)
    
    # --------------------------
    # Display Results
    # --------------------------
    st.subheader("Generated News Data")
    st.dataframe(st.session_state.news_data)
    
    # Dashboard
    st.subheader("Lead Prioritization Dashboard")
    
    # Aggregate scores
    company_scores = st.session_state.news_data.groupby('company').agg(
        total_score=('lead_score', 'sum'),
        article_count=('lead_score', 'count'),
        latest_news=('date', 'max')
    ).reset_index().sort_values('total_score', ascending=False)
    
    company_scores['priority'] = pd.cut(
        company_scores['total_score'],
        bins=[-float('inf'), 0, 3, 6, float('inf')],
        labels=['Low', 'Medium', 'High', 'Critical']
    )
    
    # Layout
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write("**Top Companies by Lead Score**")
        st.dataframe(company_scores.head(10))
    
    with col2:
        st.write("**Priority Distribution**")
        st.bar_chart(company_scores['priority'].value_counts())
    
    # Company deep dive
    st.subheader("🔍 Company Analysis")
    selected_company = st.selectbox("Select Company", company_scores['company'])
    
    if selected_company:
        company_news = st.session_state.news_data[st.session_state.news_data['company'] == selected_company]
        st.write(f"### {selected_company} News History")
        for _, row in company_news.iterrows():
            st.write(f"- **{row['date']}**: {row['headline']} (Score: {row['lead_score']})")