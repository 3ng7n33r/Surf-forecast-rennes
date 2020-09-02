import pandas as pd
import json
import arrow
# from pandas.io.json import json_normalize

with open('data.json') as json_file:
    data = json.load(json_file)

testdata = data["hours"]

flattened_data = pd.json_normalize(testdata)
flatClean = pd.DataFrame()

col_one_list = flattened_data['time'].tolist()

col_one_list = [((arrow.get(hour)).shift(hours=+2)).format('YYYY-MM-DD HH:mm') for hour in col_one_list]

flattened_data["time"] = col_one_list

# flatClean = [clean for clean in flattened_data[7::] if flattened_data["Index"] % 6 == 0]

for i in flattened_data.itertuples("time"):
    print(i)