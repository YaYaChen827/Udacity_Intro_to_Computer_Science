# Define a procedure,

# hashtable_lookup(htable,key)

# that takes two inputs, a hashtable
# and a key (string),
# and returns the value associated
# with that key.

def hashtable_lookup(htable,key):
    # Finding bucket by following function(get module)
    bucket = hashtable_get_bucket(htable, key)

    # Using the bucket(htable[x], x = 0~len(htable) in htable to find key
    for word in bucket:
        if word[0] == key:
            return word[1]
    return None
    
def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

# Testing1
table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtable_lookup(table, 'Francis')
#>>> 13

print hashtable_lookup(table, 'Louis')
#>>> 29

print hashtable_lookup(table, 'Zoe')
#>>> 14

# Testing2
table2 = [[['search', 'verb']], [], [['Peter', 'proper noun']], 
[['Udacity', 'super noun']], [['with', 'preposition']]]

print hashtable_lookup(table2, 'Udacity')
#>>> super noun