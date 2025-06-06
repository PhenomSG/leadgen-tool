# AI-Powered Lead Generation Dashboard — Project Report

**Submitted by:** Sahaj Gupta  
**Challenge:** Reimagine part of SaaSquatchLeads in under 5 hours  
**Approach:** Quality-first strategy focusing on impactful features + innovation

## Approach & Thought Process

Inspired by the SaaSquatchLeads platform, I designed a streamlined lead generation dashboard tailored for sales teams targeting early-stage and underserved B2B companies. Rather than recreating the entire platform, I chose to focus deeply on two high-impact areas:

1. **Structured Company Data Analysis** — enabling clear segmentation and filtering.
2. **Intent + Sentiment Signals** — to identify leads based on real-world business activity.

This approach allowed me to blend static datasets with dynamic data sources (news and sentiment) to support smarter sales decisions, not just more data.

## Technical Overview

### 1. **Stack Used**
- **Python** (Pandas, Streamlit, BeautifulSoup, Requests, Selenium)
- **TextBlob** for sentiment analysis
- **Kaggle Dataset + LinkedIn scraping** for foundational company data

### 2. **Dashboard Features**
- Visual Analytics (Industry trends, LinkedIn followers vs. employee count)
- Search + Filter by Company Name, Industry, Size, Country
- CSV/Excel Export with selectable columns
- **Lead Scoring System** based on real-time business signals

## Innovation: Lead Scout — News-Based Scoring

To push the boundaries of traditional scraping, I built a module called **Lead Scout**, which scrapes recent news about companies and scores leads using a custom logic:

| Signal               | Score |
|----------------------|-------|
| Funding Announcement | +3    |
| Product Launch       | +2    |
| Executive Hire       | +1    |
| Layoffs/Scandal      | -2    |
| TextBlob Sentiment   | ±0.5  |

Companies are then categorized as **High**, **Mid**, **Neutral**, or **Cautionary** leads—helping sales teams prioritize outreach with much greater precision.


## Evaluation & Limitations

- This tool focuses more on **usefulness than raw ML metrics**. It’s designed for sales teams, not data scientists.
- The sentiment analysis is handled via **TextBlob**, a lightweight NLP model. While simple, it provides effective polarity scoring for news headlines.
- Due to time limits, the news parsing logic is basic—this could be enhanced using spaCy or a transformer-based custom NLP model for better contextual scoring.


## Conclusion

This project was a wonderful opportunity to merge **technical scraping**, **data visualization**, and **real-world lead prioritization**. I'm genuinely excited about how Lead Scout blends traditional leadgen with dynamic signals to improve decision-making.

Thank you for the opportunity to build this. I learned a lot—and I hope the tool brings value beyond just its simplicity.

