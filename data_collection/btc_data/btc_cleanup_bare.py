import json
import numpy as np
import csv

price_list = []
date_list = []

with open("coinprices.txt", "r") as f:
    data = json.loads(f.read())["bpi"]
    for k, v in data.items():
        price_list.append(v)
        date_list.append(k)

final_price = []

for i in range(len(date_list)):
    final_price.append((date_list[i], price_list[i]))

with open("coin_price_bare.csv", "w") as fo:
    writer = csv.writer(fo, delimiter=",")
    writer.writerows(final_price)