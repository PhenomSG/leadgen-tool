import streamlit as st
import pandas as pd
from textblob import TextBlob

# Page setup
st.set_page_config(layout="wide")
st.title("NewsLead Scout (Demo)")
st.subheader("Pitch Deck: AI-Powered Lead Generation from News")

# Load the CSV data
@st.cache_data
def load_data():
    return pd.read_csv("news_leads.csv")

df = load_data()

# Sentiment analysis
df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Lead scoring system
def calculate_score(row):
    if row['news_type'] == 'funding': return 3 + row['sentiment']
    elif row['news_type'] == 'product': return 2 + row['sentiment']
    elif row['news_type'] == 'hire': return 1 + row['sentiment']
    elif row['news_type'] in ['layoff','scandal']: return -2 + row['sentiment']
    else: return 0 + row['sentiment']

df['lead_score'] = df.apply(calculate_score, axis=1)

# Priority calculation
def get_priority(score):
    if score >= 3: return "High Potential Lead"
    elif score >= 1: return "Mid Potential Lead"
    elif score >= 0: return "Neutral Lead"
    else: return "Caution"

df['priority'] = df['lead_score'].apply(get_priority)

# Dashboard
st.subheader("Sample News Data")
st.dataframe(df)

# Key metrics
st.subheader("Lead Quality Breakdown")
col1, col2, col3 = st.columns(3)
col1.metric("Total Companies", df['company'].nunique())
col2.metric("Hot Leads", len(df[df['priority'] == "Hot Potential Lead"]))
col3.metric("Warning Signs", len(df[df['priority'] == "Caution"]))

# Visualizations
st.subheader("Best Potential Leads")
top_leads = df.sort_values('lead_score', ascending=False).head(5)
st.table(top_leads[['company','headline','lead_score','priority']])

# Value proposition
st.markdown("""
## Investor Pitch

**Problem**: 
- Sales teams waste time on cold outreach
- Miss emerging companies showing buying signals

**Solution**: 
Automatically identify companies in growth mode  
Score leads based on news sentiment  
Prioritize prospects likely to buy  

**Key Differentiators**:
- Real-time intelligence (vs static CRM data)
- Predictive scoring (not just firmographics)
- Industry-specific signals

**Next Steps**:
1. Connect to 50+ news sources
2. Add executive contact enrichment
3. CRM integrations (Salesforce/HubSpot)
""")