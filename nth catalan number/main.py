import time
from mem import *
from tab import *

print "Dynamic programming for calculate the nth Catalan Number"
print "Tabulation:"
start_time = time.clock()
tab_init()
print time.clock() - start_time, "seconds"
print "Memoization:"
start_time = time.clock()
mem_init()
print time.clock() - start_time, "seconds"
