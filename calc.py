
from tkinter import *

ventana = Tk()
ventana. title ("calculadora")
ventana.configure(bg="pink")
#i = 0

#entrada
e_texto = Entry(ventana, font = "Commforta 45")
e_texto.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
e_texto.config(bg="turquoise")

i = 0
def click_boton(valor):
     global i
     e_texto.insert(i,valor)
     i += 1
     
def Delete():
    e_texto.delete(0,END)    
    i = 0
def Eliminar():
    global i
    i=i-1
    e_texto.delete(i,END)
    
def operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i = 0
    
def operacion_binaria():
    ecuacion=e_texto.get()
    resultado= eval(ecuacion)
    resultado_binario =bin(int(resultado))
    e_texto.delete(0,END)
    e_texto.insert(0, resultado_binario)
    global i
    i=0    


def Activate_deactivate():
    estado_actual = boton_Eliminar.cget('state')  
    nuevo_estado='normal' if estado_actual== 'disabled' else 'disabled'
    boton_Eliminar.configure(state=nuevo_estado)
       

boton1 = Button(ventana, text="1", width=5, height=2,bg="orange", fg="green", font= "arial 11", cursor= "pirate",relief="flat", command=lambda: click_boton(1))
boton2= Button(ventana, text="2", width=5, height=2, bg="orange", fg="green", font= "arial 11", cursor= "star", command=lambda: click_boton(2))
boton3 = Button(ventana, text="3", width=5, height=2, bg="orange", fg="green", font= "arial 11",  cursor= "cross",command=lambda: click_boton(3))
boton4 = Button(ventana, text="4", width=5, height=2,bg="turquoise", fg="black", font= "arial 11",cursor= "heart",  command=lambda: click_boton(4))
boton5 = Button(ventana, text="5", width=5, height=2,bg="turquoise", fg="black", font= "arial 11", cursor= "watch", command=lambda: click_boton(5))
boton6 = Button(ventana, text="6", width=5, height=2,bg="turquoise", fg="black", font= "arial 11", cursor= "pencil",command=lambda: click_boton(6))
boton7 = Button(ventana, text="7", width=5, height=2,bg="magenta", fg="white", font= "arial 11",cursor= "pirate",command=lambda: click_boton(7))
boton8 = Button(ventana, text="8", width=5, height=2,bg="magenta", fg="white", font= "arial 11",cursor= "star", command=lambda: click_boton(8))
boton9 = Button(ventana, text="9", width=5, height=2,bg="magenta", fg="white", font= "arial 11",cursor= "cross", command=lambda: click_boton(9))
boton0= Button(ventana, text="0", width=5, height=2, bg="red", fg="white", font= "arial 11",cursor= "heart",command=lambda: click_boton(0))

boton_Delete =Button(ventana, text="DL", width=5, height=2, bg="green", fg="white", font= "arial 11", cursor= "watch",command=lambda:Delete())
boton_Parenthesis1 = Button(ventana, text="(", width=5, height=2, bg="green", fg="white", font= "arial 11",cursor="pencil", command=lambda: click_boton("("))
boton_Parenthesis2 = Button(ventana, text=")", width=5, height=2,bg="green", fg="white", font= "arial 11", cursor="pirate",command=lambda: click_boton(")"))
boton_Dot = Button(ventana, text=".", width=5, height=2,bg="red", fg="white", font= "arial 11", cursor="star", command=lambda: click_boton("."))
boton_Eliminar= Button(ventana, text="<-", width=5, height=2, bg="red", fg="white", font= "arial 11", cursor="cross", command=lambda:Eliminar())
boton_Binomial=Button(ventana, text="BIN", width=5, height=2,bg="black", fg="white", font= "arial 12", cursor="heart", command=lambda:operacion_binaria())

boton_Division =Button(ventana, text="/", width=5, height=2, bg="green", fg="white", font= "arial 11", cursor="watch",command=lambda: click_boton("/"))
boton_Multiplication =Button(ventana, text="*", width=5, height=2,bg="purple", fg="white", font= "arial 11", cursor="pencil",command=lambda: click_boton("*"))
boton_Adittion =Button(ventana, text="+", width=5, height=2,bg="turquoise", fg="black", font= "arial 11",cursor="pirate", command=lambda: click_boton("+"))
boton_Subtraction =Button(ventana, text="-", width=5, height=2, bg="orange", fg="green", font= "arial 11", cursor="star", command=lambda: click_boton("-"))
boton_Equal =Button(ventana, text="=", width=5, height=2, bg="red", fg="white", font= "arial 11", cursor="cross",command=lambda: operacion())
boton_Retorn = Button(ventana, text="Acti/Des", width=5, height=2, bg="black", fg="white", font= "arial 12",cursor="heart", command=lambda: Activate_deactivate())

#asignamos colocacion de elementos en ventana
boton_Delete.grid(row=1, column=0, padx=5, pady=5)
boton_Parenthesis1.grid(row=1, column=1, padx=5, pady=5)
boton_Parenthesis2.grid(row=1, column=2, padx=5, pady=5)
boton_Dot.grid(row=1, column=3, padx=5, pady=5)
boton_Division.grid(row=1, column=3, padx=5, pady=5 )

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_Multiplication.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_Adittion.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_Subtraction.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, padx=5, pady=5)
boton_Dot.grid(row=5, column=1, padx=5, pady=5)
boton_Equal.grid(row=5, column=2, padx=5, pady=5)
boton_Eliminar.grid(row=5,column=3, padx=5, pady=5)
boton_Binomial.grid(row=5,column=4, padx=5, pady=2)
boton_Retorn.grid(row=5,column=5, padx=5, pady=2)


ventana.mainloop()
