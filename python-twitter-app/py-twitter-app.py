import twitter
import json
import os, errno
import time, datetime, getopt, sys
from configurations import *

# default parameters
result_file_name = 'output/output-{0}.json'.format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M%S'))
search_term = "popular"
tweets_count = 10

# get parameters
try:
    opts, args = getopt.getopt(sys.argv[1:], "t:c:o:", ["term=", "count=", "output-file="])
except getopt.GetoptError:
    print("Invalid parameters.")
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-t", "--term"):
        search_term = arg
    elif opt in ("-c", "--count"):
        tweets_count = arg
    elif opt in ("-o", "--output-file"):
        result_file_name = arg

# create api
api = twitter.Api(
                consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token_key=ACCESS_TOKEN_KEY,
                access_token_secret=ACCESS_TOKEN_SECRET
            )
print(f"Downloading {tweets_count} tweets for search term: {search_term}.")

tweets = api.GetSearch(term=search_term, count=tweets_count, return_json=True)
print("Tweets downloaded successfully!")

# create directory if not exists
if not os.path.exists(os.path.dirname(result_file_name)):
    try:
        os.makedirs(os.path.dirname(result_file_name))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# save to file
print(f"Saving tweets to file: {result_file_name}")
with open(result_file_name, 'w') as outfile:
    json.dump(tweets, outfile, sort_keys=True, indent=4)
print("Tweets saved successfully!")