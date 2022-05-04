#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import json

# Load ClimateTweets.json as a pandas table
def main():
    with open("ClimateTweets.json", "r") as infile:
        data = json.load(infile)
    data = pd.DataFrame.from_records(data)
    print(data.head())
    print(data.info())
    
if __name__ == "__main__":
    main()





