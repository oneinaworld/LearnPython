def gold_room():
    print "This room is full of gold. How much do you take?"
    
    choice = raw_input("Input a number:")

    how_much = int(choice)
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
