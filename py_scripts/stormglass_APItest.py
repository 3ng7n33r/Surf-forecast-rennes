# Initializ libs and pw's
import requests
import arrow
import simplejson

f = open("storm_API.txt", "r")
apiKey = f.read()


# %% Fetch data from stormglass

# Get first hour of today
start = arrow.utcnow()
start = start.replace(hour=0, minute=0, second=0)

# Get last hour of today
end = start.shift(days=+6)

response = requests.get(
  'https://api.stormglass.io/v2/weather/point',
  params={
    'lat': 47.72,
    'lng': -3.49,
    'params': ','.join(['waveHeight', 'airTemperature'
                        , 'swellDirection', 'swellHeight', 'swellPeriod', 
                        'secondarySwellPeriod', 'secondarySwellDirection', 
                        'secondarySwellHeight', 'waterTemperature', 
                        'waveDirection', 'waveHeight', 'wavePeriod', 
                        'windWaveDirection', 'windWaveHeight', 'windWavePeriod',
                        'windSpeed']),
    'start': start.timestamp,  # Convert to timestamp
    'end': end.timestamp,  # Convert to UTC timestamp
    'source': 'noaa'
  },
  headers={
    'Authorization': apiKey
  }
)

json_data = response.json()

# %% Format data

# weather = pd.DataFrame.from_dict(json_data)

# %% Save response to JSON file

# now write output to a file
weatherDataFile = open("data.json", "w")
# magic happens here to make it pretty-printed
weatherDataFile.write(simplejson.dumps(json_data, indent=4, sort_keys=True))
weatherDataFile.close()
