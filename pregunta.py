from alternativa import Alternativas
from abc import ABC, abstractmethod

class Preguntas():
    def __init__(self, enunciado: str, ayuda: str):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = bool
        self.lista_alternativas = Alternativas()

    @property
    def get_enunciado(self):
        return self.enunciado 
    
    @property
    def get_ayuda(self):
        return self.ayuda
    
    @property
    def get_requerida(self):
        return self.requerida
    
    @get_enunciado.setter
    def set_enunciado(self, enunciado):
        self.enunciado = enunciado

    @get_ayuda.setter
    def set_ayuda(self, ayuda):
        self.ayuda = ayuda

    def mostrar_pregunta(self):


        