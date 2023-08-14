import streamlit as st
import pandas as pd
import requests
from io import StringIO
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Google Sheet link
sheet_link = "https://docs.google.com/spreadsheets/d/1MKoaRoqYt_BWbdLRvFClNtFZv4byGPaWPqY-OHW4Cbo/gviz/tq?tqx=out:csv"

# Fetch the data from Google Sheet
response = requests.get(sheet_link)
data = response.content.decode('utf-8')

# Create a DataFrame from the data
df = pd.read_csv(StringIO(data))

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y %H:%M:%S')

# Sort data in descending order based on the 'Date' column
df = df.sort_values(by='Date', ascending=False)

# Streamlit App
def main():
    st.title('IoT Data Visualization')

    st.write('## Display All Data')

    # Button to display all data
    if st.button('Show All Data'):
        st.write('### All Data')
        st.write(df)

        # Create a line plot for temperature
        plt.figure(figsize=(10, 6))
        plt.plot(df['Date'], df['Temperature (Celcius)'], marker='o')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Variation')
        st.pyplot(plt)

        # Create a line plot for humidity
        plt.figure(figsize=(10, 6))
        plt.plot(df['Date'], df['Humidity (%)'], marker='o', color='orange')
        plt.xlabel('Time')
        plt.ylabel('Humidity (%)')
        plt.title('Humidity Variation')
        st.pyplot(plt)

    st.write('## Data Visualization for Specific Date Range')
    
    # Date range selection
    start_date = st.date_input('Select Start Date')
    end_date = st.date_input('Select End Date')

    if st.button('Show Graph'):
        # Convert date input to datetime
        start_datetime = datetime.combine(start_date, datetime.min.time())
        end_datetime = datetime.combine(end_date, datetime.max.time())

        # Filter data based on selected date range
        filtered_data = df[(df['Date'] >= start_datetime) & (df['Date'] <= end_datetime)]

        if not filtered_data.empty:
            # Create a line plot for temperature based on date range
            plt.figure(figsize=(10, 6))
            plt.plot(filtered_data['Date'], filtered_data['Temperature (Celcius)'], marker='o')
            plt.xlabel('Time')
            plt.ylabel('Temperature (°C)')
            plt.title(f'Temperature Variation between {start_date} and {end_date}')
            st.pyplot(plt)

            # Create a line plot for humidity based on date range
            plt.figure(figsize=(10, 6))
            plt.plot(filtered_data['Date'], filtered_data['Humidity (%)'], marker='o', color='orange')
            plt.xlabel('Time')
            plt.ylabel('Humidity (%)')
            plt.title(f'Humidity Variation between {start_date} and {end_date}')
            st.pyplot(plt)
        else:
            st.write(f'No data available between {start_date} and {end_date}')

if __name__ == '__main__':
    main()
