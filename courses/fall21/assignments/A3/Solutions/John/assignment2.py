#!/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3.6

#John Villaflor - 2/19/2018
#Assignment 2 - Tweet Analyzer

### Import Modules ###
import json

### Functions ###
#load data from the .json file
def load_json():
	data = []
	for line in open("Tweets.json", "r"):
		data.append(json.loads(line))
	return data

#grab just the tweet id and the tweet text
def grab_id_text(data):
	idtext = {}
	for tweet in data:
		idtext[tweet["id"]] = set(tweet["text"].strip().split())
	return idtext

#compute the Jacard Distance of two sets
def distance(set1, set2):
	union = len(set1|set2)
	intersection = len(set1&set2)
	return 1 - (intersection / union)

#load the initial seeds
def load_seeds():
	data = []
	for line in open("InitialSeeds.txt", "r"):
		data.append(int(line.strip().strip(",")))
	return data

#takes seeds and tweet data then return clusters. the CLUSTERS data structure is a dictionary where the key
#is the seed and the value is a list with all of the elements that fall into that cluster
def make_clusters(seeds, id_text):
	#initialize the clust data struct
	clust = {}
	for s in seeds:
		clust[s] = set()
		clust[s].add(s)

	#for every tweet, compute its Jacard Distance to each seed, cluster it with the closest seed 
	for num, text in id_text.items():
		curr_dist = 10**10
		curr_seed = -1
		for sid in seeds:
			d = distance(text, id_text[sid])
			if d < curr_dist:
				curr_dist = d
				curr_seed = sid
		clust[curr_seed].add(num)

	return clust

#function that takes in the current clusters and finds a new list of seeds
def get_new_seeds(clusters, id_text):
	new_seeds = []
	#for every cluster compute the JD of each tweet to all other tweets in that cluster
	#then save the tweet that has the min distance throughout the whole cluster
	for cid, cluster in clusters.items():
		curr_dist = 10**10
		new_seed = -1
		for tid1 in cluster:
			sum_dist = 0
			for tid2 in cluster:
				sum_dist += distance(id_text[tid1], id_text[tid2])

			if sum_dist < curr_dist:
				curr_dist = sum_dist
				new_seed = tid1
		new_seeds.append(new_seed)

	return new_seeds	

### Main Execution ###
all_tweets = load_json()
id_text    = grab_id_text(all_tweets)
init_seeds = load_seeds()

#Continue computing new seeds and clusters until the NEW_SEEDS does not change between iterations
while True:
	CLUSTERS = make_clusters(init_seeds, id_text)
	NEW_SEEDS = get_new_seeds(CLUSTERS, id_text)
	if set(init_seeds) == set(NEW_SEEDS):
		break
	init_seeds = NEW_SEEDS

#write to output file
with open("A2_output_jvillafl.txt", "w") as ofile:
	for cid, clust in CLUSTERS.items():
		string = "{}: ".format(str(cid))
		string += " ".join(map(str, clust))
		string += "\n\n"
		ofile.write(string)
