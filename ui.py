from tkinter import *
from tkinter.ttk import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import pointsGenerator as pg

root = Tk()
root.title("Interfaz gráfica")
root.resizable(0, 0)
root.config(bg="white", cursor="target")
# root.geometry("400x400")

# Interface constants
fontSize = 8
algorithm = ""
renderType = ""

# Auxliar functions


def changeAlgorithms(event):
    global renderType
    selected = event.widget.get()
    algorithm_cb.set("")
    if (selected == "Línea"):
        renderType = "line"
        createInputs('Línea')
        algorithm_cb['values'] = (
            "Algoritmo básico", "Analizador diferencial digital", "Algoritmo de Brenseham")
    else:
        renderType = "circle"
        createInputs('Círculo')
        algorithm_cb['values'] = ("Algoritmo de dibujo de punto medio",)


def selectAlgorithm(event):
    global algorithm
    selected = event.widget.get()
    if selected == "Algoritmo básico":
        algorithm = "basic"
    if selected == "Analizador diferencial digital":
        algorithm = "DDA"
    if selected == "Algoritmo de Brenseham":
        algorithm = 'bresenham'
    if selected == "Algoritmo de dibujo de punto medio":
        algorithm = 'mid-point'


# inputs
# type of graph
typeOfGraph_cb = Combobox(root)
typeOfGraph_cb['values'] = ("Círculo", "Línea")
typeOfGraph_cb.config(font=("Arial", fontSize))
x1_in = Entry(width=5)
y1_in = Entry(width=5)
x2_in = Entry(width=5)
y2_in = Entry(width=5)
# Circle inputs
h_cb = Entry(width=5)
k_cb = Entry(width=5)
r_cb = Entry(width=5)
# Algorithm
algorithm_cb = Combobox(root)
algorithm_cb.config(font=("Arial", fontSize))


# Labels
# type of graph
TypeOfGraph_label = Label(root, text="Tipo de gráfica:", background="white")
TypeOfGraph_label.config(font=("Arial", fontSize+4))
# inputs labels
x1_label = Label(root, text="x1:", background="white", font="comicsans")
y1_label = Label(root, text="y1:", background="white", font="comicsans")
x2_label = Label(root, text="x2:", background="white", font="comicsans")
y2_label = Label(root, text="y2:", background="white", font="comicsans")
# Circle inputs
h_label = Label(root, text="h:", background="white", font="comicsans")
k_label = Label(root, text="k:", background="white", font="comicsans")
r_label = Label(root, text="r:", background="white", font="comicsans")
# Algorithm
TypeOfAlgorithm_label = Label(root, text="Algoritmo:", background="white")
TypeOfAlgorithm_label.config(font=("Arial", fontSize+4))
# Details
details_label = Label(root, text="Detalles", background="white")
details_label.config(font=("Arial Black", fontSize+4))
info_label = Label(root, text="",
                   background="white", font="comicsans")
# Grid positions
TypeOfGraph_label.grid(row=0, column=0, sticky=W, pady=2)
TypeOfAlgorithm_label.grid(row=1, column=0, sticky=W, pady=2)
typeOfGraph_cb.grid(row=0, column=1, sticky=W, pady=2)
algorithm_cb.grid(row=1, column=1, sticky=W, pady=2)
details_label.grid(row=7, column=0, columnspan=3,
                   sticky="", pady=2)
info_label.grid(row=8, column=0, columnspan=4,
                sticky="", pady=2)

# Inputs positions


def createInputs(type):

    if type == 'Línea':
        info_label.config(
            text="Debes especificar los puntos P(x1, y1) y Q(x2, y2) para graficar una recta.")
        h_cb.grid_remove()
        k_cb.grid_remove()
        r_cb.grid_remove()
        h_label.grid_remove()
        k_label.grid_remove()
        r_label.grid_remove()

        x1_label.grid(row=2, column=0, sticky="", pady=1, columnspan=2)
        x1_in.grid(row=2, column=1, sticky="", pady=1)
        y1_label.grid(row=3, column=0, sticky="", pady=1, columnspan=2)
        y1_in.grid(row=3, column=1, sticky="", pady=1)

        x2_label.grid(row=4, column=0, sticky="", pady=1, columnspan=2)
        x2_in.grid(row=4, column=1, sticky="", pady=1)
        y2_label.grid(row=5, column=0, sticky="", pady=1, columnspan=2)
        y2_in.grid(row=5, column=1, sticky="", pady=1)
    if type == 'Círculo':
        info_label.config(
            text="Debes especificar un origen O(h, k) y un radio r para graficar una circunferencia.")
        x1_in.grid_remove()
        x1_label.grid_remove()
        x2_in.grid_remove()
        x2_label.grid_remove()
        y1_in.grid_remove()
        y1_label.grid_remove()
        y2_in.grid_remove()
        y2_label.grid_remove()

        h_label.grid(row=2, column=0, sticky="", pady=1, columnspan=2)
        h_cb.grid(row=2, column=1, sticky="", pady=1)

        k_label.grid(row=3, column=0, sticky="", pady=1, columnspan=2)
        k_cb.grid(row=3, column=1, sticky="", pady=1)
        r_label.grid(row=4, column=0, sticky="", pady=1, columnspan=2)
        r_cb.grid(row=4, column=1, sticky="", pady=1)
    graph = Button(text="Graficar", command=graficar)
    graph.grid(row=6, column=0, columnspan=3,
               sticky="", pady=2)


# NUMPY ELEMENTS

def graficar():
    if renderType == 'line':
        pointsGen = pg.pointsGenerator()
        list = pointsGen.line(int(x1_in.get()), int(y1_in.get()),
                              int(x2_in.get()), int(y2_in.get()), algorithm)
        #list = np.array([1, 2, 3, 4, 2, 6, 7, 8, 9, 10])
        fig = plt.figure(figsize=(5, 5))
        # plt.plot(list)
        plt.grid()
        plt.plot(list[:, 0], list[:, 1], marker='o')
        # plt.show()
        # Graph
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=9, column=0, pady=2, columnspan=3,
                                    sticky="")
        # navigation
        toolbarFrame = Frame(master=root)
        toolbarFrame.grid(row=10, column=0, columnspan=3,
                          sticky="", pady=2)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    if renderType == 'circle':
        pointsGen = pg.pointsGenerator()
        list = pointsGen.circle(-2, -3, 8, algorithm)
        #list = np.array([1, 2, 3, 4, 2, 6, 7, 8, 9, 10])
        fig,  ax = plt.subplots()
        # ax.spines['top'].set_position(('data',15))
        # ax.spines['left'].set_position(('data',0))
        ax.scatter(list[:, 0], list[:, 1], s=100, label='perimeter points')
        ax.scatter([3], [5], s=50, color='blue', label='center')
        plt.grid()
        ax.set_aspect('equal')
        ax.axhline(y=0, color='gray')
        ax.axhline(y=0, color='white')
        ax.axvline(x=0, color='gray')
        plt.legend()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=9, column=0, pady=2, columnspan=3,
                                    sticky="")
        # navigation
        toolbarFrame = Frame(master=root)
        toolbarFrame.grid(row=10, column=0, columnspan=3,
                          sticky="", pady=2)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)


typeOfGraph_cb.current()
typeOfGraph_cb.bind("<<ComboboxSelected>>", changeAlgorithms)
algorithm_cb.current()
algorithm_cb.bind("<<ComboboxSelected>>", selectAlgorithm)

root.mainloop()
