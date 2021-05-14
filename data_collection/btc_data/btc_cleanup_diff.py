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

alt_price_list = ([price_list[0]]+price_list).copy()
alt_price_list = alt_price_list[:-1]

numpy_price = np.array(price_list)
numpy_alt_price = np.array(alt_price_list)

price_diff = numpy_price - numpy_alt_price

final_price_diff = []

for i in range(len(date_list)):
    final_price_diff.append((date_list[i], price_diff[i]))

with open("coin_price_diff.csv", "w") as fo:
    writer = csv.writer(fo, delimiter=",")
    writer.writerow(['datetime', 'px_change'])
    writer.writerows(final_price_diff)