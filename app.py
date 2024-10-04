import streamlit as st
import requests

def get_weather(city):
    url = f"http://127.0.0.1:8000/weather/{city}"
    response = requests.get(url)
    return response.json()

def main():
    st.title("Weather App")

    city = st.text_input("Enter a city:")

    if st.button("Get Weather"):
        weather_data = get_weather(city)

        if weather_data:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            sunrise = weather_data['sys']['sunrise']
            sunset = weather_data['sys']['sunset']

            st.markdown(f"**Temperature:** {temperature}°C")
            st.markdown(f"**Description:** {description}")
            st.markdown(f"**Humidity:** {humidity}%")
            st.markdown(f"**Wind Speed:** {wind_speed} m/s")
            st.markdown(f"**Sunrise:** {sunrise}")
            st.markdown(f"**Sunset:** {sunset}")
        else:
            st.write("City not found.")

if __name__ == "__main__":
    main()