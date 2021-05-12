import requests
import json
import csv
from datetime import datetime, timezone, timedelta


# search params, iso format, yyyy-mm-dd
START_DATE = datetime.fromisoformat("2016-01-01").replace(tzinfo=timezone.utc)
END_DATE = datetime.fromisoformat("2016-01-05").replace(tzinfo=timezone.utc)
SEARCH_TERM = "bitcoin"
QUERY_SIZE = 0 # int <= 500

# convert to epoch
def normalise_datetime_epoch(datetime_in):
    return(int(datetime_in.replace(tzinfo=timezone.utc).timestamp()))

# data store
reddit_sent_list = []

# init loop vars
current_date_since = START_DATE

while current_date_since < END_DATE:
    current_date_before = current_date_since + timedelta(days=1)
    # only search for posts with more than 3 comments
    #r = requests.get(f'https://api.pushshift.io/reddit/search/comment/?q={SEARCH_TERM}&after={normalise_datetime_epoch(current_date_since)}&before={normalise_datetime_epoch(current_date_before)}&aggs=>created_utc&size={QUERY_SIZE}&frequency=day')
    r = requests.get('https://api.pushshift.io/reddit/search/comment/?q=trump&after=7d&aggs=created_utc&frequency=hour&size=0')
    data = r.json()

    num_samples = 0
    total_population = 0
    
    print(data)

    # store data
    #reddit_sentiment_tuple = (current_date_since.isoformat(), avg_sentiment, num_samples)
    #reddit_sent_list.append(reddit_sentiment_tuple)

    # stdout stuff
    print("date finished: ", current_date_since.isoformat())
    print("sample size: ", num_samples)
    print("population size: ", total_population)
    print("==================================")

    # increment day
    current_date_since += timedelta(days=1)

for i in reddit_sent_list:
    print(i)