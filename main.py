import streamlit as st
import pandas as pd
import plotly.express as px
from ydata_profiler import ydata_profiler
from st_more_maps import st_more_vizualization

# Create tabs
tab1, tab2 = st.tabs(["Know your data", "Data Profiling"])





# Load the data
#@st.cache
def load_data():
    # Replace 'nyc_taxi_zones.csv' with your actual file path
    return pd.read_csv('taxi_zone_lookup.csv')


# Load the data
def main(df):
    # App title and description
    st.title("NYC Taxi Data Visualization")
    st.write("Explore NYC Taxi data interactively with multiple visualizations rendered sequentially.")
    
 
    
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
    
    # Display filtered data
    st.write(f"Filtered Data: {len(filtered_df)} rows")
    st.dataframe(filtered_df)
    
    # Render all visualizations sequentially
    
    ## 1. Bar Chart: Count of Zones per Borough
    st.subheader("Bar Chart: Count of Zones per Borough")
    bar_chart = px.bar(
        filtered_df,
        x="Borough",
        color="service_zone",
        title="Count of Zones per Borough",
        labels={"count": "Number of Zones"}
    )
    st.plotly_chart(bar_chart, use_container_width=True)
    
    ## 2. Pie Chart: Distribution of Zones by Borough
    st.subheader("Pie Chart: Distribution of Zones by Borough")
    pie_chart = px.pie(
        filtered_df,
        names="Borough",
        title="Distribution of Zones by Borough",
        hole=0.4  # Donut-style pie chart
    )
    st.plotly_chart(pie_chart, use_container_width=True)
    
    ## 3. Scatter Plot: Zone vs LocationID
    st.subheader("Scatter Plot: LocationID vs Zone")
    scatter_plot = px.scatter(
        filtered_df,
        x="LocationID",
        y="Zone",
        color="Borough",
        title="Scatter Plot of LocationID vs Zone"
    )
    st.plotly_chart(scatter_plot, use_container_width=True)
    
    ## 4. Map Visualization (if latitude/longitude columns exist)
    if "latitude" in filtered_df.columns and "longitude" in filtered_df.columns:
        st.subheader("Map: Geospatial Visualization of Taxi Zones")
        map_chart = px.scatter_mapbox(
            filtered_df,
            lat="latitude",
            lon="longitude",
            color="Borough",
            size_max=15,
            zoom=10,
            mapbox_style="carto-positron",
            title="Geospatial Map of Taxi Zones"
        )
        st.plotly_chart(map_chart, use_container_width=True)
    else:
        st.warning("Latitude and Longitude columns are required for map visualization.")


# Load dataset
df = load_data()
# Tab 1: Using Streamlit Native Components
with tab1:
    st_more_vizualization(df)
with tab2:
    print(df.head())
    ydata_profiler(df)



#if __name__ == "__main__":
    # Load dataset
     #  df = load_data()
    #main(df)
    #   print(df.head())
    #   ydata_profiler(df)
