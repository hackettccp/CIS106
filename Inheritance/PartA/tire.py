"""
Tire Object.
"""

#Class Header
class Tire() :

  #Initializer
  def __init__(self, pressure_in, radius_in) :
    self.pressure = pressure_in
    self.radius = radius_in

  #Retrieves the pressure field
  def getpressure(self) :
    return self.pressure

  #Changes the pressure field
  def setpressure(self, pressure_in) :
    if isinstance(pressure_in, int) :
      if pressure_in >= 0 and pressure_in <= 60 :
        self.pressure = pressure_in
      else :
        raise ValueError("Invalid Tire Pressure") 
    else :
      raise TypeError("Invalid Data Type")

  #Retrieves the radius field
  def getradius(self) :
    return self.radius

  #Changes the radius field
  def setradius(self, radius_in) :
    self.radius = radius_in

