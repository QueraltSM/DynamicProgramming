import time
from mem import *
from tab import *

print "Tabulation:"
start_time = time.clock()
tab_init()
print time.clock() - start_time, "seconds"
print "Memoization:"
start_time = time.clock()
mem_init()
print time.clock() - start_time, "seconds"
