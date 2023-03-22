import pandas as pd
import plotly.express as px
import streamlit as st

# Display title and text
st.title("Airbnb Listings: Amsterdam")
st.markdown("Airbnb listings near *Zaanse Schans*, Amsterdam with budget of IDR 2,000,000 or less")

# Read dataframe
dataframe = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Meters from chosen location",
        "Location",
    ],
)

# We have a limited budget, therefore we would like to exclude
# listings with a price below 2000000 IDR per night
dataframe = dataframe[dataframe["Price"] <= 2000000]
dataframe = dataframe[dataframe["Meters from chosen location"] <= 7000

# Display as integer
dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
# Round of values
dataframe["Price"] = "Rp " + (dataframe["Price"].astype(int)).astype(str) # <--- CHANGE THIS POUND SYMBOL IF YOU CHOSE CURRENCY OTHER THAN POUND
# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "To visit", 0.0: "Airbnb listing"}
)

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("All the Airbnb listings with a blue dot and the Zaanse Schans with a red dot.")

# Create the plotly express figure
fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    color_discrete_sequence=["red", "blue"],
    zoom=11,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Meters from chosen location", "Location"],
    labels={"color": "Locations"},
)
fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Show the figure
st.plotly_chart(fig, use_container_width=True)
