class Mathematics:

	def __init__(self,a=(int(),int()),b=(int(),int()),c=(int(),int())):
		self.a = a
		self.b = b
		self.c = c


	def squareRootValid(value):
	    squareRoot = value ** 0.5
	    divisionPossibilites = [2,3,4,5,6,7,8,9]
	    if not str(squareRoot).endswith(".0"):
	        for n in divisionPossibilites:
	            if value % n == 0:
	                squareRootValid = value / n
	                squareRootValid_ = squareRootValid ** 0.5
	                if str(squareRootValid_).endswith(".0"):
	                	return squareRootValid_,n
	                else:
	                	return squareRootValid, n
	                break
	            else:
	                None
	    else:
	        return squareRoot
	        