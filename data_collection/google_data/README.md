## google data
google trend data is fetched with the `googletrend.js` script (node had a simpler google trend package 👍) and cleaned up with `googlecleanup.py`. there is 1 value per day. 

do note that the google trend website and api both return results with a resolution that varies with your query window. i found that a 6 months wide window gives you a resolution of 1 value/day.
