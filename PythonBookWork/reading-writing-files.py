from sys import argv

from pip._vendor.distlib.compat import raw_input

script, filename = argv

print("we are going to erase %r" % filename)
target = open(filename,'w')
print("Truncating the file")
target.truncate()

print("Now I am going to ask you for 3 lines of text")
line1 = raw_input('Line 1:')
line2 = raw_input('Line 2:')
line3 = raw_input('Line 3:')

print("Writing these to a file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Done now closing")
target.close()





