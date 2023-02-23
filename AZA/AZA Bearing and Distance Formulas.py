import math

def calcBearing(xpos, ypos, xmax, ymax):
    xpos = xmax - xpos
    # Validate input values
    if xmax <= 0 or ymax <= 0:
        print("Error: xmax and ymax must be positive values.")
        return float('nan')
    if xpos < 0 or xpos > xmax or ypos < 0 or ypos > ymax:
        print("Error: (xpos, ypos) must be within the range of (0, 0) to (xmax, ymax).")
        return float('nan')
    if xpos > xmax/2 and ypos < ymax/2:
        radians = math.atan(float(xpos - xmax/2)/(ymax/2 - ypos))
        radians += math.pi/2
    elif xpos > xmax/2 and ypos > ymax/2:
        radians = math.atan(float(ypos - ymax/2)/(xpos - xmax/2))
        radians += math.pi
    elif xpos < xmax/2 and ypos > ymax/2:
        radians = math.atan(float(xmax/2 - xpos)/(ypos - ymax/2))
        radians += 3*math.pi/2
    else:
        radians = math.atan(float(ymax/2 - ypos)/(xmax/2 - xpos))
    return radians * 180 / math.pi

def calcMagnitude(xpos, ypos, xmax, ymax, height, maxDegrees):
    xpos = xmax - xpos
    if xmax <= 0 or ymax <= 0:
        print("Error: xmax and ymax must be greater than 0")
        return -1
    if maxDegrees < 0 or maxDegrees >= 90:
        print("Error: maxDegrees must be between 0 and 90 degrees")
        return -1
    if xpos < 0 or xpos > xmax:
        print("Error: xpos and ypos must be between 0 and xmax, ymax respectively")
        return -1
    maxFeet = height * math.tan(maxDegrees/180 * math.pi)
    xDistPixels = xpos - xmax/2
    yDistPixels = ypos - ymax/2
    pixelsFromCornertoMiddle = math.pow(math.pow(xmax/2, 2) + math.pow(ymax/2, 2), 1.0/2)
    feetPerPixel = maxFeet / pixelsFromCornertoMiddle
    if xpos != 0:
        totalDistPixels = math.pow(math.pow(xDistPixels, 2) + math.pow(yDistPixels, 2), 0.5)
        feet = totalDistPixels * feetPerPixel
    else:
        feet = yDistPixels * feetPerPixel
    return abs(feet)

if __name__ == '__main__':
    with open("output1.csv", "w") as file:
        file.write("x, y, feet, theta\n")
        for i in range(0, 3000, 10):
            for j in range(0, 4000, 10):
                file.write("{},  {}, {:.2f}, {:.2f}\n".format(i, j, calcMagnitude(i, j, 3000, 4000, 50, 10.7), calcBearing(i, j, 3000, 4000)))
    print("Text written to file successfully.")