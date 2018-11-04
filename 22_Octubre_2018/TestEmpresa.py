import unittest
import Empresa
class TestEmpresaMethods(unittest.TestCase):

	def test_agregarEmpleados(self):
		empresa=Empresa.Empresa()
		empresa.agregarEmpleados(10)
		self.assertEqual(empresa.NumeroEmpleados, 11)

if __name__ == '__main__':
    unittest.main()