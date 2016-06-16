# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
	hashtable = []
	for i in range(0, nbuckets):
		hashtable.append([])
	return hashtable

#Testing right make_hashtable
print make_hashtable(3)
#>>> [[], [], []]
table = make_hashtable(3)
table[0].append(['Udacity',['https://www.udacity.com']])
print table[0]
#>>> [['Udacity', ['https://www.udacity.com']]]
print table[1]
#>>> []



#In this course, doc says the wrong function(make_hashtable_NOT)

def make_hashtalbe_NOT(nbuckets):
	return [[]]*nbuckets

#Testing the wrong function
print make_hashtalbe_NOT(3)
#>>> [[]]
table = make_hashtalbe_NOT(3)
table[0].append(['Udacity',['https://www.udacity.com']])
print table[0]
#>>> [['Udacity', ['https://www.udacity.com']]]
print table[1]
#>>> [['Udacity', ['https://www.udacity.com']]]

#That is tricky function, I think a logical mistake on this way.
#If you use [[]]*buckets and then set a value to any element which equal set all element.