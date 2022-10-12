from vpython import *
import numpy as np

# piston1 = cylinder(radius=1,length=2,color=color.red, opacity=.5)
# mySphere = sphere(radius=1,color=color.red,opacity=.5)

# while True:
#     for myRadius in np.linspace(.1,1,1000):
#         rate(250)
#         mySphere.radius=myRadius
#     for myRadius in np.linspace(1,.1,1000):
#         rate(250 )
#         mySphere.radius=myRadius

thermometer_case = cylinder(radius=1, length=5, opacity = .25)
red_liquid = cylinder(radius=.80, length=5, color=color.red)
ballthing = sphere(pos=vector(0,0,0),radius=1.5,opacity=.25)
red_liquid_ball = sphere(pos=vector(0,0,0),radius=1.30,color=color.red)

for tick in np.linspace(1,5,15):
    temp_mark = box(size=vector(.05,.5,.25), pos=vector(tick,0,1))

while True:
    for i in np.linspace(1,5,1000):
        rate(250)
        red_liquid.length = i
    for i in np.linspace(5,1,1000):
        rate(250)
        red_liquid.length = i