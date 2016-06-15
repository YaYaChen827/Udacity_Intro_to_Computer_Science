import time

def time_execution(code):
	start = time.clock()
	#The eval function lets the python program to run python code.
	#The code format is string (ex: eval('print 1'))
	result = eval(code)
	#Get execution time
	run_time = time.clock()
	return result, run_time

#Testing time function
def spin_loop(n):
	i = 0
	while i < n:
		i += 1
