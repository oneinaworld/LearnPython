formatter = "%r %r %r %r"

print formatter %(1,2,3,4)      # result is "1,2,3,4"   # No ""! Why!
print formatter %("one", "two", "three", "four")  # result is 'one', 'two', 'three', 'four'
print formatter %(True, False, False, True)  # result is "True False False True"  # No ""!
print formatter %(formatter, formatter, formatter, formatter)   # result is 
print formatter %(
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
)
# After the exercise, I found the rule.
# We had double quatation mark to be single marks, and keep to be no quatation mark.

