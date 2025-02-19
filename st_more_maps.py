import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


def st_more_vizualization(df):
    # App title and description
    st.title("NYC Taxi Data Visualization")
    st.write("Explore NYC Taxi data with various visualizations rendered sequentially.")
    # Display the first few rows of the dataset
    st.write("### Dataset Preview")
    st.dataframe(df.head())

    # 1. Bar Chart: Count of Zones per Borough
    st.subheader("1. Bar Chart: Count of Zones per Borough")
    bar_chart = px.bar(
        df.groupby("Borough").size().reset_index(name="Counts"),
        x="Borough",
        y="Counts",
        color="Borough",
        title="Count of Zones per Borough"
    )
    st.plotly_chart(bar_chart, use_container_width=True)

    # 2. Pie Chart: Distribution of Zones by Service Zone
    st.subheader("2. Pie Chart: Distribution of Zones by Service Zone")
    pie_chart = px.pie(
        df,
        names="service_zone",
        title="Distribution of Zones by Service Zone",
        hole=0.4  # Donut-style pie chart
    )
    st.plotly_chart(pie_chart, use_container_width=True)

    # 3. Scatter Plot: LocationID vs Zone (Categorical Data)
    st.subheader("3. Scatter Plot: LocationID vs Zone")
    scatter_plot = px.scatter(
        df,
        x="LocationID",
        y="Zone",
        color="Borough",
        title="Scatter Plot of LocationID vs Zone"
    )
    st.plotly_chart(scatter_plot, use_container_width=True)

    # 4. Geospatial Visualization (if latitude and longitude exist)
    if "latitude" in df.columns and "longitude" in df.columns:
        st.subheader("4. Map: Geospatial Visualization of Taxi Zones")
        st.map(df[["latitude", "longitude"]])

    # 5. Correlation Heatmap (if numerical columns exist)
    numerical_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(numerical_columns) > 1:
        st.subheader("5. Correlation Heatmap")
        correlation_matrix = df[numerical_columns].corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
        ax.set_title("Correlation Matrix")
        st.pyplot(fig)

    # 6. Histogram: Distribution of LocationIDs
    st.subheader("6. Histogram: Distribution of LocationIDs")
    fig, ax = plt.subplots()
    sns.histplot(df['LocationID'], kde=True, ax=ax)
    ax.set_title("Distribution of LocationIDs")
    st.pyplot(fig)