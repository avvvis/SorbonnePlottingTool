# external libraries
from math import *
import matplotlib.pyplot as plt
import numpy as np


# add points on a line between two other points: f steps between p1 and p2
def ligne(p1,p2,f):
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    X = [p1[0]]
    Y = [p1[1]]
    for i in range (f):
        X.append(X[i] + (1/f)*dx )
        Y.append(Y[i] + (1/f)*dy )
    return X,Y


# draws a custom figure, connecting each point in the list in the list order (warning: connects Lp[-1] with Lp[0])
def custom(Lp,f):
    #print(Lp, type(Lp))
    # the coordinates of all points of the figure
    X=[]
    Y=[]
    # a dictionnary assigning each int value of x all the y values of the intersection between the vertical line and the figure
    # ==> pts of figure on one vertical line
    Dcoord = {}
    # a dictionnary assigning each int value of y all the x values of the intersection between the horizontal line and the figure
    # ==> pts of figure on one horizontal line
    Dcoord2 = {}
    for i in range (len(Lp)):
        # choosing the two points
        p1 = Lp[i]
        p1[0] = float(p1[0])
        p1[1] = float(p1[1])
        if i+1 == len(Lp):
            p2 = Lp[0]
            p2[0] = float(p2[0])
            p2[1] = float(p2[1])
        else:
            p2 = Lp[i+1]
            p2[0] = float(p2[0])
            p2[1] = float(p2[1])
        # fundaments of the grid
        if (p1[0]-p2[0]) == 0:  # special case for xp1 == xp2
            Dcoord2[p1[1]] = [p1[0],p2[0]]
        else:
            for j in range(  ceil(min([p1[0],p2[0]])) , int(max([p1[0],p2[0]])+1) ):  # j an int between xmin and xmax
                    fx = (p1[1]-p2[1])/(p1[0]-p2[0]) *(j-p1[0]) +p1[1]  # the genreal equation of a line

                    if j in Dcoord and fx in Dcoord[j]:  # if the intersection point is already considered dont add it a seccond time
                        pass
                    # add the y coordinate into the dict
                    elif j in Dcoord:
                        Dcoord[j].append(fx)
                    else:
                        Dcoord[j] = [fx]

        # the same for j an int between ymin and ymax
        if (p1[1]-p2[1]) == 0:
            pass
        else:
            for j in range(  ceil(min([p1[1],p2[1]])) , int(max([p1[1],p2[1]])+1) ):
                        x = ((j - p1[1])*(p1[0]-p2[0]) + (p1[1]-p2[1])*p1[0] )/(p1[1]-p2[1])
                        if j in Dcoord2 and x in Dcoord2[j]:
                            pass
                        elif j in Dcoord2:
                            Dcoord2[j].append(x)
                        else:
                            Dcoord2[j] = [x]

        # append all the coordinates of our figure into X and Y
        for j in ligne(p1,p2,f)[0]:
            X.append(j)
        for j in ligne(p1,p2,f)[1]:
            Y.append(j)
    return X,Y,Dcoord,Dcoord2


# a function to add all the points on the lines of the grid
def plot_mgrid(Dcoord, Dcoord2, f):

    Lgrid = [[],[]]
    for i in Dcoord: # i == x
        for j in range(0,len(Dcoord[i]),2): # j an element of Dcoord[i] ==> y coordinate

            if j+1 < len(Dcoord[i]): # connecting hte points wwith lines (p1 and p2, p3 and p4,...)
                X, Y = ligne([i, Dcoord[i][j]], [i, Dcoord[i][j+1]],f)

                Lgrid[0].extend(X)
                Lgrid[0].append(np.nan) # a np.nan (= not a number) is not plotted ==> separates the lines from eachother
                Lgrid[1].extend(Y)
                Lgrid[1].append(np.nan)

    # same for Dcoord2
    for i in Dcoord2:
        for j in range(0,len(Dcoord2[i]),2):
            if j+1 < len(Dcoord2[i]):
                X, Y= ligne([Dcoord2[i][j],i], [Dcoord2[i][j+1],i],f)
                Lgrid[0].extend(X)
                Lgrid[0].append(np.nan)
                Lgrid[1].extend(Y)
                Lgrid[1].append(np.nan)

    return np.array(Lgrid[0]), np.array(Lgrid[1])

def triangle(p1,p2,p3,f):
    return custom([p1,p2,p3], f)


def rectangle(xc, yc, l, h, f):  # center (xc,yc) l the length on x, h the highth on y
    xc = float(xc)
    yc = float(yc)
    l = float(l)
    h = float(h)
    p1 = [xc - 1/2*l, yc - 1/2*h]
    p2 = [p1[0] + l, p1[1]]
    p3 = [p2[0], p2[1] + h]
    p4 = [p1[0], p1[1] + h]
    return custom([p1,p2,p3,p4], f)

# an ellypse centered on (0,0)
def ellipse_0(a,b,Np): # a the half axe on x, b the half axe on y, Np the number of points
    a = float(a)
    b = float(a)
    X = []
    Y = []
    angle=0
    while angle <= 2*pi:
        X.append(cos(angle)*a)
        Y.append(sin(angle)*b)
        angle += (2*pi)/Np
    return X,Y

def ellypse(xc, yc, a,b, Np):  # center (xc,yc)
    xc = float(xc)
    yc = float(yc)
    X, Y = ellypse_0(a,b,Np)
    Lp = []
    for i in range(Np+1):
        X[i] += xc
    for i in range(Np+1):
        Y[i] += yc
    for i in range(Np+1):
        Lp.append([X[i], Y[i]])

    return custom(Lp,1) # the purpose of passing it through custom is to create the grid

def scatterpoints(Lp):
    X=[]
    Y=[]
    Dcoord = -1
    Dcoord2 = -1

    for i in range (len(Lp)):
        X.append(Lp[i][0])
        X.append(np.nan)
        Y.append(Lp[i][1])
        Y.append(np.nan)
    return X,Y,Dcoord,Dcoord2








