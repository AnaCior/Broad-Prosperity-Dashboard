import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import json
import pydeck as pdk 
from path_en import indicator_options, theme_options, color_schemes
from engdict import Themes, Sources

# Page configuration: Sets title, layout, and sidebar state
st.set_page_config(
    page_title="Broad Prosperity: Netherlands",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title section with custom HTML for styling
st.markdown("""
<div style='text-align: left; padding: 10px;'>
<h1 style='color: #009ee3; font-size: 48px; font-weight: bold; margin-bottom: 0;'>cmo stamm.</h1>
<h2 style='color: #e5007d; font-size: 32px; font-weight: bold; margin-top: 0;'>Broad Prosperity in the Netherlands</h2>
</div>
""", unsafe_allow_html=True)

# Custom CSS styling to modify sidebar and content container
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #149bed;
    padding: 10px;
}
.stApp [data-testid="block-container"] {
    background-color: #cce1ee !important;
    padding: 0;
}
</style>
""", unsafe_allow_html=True)

#######################

# Sidebar: User selects what to visualize and additional settings
with st.sidebar:
    st.title("Broad Prosperity Indicators")

    # Choose whether to visualize themes or specific indicators
    type = st.radio("What would you like to visualise ?",
             ["Themes", "Indicators"],
             captions = [
                 "Overall themes",
                 "Indicators within the themes"
             ],)

    # Set options based on user choice (Themes or Indicators)
    if type == "Themes":
        options = theme_options
    else:
        options = indicator_options

    # Dropdown menu to select a specific theme/indicator
    selected_indicator = st.selectbox("Select a Theme/an Indicator:", options)

    # Extract the relevant year columns for the selected indicator
    year_columns = options[selected_indicator]["year_columns"]
    selected_year = st.selectbox("Select a year:", list(year_columns.keys()))
    
    # Dropdown to select a color scheme for visualization
    selected_scheme_name = st.selectbox("Select a color scheme:", list(color_schemes.keys()))
    selected_scheme = color_schemes[selected_scheme_name]

# Create two columns for layout
col = st.columns((2,1), gap='medium')

# Left Column: Display interactive map with indicator data
with col[0]:
    # Define path and title for the selected indicator
    indicator_path = options[selected_indicator]["path"]
    title_base = options[selected_indicator]["title"]

    # Load the data from the file path
    indicator = gpd.read_file(indicator_path)

    # Select the column for the chosen year
    selected_column = year_columns[selected_year]

    # Ensure geometry is valid by filtering out any invalid entries
    indicator = indicator[indicator.geometry.notnull()]

    # Convert non-JSON serializable types to strings
    for column in indicator.columns:
        if pd.api.types.is_datetime64_any_dtype(indicator[column]):
            indicator[column] = indicator[column].dt.strftime('%Y-%m-%d')

    # Handle missing values by converting them to NaN and assigning a placeholder color later
    indicator[selected_column] = pd.to_numeric(indicator[selected_column], errors='coerce')

    # Calculate quantiles for color classification
    quantiles = indicator[selected_column].quantile([0.0, 0.25, 0.5, 0.75, 1.0]).values

    # Function to assign colors based on quantiles
    def get_color(value):
        if pd.isna(value):
            return selected_scheme[0]  # Color for missing values
        elif value <= quantiles[1]:  # 0-25% quantile range
            return selected_scheme[1]
        elif value <= quantiles[2]:  # 25-50% quantile range
            return selected_scheme[2]
        elif value <= quantiles[3]:  # 50-75% quantile range
            return selected_scheme[3]
        else:  # 75-100% quantile range
            return selected_scheme[4]

    # Apply the color function to each feature based on the selected year data
    indicator["fill_color"] = indicator[selected_column].apply(get_color)

    # Prepare hover information to display feature details on hover
    indicator["hover_info"] = indicator.apply(lambda row: f"{row['statnaam']}: {row[selected_column]}", axis=1)

    # Convert coordinate reference system to WGS84 (EPSG 4326) for compatibility with pydeck
    indicator = indicator.to_crs(epsg=4326)  

    # Manually serialize GeoJSON to add custom properties (e.g., hover_info, fill_color)
    geojson_data = json.loads(indicator.to_json())
    for feature, hover_text, fill_color in zip(geojson_data["features"], indicator["hover_info"], indicator["fill_color"]):
        feature["properties"]["hover_info"] = hover_text
        feature["properties"]["fill_color"] = fill_color

    # Create a PyDeck layer using the GeoJSON data with dynamic colors
    layer = pdk.Layer(
        "GeoJsonLayer",
        data=geojson_data,
        pickable=True,
        get_fill_color="properties.fill_color",
        get_line_color="[255, 255, 255]",
        line_width_min_pixels=1,
        auto_highlight=True,
    )

    # Define the initial view state for the map
    view_state = pdk.ViewState(
        latitude=indicator.geometry.centroid.y.mean(),
        longitude=indicator.geometry.centroid.x.mean(),
        zoom=6
    )

    # Create a PyDeck deck to display the map with custom tooltip for hover interaction
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"html": "<b>{hover_info}</b>"})

    # Display the map in the Streamlit app
    st.pydeck_chart(r)

    # Show the description of the selected indicator
    if selected_indicator:
        st.markdown(Themes[selected_indicator])

# Right Column: Provide additional context and links
with col[1]:
    st.markdown("""
    <div style='text-align: left; padding: 10px;'>
    <h1 style='color: #009ee3; font-size: 30px; font-weight: bold; margin-bottom: 0;'>What is Broad Prosperity</h1>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Broad prosperity is about everything that makes life 'worthwhile'. It includes income, 
    work, housing quality, nature, health, and well-being. CMO STAMM focuses on improving 
    broad prosperity in the North through research, strategy, and raising awareness.
    """)

    with st.expander('Sources', expanded=True):
        st.write('''
            - Data: [CBS data: Nederland (https://www.cbs.nl/nl-nl/visualisaties/regionale-monitor-brede-welvaart/indicator)]''')
        if selected_indicator in Sources:
            st.write(Sources[selected_indicator])
        else:
            st.write("")  # Blank output

    st.write('''  Municipalities ranked from high to low are only available for indicators, not for themes. 
        **Disclaimer:** This ranking is based solely on numerical values from highest to lowest and does not indicate the relative well-being or superiority of any municipality.
    ''')

    df_indicators = pd.read_csv("small_mergedEN.csv")
    
    df_indicators['jaar'] = df_indicators['jaar'].astype(str)  # Convert to string
    selected_year = str(selected_year)  # Convert selected year to string

    df_selectedindicator = df_indicators[
        (df_indicators['Label'] == selected_indicator)&
        (df_indicators['jaar'] == selected_year)]

    df_selectedindicator_sorted = df_selectedindicator.sort_values(by='waarde', ascending=False)
    
    columns_to_include = ['Gemeentenaam', 'waarde'] 
    
    df_selectedindicator_sorted = df_selectedindicator_sorted[columns_to_include]
    with st.expander(f'*Municipalities ranked from high to low in {selected_indicator}*'):

        if df_selectedindicator_sorted.empty:
                st.warning("No data available for the selected indicator.")
        else:
            # Display the DataFrame using Streamlit
            st.dataframe(
            df_selectedindicator_sorted, 
            column_order=("Gemeentenaam", "waarde"), 
            hide_index=True, 
            width=None, 
            column_config={
                "Gemeentenaam": st.column_config.TextColumn(
                    "Municipality",
                ),
                "waarde": st.column_config.TextColumn(
                    "Values",  # This will now display as plain numbers
                ),
            }
        )
    # Links to the Dutch page and download page
    st.markdown("""
    <div style='text-align: left; padding: 10px; display: flex; align-items: center;'>
        <h1 style='color: #e5007d; font-size: 20px; font-weight: bold; margin-top: 0; margin-right: 8px;'>For the Dutch page:</h1>
        <a href="https://bp-dashboard-dutch.streamlit.app/" target="_blank" style="
            text-decoration: none;
            background-color: #e5007d;
            color: white;
            padding: 6px 12px;
            border-radius: 5px;
            font-size: 14px;
            font-weight: bold;
            margin-left: -5px;
        ">Click here</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: left; padding: 10px; display: flex; align-items: center;'>
        <h1 style='color: #e5007d; font-size: 20px; font-weight: bold; margin-top: 0; margin-right: 8px;'>For the download page:</h1>
        <a href="https://mapdownload.streamlit.app/" target="_blank" style="
            text-decoration: none;
            background-color: #e5007d;
            color: white;
            padding: 6px 12px;
            border-radius: 5px;
            font-size: 14px;
            font-weight: bold;
            margin-left: -5px;
        ">Click here</a>
    </div>
    """, unsafe_allow_html=True)
