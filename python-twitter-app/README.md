# Python Twitter Search API client

Simple python tool for getting tweets for exact search term and saving to json file.

## Prerequisites

1. [python-twitter](https://github.com/bear/python-twitter)
2. Configuration file with api keys and secrets setup as above:
```bash
CONSUMER_KEY=[twitter api consumer key]
CONSUMER_SECRET=[twitter api consumer secret]
ACCESS_TOKEN_KEY=[twitter api access token key]
ACCESS_TOKEN_SECRET=[twitter api access token secret]
```

## Usage

```bash
python ./py-twitter-app.py -t <search_term> -c <tweets_count> -o <output_file_name>
# only -t parameter is required
# default tweets count to download - 10
# default output name - output-{TimeStamp}.json
```

## Libraries used

* [python-twitter](https://github.com/bear/python-twitter)
* json
* os, errno
* time, datetime, getopt, sys