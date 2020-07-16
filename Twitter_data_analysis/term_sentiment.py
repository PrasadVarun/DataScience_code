# Author : Varun Prasad
# Date : Jun 26 2020

import sys
import json
import re

# Function to read Afinn file and prepare a word-score Dict
def afinnDict(afinnFile, scoresDict):
    for line in afinnFile:
        word, score = line.split("\t")
        scoresDict[word] = int(score)

#Function to parse the json file
def parseJson(tweetFile):
    jsonList = []
    # Parse the json file and store it in jsonlist
    for jsonListObject in (tweetFile.read().split("\n")):
        if jsonListObject != '':
            jsonDict = json.loads(jsonListObject)
            jsonList.append(jsonDict)
    return jsonList

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

# Function to read tweet file and calculate the Sentiment score
def tweetScore(scoresDict, twitterJsonList):
    sentiScores={}
    sentiScoresOfLine={}
    # Read every tweet from jsonList and get the text field to analyze the sentiment
    for singleJson in twitterJsonList:
        if singleJson.has_key("text"):
            for line in singleJson["text"].encode("utf-8").split("\t"):
                line = line.strip('?:!.,'';"!@').replace("\n", " ")
                # Cehck the Sentiment score of each word from scoresDict and sum up for the whole line
                score = 0
                for word in line.split():
                    word=re.sub(r'([+-]?\d+(?:\.\d+)?(?:[eE][+-]\d+)?(www\.[\S]+)|(https:?://[\S]+))','',word.lower())
                    if isEnglish(word) and scoresDict.has_key(word.lower()):
                        score=score + scoresDict.get(word.lower())
                    else:
                        score
                sentiScoresOfLine[line]=score
    return sentiScoresOfLine

#Function to derive the sentiment of new terms
def sentiNewTerms(sentiScoresOfLine, sentiScores, sentiScoresNewTerms):
    # Read every tweet from jsonList and get the text field to analyze the sentiment
            for line in sentiScoresOfLine.keys():
                score = sentiScoresOfLine[line]
                for word in line.split():
                    word = re.sub(r'([+-]?\d+(?:\.\d+)?(?:[eE][+-]\d+)?(www\.[\S]+)|(https?://[\S]+))','',word.lower()).strip('?:!.,'';"!@').replace("\n", "")
                    if word not in sentiScores.keys():
                        if word in sentiScoresNewTerms.keys():
                            totalScore =float(score + sentiScoresNewTerms[word])
                        else:
                            totalScore = score
                print line,totalScore
                #print("{} {}".format(line,totalScore))


# Main Method

def main():
    scoresDict = {}
    twitterJsonList=[]
    sentiScoresNewTerms={}

    afinnFile = open(sys.argv[1])  # Get the afinn file
    tweetFile = open(sys.argv[2])  # Get the tweets file

    afinnDict(afinnFile, scoresDict)
    afinnFile.close()
    twitterJsonList = parseJson(tweetFile)
    tweetFile.close()
    sentiScoresOfLine = tweetScore(scoresDict, twitterJsonList)

    sentiNewTerms(sentiScoresOfLine,scoresDict,sentiScoresNewTerms)

if __name__ == '__main__':
    main()
