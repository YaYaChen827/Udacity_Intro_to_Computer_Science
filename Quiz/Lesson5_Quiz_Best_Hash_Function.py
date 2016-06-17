# Define a function, hash_string,that takes as inputs a keyword
# (string) and a number of buckets, and returns a number representing
# the bucket for that keyword.
# We can use the % operator to know the keyword's address in buckets.
# Note that the buckets number

def hash_string(keyword,buckets):
    temp = 0
    for word in keyword:
    	#ord(<one letter string>) get string number
    	#ex: ord('a') == 97
        temp = (temp + ord(word))%buckets
    return temp

#Testing
print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('Udacity',14)
#>>> 9

print hash_string('abcdefghijklmnop', 80)
#>>> 72

print hash_string('searchwithpeter.info',73)
#>>> 48

print hash_string('udacity',12)
#>>> 11
