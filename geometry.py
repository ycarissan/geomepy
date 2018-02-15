#!/usr/bin/python

import elements
import numpy as np

class Geometry:
   def __init__(self, geom=None):
      if geom==None:
         self.geom={}
      else:
         self.geom=geom

   def addAtom(self, lbl, x, y, z):
      self.geom.append(Atom(lbl, np.array[x,y,z]))

   def getGeom(self):
      return self.geom

   def getCenterofMass():
      pos=np.array[0,0,0]
      for a in self.geom:
         pos=a.getMass()*a.getPos()
   return pos

class Atom:
   def __init__(self, lbl, pos):
      self.lbl=lbl
      self.pos=pos
   
   def getPos(self):
      return self.pos

   def getLabel(self):
      return self.lbl

   def getMass(self):
      return elements.self.getLabel()

def main():
   print elements.Table

if __name__ == '__main__':
   main()
