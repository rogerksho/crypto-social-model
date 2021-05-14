import json
import csv
from datetime import datetime

trend_list = []

with open('googletrends.json', 'r') as f:
    data = json.load(f)
    data_values = data.values()

    for chunk in data_values:
        for day in chunk:
            #formatted_date = datetime.fromtimestamp(int(day["time"]))
            trend_tuple = (day["time"], day["value"][0])
            trend_list.append(trend_tuple)

with open("google_trends.csv", "w") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerow(("datetime", "google_trend"))
    writer.writerows(trend_list)