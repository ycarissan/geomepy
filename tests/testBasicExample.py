import sys
import unittest
if (sys.version_info > (3, 0)):
   from geomepy.geometry import *
   from geomepy.analysis import *
else:
   from geometry import *
   from analysis import *

class TestBasic(unittest.TestCase):

   def test_geoms12(self):
      geoms=[]
      geoms.append(pseudoreadxyz(generateLines1()))
      geoms.append(pseudoreadxyz(generateLines2()))
      for g in geoms:
         logging.info(g)
      geoms[0].center()
      geoms[1].center()
      logging.info("Geometries centered".format())
      for g in geoms:
         logging.info(g)
      RMSD, mat = compareGeoms(geoms[0], geoms[1])
      self.assertAlmostEqual(RMSD, 0.1861447, places=7, msg=None, delta=None)

def pseudoreadxyz(lines):
   geom=Geometry()
   for line in lines[2:]:
      item=line.split()
      lbl=item[0]
      x=float(item[1])
      y=float(item[2])
      z=float(item[3])
      fn="dum"
      logging.debug("Adding atom from file {0} : {1} {2} {3} {4}".format(fn, lbl, x, y, z))
      geom.addAtom(lbl,x,y,z)
   return geom

def generateLines1():
   lines=[]
   lines.append("48")
   lines.append("Energy =")
   lines.append("C             7.51947          -3.58661           2.13827")
   lines.append("C             6.20401          -3.84591           1.72473")
   lines.append("C             5.33816          -2.80926           1.46188")
   lines.append("C             5.73658          -1.46034           1.58583")
   lines.append("C             7.03359          -1.21039           2.11703")
   lines.append("C             7.91494          -2.28775           2.34869")
   lines.append("C             4.38519          -2.14366          -1.28034")
   lines.append("C             4.86969          -0.33359           1.28034")
   lines.append("C             3.68945          -0.40726           0.46701")
   lines.append("C             3.39957          -1.49025          -0.46701")
   lines.append("C             2.72046           0.61435           0.54497")
   lines.append("C             3.03306           1.79914           1.26028")
   lines.append("C             4.26729           1.97509           1.81092")
   lines.append("C             5.21330           0.92333           1.83329")
   lines.append("C             6.50191           1.12683           2.41244")
   lines.append("C             7.40417           0.11833           2.48325")
   lines.append("H             8.39712           0.29039           2.88151")
   lines.append("H             6.75123           2.11815           2.77246")
   lines.append("H             8.20395          -4.40496           2.32322")
   lines.append("H             8.90863          -2.07172           2.72376")
   lines.append("H             2.28776           2.57230           1.36356")
   lines.append("H             4.51634           2.91021           2.29852")
   lines.append("C             6.35502          -3.80124          -2.48325")
   lines.append("C             5.06961          -4.22417          -2.41244")
   lines.append("C             4.05496          -3.40416          -1.83329")
   lines.append("H             7.12925          -4.44632          -2.88151")
   lines.append("H             4.79038          -5.20748          -2.77246")
   lines.append("C             2.71004          -3.84270          -1.81092")
   lines.append("C             1.72874          -3.07373          -1.26028")
   lines.append("C             2.04980          -1.89120          -0.54497")
   lines.append("H             2.45865          -4.77720          -2.29852")
   lines.append("H             0.69687          -3.37119          -1.36356")
   lines.append("C             1.36578           0.36027           0.06685")
   lines.append("C             5.69903          -1.60062          -1.58583")
   lines.append("C             6.69775          -2.46507          -2.11703")
   lines.append("H             5.86226          -4.86740           1.61503")
   lines.append("H             4.32675          -3.04059           1.16859")
   lines.append("C             7.99945          -1.97205          -2.34869")
   lines.append("C             6.02773          -0.23305          -1.46188")
   lines.append("C             7.29567           0.23246          -1.72473")
   lines.append("C             8.30570          -0.64931          -2.13827")
   lines.append("H             8.75235          -2.65559          -2.72376")
   lines.append("H             5.26713           0.47260          -1.16859")
   lines.append("H             7.50989           1.28808          -1.61503")
   lines.append("H             9.30746          -0.28231          -2.32322")
   lines.append("C             1.00318          -0.99437          -0.06685")
   lines.append("H             0.54188           1.18374          -0.04262")
   lines.append("H            -0.12191          -1.29615           0.04262")
   return lines

