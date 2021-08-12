#!/usr/bin/env python3
import json

# Each tweet is a set() of tokens
def jaccard(tweet1, tweet2):
    return 1 - len(tweets[tweet1].intersection(tweets[tweet2])) / len(tweets[tweet1].union(tweets[tweet2]))

def kmeans(tweets, centroids):
    def assign(tweets, centroids):
        assignments = {cent : set() for cent in centroids}
        for tweet in tweets:
            assignments[min(centroids, key=lambda centroid: jaccard(tweet, centroid))].add(tweet)
        return assignments
    def update(assignments):
        # This will be messy. The centroid is the tweet with the smallest squared distance to all others (N^2! Ick!)
        return [min(tweets, key=lambda tweet: sum(jaccard(tweet, tweet2) ** 2 for tweet2 in tweets)) for tweets in assignments.values()]
    assigns = assign(tweets, centroids)
    cents = update(assigns)
    while(True):
        newAssigns = assign(tweets, cents)
        cents = update(assigns)
        if newAssigns == assigns:
            break
        assigns = newAssigns
    return newAssigns
        
def inferCents(tweets, K=25):
    cents = [next(iter(tweets))]
    while len(cents) < K:
        cents.append(max(tweets, key=lambda tweet: sum(jaccard(tweet, tweet2) ** 2 for tweet2 in cents)))
    return cents

print("Reading in Tweets.json")
tweets = {}
with open("Tweets.json") as f:
    for line in f:
        tweet = json.loads(line)
        tweets[int(tweet['id'])] = set(tweet['text'].lower().split())
print("Reading in InitialSeeds.txt")
cents = []
#with open('InitialSeeds.txt') as f:
#    for line in f:
#        if line[-2] == ',':
#            line = line[:-2]
#        cents.append(int(line))
cents = inferCents(tweets)

assignments = kmeans(tweets, cents)
for cent in assignments:
    print("{}: {}".format(cent, ", ".join(map(str, assignments[cent]))))
    #for tweet in assignments[cent]:
    #    print("\t{}".format(tweet))
