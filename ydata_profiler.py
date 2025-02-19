import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report

def ydata_profiler(df):
    # App title and description
    st.title("NYC Taxi Data Profiling")
    st.write("Generate an interactive profiling report for NYC Taxi data using YData Profiling.")

    # Load dataset
    #df = load_data()

    # Display dataset preview
    st.write("### Dataset Preview")
    st.dataframe(df.head())

    # Generate and display profiling report
    st.write("### Profiling Report")
    profile = ProfileReport(
        df,
       # minimal=True,  # Use minimal configuration for faster generation
       # explorative=True,  # Enable interactive features
       # orange_mode=False  # Use orange theme for better visuals
    )
    st_profile_report(profile, navbar=True)
