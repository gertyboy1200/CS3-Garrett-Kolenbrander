# bubble sort algorithm
import numbers
import time

array = numbers.list_of_numbers.copy()

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == "__main__":
    start = time.time()
    bubble_sort(array)
    end = time.time()
    print(f"Total runtime of the program is {end - start} seconds")
