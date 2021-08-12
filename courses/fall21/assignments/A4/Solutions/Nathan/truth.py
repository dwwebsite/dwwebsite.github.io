#!/usr/bin/env python3
import sys

SCMat = {}
N = 0
M = 0

filename=sys.argv[1]

with open(filename) as f:
    for line in f:
        (source, claim) = line.split(',')
        source = int(source)
        claim = int(claim)
        if source-1 not in SCMat:
            SCMat[source-1] = set()
        SCMat[source-1].add(claim-1)
        if source > M:
            M = source
        if claim > N:
            N = claim

A = [len(SCMat[i]) / N for i in range(0, M)]
B = [A[i] / 2 for i in range(0, M)]
import random
D = random.random()
Z = [.5] * N

def compZ():
    def XTJ(X, j):
        XJ = 1
        for i in range(0, M):
            if j in SCMat[i]:
                XJ *= X[i]
            else:
                XJ *= 1 - X[i]
        return XJ
    for j in range(0, N):
        ATJ = XTJ(A, j)
        BTJ = XTJ(B, j)
        Z[j] = ATJ * D / (ATJ * D + BTJ * (1 - D))

def nextA(sumz):
    return [sum(Z[j] for j in SCMat[i]) / sumz for i in range(0, M)]

def nextB(sumz):
    return [(len(SCMat[i]) - sum(Z[j] for j in SCMat[i])) / (N - sumz) for i in range(0, M)]

def nextD(sumz):
    return sumz / N

iteration = 0
while True:
    iteration += 1
    compZ()
    sumz = sum(Z)
    nA = nextA(sumz)
    nB = nextB(sumz)
    nD = nextD(sumz)
    if nA == A and nB == B and nD == D or iteration > 100:
        break
    A = nA
    B = nB
    D = nD

for j in range(0, N):
    if Z[j] > .5:
        print('{},{}'.format(j+1,1))
    else:
        print('{},{}'.format(j+1,0))
