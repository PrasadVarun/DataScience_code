# Author : Varun Prasad
# Date : Jun 26 2020

import sys
import json

# Function to read Afinn file and prepare a word-score Dict
def afinnDict(afinnFile):
    scores = {}
    for line in afinnFile:
        term, score = line.split("\t")
        scores[term] = float(score)
    return scores

def parseData(statesMap, tweetFile):
    twitter_dict = {}
    states = {}
    for line in tweetFile:
        tweet = json.loads(line)
        if all(k in tweet.keys() for k in ("text", "id", "place")):
            if tweet['place'] is not None and "country_code" in tweet['place'].keys():
                if tweet['place']['country_code'] in statesMap.keys():
                    id = tweet['id']
                    text = tweet['text'].encode('utf-8')
                    state = tweet['place']['country_code']
                    twitter_dict[id] = text
                    states[id] = state

    return (twitter_dict, states)

def sentiScore(Sentiscores, message):
    scores = {}
    for id in message.keys():
        words = message[id].split()
        scores[id] = 0
        for word in words:
            word = word.rstrip('?:!.,;"!@')
            word = word.replace("\n", "")
            if word in Sentiscores.keys():
                scores[id] += Sentiscores[word]

    return scores

def stateSentiScore(scores, states, statesMap):
    tweetCount = {}
    twitState = {}
    for id in states.keys():
        state = states[id]
        score = scores[id]

        if state in twitState.keys():
            twitState[state] += score
            tweetCount[state] += 1
        else:
            twitState[state] = score
            tweetCount[state] = 1

    for word in twitState.keys():
        twitState[word] = twitState[word] / tweetCount[word]

    return twitState


def main():

    afinnFile = open(sys.argv[1])  # Get the afinn file
    tweetFile = open(sys.argv[2])  # Get the tweets file


    statesMap = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    sentiscores=afinnDict(afinnFile)
    afinnFile.close()
    (message, states) = parseData(statesMap, tweetFile)
    tweetFile.close()

    scores = sentiScore(sentiscores, message)


    avgStateScores = stateSentiScore(scores, states, statesMap)

    max_sent = max(avgStateScores.values())
    for key, val in avgStateScores.items():
        if val == max_sent:
            happiest_state = key

    print happiest_state


if __name__ == '__main__':
    main()