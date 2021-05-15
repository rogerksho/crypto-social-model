import csv
import numpy as np
import pandas as pd
from datetime import date, datetime, timedelta
import statistics

import seaborn as sns
import matplotlib.pyplot as plt

# init containers
time_series = []
coin_price_change = []

google_trend = []

twitter_time = []
twitter_sentiment = []
twitter_sample_size = []

erroneous_dates = []

# btc data
with open("btc_data/coin_price_bare.csv", "r") as f:
    reader = csv.reader(f)

    # skip first line
    _ = next(reader)

    for row in reader:
        time_series.append(row[0])
        coin_price_change.append(float(row[1]))

# google data
with open("google_data/google_trends.csv", "r") as f:
    reader = csv.reader(f)

    # skip first line
    _ = next(reader)

    for row in reader:
        google_trend.append(float(row[1]))

twitter_file_name = "sentiment_data_consolidated.csv"

# twitter data
with open(f"twitter_data/{twitter_file_name}", "r") as f:
    reader = csv.reader(f)

    # skip first line
    _ = next(reader)

    for row in reader:
        # if int(row[2]) < 4000:                     # weed out all sample size < 4000
        #     print(row)
        #     erroneous_dates.append(str(row[0]))
        twitter_time.append(row[0])
        twitter_sentiment.append(float(row[1]))
        twitter_sample_size.append(int(row[2]))

# transform to np
twitter_sample_size_np = np.array(twitter_sample_size)

# trim coin price and time series (time series is from coin price)
coin_price_change = coin_price_change[:-38]
time_series = time_series[:-38]

############################################
######         PROCESSING DONE        ######
############################################

# combine to df
df = pd.DataFrame(list(zip(time_series, coin_price_change, google_trend, twitter_sentiment)), columns=['time','px','google_trend', 'twitter_sent'])
df.to_csv("consolidated_data_bare.csv", index='time')


# dataframe stats
print('sample size below 4000: ', np.sum(twitter_sample_size_np < 4000))
print('btc data size: ', len(coin_price_change))
print('google data size: ', len(google_trend))
print('twitter data size: ', len(twitter_sentiment))

# write days where sample size < 4000
# with open('erroneous_dates.csv', 'w') as fp:
#     writer = csv.writer(fp)

#     for i in erroneous_dates:
#         writer.writerow([i])
