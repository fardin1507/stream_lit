import streamlit as st
import requests
from datetime import datetime, timedelta
import pytz

# Constants
API_KEY = 'your_aladhan_api_key'
QURAN_API_URL = 'https://api.example.com/quran'  # Replace with a valid Quran API URL

# Function to fetch Namaz timings
def get_namaz_timings(location):
    url = f'https://api.aladhan.com/v1/timingsByCity?city={location}&country=your_country&method=2&api_key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    timings = data['data']['timings']
    return timings

# Function to fetch the Quran text
def get_quran_text():
    response = requests.get(QURAN_API_URL)
    data = response.json()
    return data

# Streamlit app
st.title("Namaz Timings and Quran App")

# User input for location
location = st.text_input("Enter your city:", "")

if location:
    try:
        # Fetch and display Namaz timings
        timings = get_namaz_timings(location)
        st.write("**Namaz Timings:**")
        for prayer, time in timings.items():
            st.write(f"{prayer}: {time}")

    except Exception as e:
        st.write(f"Error fetching Namaz timings: {e}")

# Display the Quran text
if st.button('Show Quran Text'):
    try:
        quran_data = get_quran_text()
        st.write("**Quran Text:**")
        st.write(quran_data)  # Adjust as necessary to format and display text
    except Exception as e:
        st.write(f"Error fetching Quran text: {e}")
