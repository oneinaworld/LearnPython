# escape sequences
print "I am 6'2\" tall."  # escape a double-quote inside a string
print 'I am 6\'2" tall.'  # escape a single-quote inside a string

tabby_cat = "\tI'm tabbed in."   # \t
persian_cat = "I'm split\non a line."   # \n
backslash_cat = "I'm \\a\\ cat."   # \\
fat_cat = """
I'll do a list:
\t*Cat food
\t*Fishies
\t*Catnip\n\t*Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

