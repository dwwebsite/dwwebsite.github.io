####!/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3.6
# John Villaflor - jvillafl
# Social Sensing - Assignment 3
# March 8th

import random

### Function Space ###
#finds the total number of measured variables
def find_total_number_measured_vars(SC):
	num = -1
	for k, v_list in SC.items():
		for val in v_list:
			if val > num:
				num = val
	return num

#computes the s, b, k probabilities and stores them in a dict
def get_si_bi_ki(SC, total_MV):
	si_dict = dict()
	bi_dict = dict()
	ki_dict = dict()
	for k,v in SC.items():
		si_dict[k] = len(v)/ total_MV
		bi_dict[k] = 0.5*si_dict[k]
		ki_dict[k] = len(v)
	return si_dict, bi_dict, ki_dict

# EM Algorithm Implementation, based on the pseudocode given to us
def calc_Z(a, b, k, tnmv, numSources):
	d = random.uniform(0, 1)
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
### End Function Space ###


### Main Function ###
#SC is a dictionary, the key is the [sourceid] and the value is a list of all measured variables where SiCj=1
SC = dict()
fname = 'SCMatrix_Submit'
with open(fname, 'r') as f:
	for line in f:
		sourceid, claimid = map(int, line.strip().split(','))
		if sourceid not in SC:
			SC[sourceid] = []
		SC[sourceid].append(claimid)

#si_dict, where the key sourceid and the value is the si value
#bi is 1/2 * si
#ki key is a source id, value is the number of claim ID's that they have posted
tnmv = find_total_number_measured_vars(SC)
si, bi, ki = get_si_bi_ki(SC, tnmv)

#initialize ai=si, d = random(0,1)
ai = si

#call the function to determine Z
Z = calc_Z(ai, bi, ki, tnmv, len(SC))

#process results and write them to 'task1.txt'
ofname = 'task1_results.txt'
with open(ofname, 'w') as f:
	for k,v in Z.items():
		if v>=0.5: output = 1
		else:      output = 0
		f.write(str(k)+", "+str(output)+"\n")
