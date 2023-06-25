import constantes
import requests
from genero import Genero
from pelicula import Pelicula
from manejadorGeneros import ManejadorGeneros
from manejadorPeliculas import ManejadorPeliculas
from tkinter import *
from tkinter import ttk
from ventana import Ventana


if __name__ == '__main__':
	pelis=ManejadorPeliculas()
	pelis.cargar()
	generos=ManejadorGeneros()
	generos.cargar()
	a=Ventana(pelis,generos)
