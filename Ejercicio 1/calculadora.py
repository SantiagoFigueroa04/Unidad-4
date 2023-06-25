from tkinter import *
from tkinter import ttk

class calculador():
    __ventana = None
    __vestimentacantidad = None
    __vestimentabase = None
    __vestimentaactual = None
    __alimentoscantidad = None
    __alimentosbase = None
    __alimentosactual = None
    __educacionactual = None
    __educacionbase = None
    __educaciocantidad = None
    
    __total=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('800x400')
        self.__ventana.configure(background='light blue')
        self.__ventana.title('Calculadora de indec')

        self.__vestimentacantidad = StringVar()
        self.__vestimentabase = StringVar()
        self.__vestimentaactual = StringVar()
        self.__alimentoscantidad = StringVar()
        self.__alimentosbase = StringVar()
        self.__alimentosactual = StringVar()
        self.__educacionactual = StringVar()
        self.__educacionbase = StringVar()
        self.__educaciocantidad = StringVar()
        self.__total=StringVar()
        

        ttk.Button(self.__ventana, text='Salir', command=self.__ventana.destroy).place(x=345, y=266)
        ttk.Button(self.__ventana,text='Calcular',command=self.calcular).place(x=250,y=266)
        ttk.Label(self.__ventana, text='Item').place(x=67, y=80)
        ttk.Label(self.__ventana, text='Cantidad').place(x=150, y=80)
        ttk.Label(self.__ventana, text='Precio Año base').place(x=260, y=80)
        ttk.Label(self.__ventana, text='Precio Año actual').place(x=380, y=80)
        ttk.Label(self.__ventana, text='Vestimenta').place(x=58, y=130)
        ttk.Label(self.__ventana, text='Alimentos').place(x=58, y=170)
        ttk.Label(self.__ventana, text='Educacion').place(x=58, y=210)
    
        ttk.Entry(textvariable=self.__vestimentacantidad).place(x=150,y=130,width=80)
        ttk.Entry(textvariable=self.__vestimentabase).place(x=260,y=130,width=80)
        ttk.Entry(textvariable=self.__vestimentaactual).place(x=380,y=130,width=80)
        ttk.Entry(textvariable=self.__alimentosactual).place(x=150,y=170,width=80)
        ttk.Entry(textvariable=self.__alimentosbase).place(x=260,y=170,width=80)
        ttk.Entry(textvariable=self.__alimentoscantidad).place(x=380,y=170,width=80)
        ttk.Entry(textvariable=self.__educaciocantidad).place(x=150,y=210,width=80)
        ttk.Entry(textvariable=self.__educacionbase).place(x=260,y=210,width=80)
        ttk.Entry(textvariable=self.__educacionactual).place(x=380,y=210,width=80)
        
        ttk.Label(self.__ventana,text='El IPC es %').place(x=55,y=310)
        ttk.Label(self.__ventana,textvariable=self.__total).place(x=120,y=310)

        self.__ventana.mainloop()
    def calcular(self):
        try:
            vestimentacan = float(self.__vestimentacantidad.get())
            vestimentaba = float(self.__vestimentabase.get())
            vestimentaac = float(self.__vestimentaactual.get())
            alimentoscan = float(self.__alimentoscantidad.get())
            alimentosba = float(self.__alimentosbase.get())
            alimentosac = float(self.__alimentosactual.get())
            educacionact = float(self.__educacionactual.get())
            educacionba = float(self.__educacionbase.get())
            educaciocan = float(self.__educaciocantidad.get())
            
            
            vestimenta=float((vestimentacan*vestimentaba)/vestimentaac)
            alimentos=float((alimentoscan*alimentosba)/alimentosac)
            educacion=float((educaciocan*educacionba)/educacionact)
            
            
            totalipb=float((vestimenta+alimentos+educacion)%100)
            self.__total.set(totalipb)
        except ValueError:
            ttk.Label(self.__ventana,text='Error').place(x=120,y=310)

def testAPP():
    miapp = calculador()

if __name__ == '__main__':
    testAPP()