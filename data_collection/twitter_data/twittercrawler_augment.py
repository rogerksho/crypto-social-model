import twint
import csv
import os
import pandas
from datetime import date, timedelta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
import sys

# max number of tries
MAX_TRIES = 20

# vader setup
analyzer = SentimentIntensityAnalyzer()

# twint config
c = twint.Config()
c.Search = "bitcoin OR btc"
c.Hide_output = True
c.Limit = 200000
c.Stats = True

# pandas-specific settings
c.Pandas = True
c.Pandas_clean = True

# dates to do
dates_to_do = []

with open('erroneous_dates.csv', 'r') as fp:
    reader = csv.reader(fp)

    for row in reader:
        dates_to_do.append(date.fromisoformat(row[0]))

# init scraper vars
current_date = dates_to_do[0]

# hold final data
daily_sentiment = []

# while
for date in dates_to_do:
    # per day stuff
    sentiment_sum = 0.0
    neg_sent = 0
    pos_sent = 0

    c.Since = date.isoformat()
    current_date = date
    c.Until = (date + timedelta(days=1)).isoformat()

    current_tries = 0

    # try up to MAX_TRIES times if the call fails
    while current_tries < MAX_TRIES:
        try:
            twint.run.Search(c)

                # store in pandas df
            tweets_df = twint.storage.panda.Tweets_df

            # access tweet
            tweets_series = tweets_df.loc[:, "tweet"]
            num_samples = 0

            for t in tweets_series:
                sentiment = analyzer.polarity_scores(t)

                # skip neutral
                if sentiment["compound"] < 0.05 and sentiment["compound"] > -0.05:
                    continue
                else:
                    num_samples += 1

                # record positive vs negative
                if sentiment["compound"] >= 0.05: pos_sent += 1
                if sentiment["compound"] <= -0.05: neg_sent += 1

                sentiment_sum += sentiment["compound"]

        except Exception as e:
            print("ERROR... retrying...")
            os.system("say ERROR")
            current_tries += 1
            time.sleep(2)
            continue
        except KeyboardInterrupt as k:
            sys.exit()
        break



    # stdout stuff
    avg_sentiment = sentiment_sum / num_samples
    print("date finished: ", current_date.isoformat())
    print("sample size: ", num_samples)
    print("average sentiment: ", avg_sentiment)
    print("positive sentiment: ", pos_sent)
    print("negative sentiment: ", neg_sent)
    print("=========================")

    # data organisation
    sentiment_tuple = (current_date.isoformat(), avg_sentiment, num_samples)
    daily_sentiment.append(sentiment_tuple)

    # increment day
    current_date += timedelta(days=1)

    # writes to csv after each scrape
    with open("sentiment_data_augment1.csv", "a") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(sentiment_tuple)

for elt in daily_sentiment:
    print(elt)

