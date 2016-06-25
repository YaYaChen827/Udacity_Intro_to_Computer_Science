# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(lst):
	# This is my idea, it can change the p, q list value
#	reverse_lst = lst
#	reverse_lst.reverse()
#	result = []
#	for i in reverse_lst:
#		if is_list(i):	
#			result.append(deep_reverse(i))
#		else:			
#			result.append(i)
#	return lst

	# Submit code
	if is_list(lst):
		result = []
		# The range expression format range([start],stop,[step])
		# So, we count reversing lst from max index (length - 1) to zero which step equal -1 
		for element in range(len(lst)-1,-1,-1):
			result.append(deep_reverse(lst[element]))
		return result
	return lst

#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]

r = [1,2,3,4]
print deep_reverse(r)