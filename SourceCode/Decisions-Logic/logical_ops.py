"""
Demonstrates logical operators
"""

#Declares four variables named b1, b2, b3 and b4
#Assigns to the variables the values True, False, False and True, respectively
b1 = True
b2 = False
b3 = False
b4 = True
        
#Declares a variable named result1 and assigns it the result of
#b1 and'ed with b2
result1 = b1 and b2
        
#Prints the value of result1.
print("b1 and b2 is", result1)
        
#********************************#
print()
"""
#Declares a variable named result2 and assigns it the result of
#b1 or'ed with b2.
result2 = b1 or b2
        
#Prints the value of result2.
print("b1 or b2 is ", result2)
"""
#********************************#
print()
"""
#Declares a variable named result3 and assigns it the result of
#b1 or'ed with b2 and'ed with b3.
result3 = b1 or b2 and b3
        
#Prints the value of result3.
print("b1 or b2 and b3 is ", result3)
"""
#********************************#
print()
"""
#Declares a variable named result4 and assigns it the result of
#b1 or'ed with (b2 and'ed with b3).
result4 = b1 or (b2 and b3)
        
#Prints the value of result4.
print("b1 or (b2 and b3) is ", result4)
"""
#********************************#
print()
"""
#Declares a variable named result5 and assigns it the result of
#b1 or'ed with not b2 and'ed with b3.
result5 = b1 or not b2 and b3
        
#Prints the value of result5.
print("b1 or not b2 and b3 is ", result5)
"""
#********************************#
print()
"""
#Declares a variable named result6 and assigns it the result of
#b1 or'ed with not(b2 and'ed with b3).
result6 = b1 or not(b2 and b3)
        
#Prints the value of result6.
print("b1 or not(b2 and b3) is ", result6)
"""
