import streamlit as st
import plotly.express as px
from backend import get_data

# Add tile, text input, slider, select box, and sub-header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days you want forecasted")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get temperature/sky data
    filtered_data = get_data(place, days)

    if option == 'Temperature':
        # Create temperature plot
        temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature"})
        st.plotly_chart(figure)

    if option == 'Sky':
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                  'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        image_path = [images[condition] for condition in sky_conditions]
        st.image(image_path, width=115)
