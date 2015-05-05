# -*- coding: latin-1 -*-
"""
Breakout solution for Data Structures.

There are many ways you can achieve this. Here is one:
"""

ignore = {'la','à','et','le','les','des','un','du','en','que','dans','se',
          'il', 'une', 'ne', 'qui', 'au', 'pas', 'son', 'par',
          'plus', 'pour',
          'ce', 'sur', 'cette', 'avec','de','\xc3\xa0'}

punctuation="[]_.?!,;'\"-=«" # a string with some punctuation
                             # characters to remove later

with open( "verne-de_la_terre_a_la_lune.txt" ) as infile:
    lines = infile.readlines()

    
word_frequency = {}
numwords = 0

for line in lines:

    # to be really correct, we should make all one case and remove
    # punctuation. Here is one way to do that using
    # str.translate(table,remove), but there are many ways
    line = line.lower()
    for character in punctuation:
        line=line.replace( character,"" )
    # can also use line.translate(None,punctuation)

    for word in line.lower().split():
        numwords += 1
        if word not in ignore:
            if word not in word_frequency:
                word_frequency[word] = 0
            word_frequency[word] += 1

# now make it a list so we can sort it (dictionaries cannot be sorted
# directly)
freq_and_word_list =  zip(word_frequency.values(),word_frequency.keys())
freq_and_word_list.sort( reverse=True )

print "The total number of lines is: ",len(lines)
print "The total number of words is:",numwords
print "The total number of distinct words is: ", len(word_frequency)

print "THE TOP 20 WORDS"
for count,word in freq_and_word_list[:20]:
    print "{0:>15s} : {1:5d} times".format(word, count)

