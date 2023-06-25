import requests


class valordolar():
    __valordolaroficial=''
    __valordolarblue=''
    def __init__(self):
        self.__valordolaroficial=None
        self.__valordolarblue=None
    
    def traerapi(self):
        response = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')

        if response.status_code == 200:
            # Procesar los datos de la respuesta
            data = response.json()
            self.__valordolaroficial=float(data[0]['casa']['venta'].replace(',','.'))
            self.__valordolarblue=float(data[1]['casa']['venta'].replace(',','.'))
        else:
            # Manejar errores de solicitud
            print('Error en la solicitud. Código de estado:', response.status_code)
    def oficial(self):
        return self.__valordolaroficial
    def blue(self):
        return self.__valordolarblue
    
    
if __name__=='__main__':
     traer=valordolar()
     traer.traerapi()