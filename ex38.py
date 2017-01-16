# -*- coding:utf-8 -*-

"""第38课的笔记
mystuff.sppend('hello') 即被翻译为 append(mystuff, 'hello')
"""

# ten_things 不是一个list 
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# 对ten_things进行切片
stuff = ten_things.split(' ')
# 引入另一个list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# 当stuff的length小于10时
while len(stuff) != 10:
    # 从more_stuff中拿出一个元素。为空则为-1，即最后一个元素。
    next_one = more_stuff.pop()    
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)
    
print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]    # 打印最后一个元素
print stuff.pop()   # 拿出最后一个元素
print ''.join(stuff)    #
print '#'.join(stuff[3:5])
