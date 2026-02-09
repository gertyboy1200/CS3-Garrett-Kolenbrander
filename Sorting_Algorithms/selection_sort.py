#selection sort algorithm
import numbers
import time

start = time.time()
array = numbers.list_of_numbers.copy()

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

selection_sort(array)
end = time.time()

print(f"Total runtime of the program is {end - start} seconds")