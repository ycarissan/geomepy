#!/usr/bin/python

import argparse
import datetime
from spectrum import *
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt 
import logging
import numpy as np
logging.basicConfig(filename='geompy.log',level=logging.DEBUG)

class geometry:

def readxyz(fn):
   f = open(fn, 'r')
   lines=f.readlines()
   nat=int(lines[0])
   geom=[]
   for line in lines[2:]:
      lbl=line[0]
      x=line[1]
      y=line[2]
      z=line[3]
      geom.append([lbl,x,y,z])
   return geom

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("-g", "--geoms", help="geometries to compare in xyz format", default="geom1.xyz geom2.xyz")
   args = parser.parse_args()
#Default values
#
   geomfiles=args.geoms
   for f in geomfiles:
      geoms.append(readxyz(f))

if __name__ == '__main__':
    main()
