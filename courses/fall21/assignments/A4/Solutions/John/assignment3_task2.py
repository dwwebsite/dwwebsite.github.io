####!/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3.6
# John Villaflor - jvillafl
# Social Sensing - Assignment 3
# March 8th

import random
import json

### Function Space ###
#Many of these functions are explained in the other Python file.
def find_total_number_measured_vars(SC):
	num = -1
	for k, v_list in SC.items():
		for val in v_list:
			if val > num:
				num = val
	return num

def get_si_bi_ki(SC, total_MV):
	si_dict = dict()
	bi_dict = dict()
	ki_dict = dict()
	for k,v in SC.items():
		si_dict[k] = len(v)/ total_MV
		bi_dict[k] = 0.5*si_dict[k]
		ki_dict[k] = len(v)
	return si_dict, bi_dict, ki_dict

def calc_Z(a, b, k, tnmv, numSources):
	d = 0.5
	Z = dict()
	counter = 0
	while counter < 20:
		counter += 1
		j = 1
		while j <= tnmv:
			i = 1
			Atj = 1
			Btj = 1
			while i < numSources:
				if j in SC[i]: mval = 1
				else:          mval = 0
				Atj *= pow(a[i], mval)*pow((1-a[i]), (1-mval))
				Btj *= pow(b[i], mval)*pow((1-b[i]), (1-mval))
				i += 1
			Z[j] = (Atj*d) / float(Atj*d + Btj*(1-d))
			j+=1

		totalZ = sum(Z.values())
		i = 0
		while i < numSources:
			i += 1
			obsZ = 0
			for claim_id in SC[i]:
				obsZ += Z[claim_id]
			
			try:
				a[i] = obsZ / float(totalZ)
			except ZeroDivisionError:
				a[i] = 0

			try:
				b[i] = (k[i] - obsZ) / float(tnmv - totalZ)
			except ZeroDivisionError:
				b[i] = 0

			d = totalZ/tnmv
	return Z

### Functions needed for Task 2
#function that loads the Json data and computes several 
#"mapping" dictionaries, to keep track of the userID and tweetIDs
def load_json_return_UT():
	# UTid - key is the user ID, value is a list of TweetID's
	# TUid - key is tweet id, value is the user id
	# U counter  - is a map from userid to an integer 1-251
	UTid = dict()
	TUid = dict()
	UCounter = dict()
	data = []
	for line in open("Tweets.txt", "r"):
		data.append(json.loads(line))

	counter_user = 1
	for tweet in data:
		key = int(tweet["from_user_id"])
		val = int(tweet["id"])
		if key not in UTid: #if the userID has not been seen before
			UTid[key] = []
			UCounter[key] = counter_user
			counter_user += 1
		TUid[val] = key
		UTid[key].append(val)
	return UTid, TUid, UCounter

#open and read the Clusters file and create an SC data structure
#where the key is the UserID and the value is the ClusterID (measured var)
def parse_clusters_return_SC(TUid):
	SC = dict()
	for line in open("Cluster_Result_Tweetsid.txt", "r"):
		line = line.strip().replace(':', ',')
		tokens = line.split(',')
		measured_var = int(tokens.pop(0))
		tweetids = list(map(int, tokens))

		for tid in tweetids:
			from_user = TUid[tid]
			if from_user not in SC:
				SC[from_user] = []
			SC[from_user].append(measured_var)
	return SC
### End Functions needed for Task 2
### End Function Space ###


### Main Function ###
user_tweetid, tweet_userid, user_count_map = load_json_return_UT()
SC_temp = parse_clusters_return_SC(tweet_userid)
SC = dict()
#convert the original key (which was the User ID) to an integer 1-251
for k,v in SC_temp.items(): 
	SC[user_count_map[k]] = v

#si_dict, where the key sourceid and the value is the si value
#bi is 1/2 * si
#ki key is a source id, value is the number of claim ID's that they have posted
tnmv = find_total_number_measured_vars(SC)
si, bi, ki = get_si_bi_ki(SC, tnmv)

#initialize ai=si
ai = si

#call the function to determine Z and write to file
Z = calc_Z(ai, bi, ki, tnmv, len(SC))
ofname = 'task2_results.txt'
with open(ofname, 'w') as f:
	for k,v in sorted(Z.items(), key=lambda x: x[1], reverse=True): 
		f.write(str(k)+'\t'+str(v)+'\n')
