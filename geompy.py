#!/usr/bin/python

import argparse
import datetime
from geometry import *
import logging
import numpy as np
logging.basicConfig(filename='geompy.log',level=logging.DEBUG)

def readxyz(fn):
   f = open(fn, 'r')
   lines=f.readlines()
   nat=int(lines[0])
   geom=Geometry()
   for line in lines[2:]:
      item=line.split()
      lbl=item[0]
      x=item[1]
      y=item[2]
      z=item[3]
      logging.info("Adding atom from file {0} : {1} {2} {3} {4}".format(fn, lbl, x, y, z))
      geom.addAtom(lbl,x,y,z)
   return geom

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("-g", "--geoms", help="geometries to compare in xyz format", default="geom1.xyz geom2.xyz")
   args = parser.parse_args()
#Default values
#
   geomfiles=args.geoms.split()
   geoms=[]
   for f in geomfiles:
      geom=readxyz(f)
      print geom
      geoms.append(geom)

if __name__ == '__main__':
    main()
