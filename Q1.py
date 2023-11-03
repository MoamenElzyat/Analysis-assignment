import time
import matplotlib.pyplot as plt


# Iterative Method:
def iterative(a, n):
  #  time.sleep(1)
    result = 1
    for _ in range(n):
        result *= a
    return result

###################################################

#Divide-and-Conquer
def conquer(a, n):
   # time.sleep(1)

    if n == 0:
        return 1
    elif n % 2 == 0:
        z = conquer(a, n // 2)
        return z * z
    else:
        z = conquer(a, (n - 1) // 2)
        return  z * z * a
 
###################################################




RAANGE = list(range(0, 1000, 500))  
iterative_times = []
divide_conquer_times = []

for n in RAANGE:
    START = 1  
    start_time = time.time()
    result = iterative(START, n)  
    iterative_times.append(time.time() - start_time)

    start_time = time.time()
    result = conquer(START, n)  
    divide_conquer_times.append(time.time() - start_time)


plt.plot(RAANGE, iterative_times, label="Iterative" ,color='green')
plt.plot(RAANGE, divide_conquer_times, label="Divide &Conquer", color='blue', linestyle='dashdot')
plt.xlabel('RANGE')
plt.ylabel('Runtime')
plt.ylim(0, max(max(iterative_times), max(divide_conquer_times)))  # Set the y-axis range
plt.legend()
plt.show()
