from pelicula import Pelicula
from genero import Genero
from manejadorGeneros import ManejadorGeneros
from tkinter import *
from tkinter import ttk
class VentanaPelicula(object):
	"""docstring for VentanaPelicula"""
	def __init__(self,ventanaPadre,pelicula,generos):
		self.__ventanita=Toplevel()
		self.__ventanita.title(pelicula.nombre())
		self.__ventanita.geometry("300x300")
		self.__titulo=ttk.Label(self.__ventanita,text=f"Titulo: {pelicula.nombre()}")
		self.__titulo.grid(column=0,row=0)
		self.__descripcion_frame=ttk.LabelFrame(self.__ventanita,text="Descripcion")
		self.__descripcion_frame.grid(column=0,row=1)
		ttk.Label(self.__descripcion_frame,text=pelicula.descr(),wraplength=280).grid(column=0,row=0)
		self.__generos=ttk.LabelFrame(self.__ventanita,text="Generos")
		self.__generos.grid(column=0,row=2)
		for genero in pelicula.generos():
			ttk.Label(self.__generos,text=f"-{generos.genero(genero)}").pack(side="left")
		ttk.Label(self.__ventanita,text=f"Lanzamiento: {pelicula.fecha()}").grid(column=0,row=3)
		ttk.Label(self.__ventanita,text=f"Idioma: '{pelicula.idioma()}'").grid(column=0,row=4)
		self.__ventanita.transient(master=ventanaPadre)
		self.__ventanita.grab_set()
		ventanaPadre.wait_window(self.__ventanita)
		# self.__generos=ttk.LabelFrame(self.__ventanita)		