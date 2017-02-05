# This example demonstrates copying in Python.
# Two files are opened and contents of one file is copied into another.
# File from which the content is to be copied = fromfile
# File where the content is to be copied = tofile

from sys import argv
from os.path import exists

script, fromfile, tofile = argv   

print "copying from %s to %s " % (fromfile, tofile)       

infile = open(fromfile)    # ------------ opening the fromfile 
indata = infile.read()     # ------------ reading the contents of the fromfile

print "the input file is %d bytes long." % len(indata)    #--------- calculating the size of the file in bytes

print "does the output file exits ? %r" % exists (tofile)    #--------- checking whether tofile exists or not
print "ready, hit enter to contiune or CTRL - C to abort."
raw_input()

outfile = open(tofile, 'w')    #--------- opening the tofile. w means opening the file in writing mode
outfile.write(indata)          #--------- writing the data from fromfile to tofile using write()

print "allright ! all done."

outfile.close()    #-------- closing fromfile using close()
infile.close()     #-------- closing tofile using close()