def generateLines2():
   lines=[]
   lines.append("48")
   lines.append("Energy = -1152.484607320")
   lines.append("C    -1.4677174    2.3118606    2.8911465 ")
   lines.append("C    -2.0721663    1.8299749    1.7103167 ")
   lines.append("C    -1.2996664    1.4917578    0.6121497 ")
   lines.append("C     0.1159219    1.6160163    0.6245486 ")
   lines.append("C     0.7075992    2.2044115    1.7906014 ")
   lines.append("C    -0.0999437    2.5066811    2.9181982 ")
   lines.append("C    -0.9605659   -1.2879373   -0.5197816 ")
   lines.append("C     0.9605659    1.2879373   -0.5197816 ")
   lines.append("C     0.5335704    0.4989094   -1.6663216 ")
   lines.append("C    -0.5335704   -0.4989094   -1.6663216 ")
   lines.append("C     1.2053271    0.7319613   -2.9072006 ")
   lines.append("C     2.4644668    1.4057531   -2.9231337 ")
   lines.append("C     3.0210115    1.8647610   -1.7609686 ")
   lines.append("C     2.2681430    1.8518991   -0.5470506 ")
   lines.append("C     2.8257483    2.4438156    0.6336424 ")
   lines.append("C     2.0949309    2.5583250    1.7806714 ")
   lines.append("H     2.5361409    2.9888492    2.6855047 ")
   lines.append("H     3.8595744    2.8023580    0.5930471 ")
   lines.append("H    -2.0809645    2.5605572    3.7631620 ")
   lines.append("H     0.3819792    2.9301243    3.8058191 ")
   lines.append("H     2.9859093    1.5182027   -3.8791530 ")
   lines.append("H     4.0175054    2.3179669   -1.7567874 ")
   lines.append("C    -2.0949309   -2.5583250    1.7806714 ")
   lines.append("C    -2.8257483   -2.4438156    0.6336424 ")
   lines.append("C    -2.2681430   -1.8518991   -0.5470506 ")
   lines.append("H    -2.5361409   -2.9888492    2.6855047 ")
   lines.append("H    -3.8595744   -2.8023580    0.5930471 ")
   lines.append("C    -3.0210115   -1.8647610   -1.7609686 ")
   lines.append("C    -2.4644668   -1.4057531   -2.9231337 ")
   lines.append("C    -1.2053271   -0.7319613   -2.9072006 ")
   lines.append("H    -4.0175054   -2.3179669   -1.7567874 ")
   lines.append("H    -2.9859093   -1.5182027   -3.8791530 ")
   lines.append("C     0.6109055    0.3071566   -4.1348001 ")
   lines.append("C    -0.1159219   -1.6160163    0.6245486 ")
   lines.append("C    -0.7075992   -2.2044115    1.7906014 ")
   lines.append("H    -3.1607779    1.7299623    1.6544302 ")
   lines.append("H    -1.8002964    1.1560873   -0.2947506 ")
   lines.append("C     0.0999437   -2.5066811    2.9181982 ")
   lines.append("C     1.2996664   -1.4917578    0.6121497 ")
   lines.append("C     2.0721663   -1.8299749    1.7103167 ")
   lines.append("C     1.4677174   -2.3118606    2.8911465 ")
   lines.append("H    -0.3819792   -2.9301243    3.8058191 ")
   lines.append("H     1.8002964   -1.1560873   -0.2947506 ")
   lines.append("H     3.1607779   -1.7299623    1.6544302 ")
   lines.append("H     2.0809645   -2.5605572    3.7631620 ")
   lines.append("C    -0.6109055   -0.3071566   -4.1348001 ")
   lines.append("H     1.1245912    0.5389760   -5.0733098 ")
   lines.append("H    -1.1245912   -0.5389760   -5.0733098 ")
   return lines

if __name__ == '__main__':
   unittest.main()
