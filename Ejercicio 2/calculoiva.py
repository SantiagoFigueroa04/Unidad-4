from tkinter import *
from tkinter import ttk


class calculariva():
    __ventana=None
    __preciobase=None
    __precioiva=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry('400x400')
        self.__ventana.configure(bg='light blue')
        self.__ventana.title('Calculador de iva')
        self.iva=DoubleVar()
        
        ttk.Label(self.__ventana,text='Calculo de IVA',background='blue').place(width=400,height=50)
        
        ttk.Button(self.__ventana, text='Salir', command=self.__ventana.destroy).place(x=300, y=325)

        ttk.Button(self.__ventana, text='Calcular', command=self.calcular).place(x=80, y=325)
        
        ttk.Label(self.__ventana,text='Precio sin IVA').place(x=80,y=90)
        self.__preciobase=DoubleVar()
        self.__precioiva=DoubleVar()
        ttk.Entry(self.__ventana,textvariable=self.__preciobase).place(x=180,y=90)

        
        seleccionar=ttk.LabelFrame(self.__ventana,text="Seleccione el IVA del producto").place(x=110,y=140)
        ttk.Label(self.__ventana,text='Seleccione tipo el iva del producto')
        ttk.Radiobutton(seleccionar,text="IVA 21%",value=0,variable=self.iva).place(x=130,y=180)
        ttk.Radiobutton(seleccionar,text="IVA 10.5%",value=1,variable=self.iva).place(x=130,y=220)
        
        ttk.Label(self.__ventana,text="Precio con IVA: ").place(x=100,y=260)
        ttk.Label(self.__ventana,textvariable=self.__precioiva).place(x=200,y=260)
        
        self.__ventana.mainloop()
        
    def calcular(self):
        valor=float(self.__preciobase.get())
        if self.iva.get()==0:
            iva21=valor*21/100
            self.__precioiva.set(valor+iva21)
        else:
            if self.iva.get()==1:
                iva10=valor*10.5/100
                self.__precioiva.set(valor+iva10)
def testapp():
    miapp=calculariva()

if __name__=='__main__':
    testapp()