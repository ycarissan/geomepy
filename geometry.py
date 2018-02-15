#!/usr/bin/python

import elements
import numpy as np

class Geometry:
   def __init__(self, geom=None):
      if geom==None:
         self.geom={}
      else:
         self.geom=geom

   def __str__(self):
      nat=len(self.geom)
      val="{0} atoms\n".format(nat)
      for a in self.geom.keys():
         val += str(self.geom[a])+'\n'
      return val

   def addAtom(self, lbl, x, y, z):
      nat=len(self.geom)
      self.geom[str(nat)]=Atom(lbl, np.array([x,y,z]))

   def getGeom(self):
      return self.geom

   def getCenterofMass():
      pos=np.array(0,0,0)
      for a in self.geom:
         pos=a.getMass()*a.getPos()
      return pos

class Atom:
   def __init__(self, lbl, pos):
      self.lbl=lbl
      self.pos=pos

   def __str__(self):
      val="{0} {1} {2} {3}".format(self.lbl, self.pos[0], self.pos[1], self.pos[2])
      return val
   
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
