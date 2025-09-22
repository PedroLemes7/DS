class Forma:
    def __init__(self,nome):
        self.nome = nome 


    def calcula_area(self):
        raise NotImplementedError("o método deve ser implementado em subclasse")

    def calcula_perimetro(self):
        raise NotImplementedError

    def calcula_parimetro(self):
        raise NotImplementedError("o método deve ser implementado em subclasse")


    def __str__ (self): 
       return f"Nome da Forma: {self.nome}"