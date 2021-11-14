class Cubo:
    '''classe para calcula o cubo de um numero'''
    def __init__(self,valor):#método construtor da class
        self.x = valor
        print("Objeto criado !")
    
    def calcula_cubo(self):
        cubo = self.x * self.x * self.x
        return 'Cubo calculado: ' +  str(cubo)



texte = Cubo(6)
c = texte.calcula_cubo()
print(c)