class Imaginario:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return f"{self.real} + {self.imaginario}i"

    def __add__(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return Imaginario(real, imaginario)

    def __sub__(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return Imaginario(real, imaginario)

    def __mul__(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return Imaginario(real, imaginario)

    def __truediv__(self, otro):
        denominador = otro.real**2 + otro.imaginario**2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return Imaginario(real, imaginario)
