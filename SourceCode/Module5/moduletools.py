"""
Demonstrates creating a module
"""

#A function named getvolume.
#This function will return the volume of a rectangular prism.
#The function should accept three parameters: l, w and h
def getvolume(l, w, h) :
  return l * w * h

#A function named getsurfacearea.
#This function will return the surface area of a rectangular prism.
#The function should accept three parameters: l, w and h
def getsurfacearea(l, w, h) :
  return 2 * (l * w + w * h + l * h)

#A function named iscube.
#This function will return if the rectangular prism is a cube.
#The function should accept three parameters: l, w and h
#The function should return True or False
def iscube(l, w, h) :
  if l == h and h == w :
    return True
  else :
    return False



