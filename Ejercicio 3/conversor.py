from tkinter import *
from tkinter import ttk
from api import valordolar

class conversor:
    __ventana=None
    __peso=None
    __dolares=None
    __preciodolar=None
    
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry('300x300')
        self.__ventana.title("CONVERSOR")
        
        self.__dolares=DoubleVar()
        self.__peso=DoubleVar()
        self.tipo=DoubleVar()
        self.__preciodolar=DoubleVar()
        api=valordolar()
        api.traerapi()
        
        dolar=ttk.LabelFrame(self.__ventana,text='Seleccionar tipo dolar').place(x=40,y=20)
        ttk.Label(self.__ventana,text='Seleccione tipo dolar').place(x=40,y=20)
        ttk.Radiobutton(dolar,text="Dolar Oficial",value=0,variable=self.tipo,command=self.cambiardolar).place(x=40,y=50)
        ttk.Radiobutton(dolar,text='Dolar Blue',value=1,variable=self.tipo,command=self.cambiardolar).place(x=40,y=80)
        
        self.__dolares.trace('w',self.calcular)
        ttk.Entry(self.__ventana,textvariable=self.__dolares).place(x=120,y=130,width=50)
        ttk.Label(self.__ventana,text='Dolares').place(x=190,y=130)
        
        
        
        ttk.Label(self.__ventana,text="Es equivalente a: ").place(x=10,y=170)
        ttk.Label(self.__ventana,textvariable=self.__peso).place(x=120,y=170)
        ttk.Label(self.__ventana,text='Pesos').place(x=190,y=170)
        
        ttk.Button(self.__ventana,text="Salir",command=self.__ventana.destroy).place(x=210,y=260)
        
        self.__ventana.mainloop()
    def calcular(self,*args):
        precio=float(self.__preciodolar.get())
        valor=float(self.__dolares.get())
        self.__peso.set(valor*precio)
    
    def cambiardolar(self):
        api=valordolar()
        api.traerapi()
        if self.tipo.get() == 0:
            self.__preciodolar.set(api.oficial())
        if self.tipo.get() == 1:
            self.__preciodolar.set(api.blue())

def testapp():
    app=conversor()
    
if __name__=='__main__':
    testapp()