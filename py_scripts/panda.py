import pandas as pd
import json
import arrow
# from pandas.io.json import json_normalize

with open('data.json') as json_file:
    data = json.load(json_file)

testdata = data["hours"]

flattened_data = pd.json_normalize(testdata)
flatClean = pd.DataFrame()

for row in flattened_data.itertuples():
    arrowtime = arrow.get(row.time)
    row.time = arrowtime.to('cet')


# for i in range(0,len(flattened_data),6):
#     print(i)
#     flatClean.append(flattened_data.iloc[i])
    

