import os
import sys
import pandas as pd
import json
import simplejson
import arrow

# %%

try:
    with open(os.path.join(sys.path[0], "dataApi.json"), "r") as json_file:
        data = json.load(json_file)
except: 
    with open("dataApi.json", "r") as json_file:
        data = json.load(json_file)

testdata = data["hours"]

flattened_data = pd.json_normalize(testdata)
flatClean = pd.DataFrame()

col_one_list = flattened_data['time'].tolist()

col_one_list = [((arrow.get(hour)).shift(hours=+2)).format('YYYY-MM-DD HH:mm') for hour in col_one_list]
flattened_data["time"] = col_one_list

#Remove noaa from column header
for i in flattened_data:
    flattened_data.rename(columns={i : i.split('.', 1)[0]}, inplace=True)

#Delete all but the selected hours
flattened_data['date'], flattened_data['hour'] = flattened_data['time'].str.split(' ', 1).str
flattened_data.pop("time")
hours = ["06:00",
         "09:00",
         "12:00",
         "15:00",
         "18:00",
         "21:00",
         ]
flatClean = flattened_data[flattened_data.hour.isin(hours)]

cleanjson = json.loads(flatClean.to_json(orient="records"))

# now write output to a file
cleandata = open("../static/data.json", "w")
# magic happens here to make it pretty-printed
cleandata.write(simplejson.dumps(cleanjson, indent=4, sort_keys=True))
cleandata.close()

# %% tide data

try:
    with open(os.path.join(sys.path[0], "dataTideApi.json"), "r") as json_file:
        tides = json.load(json_file)
except: 
    with open("dataTideApi.json", "r") as json_file:
        tides = json.load(json_file)
    
testdata = tides["data"]
flattened_data = pd.json_normalize(testdata)
col_one_list = flattened_data['time'].tolist()
col_one_list = [((arrow.get(hour)).shift(hours=+2)).format('YYYY-MM-DD HH:mm') for hour in col_one_list]
flattened_data["time"] = col_one_list

flattened_data['date'], flattened_data['hour'] = flattened_data['time'].str.split(' ', 1).str
flattened_data.pop("time")

cleanjson = json.loads(flattened_data.to_json(orient="records"))

# now write output to a file
cleandata = open("../static/tides.json", "w")
# magic happens here to make it pretty-printed
cleandata.write(simplejson.dumps(cleanjson, indent=4, sort_keys=True))
cleandata.close()
