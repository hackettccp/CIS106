#Imports the Tire object
from tire import Tire

"""
Bicycle Object.
"""

#Class Header
class Bicycle :

  #Initializer
  def __init__(self) :
    self.front_tire = Tire(45, 27)
    self.back_tire = Tire(50, 27)
    self.speed = 0

  #Retrieves the front tire pressure
  def getfrontpressure(self) :
    return self.front_tire.getpressure()

  #Changes the front tire pressure
  def setfrontpressure(self, pressure_in) :
    try :
      self.front_tire.setpressure(pressure_in)
    except ValueError :
      print("Invalid Front Tire Pressure Provided")
    except TypeError :
      print("Invalid Front Tire Data Type Provided")


  #Retrieves the back tire pressure
  def getbackpressure(self) :
    return self.back_tire.getpressure()

  #Changes the back tire pressure
  def setbackpressure(self, pressure_in) :
    try :
      self.back_tire.setpressure(pressure_in)
    except ValueError :
      print("Invalid Back Tire Pressure Provided")
    except TypeError :
      print("Invalid Back Tire Data Type Provided")


  #Increases the speed
  def speedup(self) :
    if self.getfrontpressure() < 5 or self.getbackpressure() < 5 :
      self.speed = 0 #Tire is too flat
    else :
      self.speed += 5

  #Retreives the speed field
  def getspeed(self) :
    return self.speed
