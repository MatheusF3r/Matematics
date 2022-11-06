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
			# *possui dois retornos, 
			# um simplificado e outro bruto
			# squareRootValid - resultado inteiro
			# n - valor inteiro
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
						return squareRootValid_,n
					else:
						return squareRootValid,n
					break
		else:
			return squareRoot


	def triangleType(valueA,valueB,valueC):
		''' # De acordo com os valores passados, 
		    # define o tipo do triangulo
			# parametros:
			# valueA - recebe um valor numerico
			# valueB - recebe um valor numerico
			# valueC - recebe um valor numerico
			# retorno:
			# return - Tipo do triangulo, em string
		'''
		if valueA == valueB == valueC:
			return "Triangulo equilatero"
		elif valueA != valueB and valueA != valueC and valueB != valueC:
			return "Triangulo escaleno"
		else:
			return "Triangulo isoceles"


	def pytagoras(valueA,valueB):
		pytagoras = valueA **2 + valueB **2
		pytagoras_ = pytagoras ** 0.5
		
		divisionPossibilites = [2,3,4,5,6,7,8,9]
		if not str(pytagoras_).endswith(".0"):
			for n in divisionPossibilites:
				if pytagoras % n == 0:
					squareRootValid = pytagoras / n
					squareRootValid_ = squareRootValid ** 0.5
					if str(squareRootValid_).endswith(".0"): 
						return squareRootValid_,n
						break
					else:
						return squareRootValid,n
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

values = (ab,bc,ca)
typeTriangle = Triangle.triangleType(values[0],values[1],values[2])

print("O triangulo é do tipo {} de acordo com as medidas ab {}, bc {}, ca {}".format(typeTriangle,ab,bc,ca))

print('O valor X do lado do triangulo é: {}'.format(Triangle.pytagoras(ca,bc)))


#print('Lado AB: {} \n Lado BC: {} \n LADO AC: {} \n'.format(ab,bc,ca))