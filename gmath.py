import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    return [255,0,0]
    return [calculate_ambient(ambient,areflect)[0]+calculate_diffuse(light, dreflect, normal)[0]+calculate_specular(light, sreflect, view, normal)[0],
            calculate_ambient(ambient,areflect)[1]+calculate_diffuse(light, dreflect, normal)[1]+calculate_specular(light, sreflect, view, normal)[1],
            calculate_ambient(ambient,areflect)[2]+calculate_diffuse(light, dreflect, normal)[2]+calculate_specular(light, sreflect, view, normal)[2]]

def calculate_ambient(alight, areflect):
    return shorten(alight,areflect)

def calculate_diffuse(light, dreflect, normal):
    return shorten(light[1],shorten2(dreflect,dot_product(normal,light[0])))

def calculate_specular(light, sreflect, view, normal):
    twice=[2,2,2]
    return shorten(light[1],shorten2(sreflect,math.pow(dot_product(subtract(shorten(twice,shorten2(normal,dot_product(light[0],normal))),light[0]),view),SPECULAR_EXP)))

def limit_color(color):
    return [color[0]/max(color),color[1]/max(color),color[2]/max(color)]

def shorten(a,b):
    return [a[0] * b[0],a[1] * b[1], a[2] * b[2]]
def shorten2(a,b):
    return [a[0] * b,a[1] * b, a[2] * b]

def subtract(a,b):
    return [a[0] - b[0],a[1] - b[1], a[2] - b[2]]

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
