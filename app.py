import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

# Load data
@st.cache_data
def load_data():
    return pd.read_csv(r"E:\leadgen-tool\Cleaned_Dataset\cleaned_company_data.csv")

df = load_data()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Company Search", "Lead Generator", "Data Export"])

# Dashboard Page
if page == "Dashboard":
    st.title("📊 Company Data Dashboard")
    st.subheader("Business Intelligence Insights")
    
    # Key metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Companies", len(df))
    col2.metric("Most Common Size", df['company_size'].mode()[0])
    col3.metric("Top Industry", df['industries'].value_counts().index[0] if not df['industries'].empty else "N/A")
    
    # Visualization 1: Company Size Distribution
    st.subheader("Company Size Distribution")
    size_counts = df['company_size'].value_counts()
    fig1 = px.pie(size_counts, 
                 values=size_counts.values, 
                 names=size_counts.index,
                 hole=0.3)
    st.plotly_chart(fig1)
    
    # Visualization 2: Top Industries
    st.subheader("Top Industries")
    industry_counts = df['industries'].value_counts().head(10)
    fig2 = px.bar(industry_counts, 
                 x=industry_counts.values, 
                 y=industry_counts.index,
                 orientation='h')
    st.plotly_chart(fig2)
    
    # Visualization 3: Employees vs Followers
    st.subheader("Employees vs Followers")
    fig3 = px.scatter(df, 
                     x='employees', 
                     y='followers',
                     size='employees',
                     color='company_size',
                     hover_name='name',
                     log_x=True,
                     log_y=True)
    st.plotly_chart(fig3)
    
    # Visualization 4: World Map
    st.subheader("Global Distribution")
    country_counts = df['country_code'].value_counts().reset_index()
    country_counts.columns = ['country_code', 'count']
    fig4 = px.choropleth(country_counts,
                        locations="country_code",
                        color="count",
                        hover_name="country_code",
                        projection="natural earth")
    st.plotly_chart(fig4)

# Company Search Page
elif page == "Company Search":
    st.title("🔍 Company Search")
    
    search_option = st.radio("Search by:", ["Company Name", "Industry/Sphere"])
    
    if search_option == "Company Name":
        search_term = st.text_input("Enter company name:")
        results = df[df['name'].str.contains(search_term, case=False, na=False)] if search_term else df
    else:
        search_term = st.text_input("Enter industry/sphere:")
        results = df[df['sphere'].str.contains(search_term, case=False, na=False)] if search_term else df
    
    st.subheader(f"Found {len(results)} Companies")
    st.dataframe(results[['name', 'country_code', 'industries', 'employees', 'followers', 'website']])

# Lead Generator Page
elif page == "Lead Generator":
    st.title("💼 Lead Generator")
    
    st.subheader("Filter Companies")
    col1, col2 = st.columns(2)
    
    with col1:
        size_options = st.multiselect("Company Size", df['company_size'].unique())
        country_options = st.multiselect("Country", df['country_code'].unique())
    
    with col2:
        min_employees = st.slider("Minimum Employees", 0, 1000, 0)
        min_followers = st.slider("Minimum Followers", 0, 100000, 0)
    
    # Apply filters
    filtered = df.copy()
    if size_options:
        filtered = filtered[filtered['company_size'].isin(size_options)]
    if country_options:
        filtered = filtered[filtered['country_code'].isin(country_options)]
    filtered = filtered[filtered['employees'] >= min_employees]
    filtered = filtered[filtered['followers'] >= min_followers]
    
    st.subheader(f"Filtered Leads: {len(filtered)} Companies")
    
    if not filtered.empty:
        st.dataframe(filtered[['name', 'country_code', 'industries', 'employees', 'followers', 'website']])
        
        # Show company details when selected
        selected_company = st.selectbox("Select a company for details", filtered['name'])
        company_data = filtered[filtered['name'] == selected_company].iloc[0]
        
        st.subheader(company_data['name'])
        col1, col2 = st.columns(2)
        col1.metric("Country", company_data['country_code'])
        col1.metric("Employees", company_data['employees'])
        col2.metric("Followers", company_data['followers'])
        col2.metric("Founded", company_data['founded'])
        
        st.write("**About:**")
        st.write(company_data['about'])
        st.write(f"**Website:** {company_data['website']}")
        st.write(f"**Specialties:** {company_data['specialties']}")

# Data Export Page
elif page == "Data Export":
    st.title("💾 Data Export")
    st.subheader("Export Company Data")
    
    # Select columns to export
    default_cols = ['name', 'country_code', 'industries', 'employees', 'followers', 'website']
    selected_columns = st.multiselect("Select columns to export", 
                                     df.columns.tolist(),
                                     default=default_cols)
    
    if selected_columns:
        export_df = df[selected_columns]
        st.dataframe(export_df.head())
        
        # Export options
        export_format = st.radio("Select export format", ["CSV", "Excel"])
        
        if st.button("Export Data"):
            if export_format == "CSV":
                csv = export_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='company_data.csv',
                    mime='text/csv'
                )
            else:
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    export_df.to_excel(writer, index=False)
                st.download_button(
                    label="Download Excel",
                    data=output.getvalue(),
                    file_name='company_data.xlsx',
                    mime='application/vnd.ms-excel'
                )
    else:
        st.warning("Please select at least one column to export")