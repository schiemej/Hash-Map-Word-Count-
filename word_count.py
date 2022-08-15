# Author Jacob Schiemenz
# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

# Regular expression used to capture words from the document. 
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """
    keys = set()
    ht = HashMap(2500,hash_function_2)
    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    from hash_map import hash_function_1
    final_list=[]
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                #set all words to lower to avoid miscounts
                w=w.lower()
                key = w
                hash_key=ht._hash_function(w)%ht.capacity
                #if key is in map, update value to +=1
                if ht.contains_key(w)==True:
                    while ht._buckets[hash_key].head.key != key:
                        ht._buckets[hash_key].head = ht._buckets[hash_key].head.next
                    ht._buckets[hash_key].head.value+=1
                #else place key in map with value of one
                else:
                    ht.put(w,1)
    for i in ht._buckets:
        if i.head==None:
            pass
        else:
            #append values in tuple format to final list
            while i.head is not None:
                final_list.append((i.head.key, i.head.value))
                i.head=i.head.next
    #sorts list by greatest to least and returns the number of elements the user requests
    final_list.sort(key=lambda x:x[1],reverse=True)
    return final_list[:number]

#example of how program should be used
print(top_words("alice.txt",10))
