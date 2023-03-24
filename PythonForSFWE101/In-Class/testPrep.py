import math
import random
def checker():
    booleanVals = [True, False]
    for a in booleanVals:
        for b in booleanVals:
            for y in booleanVals:
                for x in booleanVals:
                    # Add tested vals to the if
                    boolVal1 = not x and y == a and b
                    boolVal2 = not ((x and (y == a)) and b)
                    if((boolVal1) != (boolVal2)):
                        print("Not Equal")
                        return
    print("Equal")
    return

checker()