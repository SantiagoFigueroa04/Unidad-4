import requests
import constantes
from genero import Genero
class ManejadorGeneros(object):
	def __init__(self):
		self.__lista = []
	def cargar(self):
		ap=requests.get(constantes.URL_G,headers=constantes.HEADERS)
		ap=ap.json()
		res=ap["genres"]
		for gen in res:
			self.__lista.append(Genero(gen["id"],gen["name"]))
	def genero(self,id_):
		i=0
		while i<len(self.__lista):
			if self.__lista[i].id()==id_:
				return self.__lista[i].nombre()
			i+=1
		


