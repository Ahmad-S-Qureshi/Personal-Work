import math
import random
# def checker():
#     booleanVals = [True, False]
#     for a in booleanVals:
#         for b in booleanVals:
#             for y in booleanVals:
#                 for x in booleanVals:
#                     # Add tested vals to the if
#                     boolVal1 = not x and y == a and b
#                     boolVal2 = not ((x and (y == a)) and b)
#                     if((boolVal1) != (boolVal2)):
#                         print("Not Equal")
#                         return
#     print("Equal")
# checker()

grades = { 'A': 90, 'B': 80, 'C': 70, 'D': 60 }
my_grade = 70
if my_grade not in grades:
    z = 1
else:
    z = 2
if 'F' in grades:
    z = z + 10
else:
    z = z + 20
print(z)