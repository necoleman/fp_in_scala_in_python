##############################################################################
#
#	Chapter 2 exercises from *Functional Programming in Scala*
#
##############################################################################

# Exercise 2.1: Write a recursive function to get the nth Fibonacci number
def fib(n):
	if n < 1:
		return 0
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

# Exercise 2.2: Implement isSorted, which checks whether an Array is sorted
# according to a given comparison function
def isSorted(arr, ordered):
	if len(arr) == 1:
		return True
	elif len(arr) == 2:
		return ordered(arr[0],arr[1])
	else:
		return (ordered(arr[0],arr[1]) and isSorted(arr[2:],ordered))

# Exercise 2.3: Implement curry
def curry(f):
	return lambda x: (lambda y: f(x,y))

# Exercise 2.4: Implement uncurry
def uncurry(f):
	return lambda (x,y): f(x)(y)

# Exercise 2.5: Implement function composition
def compose(f,g):
	return lambda x: f(g(x))

##############################################################################
#	Tests
##############################################################################

# Test Ex 2.1
def test_fib():
	for j in range(15):
		print fib(j)

# Test Ex 2.2
def test_isSorted():
	def comparison(a,b):
		return a < b
	def nosirapmoc(a,b):
		return a > b
	print isSorted(range(25),comparison)
	print isSorted(range(25),nosirapmoc)

# Test Ex 2.3
def test_curry():
	def f(x,y):
		return x*y
	g = curry(f)
	print g(1)
	print g(2)
	for x in range(-5,5):
		print g(1)(x)
	for x in range(-5,5):
		print g(2)(x)

# Test Ex 2.4
def test_uncurry():
	def g(x):
		return lambda y: x+y
	f = uncurry(g)
	print f((2,3))

# Test Ex 2.5
def test_compose():
	def f(x):
		return x**2
	def g(x):
		return x+1
	h = compose(f,g)
	for t in range(-5,5):
		print h(t)

if __name__=='__main__':
	test_fib()
	test_isSorted()
	test_curry()
	test_uncurry()
	test_compose()
