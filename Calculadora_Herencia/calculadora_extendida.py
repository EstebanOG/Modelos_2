from calculadora import Calculadora

class CalculadoraExtendida(Calculadora):
    
    def sumar(self):
        self.resultado = self.valor1 + self.valor2
    
    def restar(self):
        self.resultado = self.valor1 - self.valor2
    
    def multiplica(self):
        self.resultado = self.valor1 * self.valor2