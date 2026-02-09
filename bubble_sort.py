#bubble sort algorithm
import numbers
import time

start = time.time()
array = numbers.list_of_numbers

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

time.sleep(1)
end = time.time() # from geekforgeeks

bubble_sort(array)

print(f"Total runtime of the program is {end - start} seconds")

