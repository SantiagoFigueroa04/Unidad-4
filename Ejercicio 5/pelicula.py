class Pelicula(object):
	"""Pelicula (id, titulo,generos=[],lenguaje,descripcion,lanzamiento)"""
	def __init__(self, idPeli,titulo,generos,lenguaje,descripcion,lanzamiento):
		"""Pelicula (id, titulo,generos=[],lenguaje,descripcion,lanzamiento)"""
		self.__id=str(idPeli)
		self.__titulo=titulo
		self.__generos=generos
		self.__lenguaje=lenguaje
		self.__descripcion=descripcion
		self.__lanzamiento=lanzamiento
	def nombre(self):
		return self.__titulo
	def id(self):
		return self.__id
	def descr(self):
		return self.__descripcion
	def generos(self):
		return self.__generos
	def fecha(self):
		return self.__lanzamiento[8:10]+"/"+self.__lanzamiento[5:7]+"/"+self.__lanzamiento[0:4]
	def idioma(self):
		return self.__lenguaje