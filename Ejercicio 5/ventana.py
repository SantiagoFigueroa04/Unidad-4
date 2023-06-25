import tkinter as tk
from tkinter import ttk
from functools import partial
from ventanaPelicula import VentanaPelicula
class Ventana(object):
	"""docstring for Ventana"""
	def __init__(self,peliculas,generos):
		self.__ventana = tk.Tk()
		opts = { 'ipadx': 10, 'ipady': 10, 'fill': tk.BOTH}
		self.__ventana.title("Visor de peliculones")
		self.__ventana.geometry("300x300")
		self.__mainframe=ttk.Frame(self.__ventana,padding="3 3 12 12")
		self.__mainframe.pack(side="top")
		self.__lista=tk.Listbox(self.__mainframe)
		self.__lista.configure(width=200,height=150)
		scroll = tk.Scrollbar(self.__mainframe, command=self.__lista.yview)
		self.__lista.config(yscrollcommand=scroll.set)
		scroll.pack(side=tk.RIGHT, fill=tk.Y)
		self.__lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
		self.__lista.pack(side="top",fill="x")
		self.__lista.bind("<Double-Button-1>",partial(self.bind_pelicula,peliculas,generos))
		# self.__lista.bind("<<ListboxSelect>>",partial(self.bind_pelicula,peliculas,generos))
		self.cargarLista(peliculas,generos)
		self.__ventana.mainloop()
	def abrir(self,*args):
		self.__dialogo=tk.Toplevel()
		self.__dialogo.geometry("200x200+15+15")
	def cargarLista(self,peliculas,generos):
		self.__pelis_ids={}
		for peli in peliculas:
			# print(peli.id(),peli.nombre())
			self.__lista.insert(tk.END,peli.nombre())
			self.__pelis_ids[self.__lista.size()-1]=peli.id()
	def bind_pelicula(self,peliculas,generos,*args):
		id_peli=self.__pelis_ids[self.__lista.curselection()[0]]
		pelicula=VentanaPelicula(self.__ventana,peliculas.pelicula(id_peli),generos)

if __name__ == '__main__':
	a=Ventana()
	a.abrir()
	