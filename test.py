from pylab import *
import random

dieVals = [1,2,3,4,5,6]
vals = []
for i in range(1000):
    vals.append(random.choice(dieVals) * random.choice(dieVals))

plot(vals)
show()

