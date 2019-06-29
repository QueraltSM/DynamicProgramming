import time
from mem import *
from tab import *

print "Dynamic programming for the recurrence relationship:"
print "V(1) = V(2) = 1 otherwise V(n) = V (V (n-1)) + V(n – V(n-1))"
print "Tabulation:"
start_time = time.clock()
tab_init()
print time.clock() - start_time, "seconds"
print "Memoization:"
start_time = time.clock()
mem_init()
print time.clock() - start_time, "seconds"