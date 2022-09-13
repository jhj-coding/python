import random
import time
import numpy as np

python_list=[]
for i in range(100000000):
    python_list.append(random.random())

ndarry_list=np.array(python_list)

#原生list求和
t1=time.time()
a=sum(python_list)
t2=time.time()
d1=t2-t1
#0.43579530715942383

print(d1)
t1=time.time()
a=np.sum(ndarry_list)
t2=time.time()
d1=t2-t1
#0.1137235164642334
print(d1)

