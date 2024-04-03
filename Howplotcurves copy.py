import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()

Xi = 0
Yi = 0
Thetai = 45
RPM1 = 5
RPM2 = 10

actions = [(0, RPM1), (RPM1, 0), (RPM1, RPM1), (0, RPM2), (RPM2, 0), (RPM2, RPM2), (RPM1, RPM2), (RPM2, RPM1)]

moves = []
for action in actions:
    UL,UR=action
    t = 0
    r = 0.038
    L = 0.354
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes

    D=0
    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        plt.plot([Xs, Xn], [Ys, Yn], color="blue")

    Thetan = 180 * (Thetan) / 3.14
    moves.append((Xn,Yn, Thetan))

print(moves)     
   

  

plt.grid()

ax.set_aspect('equal')

plt.xlim(0,1)
plt.ylim(0,1)

plt.title('How to plot a vector in matplotlib ?',fontsize=10)

plt.show()
plt.close()
    
