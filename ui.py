from tkinter import*
from tkinter.ttk import*
from turtle import window_height, window_width

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
#typeOfGraph_cb.place(x = 152, y = 12, width = 200, heigh = 20)
typeOfGraph_cb.config(font = ("Arial",fontSize))



#Algorithm
algorithm_cb = Combobox(root)
#algorithm_cb.place(x = 152, y = 40, width = 200, heigh = 20)
algorithm_cb.config(font = ("Arial",fontSize))


# Labels
TypeOfGraph_label = Label(root, text = "Tipo de gráfica:",background="white")
#TypeOfGraph_label.place(x = 30, y = 10, width = 120, heigh = 20)
TypeOfGraph_label.config(font = ("Arial",fontSize+4))

TypeOfAlgorithm_label = Label(root, text = "Algoritmo:",background="white")
#TypeOfGraph_label.place(x = 30, y = 40, width = 120, heigh = 20)
TypeOfAlgorithm_label.config(font = ("Arial",fontSize+4))


#Grid positions
TypeOfGraph_label.grid(row=0,column=0,sticky=W,pady=2)
TypeOfAlgorithm_label.grid(row=1,column=0,sticky=W,pady=2)
typeOfGraph_cb.grid(row=0,column=1,sticky=W,pady=2)
algorithm_cb.grid(row=1,column=1,sticky=W,pady=2)

def callback(sel):
    print(sel)

typeOfGraph_cb.current()
typeOfGraph_cb.bind("<<ComboboxSelected>>",changeAlgorithms)

root.mainloop()