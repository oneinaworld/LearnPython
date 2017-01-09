# The program is to calculate How many people we can drive today.

# The given number
cars=100
space_in_a_car=4.0
drivers=30
passengers=90

# Calculate fomular,to calculate to people we can drive.
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven

# To show the result
# At last we calculate how many people to take in a car.
print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."


# "average_passengers_per_car=car_pool_capacity/passenger" in line 13 to be a wrong fomula, I guess...we can't use a variable in a fomula?...
# To use 4.0 for space_in_a_car,I guess...is to make sure the result to be more accurate.
# I found I don't add space between operators...
