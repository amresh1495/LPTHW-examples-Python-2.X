# program to show that a function can return some value.

def add(a, b):
	print "ADDING %d and %d " % (a, b)    #------- returns the sum of a and b
	return a + b

def subt(a, b):
	print "SUBTRACTING %d and %d " % (a, b)   #------- returns the difference of and b
	return a - b

def mult(a, b):                
	print "MULTIPLYING %d and %d " % (a, b)    #------- returns the product of and b
	return a * b

def div(a, b):
	print "DIVIDING %d BY %d" % (a, b)     #------- returns the quotient of and b
	return a / b

age = add(30, 5)
height = subt(78, 4)  
weight = mult(90, 2)
iq = div(100, 2)

print ""
print "Age : %d, Height : %d, Weight : %d, IQ : %d" % (age, height, weight, iq)
print ""

# a puzzle 

what = add(age, subt(height, mult(weight,div(iq, 2))))

print "That becomes : ", what, ".Can you do it by hand ?"
