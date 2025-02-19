import streamlit as st
import pandas as pd
import plotly.express as px
from ydata_profiler import ydata_profiler
from st_more_maps import st_more_vizualization



@st.cache
def load_data():
    # Replace 'taxi_zone_lookup.csv' with your actual file path
    return pd.read_csv('taxi_zone_lookup.csv')

# Sidebar filters
def side_bar_data(df):
    # Sidebar filters
    st.sidebar.header("Filter Options")
    
    # Filter by Borough
    boroughs = st.sidebar.multiselect(
        "Select Borough(s):",
        options=df["Borough"].unique(),
        default=df["Borough"].unique()
    )
    
    # Filter by Service Zone
    service_zones = st.sidebar.multiselect(
        "Select Service Zone(s):",
        options=df["service_zone"].unique(),
        default=df["service_zone"].unique()
    )
    
    # Apply filters to the dataframe
    filtered_df = df[
        (df["Borough"].isin(boroughs)) &
        (df["service_zone"].isin(service_zones))
    ]
    
    return filtered_df

# Main application
def main():
    # App title
    st.title("NYC Taxi Data Dashboard")

    # Load dataset
    df = load_data()

    # Sidebar filters
    filtered_df = side_bar_data(df)

    # Tabs for different functionality
    tab1, tab2 = st.tabs(["🔍 Data Explorer", "📊 Data DNA"])

    with tab1:
        st.header("Know Your Data")
        st.write(f"Filtered Data: {len(filtered_df)} rows")
        st.dataframe(filtered_df)
        st_more_vizualization(filtered_df)

    with tab2:
        st.header("Data Profiling")
        ydata_profiler(filtered_df)

# Run the app
if __name__ == "__main__":
    main()
