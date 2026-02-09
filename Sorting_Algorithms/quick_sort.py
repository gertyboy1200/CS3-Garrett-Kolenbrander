#quick sort implimentation
import numbers
import time
start = time.time()
array = numbers.list_of_numbers.copy()
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

quick_sort(array)
end = time.time()

print(f"Total runtime of the program is {end - start} seconds")
