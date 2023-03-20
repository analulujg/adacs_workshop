""""
Determine Andromeda location in ra/dec degrees
"""

from math import  cos, pi
from random import uniform

NSRC = 1_000_000

def get_radec():
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'
    
    # convert to decimal degrees
    D, M, S = DEC.split(':')
    DEC = int(D)+int(M)/60+float(S)/3600
    
    H, M, S = RA.split(':')
    RA = 15*(int(H)+int(M)/60+float(S)/3600)
    RA = RA/cos(DEC*pi/180)

    return (RA, DEC)

def make_stars(RA, DEC, NUM_STARS):
    RAS = []
    DECS = []
    for i in range(NSRC):
        RAS.append(RA + uniform(-1, 1))
        DECS.append(DEC + uniform(-1, 1))
    return(RAS, DECS)

def main():
    RA, DEC = get_radec()
    RAS, DECS = make_stars(RA,DEC,NSRC)
    
    # now write these to a csv file for use by my other program
    with open('catalog.csv', 'w', encoding='utf-8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {RAS[i]:12f}, {DECS[i]:12f}", file=f)

if __name__=='__main__':
    main()
