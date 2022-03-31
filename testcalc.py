from unittest import TestCase, main
from calculadora import Calculadora

class Testes(TestCase):
    def test_sum(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(9,10,'soma')
        self.assertEqual(resultado, 19)
    
    def test_sub(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(20, 19, 'subtracao')
        self.assertEqual(resultado, 1)
    
    def test_divisao(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(25,5, 'divisao')
        self.assertEqual(resultado, 5)
    
    def test_mult(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(10, 100, 'multiplicacao')
        self.assertEqual(resultado, 1000)

if __name__ == '__main__':

    main()