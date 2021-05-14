## twitter data
because of twitter's extremely strict :( api policies, the data cap made it hard to collect tweets through the api, hence twitter data was collected using the [twint](https://github.com/twintproject/twint/wiki) package with the date ranges (yyyy-mm-dd):
> since: 2016-01-01

> before: 2021-04-01

the criteria for choosing tweets included any tweet that contained keywords 'BTC' or 'bitcoin'. these tweets were then fed through the [VADER](https://github.com/cjhutto/vaderSentiment) sentiment analyzer tool. the average sentiment for each day is calculated (-1 being the most negative, 1 being the most positive). neutral tweets were ignored, using the same criterion that the VADER github page details.

the sample size for each day is around 5000 tweets, although some days (on very rare occasions) would only return fewer than 4000 samples, and below 500 samples in 1-2 instances. this time window of 1917 days with (a conservative estimate of) 4500 samples a day results in just over 8,000,000 total samples. it should be noted that the twint package crawls for tweets through the web interface and not the api (the same tweets would show up when you search on twitter with the search bar), so in a way they were "randomly sampled". 

>**note:** i did play around a bit with the sample sizes and found minimal variance when increasing sample size past ~3000, so i went with the largest sample size that would allow me to finish data collection within a week (twint takes a loooooong time).

twitter_data contains:
- `twittercrawler.py` (the original crawler script)
- `erroneous_dates.csv` (the dates on which the original crawl resulted in lower-than-i-am-ok-with sample sizes, generated with `data_consolidation.py`)
- `twittercrawler_augment.py` (the crawler script that reads off `erroneous_dates.csv` to refetch bad dates with a larger sample size)
- `insert_augments.py` (script to insert the corrected dates/sentiment data into the consolidated csv)


***

if you do plan on trying to collect data with the above script/twint, i would *STRONGLY* recommend partitioning the date range up and running multiple instances of the script.
