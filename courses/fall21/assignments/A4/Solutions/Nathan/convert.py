#!/usr/bin/env python3

userses = []
claims = {}

with open('Cluster_Result_Tweetsid.txt') as f:
    for line in f.read().split('\n'):
        if not line:
            continue
        claim, users = line.split(':')
        claims[claim] = []
        for user in users.split(','):
            if user not in userses:
                userses.append(user)
            index = userses.index(user)
            claims[claim].append(index)

for claim in claims:
    for user in claims[claim]:
        print('{},{}'.format(user, claim))
