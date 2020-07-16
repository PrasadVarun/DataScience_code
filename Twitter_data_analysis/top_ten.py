# Author : Varun Prasad
# Date : Jun 26 2020

import sys
import json

# Function to read tweet file and calculate the Sentiment score
def tweetScore(tweetFile):
    hashtagFreq = {}

    for line in tweetFile:
        tweet = json.loads(line)
        if "entities" in tweet.keys() and "hashtags" in tweet["entities"]:
            if tweet['entities']['hashtags'] != []:
                for hashtag in tweet["entities"]["hashtags"]:
                    value = hashtag["text"].encode('utf-8')
                    if value in hashtagFreq.keys():
                        hashtagFreq[value] += 1
                    else:
                        hashtagFreq[value] = 1
    ten_values = sorted(hashtagFreq.iteritems(), key=lambda x:-x[1])[:10]
    for x in ten_values:
        print "{0}: {1}".format(*x)

# Main Method
def main():

    tweetFile = open(sys.argv[1])  # Get the tweets file

    tweetScore(tweetFile)
    tweetFile.close()

if __name__ == '__main__':
    main()
