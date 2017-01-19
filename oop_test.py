# -*- coding:utf-8 -*-
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []    # 建立WORDS空list

# 建立字典PHRASES
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
# argv是从哪里来的？？
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
  
# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())    # strip函数，移除word头尾指定字符，此处移除空格。
    

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]  #   
    """random模块。
    random.sample  从WORD中随机获得snippet.count个元素且不改变WORD。
    
    capitalize函数。
    返回w的一个副本，只有第一个字母大写。
    
    count函数。
    在snippet中搜索%%%出现的次数。
    """
    other_names = random.sample(WORDS, snippet.count("***"))    # 
    results = []
    param_names = []  
    
    for i in range(0, snippet.count("@@@")):   # 在snippet的个数范围内
        param_count = random.randint(1,3)  #random.randint，在1-3范围内生成随机整数。
        param_names.append(','.join(random.sample(WORDS, param_count)))  #扩充param_names列表。用从WORDS列表中的获取元素并且用“，”连接的。
        
    for sentence in snippet, phrase:
        result = sentence[:]
        
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)  # replace函数。把%%%替换为word，不超过1次。
            
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
            
        # fake parameter listes
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)
        
    return results
        

# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()  # keys函数，返回字典所有的key。
        random.shuffle(snippets)  # random.shuffle，把snippets列表中的元素打乱更新。
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            
            print question
            
            raw_input("> ")
            print "ANSWER:   %s\n\n" % answer
except EOFError:
     print "\nBye"
