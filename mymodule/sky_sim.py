""""
Determine Andromeda location in ra/dec degrees
"""

from math import  cos, pi
from random import uniform

NSRC = 1_000_000

def get_radec():
    """
    Detarminate Andromeda location
    """

    RA = '00:42:44.3'
    DEC = '41:16:09'

    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/cos(dec*pi/180)

    return (ra, dec)

def make_stars(ra, dec, num_stars):
    """ 
    make 1000 stars within 1 degree of Andromeda
    """
    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(ra + uniform(-1, 1))
        decs.append(dec + uniform(-1, 1))
    return(ras, decs)

def main():
    """ main function"""
    ra, dec = get_radec()
    ras, decs = make_stars(ra, dec, NSRC)

    # now write these to a csv file for use by my other program
    with open('catalog.csv', 'w', encoding='utf-8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)

if __name__ == '__main__':
    main()
