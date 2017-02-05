from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print "copying from %s to %s " % (fromfile, tofile)

infile = open(fromfile)
indata = infile.read()

print "the input file is %d bytes long." % len(indata)

print "does the output file exits ? %r" % exists (tofile)
print "ready, hit enter to contiune or CTRL - C to abort."
raw_input()

outfile = open(tofile, 'w')
outfile.write(indata)

print "allright ! all done."

outfile.close()
infile.close()