# I like the statement of this lesson so I copy it here:
# "This shows all the different ways we're able to give our function the values it needs to print them. 
# "We can give it straight numbers. We can give it variables. We can give it math. We can combine math and variables.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "you have %d boxes of crackers!" %boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
 
print "And we can combine the two, varibles and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)




# I'll write a function of my own.
def buy(price_of_cloth, price_of_shoes):
    print "The price of clothe is %s!" % price_of_cloth
    print "The price of shoes is %s!" % price_of_shoes
    print "So that's too much! I won't buy!"

price_of_cloth = raw_input("What's the price of cloth?")
price_of_shoes = raw_input("What's the price of shoes?")

buy(price_of_cloth, price_of_shoes)
