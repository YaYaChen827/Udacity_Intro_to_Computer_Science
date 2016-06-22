#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

# It's using the left shift concept.
def fibonacci(n):
	current = 0
	after = 1
	for i in range(0, n):
		current, after = after, current + after
		# 0,1 => 1,1 => 1,2 => 2,3 => 3,5 ...
	return current

# Testing
print fibonacci(36)
#>>> 14930352
print fibonacci(60)
#>>> 1548008755920