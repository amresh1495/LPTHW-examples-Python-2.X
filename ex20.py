# Demo of how functions and files can work together.

from sys import argv

script, inputfile = argv

def print_all(f):
	print f.read()  #------- reads the opened file

def rewind(f):
	f.seek(0)      #------- seek(0) brings the cursor at begining of a line 

def print_a_line(line_count, f):       #------ prints the line number and reads and prints that line 
    print line_count, f.readline()     #------ because of readline()

current_file = open(inputfile)     #------ opens the file which is to be read 

print "first let's print the whole file"
print_all(current_file)        #------- prints all contents of the current file

print "now let's rewind, kind of like a tape."
rewind(current_file)            #-------- calls seek(0) fn.

print "let's print three lines :"

current_line = 1               #------- prints the 1st line number and its contents
print_a_line(current_line, current_file)

current_line = current_line + 1         #------ prints 2nd line number and its contents
print_a_line(current_line, current_file)

current_line = current_line + 1       #------ prints 3rd line number and its contents
print_a_line(current_line, current_file)