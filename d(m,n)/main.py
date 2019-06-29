import time
from mem import *
from tab import *

print "Dynamic programming for the recurrence relationship:"
print "d(m,n) = 1 if m==0 or n==0 \nd(m,n) = d(m-1,n) + d(m-1,n-1) + d(m,n-1)"
print "Tabulation:"
start_time = time.clock()
tab_init()
print time.clock() - start_time, "seconds"
print "Memoization:"
start_time = time.clock()
mem_init()
print time.clock() - start_time, "seconds"
