
import json
import pandas as pd

# Sample weather JSON data
weather_json = """
[
    {
        "location": {"city": "Kochi"},
        "weather": {"temperature": 30, "humidity": 75}
    },
    {
        "location": {"city": "Chennai"},
        "weather": {"temperature": 34, "humidity": 60}
    },
    {
        "location": {"city": "Bengaluru"},
        "weather": {"temperature": 25, "humidity": 65}
    }
]
"""

# Load the JSON data
data = json.loads(weather_json)

# Extract city, temperature and humidity
weather_list = []

for item in data:
    city = item["location"]["city"]
    temperature = item["weather"]["temperature"]
    humidity = item["weather"]["humidity"]

    weather_list.append({
        "City": city,
        "Temperature": temperature,
        "Humidity": humidity
    })

# Convert JSON data into tabular format
df = pd.DataFrame(weather_list)

print("Weather Details for Multiple Cities:")
print(df.to_string(index=False))

# Generate a summarized weather report
print("\nSummarized Weather Report:")
print("Total cities:", len(df))
print("Average temperature:", df["Temperature"].mean())
print("Average humidity:", df["Humidity"].mean())
print("Highest temperature:", df["Temperature"].max())
print("Lowest temperature:", df["Temperature"].min())
