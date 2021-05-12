import json
import csv

trend_list = []

with open('googletrends.json', 'r') as f:
    data = json.load(f)
    data_values = data.values()

    for chunk in data_values:
        for day in chunk:
            trend_tuple = (day["time"], day["value"][0])
            trend_list.append(trend_tuple)

with open("googletrends.csv", "w") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerows(trend_list)