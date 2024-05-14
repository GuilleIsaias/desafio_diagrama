class Alternativas():

    def __init__(self, contenido: str, ayuda: str):
        self.contenido = contenido
        self.ayuda = ayuda

    @property
    def get_contenido(self):
        return self.contenido 
    
    @property
    def get_ayuda(self):
        return self.contenido
    

    @get_contenido.setter
    def set_contenido(self, contenido):
        self.set_contenido = contenido

    @get_ayuda.setter
    def set_ayuda(self, ayuda):
        self.set_ayuda = ayuda
  