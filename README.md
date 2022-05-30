# ClimateTweets

### I. Repo description

- This repo contains two folders: **./data** and **./code**.

- The **./data** folder contains ***ClimateTweets.json*** file, which can be loaded using the Python3 script ***./code/load_json.py*** or any other json library. Python3 [json](https://docs.python.org/3/library/json.html) and [pandas](https://pandas.pydata.org/) packages are required to run this script.

- The format of the ***ClimateTweets.json*** file is:

    `
    {'tweet_id': '1402050489974505474',
     'start_char': 186,
     'end_char': 280,
     'category': 'mitigation',
     'category_polarity': 'neutral'
    }
    `

- After loading the json file, one can use the Python3 script ***./code/query_text.py*** to retrieve the text from Twitter. Due to Twitter's terms and conditions, the text could not be shared but need to be retrieved using the provided tweet_id(s). Python3 [json](https://docs.python.org/3/library/json.html) and [requests](https://pypi.org/project/requests/) packages are required to run this script. Up to the date of this document, a [full-archive search API from Twitter](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction) is required to run this script.

- Up to the date of this document, Twitter only offers full-archive search API for Academic Research only. Follow this [instruction page](https://developer.twitter.com/en/products/twitter-api/academic-research) to apply for one.


### II. How-to query ClimateTweets

1. Acquire an Academic Research API key from Twitter


2. Go to ***./code/query_text.py***, replace the *bearer_token* below with your token:

`def get_tweets_from_id(parameters):
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAANWmTAEAAAAAkMjjNGED8tj8DKv_replace_with_your_token'`
    
3. Load the ***./data/ClimateTweets.json*** file using the ***./code/load_json.py*** script


4. Split the *tweet_id(s)* list from the ClimateTweets table of step 3


5. Use the ***./code/query_text.py*** to query the whole text for each *tweet_id*


6. Use the *start_char* and *end_char* from the ClimateTweets table of step 3 to split the sentences


7. Join the sentences to the ClimateTweets table of step 3

### III. Resolve missing cases

For some reason, some tweets may be removed from the archive (for example, the onwer deletes the tweet). Hence, in case of missing tweets, please contact us via duongthi001@e.ntu.edu.sg for resolution.


### IV. Acknowledgement

The authors would like to thank the volunteering annotators of this project.
