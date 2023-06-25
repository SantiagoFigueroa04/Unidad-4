class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, peli_gene):
		self.__dato = peli_gene
		self.__sig = None
	def getSiguiente(self):
		return self.__sig
	def setSiguiente(self,nodo):
		self.__sig=nodo
	def dato(self):
		return self.__dato
		