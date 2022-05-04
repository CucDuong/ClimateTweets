#!/usr/bin/env python
# coding: utf-8

# In[53]:


import requests
import json

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

# take up to 100 ids at a time
def get_tweets_from_id(parameters):
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAANWmTAEAAAAAkMjjNGED8tj8DKv_replace_with_your_token'
    headers = create_headers(bearer_token)
    url = "https://api.twitter.com/2/tweets?"
    try:
        response = requests.get(url,headers=headers,params=parameters,stream=True)
        print(response)
    
        for response_line in response.iter_lines():
            if response_line:
                json_response = json.loads(response_line)
        return json_response
    except:
        print('Error!')

def get_multi_tweets_from_id(lst_id):
    params = {'ids':(','.join(lst_id))}
    data = get_tweets_from_id(params)
    return data

def main():
    # Load ClimateTweets.json
    # Extract tweet_id column to a list
    # For example:
    lst_id = ['1450975135129812995','1450973691009929217']
    # Get response from Twitter API
    # Max number of tweet_id per query is 100
    response  = get_multi_tweets_from_id(lst_id)
    print('Type of response: ', type(response))
    print('#################################')
    data = response['data']
    print('Type of data: ', type(data))
    print('#################################')
    print('Length of data: ', len(data))
    print('#################################')
    print('First item of data: ')
    print(data[0])
    print('#################################')
    # Use the start_char, end_char column to extract the sentence from the text
    print('Text of the first item: ')
    print(data[0]['text'])
    print('#################################')
    print('Start_char and end_char of the first item are 0 and 149')
    print('#################################')
    print('The sentence is: ')
    print(data[0]['text'][0:149])
    print('#################################')

if __name__ == "__main__":
    main()

