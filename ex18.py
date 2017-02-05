# Introduces the concept of functions. 
# Demonstrates the methods / ways of passing arguements in functions.

def print_two(*args):    #------ header of the function. Takes 2 arguments
	arg1, arg2 = args
	print "arg1 : %r, arg2 : %r" % (arg1, arg2)

def print_two_again(arg1, arg2):   #------- takes 2 argumets
	print "arg1 : %r, arg2 : %r" % (arg1, arg2)

def print_one(arg):     #-------- takes 1 argument 
	print "arg : %r" % arg

def print_nothing():    #------- takes no argument
	print "I've got nothing."

print_two("Amresh", "Giri")        #------- function called. Two string arguments passed separated by a comma
print_two_again("Amresh", "Giri")  #------- same as above
print_one("Amresh")                #------- only 1 string argument passed
print_nothing()                    #------- no argument passed. Hence prints nothing

