from tkinter import*
from tkinter.ttk import*
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.title("Interfaz gráfica")
root.resizable(0,0)
root.config(bg = "white", cursor = "target")
#root.geometry("400x400")

#Interface constants
fontSize = 8


#Auxliar functions
def changeAlgorithms(event):
    selected = event.widget.get()
    algorithm_cb.set("")
    if(selected == "Línea"):
        algorithm_cb['values']=("Algoritmo básico","Analizador diferencial digital", "Algoritmo de Brenseham")
        #algorithm_cb['values']=("B","2")
    else:
        algorithm_cb['values']=("Algoritmo de dibujo de punto medio", "Algoritmo de Brenseham")
        #algorithm_cb['values']=("3","4")
    
# inputs
#type of graph
typeOfGraph_cb = Combobox(root)
typeOfGraph_cb['values']=("Círculo","Línea")
typeOfGraph_cb.config(font = ("Arial",fontSize))


#Algorithm
algorithm_cb = Combobox(root)
algorithm_cb.config(font = ("Arial",fontSize))



# Labels
#type of graph
TypeOfGraph_label = Label(root, text = "Tipo de gráfica:",background="white")
TypeOfGraph_label.config(font = ("Arial",fontSize+4))
#Algorithm
TypeOfAlgorithm_label = Label(root, text = "Algoritmo:",background="white")
TypeOfAlgorithm_label.config(font = ("Arial",fontSize+4))
#Details
details_label = Label(root, text = "Detalles",background="white")
details_label.config(font = ("Arial Black",fontSize+4))


#Grid positions
TypeOfGraph_label.grid(row=0,column=0,sticky=W,pady=2)
TypeOfAlgorithm_label.grid(row=1,column=0,sticky=W,pady=2)
typeOfGraph_cb.grid(row=0,column=1,sticky=W,pady=2)
algorithm_cb.grid(row=1,column=1,sticky=W,pady=2)
details_label.grid(row=2,column=1,sticky="",pady=2)
#graph.grid(row=3,column=1,sticky="",pady=2)

#NUMPY ELEMENTS
list = np.array([1,2,3,4,5,6,7,8,9,10])
fig = plt.figure(figsize=(4,5))
plt.plot(list)
#Graph
canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=3,column=1,sticky="",pady=2)
#navigation
toolbarFrame = Frame(master=root)
toolbarFrame.grid(row=4,column=1,sticky="",pady=2)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)



typeOfGraph_cb.current()
typeOfGraph_cb.bind("<<ComboboxSelected>>",changeAlgorithms)

root.mainloop()