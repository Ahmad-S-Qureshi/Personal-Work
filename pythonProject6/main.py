import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

def go_dist_in_centimeters(droid, dist):
    startDist = (float)(droid.get_distance())
    droid.set_speed(100)
    currDist = startDist - startDist
    while(currDist  < dist):
        print(currDist)
        print(droid.get_distance())
        currDist = droid.get_distance() - startDist

    droid.set_speed(0)
    print("successfully went " + (str)(dist) + " centimeters")

def turn_clockwise(droid, turn_degrees_clockwise):
    heading = droid.get_heading()
    droid.set_heading(heading+turn_degrees_clockwise)
    print("successfully turned " + (str)(turn_degrees_clockwise) + " degrees clockwise")

def draw_square_with_size_in_centimeters(droid, size):
    for i in range (0,4):
        go_dist_in_centimeters(droid, size)
        turn_clockwise(droid, 90)
    print("successfully drew square of size " + (str)(size) + " centimeters")

scanner.find_RVR()
toy = scanner.find_RVR()
with SpheroEduAPI(toy) as droid:
    droid.set_main_led(Color(r=0, g=0, b=255))
    dist = 100
    while(True):
        print()
        print()
        print(droid.get_distance())
        print(droid.get_speed())
        print(droid.get_acceleration())
        print()
        print()