def numprint1(a):
    i = 0
    numbers = []

    while i < a:
       print "At the top i is %d" % i
       numbers.append(i)
    
       i = i + 1
       print "Numbers now:", numbers
       print "At the bottom i is %d" % i
    
    print "The numbers:"

    for num in numbers:
       print num
        
    
def numprint2(a, b):
    i = 0
    numbers = []

    while i < a:
       print "At the top i is %d" % i
       numbers.append(i)

       i = i + b
       print "Numbers now:", numbers
       print "At the bottom i is %d" % i

    print "The numbers:"

    for num in numbers:
       print num
