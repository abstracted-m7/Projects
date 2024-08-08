import tkinter as tk
from tkinter import messagebox
import requests

# API configuration
API_KEY = 'd98761c0841cc3e208f5713893df9cd0'  # My own API key
API_URL = 'https://api.openweathermap.org/data/2.5/weather'  #API Link

def get_weather(city, units):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': units
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Unable to get weather data: {e}")
        return None

def display_weather(data, units):
    if data:
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        if units == 'metric':
            temperature_unit = 'C'
            wind_speed_unit = 'm/s'
        else:
            temperature_unit = 'F'
            wind_speed_unit = 'mph'

        result_var.set(f"City: {city}, {country}\n"
                       f"Temperature: {temperature}°{temperature_unit}\n"
                       f"Weather: {weather_description}\n"
                       f"Wind Speed: {wind_speed} {wind_speed_unit}")
    else:
        result_var.set("No weather data available")

def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    units = 'metric' if units_var.get() == 'Celsius' else 'imperial'
    weather_data = get_weather(city, units)
    display_weather(weather_data, units)

# Create main window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
tk.Label(root, text="Enter City:").grid(row=0, column=0, padx=10, pady=10)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=10)

units_var = tk.StringVar(value="Celsius")
tk.Label(root, text="Select Units:").grid(row=1, column=0, padx=10, pady=10)
units_menu = tk.OptionMenu(root, units_var, "Celsius", "Fahrenheit")
units_menu.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Get Weather", command=fetch_weather).grid(row=2, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, justify='left')
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



root.mainloop()
