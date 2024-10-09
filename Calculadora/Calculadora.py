import math

class Calc():

    def __init__(self):    
        pass;

    def soma(valor1,valor2):
        return valor1 + valor2;
    
    def sub(valor1,valor2):
        return valor1 - valor2;

    def mult(valor1,valor2):
        return valor1 * valor2;

    def div(valor1,valor2):
        if(valor1 and valor2):
            return valor1/valor2
        else:
            return "fudeu"
    
    def pot(valor1,valor2):
        return valor1**valor2
    
    def raiz(valor1):
        return math.sqrt(valor1)
