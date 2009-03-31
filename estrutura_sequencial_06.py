#encoding: latin1
#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math
class Circulo(object):
    def __init__(self):
        self.__raio = 0.00

    def get_raio(self):
        return self.__raio

    def set_raio(self, valor):
        if isinstance(valor, (float, int, long)):
            self.__raio = valor
        else:
            raise TypeError ("Raio deve ser um valor numérico")

    raio = property (get_raio, set_raio)
    
    def __str__(self):
        pi = math.pi
        return str( pi * pow(self.raio ,2) ) 
