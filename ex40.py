class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                  
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# for studydrills2
happy_bday1 = Song("Happy birthday to you")
happy_bday2 = Song("I don't want to get sued")

happy_bday1.sing_me_a_song()
happy_bady2.sing_me_a_song()
