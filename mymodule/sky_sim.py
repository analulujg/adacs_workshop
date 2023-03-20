""""
Determine Andromeda location in ra/dec degrees
"""

from math import  cos, pi
from random import uniform

# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'

# convert to decimal degrees
D, M, S = DEC.split(':')
DEC = int(D)+int(M)/60+float(S)/3600

H, M, S = RA.split(':')
RA = 15*(int(H)+int(M)/60+float(S)/3600)
RA = RA/cos(DEC*pi/180)

NSRC = 1_000_000
RAS = []
DECS = []
for i in range(NSRC):
    RAS.append(RA + uniform(-1, 1))
    DECS.append(DEC + uniform(-1, 1))


# now write these to a csv file for use by my other program
with open('catalog.csv', 'w', encoding='utf-8') as f:
    print("id,ra,dec", file=f)
    for i in range(NSRC):
        print("{0:07d}, {1:12f}, {2:12f}".format(i, RAS[i], DECS[i]), file=f)