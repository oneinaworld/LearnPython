# This is the exercise to "strings".
my_name = 'Zed A.Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "If I add %d, %d, and %d, I get %d."%(my_age, my_height, my_weight, my_age + my_height + my_weight)

# So %s is for string.%d is for integer.
# So %s and %d stand for the %.
# "%s,%d," have space between % and s?...Yes.
# Space can be everywhere.


# This is to change the variables so there is no my_ in front of them.
name = 'Zed A.Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d, and %d, I get %d."% (age, height, weight, age + height + weight)


# This program is to convert inches and pounds to centimeter and kilogram.
centimeter = 0.3937*my_height
kilogram = 0.4535*my_weight
print "My height is %s. " % centimeter   #No , here!
print "My weight is %s." % kilogram


# format characters
