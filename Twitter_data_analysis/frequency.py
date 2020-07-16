# Author : Varun Prasad
# Date : Jun 27 2020

import sys
import json
import re

# Function to read tweet file and calculate the term frequency
def termFreq(tweetFile):
    jsonList = []
    allTermsCounter=0.0
    termCounterDict={}

    # Parse the json file and store it in jsonlist
    for jsonListObject in (tweetFile.read().split("\n")):
        if jsonListObject != '':
            jsonDict = json.loads(jsonListObject)
            jsonList.append(jsonDict)

    # Read every tweet from jsonList and get the text field to calculate the term frequency
    for singleJson in jsonList:
        if singleJson.has_key("text"):
            for line in singleJson["text"].encode("utf-8").split("\n"):
                #line = 'a ball a bat, bat and a ball'

                for word in line.split():
                    word = re.sub(r'([+-]?\d+(?:\.\d+)?(?:[eE][+-]\d+)?(www\.[\S]+)|(https?://[\S]+))','',word.lower())
                    allTermsCounter+=1
                    if word in termCounterDict.keys():
                        termCounterDict[word]=float(termCounterDict[word]+1)
                    else:
                        termCounterDict[word]=1
    for item in termCounterDict.items():
        print("{} {}".format(item[0],item[1]))


# Main Method
def main():

    tweetFile = open(sys.argv[1])  # Get the tweets file

    termFreq(tweetFile)


if __name__ == '__main__':
    main()
