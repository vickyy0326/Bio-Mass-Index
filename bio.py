 import math
 
 t = int(input("Enter the total time t in days: "))
 L = float(input("Enter the latitude L in degrees: "))
 D = float(input("Enter the solar constant D in watts per square meter: "))
 r = float(input("Enter the precipitation r in centimeters per day: "))


  S = r * 10
  A = math.pi * ((L / 90) ** 2)
  V = S * A
  I = (V / 1000) * (D / 1000)



 print("The precipitation in mm/day is: %.2lf" % S)
 print("The surface area of the biomass is: %.2lf square meters" % A) 
 print("The volumetric water content is: %.2lf liters per square meter" % V) 
 print ("The Biomass Index I is: %.2lf" % I)