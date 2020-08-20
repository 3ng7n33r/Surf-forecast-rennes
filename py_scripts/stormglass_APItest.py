# Initializ libs and pw's
import requests
import arrow
import mysql.connector

f = open("storm_API.txt", "r")
apiKey = f.read()

f = open("sql_pass.txt", "r")
sql_pass = f.read()

# %% Fetch data from stormglass

# Get first hour of today
start = arrow.now()

# Get last hour of today
end = arrow.now().shift(days=+10)

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
    'start': start.to('UTC').timestamp,  # Convert to UTC timestamp
    'end': end.to('UTC').timestamp  # Convert to UTC timestamp
  },
  headers={
    'Authorization': apiKey
  }
)

# Do something with response data.
json_data = response.json()

#%% connect and write to sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=sql_pass
)
#%%

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)