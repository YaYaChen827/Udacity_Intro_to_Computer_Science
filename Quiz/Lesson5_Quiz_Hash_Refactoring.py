# 6. In video 28. Update, it was suggested that some of the duplicate code in
# lookup and update could be avoided by a better design.  We can do this by
# defining a procedure that finds the entry corresponding to a given key, and
# using that in both lookup and update.

# Here are the original procedures:
# I will be raising two functions including 
# hashtable_update and hashtable_lookup. Adding bucket_find function

# Because these two function have the same operative expression (for loop and if)
# So, rewriting to other function
def bucket_find(bucket,key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

def hashtable_update(htable, key, value):
    # List Version
    #bucket = hashtable_get_bucket(htable, key)
    #for entry in bucket:
    #    if entry[0] == key:
    #        entry[1] = value
    #        return
    #bucket.append([key, value])

    # Submit Version
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket,key)
    if entry:
        bucket.append([key, value])
    else:
        entry[1] = value


def hashtable_lookup(htable, key):
    # List Version
    #bucket = hashtable_get_bucket(htable, key)
    #for entry in bucket:
    #    if entry[0] == key:
    #        return entry[1]
    #return None

    # Submit Version
    entry = bucket_find(hashtable_get_bucket(htable,key),key)
    if entry:
        return entry[1]
    else:
        return None
# ***IMPORTANT*** List in first level, Dictionary in second
# ex: [{}, {}, {}, ...] we can convenient set and get keys/values  
def make_hashtable(size):
    table = []
    for unused in range(0, size):
        table.append([])
    return table

def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

# Testing
table = make_hashtable(10)
print table
#>>> [{}, {}, {'Python': 'Guido van Rossum'}, {}, {}, 
#>>> {'JavaScript': 'Brendan Eich'}, {}, {}, {'CLU': 'Barbara Liskov'}, {}]

hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print table
print hashtable_lookup(table, 'Python')
#>>> Guido van Rossum 

#================================================================================================
# This is my idea from List and Dictionary concept.
# ***IMPORTANT*** List in first level, Dictionary in second
# ex: [{}, {}, {}, ...] we can convenient set and get keys/values

#def make_hashtable(size):
#    table = []
#    for unused in range(0, size):
#        table.append({})
#    return table

#def hashtable_update(htable, key, value):
#    bucket = hashtable_get_bucket(htable, key)
#    bucket[key] = value

#def hashtable_lookup(htable,key):
#    return hashtable_get_bucket(htable, key)[key]

#def hash_string(s, size):
#    h = 0
#    for c in s:
#         h = h + ord(c)
#    return h % size

#def hashtable_get_bucket(htable, key):
#    return htable[hash_string(key, len(htable))]

# Testing
#table = make_hashtable(10)
#hashtable_update(table, 'Python', 'Monty')
#hashtable_update(table, 'CLU', 'Barbara Liskov')
#hashtable_update(table, 'JavaScript', 'Brendan Eich')
#hashtable_update(table, 'Python', 'Guido van Rossum')

#print table
#>>> [{}, {}, {'Python': 'Guido van Rossum'}, {}, {}, 
#>>> {'JavaScript': 'Brendan Eich'}, {}, {}, {'CLU': 'Barbara Liskov'}, {}]

#print hashtable_lookup(table, 'Python')
#>>> Guido van Rossum 