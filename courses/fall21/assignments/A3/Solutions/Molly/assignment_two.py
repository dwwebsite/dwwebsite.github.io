#!/usr/bin/env python2.7
# Molly Pierce
# Assignment 2
# CSE 40437 

import json
import sys
from math import*
from collections import defaultdict

# Jaccard Distance formula function
def Jaccard_Distance(tweet_one, tweet_two):
	intersection = len(set.intersection(*[set(tweet_one), set(tweet_two)]))
	union = len(set.union(*[set(tweet_one), set(tweet_two)]))
	return intersection / float(union)


tweets = {} # empty dictionary of tweets
f = open("Tweets.json", "r") # open Tweets file
while True:
	line = f.readline()
	if line == '': # end of text file
		break	

	data_tweets = json.loads(line)
	tweets[data_tweets["id"]] = data_tweets["text"] # add to tweets dictionary


centroids = [] # empty list of centroids
a = open("InitialSeeds.txt", "r") # open Initial Seeds text file
while True:
	line = a.readline()
	if line == '': 
		break
	data_centroids = line.strip().split(',')
	centroids.append(data_centroids)

centroidInfo = dict()
for centroid in centroids:
	for key, value in tweets.items():
		if key == int(centroid[0]):
			centroidInfo[int(centroid[0])] = value


# perform k means algorithm
minimumSimiliarity = 1 # worst case scenario
centroidTracker = ''
kmeans = defaultdict(list)
for key, value in tweets.items():
	for x, y in centroidInfo.items():
		if Jaccard_Distance(value, y) < minimumSimiliarity:
			minimumSimilarity = Jaccard_Distance(value, y)
			centroidTracker = x

	
	kmeans[centroidTracker].append(value)

# print out centroids
for key, value in kmeans.items():
	print "cluster_id", key, "tweet list", value

