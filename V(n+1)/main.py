import time
from mem import *
from tab import *

print "Dynamic programming for the recurrence relationship:"
print "V(1) = 1 otherwise V(n+1) = 1 + V(n+1-V(V(n)))"
print "Tabulation:"
start_time = time.clock()
tab_init()
print time.clock() - start_time, "seconds"
print "Memoization:"
start_time = time.clock()
mem_init()
print time.clock() - start_time, "seconds"
