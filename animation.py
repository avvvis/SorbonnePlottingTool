# locally defined function to draw geometric 2D forms
from form_functions import *
# external modules and libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mplani


# an animation of a specified form (see form_functions)
# delta = plot window size (from (0-delta, 0-delta) to (0+delta, 0+delta))
def animation(form, delta, eqt, var, clicked_grid, ahelp):
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

    # enables plotting or not plotting the Grid
    if clicked_grid.get() == True:
        Xg, Yg = plot_mgrid(Dcoord1, Dcoord2, 100)
    elif clicked_grid.get() == False:
        Xg, Yg = np.nan, np.nan

    # initialising figure and the things we want to plot
    fig = plt.figure()
    if Dcoord1 == -1 and Dcoord2 == -1:
        contour_0, = plt.plot([], [],".", color='k')
        contour, = plt.plot([], [],".", color='k')
    else:
        contour, = plt.plot([], [], color='k)
        contour_0, = plt.plot([], [], color='k)
    grid, = plt.plot([], [], color='b)
    grid_0, = plt.plot([], [], color='b)

    # defining the animation function
    def animate(i):
        t = i

        x1 = transform_x1(X1, X2, 0, t)
        x2 = transform_x2(X1, X2, 0, t)
        contour.set_data(x1, x2)
        contour_0.set_data(X1, X2)

        xg1 = transform_x1(Xg, Yg, 0, t)
        xg2 = transform_x2(Xg, Yg, 0, t)
        grid.set_data(xg1, xg2)
        grid_0.set_data(Xg, Yg)

        # setting parameters of the plot
        plt.grid("--")
        plt.xlim(-delta, delta)
        plt.ylim(-delta, delta)
        plt.axis("scaled")

        return contour_0, contour, grid_0, grid,

    ani = mplani.FuncAnimation(fig, animate, frames=(np.arange(0.0, 1000, 0.1), blit=False, interval=10, repeat=False)
    plt.show()
    # closes those wierd windows that jump out every second time
    # if you have any idea how to fix that, please do it, I did all I could
    if ahelp % 2 == 0:
        plt.close('all')
