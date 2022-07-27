# locally defined function to draw geometric 2D forms
from form_functions import *

#external modules and libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mplani


# an animation of a specified form (see form_functions)
# delta = plot window size (from (0-delta, 0-delta) to (0+delta, 0+delta))
def animation(form, delta, eqt, var):
    # create variables from input
    if '__builtins__' in var:
        del var['__builtins__']

    for key, value in var.items():
        var[key] = float(value)

    def transform_x1(x, y, z, t):
        v = var.copy()
        v['x'] = x
        v['y'] = y
        v['z'] = z
        v['t'] = t
        return eval(eqt['x'], v)

    def transform_x2(x, y, z, t):
        v = var.copy()
        v['x'] = x
        v['y'] = y
        v['z'] = z
        v['t'] = t
        return eval(eqt['y'], v)

    X1, X2, Dcoord1, Dcoord2 = np.array(form[0]), np.array(form[1]), form[2], form[3]
    Xg, Yg = plot_mgrid(Dcoord1, Dcoord2, 100)

    # initialising figure and the things we want to plot
    fig = plt.figure()
    contour, = plt.plot([], [], color='b')
    contour_0, = plt.plot([], [], color='b')

    grid, = plt.plot([], [], color='k')
    grid_0, = plt.plot([],[], color='k')

    # defining the animation function
    def animate(i):
        t = 5*i * 0.1

        x1 = transform_x1(X1, X2, 0, t)
        x2 = transform_x2(X1, X2, 0, t)
        contour.set_data(x1, x2)
        contour_0.set_data(X1, X2)

        xg1 = transform_x1(Xg,Yg,0,t)
        xg2 = transform_x2(Xg,Yg,0,t)
        grid.set_data(xg1, xg2)
        grid_0.set_data(Xg,Yg)

        # setting parameters of the plot
        plt.grid("--")
        plt.xlim(-delta, delta)
        plt.ylim(-delta, delta)
        plt.axis("scaled")

        return contour_0, contour, grid_0, grid,

    ani = mplani.FuncAnimation(fig, animate, frames=1000, blit=False, interval=5, repeat=True)
    plt.show()


