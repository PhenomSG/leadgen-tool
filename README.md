# LeadGen Tool – AI-Powered Lead Generation Dashboard

Welcome to **LeadGen Tool**, a smart, modular lead generation dashboard built for the SaaSquatchLeads challenge.

This project focuses on **quality-first development**, offering actionable insights from company data enriched with **news-based scoring and sentiment analysis** to prioritize outreach targets effectively.

> Built by [Sahaj Gupta](https://github.com/PhenomSG)

---

## Features

### Dashboard (app.py)
- Visualize top industries, company sizes, and LinkedIn trends
- Analyze employee count vs followers
- Identify underserved company segments for SaaS outreach

### Company Search
- Search by **company name** or **industry**
- Instant filtering to find specific target groups

### Lead Generator
- Filter by **company size** (small, mid, large)
- Filter by **country code**

### Data Export
- Export selected company data to **CSV** or **Excel**
- Choose specific columns for better CRM integration

### Lead Scout – *Innovation*  -->> Files - (news_lead_scout.py) and (lead_scout.py)
A custom-built AI module that scores companies based on their **real-time intent** and **news sentiment**, using scraping + NLP.

| Business Signal       | Score |
|------------------------|-------|
| Funding Announcement   | +3    |
| Product Launch         | +2    |
| Executive Hire         | +1    |
| Layoffs/Scandal        | -2    |
| Sentiment (TextBlob)   | ±0.5  |

Categorizes leads into:  
High Potential • Mid Potential • Neutral • Cautionary Leads

---

## Tech Stack

- **Python**
- **Streamlit** – UI and interactivity
- **BeautifulSoup & Selenium** – Scraping
- **Pandas** – Data handling
- **TextBlob** – Sentiment analysis
- **Kaggle Dataset + LinkedIn Scraping**

---

##  Project Structure

```bash
├── app.py                      # Main Streamlit dashboard (UI)
├── lead_scout.py               # Lead scoring logic based on company metadata
├── news_lead_scout.py          # News scraping & sentiment-based scoring module
├── dataset-cleaning.ipynb      # Notebook for data cleaning and preprocessing
├── gameplan.txt                # Project outline / development notes
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── LICENSE                     # MIT License
├── .gitignore                  # Files/folders to ignore in Git

├── Dataset/                    # Static company datasets
│   ├── LinkedIn company information datasets (Public web data).csv
│   └── LinkedIn people profiles datasets.csv

├── Cleaned_Dataset/                    # Static company datasets
│   ├── cleaned_company_data.csv
│   └── news_leads.csv  

├── Web Scrapper/               # Scripts & outputs for scraping LinkedIn data
│   ├── scrapper1.py            # Scraper script for LinkedIn
│   ├── linkedin_scrapper.ipynb # Scraping notebook
│   ├── linkedin_jobs_page.html # Saved HTML for offline parsing
│   └── linkedin_jobs_extracted.csv

├── demo/                       # Sample outputs or demo-ready data
│   └── linkedin_jobs_extracted.csv

├── news_leads.csv              # Output: News-based scored leads

```
