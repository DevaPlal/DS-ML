import numpy as np
low=int(input("enter a low limit: "))
high=int(input("enter upper limit: "))
n=int(input("enter size: "))
random_num=np.random.uniform(low, high, size=n)
print("Random numbers:")
print(random_num)
