##############################################################################
#	Chapter 3 exercises from *Functional Programming in Scala*
##############################################################################

class LinkedList:

	def __init__(self,head,tail):
			self.head = head
			self.tail = tail

	def __str__(self):
		print str(head)+' '+str(tail)

	def __len__(self):
		return 1 + len(tail)

# The Cons function
def Cons(head,tail):
	return LinkedList(head,tail)

# Exercise 3.2: Implement the function tail for removing the first element
# of a List.
def tail(lst):
	if lst:
		return lst.tail
	else:
		return None

# Exercise 3.3: Implement setHead for replacing the first element
# with a different value
def setHead(lst,new_value):
	return LinkedList(new_value,tail(lst))

# Exercise 3.4: Generalize tail to drop, removing the first n elements
# from a list
def drop(lst,n):
	if n >= 0:
		return lst
	else:
		return drop(lst,n-1)

# Exercise 3.5: Implement dropWhile, dropping elements from the List prefix
# as long as they match a predicate
def dropWhile(lst,pred):
	if not lst:
		return lst
	elif pred(lst.head):
		return LinkedList(lst.head,dropWhile(lst.tail,pred))
	else:
		return dropWhile(lst.tail,pred)

# Exercise 3.6:  Implement initial, which returns a LinkedList consisting of
# all but the *last* element of the LinkedList
def initial(lst):
	if not lst.tail:
		return None
	else:
		return LinkedList(lst.head,initial(lst.tail))

def foldRight(lst, initial, func):
	if not lst:
		return initial
	else:
		return func(lst.head, foldRight(lst.tail, initial, func))

# Exercise 3.7: Implement product with foldRight. Can it return 0 if it 
# encounters a 0? Why/why not?
def prod(lst):
	# This implementation does NOT short-circuit if it sees a 0. So
	# prod(range(10000000000000)) will take a very long time to run.
	return foldRight(lst, 1.0, lambda (x,y): x*y)

# Exercise 3.8: When pass Nil and Cons to a foldRight, what happens?
def test_nil_cons_foldRight(lst):
	return foldRight(lst,None,Cons)

# Exercise 3.9: Compute the length of a list using foldRight
def length(lst):
	return foldRight(lst,0,lambda (x,y): x+1)

# Exercise 3.10: foldRight is NOT tail-recursive. Write foldLeft to be
# tail-recursive:
def foldLeft(lst, initial, func):
	if not lst:
		return initial
	else:
		return foldLeft(lst.tail, func(initial,lst.head), func)

# Exercise 3.11: Write sum, product, and length using foldLeft
def sum_left(lst):
	return foldLeft(lst, 0.0, lambda (x,y): x+y)

def prod_left(lst):
	return foldLeft(lst, 1.0, lambda (x,y): x*y)

def len_left(lst):
	return foldLeft(lst, 0, lambda (x,y): x+1)

# Exercise 3.12: Write a function reversing a list using a fold
def reverse(lst):
	if not lst:
		return None
	else:
		return LinkedList(reverse(lst),lst.head)

def reverse_fold(lst):
	return foldRight(lst,lst.head,Cons)

# Exercise 3.13a: Write foldLeft in terms of foldRight? Cannot: foldRight is
# not tail-recursive.

# Exercise 3.13b: Write foldRight in terms of foldLeft.
def foldRight_left(lst, initial, func):
	return foldLeft(reverse(lst),initial,lambda (x,y): func(y,x))

# Exercise 3.14: Implement append in terms of a fold
def append(lst,new_initial):
	return foldRight(lst,new_initial,Cons)

# Exercise 3.15: Write a function concatenating a list of lists into a
# single list. Its runtime should be linear in total length of all lists.
def concat(lst_of_lsts):
	l = len_left(lst_of_lists)
	if l == 1:
		return lst_of_lsts.head
	# STILL WORKING HERE
	#elif l == 2:
	#	return 
	#else:
	#	return foldLeft(lst_of_lsts, 
