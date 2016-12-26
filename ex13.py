# What is an argument? The last part of a command line.
# Write a script that also accepts arguments.

# "import" 相当于“导入”. "argv" is "argument variable", what is that? 
from sys import argv

# Take whatever is in argv, unpack it, and assign it to all of these variables in order. We print them out like normal.
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# "sys" is a module.
# "argv" is 
