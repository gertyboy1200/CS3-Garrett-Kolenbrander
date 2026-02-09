#insertion sort implementation
import numbers
import time
start = time.time()
array = numbers.list_of_numbers.copy()

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


insertion_sort(array)
end = time.time()

print(f"Total runtime of the program is {end - start} seconds")
