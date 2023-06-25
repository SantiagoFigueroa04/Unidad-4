import requests
import constantes
from nodo import Nodo
from pelicula import Pelicula



class ManejadorPeliculas(object):
	def __init__(self):
		self.__comienzo = None 
		self.__actual= None
		self.__indice = 0
		self.__tope = 0
	def cargar(self):
		ap=requests.get(f"{constantes.URL_P}{constantes.API_KEY}")
		ap=ap.json()
		res=ap["results"]
		for peli in res:
			self.agregar(Pelicula(peli["id"],peli["title"],peli["genre_ids"],peli["original_language"],peli["overview"],peli["release_date"]))
	def agregar(self,pelicula):
		nodo=Nodo(pelicula)
		nodo.setSiguiente(self.__comienzo)
		self.__comienzo=nodo
		self.__actual=nodo
		self.__tope+=1
	def __iter__(self):
		return self
	def __next__(self):
		if self.__indice==self.__tope:
			self.__actual=self.__comienzo
			self.__indice=0
			raise StopIteration
		else:
			self.__indice+=1
			dato = self.__actual.dato()
			self.__actual=self.__actual.getSiguiente()
			return dato
		# Pelicula(res["id"],res["title"],res["genre_ids"],res["original_language"],res["overview"],res["release-date"]))
	def pelicula(self,id_):
		id_=str(id_)
		aux=self.__comienzo
		while aux!=None:
			peli=aux.dato()
			if peli.id()==id_:
				return peli
			aux=aux.getSiguiente()
		

if __name__ == '__main__':
	a=ManejadorPeliculas()
	a.cargar()