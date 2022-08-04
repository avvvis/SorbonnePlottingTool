#
# SorbonnePlottingTool
# ---------------------

import tkinter as tk
from form_functions import *
import animation as ani


class GUI:
    def __init__(self):
        self.master = tk.Tk()
        self.ahelp = 0
        master = self.master
        # data needed for centering windows
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        # running first window
        self.equation_window()

    # destroy last window and build new window base
    def build_new_window(self, sizex, sizey, title):
        # building window
        self.master.destroy()
        self.master = tk.Tk()
        master = self.master
        master.title(title)

        # centering the window
        center_x = int(self.screen_width / 2 - sizex / 2)
        center_y = int(self.screen_height / 2 - sizey / 2)
        master.geometry(f"{sizex}x{sizey}+{center_x}+{center_y}")

    def choose_dimension(self):
        self.build_new_window(150, 100, "choose dimension")

        self.master.lift()
        self.master.focus_force()

        # building widgets
        choose_label = tk.Label(self.master, text="Choose dimension:")
        choose_label.grid(row=0, column=1, sticky='W')

        # command runs new window with 2d figure choice
        button2D = tk.Button(self.master, text="2D", width=20, command=self.choose2d)
        button2D.grid(row=1, column=0, columnspan=2, sticky='W')

        # same as above but with 3d
        button3D = tk.Button(self.master, text="3D", width=20)
        button3D.grid(row=2, column=0, columnspan=2, sticky='W')

        # setting initial focus and adding jumping functionality
        button2D.focus_set()
        button2D.bind('<Down>', lambda event: button3D.focus_set())
        button2D.bind('<Return>', lambda event: button2D.invoke())
        button3D.bind('<Up>', lambda event: button2D.focus_set())
        button3D.bind('<Return>', lambda event: button3D.invoke())

    def ellipse_data_window(self):
        self.build_new_window(400, 200, "Input data")

        input_label = tk.Label(self.master, text="Input data:")
        input_label.grid(row=0, column=0, sticky='W')

        label_x_center = tk.Label(self.master, text="center point x coord :", width=20)
        label_x_center.grid(row=1, column=0, columnspan=1, sticky='E')
        self.entry_x_center = tk.Entry(self.master, width=20)
        self.entry_x_center.grid(row=1, column=1)

        label_y_center = tk.Label(self.master, text="center point x coord :", width=20)
        label_y_center.grid(row=2, column=0, columnspan=1, sticky='W')
        self.entry_y_center = tk.Entry(self.master, width=20)
        self.entry_y_center.grid(row=2, column=1)

        label_length = tk.Label(self.master, text="a/semi-major axis :", width=20)
        label_length.grid(row=3, column=0, sticky='w')
        self.entry_length = tk.Entry(self.master)
        self.entry_length.grid(row=3, column=1)

        label_height = tk.Label(self.master, text="b/semi-minor axis :", width=20)
        label_height.grid(row=4, column=0, sticky='w')
        self.entry_height = tk.Entry(self.master)
        self.entry_height.grid(row=4, column=1)

        self.pltdefaultX = tk.StringVar(self.master, value ="15")
        self.pltdefaultY = tk.StringVar(self.master, value ="15")
        label_pltsizeX = tk.Label(self.master, text="plt size X:", width=10)
        label_pltsizeX.grid(row=5, column=0)
        self.entry_pltsizeX = tk.Entry(self.master, textvariable=self.pltdefaultX, width=10)
        self.entry_pltsizeX.grid(row=5, column=1, sticky='w')

        label_pltsizeY = tk.Label(self.master, text="plt size Y:", width=10)
        label_pltsizeY.grid(row=5, column=2, sticky='w')
        self.entry_pltsizeY = tk.Entry(self.master,textvariable=self.pltdefaultY, width=10)
        self.entry_pltsizeY.grid(row=5, column=3, sticky='w')

        button_next = tk.Button(self.master, text="next", width=20, command=lambda: self.plot_figure("ellipse"))
        button_next.grid(row=6, column=0, columnspan=2)

        # adding feature of jumping between windows with arrows
        self.master.lift()
        self.master.focus_force()
        self.entry_x_center.focus_set()

        self.entry_x_center.bind('<Down>', lambda event: self.entry_y_center.focus_set())
        self.entry_y_center.bind('<Up>', lambda event: self.entry_x_center.focus_set())
        self.entry_y_center.bind('<Down>', lambda event: self.entry_length.focus_set())
        self.entry_length.bind('<Up>', lambda event: self.entry_y_center.focus_set())
        self.entry_length.bind('<Down>', lambda event: self.entry_height.focus_set())
        self.entry_height.bind('<Up>', lambda event: self.entry_length.focus_set())
        self.entry_height.bind('<Down>', lambda event: self.entry_pltsizeX.focus_set())
        self.entry_pltsizeX.bind('<Up>', lambda event: self.entry_height.focus_set())
        self.entry_pltsizeX.bind('<Right>', lambda event: self.entry_pltsizeY.focus_set())
        self.entry_pltsizeX.bind('<Down>', lambda event: button_next.focus_set())
        self.entry_pltsizeY.bind('<Left>', lambda event: self.entry_pltsizeX.focus_set())
        self.entry_pltsizeY.bind('<Down>', lambda event: button_next.focus_set())
        self.entry_pltsizeY.bind('<Up>', lambda event: self.entry_height.focus_set())
        button_next.bind('<Up>', lambda event: self.entry_pltsizeY.focus_set())
        button_next.bind('<Return>', lambda event: button_next.invoke())

    def choose2d(self):
        self.build_new_window(150, 150, "choose figure")

        choose_label = tk.Label(self.master, text="Choose figure:")
        choose_label.grid(row=0, column=1, sticky='W')

        # TODO: add commands
        button_rectangle = tk.Button(self.master, text="rectangle / square", width=20,
                                     command=self.rectangle_data_window)
        button_rectangle.grid(row=1, column=0, columnspan=2, sticky='W')

        button_ellipse = tk.Button(self.master, text="ellipse / circle", width=20, command=self.ellipse_data_window)
        button_ellipse.grid(row=2, column=0, columnspan=2, sticky='W')

        button_custom = tk.Button(self.master, text="custom", width=20,
                                  command=self.custom_data_window)
        button_custom.grid(row=3, column=0, columnspan=2, sticky='W')

        button_scatterpoints = tk.Button(self.master, text="scatterpoints", width=20,
                                  command=self.scatterpoints_data_window)
        button_scatterpoints.grid(row=4, column=0, columnspan=2, sticky='W')


        self.clicked_grid = tk.BooleanVar()
        checkbox_grid = tk.Checkbutton(self.master, text='Grid: ', variable=self.clicked_grid, onvalue=True,
                                       offvalue=False)
        checkbox_grid.grid(row=5, column=0, columnspan=2, sticky='w')

        # these lines allow to focus on button in new window
        self.master.lift()
        self.master.focus_force()

        # initial focus and jumping functionality
        button_rectangle.focus()
        button_rectangle.bind('<Down>', lambda event: button_ellipse.focus_set())
        button_ellipse.bind('<Up>', lambda event: button_rectangle.focus_set())
        button_ellipse.bind('<Down>', lambda event: button_custom.focus_set())
        button_custom.bind('<Up>', lambda event: button_ellipse.focus_set())

        button_rectangle.bind('<Return>', lambda event: button_rectangle.invoke())
        button_ellipse.bind('<Return>', lambda event: button_ellipse.invoke())
        button_custom.bind('<Return>', lambda event: button_custom.invoke())

    def custom_data_window(self):
        self.build_new_window(250, 550, "Input points :")

        input_label = tk.Label(self.master, text="Input points")
        input_label.grid(row=0, column=0, sticky='w')

        self.text_points = tk.Text(self.master, height=30, width=30)
        self.text_points.grid(row=1, column=0, sticky='w', rowspan=5, columnspan=2)
        self.text_points.insert(tk.END, "points=[]")

        self.button_plot_points = tk.Button(self.master, text="plot!", width=10,
                                            command=lambda: self.plot_figure("custom"))
        self.button_plot_points.grid(row=6, column=0, columnspan=2)

        # adding focus and shortcuts
        self.master.lift()
        self.master.focus_force()
        self.text_points.focus_set()

        self.text_points.bind("<Shift-Return>", lambda event: self.button_plot_points.focus_set())
        self.text_points.bind("<Shift-Down>", lambda event: self.button_plot_points.focus_set())
        self.button_plot_points.bind("<Up>", lambda event: self.text_points.focus_set())
        self.button_plot_points.bind("<Return>", lambda event: self.button_plot_points.invoke())

    def scatterpoints_data_window(self):
        self.build_new_window(250, 550, "Input points :")

        input_label = tk.Label(self.master, text="Input points")
        input_label.grid(row=0, column=0, sticky='w')

        self.text_points = tk.Text(self.master, height=30, width=30)
        self.text_points.grid(row=1, column=0, sticky='w', rowspan=5, columnspan=2)
        self.text_points.insert(tk.END, "points=[]")

        self.button_plot_points = tk.Button(self.master, text="plot!", width=10,
                                            command=lambda: self.plot_figure("scatterpoints"))
        self.button_plot_points.grid(row=6, column=0, columnspan=2)

        # adding focus and shortcuts
        self.master.lift()
        self.master.focus_force()
        self.text_points.focus_set()

        self.text_points.bind("<Shift-Return>", lambda event: self.button_plot_points.focus_set())
        self.text_points.bind("<Shift-Down>", lambda event: self.button_plot_points.focus_set())
        self.button_plot_points.bind("<Up>", lambda event: self.text_points.focus_set())
        self.button_plot_points.bind("<Return>", lambda event: self.button_plot_points.invoke())

    # window to input rectangle data
    def rectangle_data_window(self):
        self.build_new_window(400, 200, "Input data")

        # adding labels and entries
        input_label = tk.Label(self.master, text="Input data:")
        input_label.grid(row=0, column=0, sticky='W')

        label_x_center = tk.Label(self.master, text="center point x coord :", width=20)
        label_x_center.grid(row=1, column=0, columnspan=1, sticky='E')
        self.entry_x_center = tk.Entry(self.master, width=20)
        self.entry_x_center.grid(row=1, column=1)

        label_y_center = tk.Label(self.master, text="center point x coord :", width=20)
        label_y_center.grid(row=2, column=0, columnspan=1, sticky='W')
        self.entry_y_center = tk.Entry(self.master, width=20)
        self.entry_y_center.grid(row=2, column=1)

        label_length = tk.Label(self.master, text="Length :", width=20)
        label_length.grid(row=3, column=0, sticky='w')
        self.entry_length = tk.Entry(self.master)
        self.entry_length.grid(row=3, column=1)

        label_height = tk.Label(self.master, text="Height :", width=20)
        label_height.grid(row=4, column=0, sticky='w')
        self.entry_height = tk.Entry(self.master)
        self.entry_height.grid(row=4, column=1)

        self.pltdefaultX = tk.StringVar(self.master, value ="15")
        self.pltdefaultY = tk.StringVar(self.master, value ="15")
        label_pltsizeX = tk.Label(self.master, text="plt size X:", width=10)
        label_pltsizeX.grid(row=5, column=0)
        self.entry_pltsizeX = tk.Entry(self.master, textvariable=self.pltdefaultX, width=10)
        self.entry_pltsizeX.grid(row=5, column=1, sticky='w')

        label_pltsizeY = tk.Label(self.master, text="plt size Y:", width=10)
        label_pltsizeY.grid(row=5, column=2, sticky='w')
        self.entry_pltsizeY = tk.Entry(self.master,textvariable=self.pltdefaultY, width=10)
        self.entry_pltsizeY.grid(row=5, column=3, sticky='w')

        button_next = tk.Button(self.master, text="next", width=20, command=lambda: self.plot_figure("rectangle"))
        button_next.grid(row=6, column=0, columnspan=2)

        # adding feature of jumping between windows with arrows
        self.master.lift()
        self.master.focus_force()
        self.entry_x_center.focus_set()

        self.entry_x_center.bind('<Down>', lambda event: self.entry_y_center.focus_set())
        self.entry_y_center.bind('<Up>', lambda event: self.entry_x_center.focus_set())
        self.entry_y_center.bind('<Down>', lambda event: self.entry_length.focus_set())
        self.entry_length.bind('<Up>', lambda event: self.entry_y_center.focus_set())
        self.entry_length.bind('<Down>', lambda event: self.entry_height.focus_set())
        self.entry_height.bind('<Up>', lambda event: self.entry_length.focus_set())
        self.entry_height.bind('<Down>', lambda event: self.entry_pltsizeX.focus_set())
        self.entry_pltsizeX.bind('<Up>', lambda event: self.entry_height.focus_set())
        self.entry_pltsizeX.bind('<Right>', lambda event: self.entry_pltsizeY.focus_set())
        self.entry_pltsizeX.bind('<Down>', lambda event: button_next.focus_set())
        self.entry_pltsizeY.bind('<Left>', lambda event: self.entry_pltsizeX.focus_set())
        self.entry_pltsizeY.bind('<Down>', lambda event: button_next.focus_set())
        self.entry_pltsizeY.bind('<Up>', lambda event: self.entry_height.focus_set())
        button_next.bind('<Up>', lambda event: self.entry_pltsizeY.focus_set())
        button_next.bind('<Return>', lambda event: button_next.invoke())

    def plot_figure(self, figure):
        checked = self.clicked_grid
        if figure == "rectangle":
            ani.animation(rectangle(self.entry_x_center.get(), self.entry_y_center.get(), self.entry_length.get(),
                                    self.entry_height.get(), 100), self.eqt, self.var, checked, self.ahelp, float(self.entry_pltsizeX.get()), float(self.entry_pltsizeY.get()))
        if figure == "ellipse":
            ani.animation(ellipse(self.entry_x_center.get(), self.entry_y_center.get(), self.entry_length.get(),
                                  self.entry_height.get(), 100), self.eqt, self.var, checked, self.ahelp,float(self.entry_pltsizeX.get()), float(self.entry_pltsizeY.get()))

        elif figure == "custom":
            # getting data from input (lop = list of points)
            str_lop = self.text_points.get("1.0", tk.END)
            str_lop = str_lop.split("=")[1]
            # changing string into list
            # note that you have to use specific formula for list to work [x1, y1], [x2, y2], ... [xn, yn]
            str_lop = str_lop.replace(" ", '').replace("\n", '').replace("[", '').replace("]", '')
            str_lop = str_lop.split(",")
            lop = []
            # data after strip = x1,y1,x2,y2...xn,yn
            for i in range(0, len(str_lop), 2):
                lop.append([float(str_lop[i]), float(str_lop[i + 1])])
            # running animation
            ani.animation(custom(lop, 100),self.eqt, self.var, checked, self.ahelp, 50, 50)
        elif figure == "scatterpoints":
            # getting data from input (lop = list of points)
            str_lop = self.text_points.get("1.0", tk.END)
            str_lop = str_lop.split("=")[1]
            # changing string into list
            # note that you have to use specific formula for list to work [x1, y1], [x2, y2], ... [xn, yn]
            str_lop = str_lop.replace(" ", '').replace("\n", '').replace("[", '').replace("]", '')
            str_lop = str_lop.split(",")
            lop = []
            # data after strip = x1,y1,x2,y2...xn,yn
            for i in range(0, len(str_lop), 2):
                lop.append([float(str_lop[i]), float(str_lop[i + 1])])
            # running animation
            ani.animation(scatterpoints(lop), self.eqt, self.var, checked, self.ahelp, 50, 50)
        self.ahelp += 1

    def equation_window(self):
        self.build_new_window(400, 300, "Input Equation")

        self.master.lift()
        self.master.focus_force()

        equation_label = tk.Label(self.master, text="Input equation:")
        equation_label.grid(row=0, column=0, sticky='W')

        label_eq = tk.Label(self.master, text="Equation :", width=15)
        label_eq.grid(row=1, column=0, columnspan=1, sticky='E')
        self.entry_equation = tk.Text(self.master, width=30, height=5)
        self.entry_equation.grid(row=1, column=1, sticky='e')

        label_variables = tk.Label(self.master, text="Variables: ", width=15)
        label_variables.grid(row=2, column=0)
        self.entry_variables = tk.Text(self.master, width=30, height=5)
        self.entry_variables.grid(row=2, column=1)

        self.button_plot = tk.Button(self.master, text='NEXT', command=lambda: self.get_variables())
        self.button_plot.grid(row=3, column=1, columnspan=2)

        # adding keyboard shortcuts
        self.entry_equation.focus_set()
        self.entry_equation.bind("<Shift-Return>", lambda event: self.entry_variables.focus_set())
        self.entry_equation.bind("<Shift-Down>", lambda event: self.entry_variables.focus_set())
        self.entry_variables.bind("<Shift-Up>", lambda event: self.entry_equation.focus_set())
        self.entry_variables.bind("<Shift-Down>", lambda event: self.button_plot.focus_set())
        self.entry_variables.bind("<Shift-Return>", lambda event: self.button_plot.focus_set())
        self.button_plot.bind("<Return>", lambda event: self.button_plot.invoke())
        self.button_plot.bind("<Up>", lambda event: self.entry_variables.focus_set())

        # note
        label_note = tk.Label(self.master,
                              text="NOTE : Shift + Enter to jump down\n Or Shift +Arrow Down/Up to jump up/down")
        label_note.grid(row=4, column=1, sticky='w')

    def get_variables(self):
        # loading variables from tk.Text to set
        variables = self.entry_variables.get("1.0", tk.END)
        variables = variables.split("\n")
        variables.remove('')
        self.var = {}
        for v in variables:
            v = v.split("=")
            v[0] = v[0].replace(" ", "")
            v[1] = v[1].replace(" ", "")
            self.var[v[0]] = v[1]

        # loading equations from tk.Text to set
        equations = self.entry_equation.get("1.0", tk.END)
        equations = equations.split("\n")
        equations.remove('')
        self.eqt = {}
        for e in equations:
            e = e.split("=")
            e[0] = e[0].replace(" ", "")
            e[1] = e[1].replace(" ", "")
            self.eqt[e[0]] = e[1]

        self.choose_dimension()


gui = GUI()
tk.mainloop()
