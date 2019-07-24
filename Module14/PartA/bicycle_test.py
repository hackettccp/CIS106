#Imports the Bicycle object
from bicycle import Bicycle

"""
Demonstrates the use of the Bicycle object
"""
def main() :
  test_bike = Bicycle()
  print("Front pressure:", test_bike.getfrontpressure())
  print("Back pressure:", test_bike.getbackpressure())
  test_bike.setfrontpressure(47)
  test_bike.setbackpressure(49)
  print("Front pressure:",test_bike.getfrontpressure())
  print("Back pressure:", test_bike.getbackpressure())
  print()

  """
  test_bike.speedup()
  test_bike.speedup()
  print("Current Speed:", test_bike.getspeed())
  test_bike.setfrontpressure(2)
  print("Flat Tire")
  test_bike.speedup()
  print("Current Speed:", test_bike.getspeed())
  print()
  """

  """
  test_bike.setfrontpressure(500)
  test_bike.setbackpressure(-5)
  """
  

  

main()
