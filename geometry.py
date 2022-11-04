class Triangle:
	def __init__(self,a=(int(),int()),b=(int(),int()),c=(int(),int())):
		self.a = a
		self.b = b
		self.c = c

	def calcusSide(value,value_):
		''' # Calcula o lado de um triangulo
			# parametros:
			# value - recebe valor 1º
			# value_ - recebe valor 2º
			# retorno:
			# return - 
		'''
		side = (value_[0]-value[0])**2 + (value_[1]-value[1])**2
		squareRoot = side ** 0.5
		divisionPossibilites = [2,3,4,5,6,7,8,9]
		if not str(squareRoot).endswith(".0"):
			for n in divisionPossibilites:
				if side % n == 0:
					squareRootValid = side / n
					squareRootValid_ = squareRootValid ** 0.5
					if str(squareRootValid_).endswith(".0"):
						return squareRootValid_, n
					else:
						return squareRootValid, n
					break
		else:
			return squareRoot



a = (2,2)
b = (-4,-6)
c = (4,-12)
triangle = Triangle(a,b,c)
ab = Triangle.calcusSide(a,b) # 10
bc = Triangle.calcusSide(b,c) # 10
ca = Triangle.calcusSide(c,a) # Raiz quadrada de 200 = raiz de 100 * 2 = 10 raiz de 2

print('Lado AB: {} \n Lado BC: {} \n LADO AC: {} \n'.format(ab,bc,ca))

