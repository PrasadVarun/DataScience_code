# Author : Varun Prasad
# Date : Jun 26 2020

import sys
import json


# Function to read Afinn file and prepare a word-score Dict
def afinnDict(afinnFile, scoresDict):
    for line in afinnFile:
        word, score = line.split("\t")
        scoresDict[word] = int(score)


# Function to read tweet file and calculate the Sentiment score
def tweetScore(scoresDict, tweetFile):
    jsonList = []

    # Parse the json file and store it in jsonlist
    for jsonListObject in (tweetFile.read().split("\n")):
        if jsonListObject != '':
            jsonDict = json.loads(jsonListObject)
            jsonList.append(jsonDict)

    # Read every tweet from jsonList and get the text field to analyze the sentiment
    for singleJson in jsonList:
        if singleJson.has_key("text"):
            for line in singleJson["text"].encode("utf-8").split("\n"):

                # Cehck the Sentiment score of each word from scoresDict and sum up for the whole line
                score = 0
                for word in line.split():
                    if scoresDict.has_key(word):
                        score = score + scoresDict.get(word)
                print score


# Main Method
def main():
    scoresDict = {}

    afinnFile = open(sys.argv[1])  # Get the afinn file
    tweetFile = open(sys.argv[2])  # Get the tweets file

    afinnDict(afinnFile, scoresDict)
    tweetScore(scoresDict, tweetFile)


if __name__ == '__main__':
    main()
