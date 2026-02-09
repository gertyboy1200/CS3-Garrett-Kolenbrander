#merge sort implementation
import numbers
import time

start = time.time()
array = numbers.list_of_numbers.copy()

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

time.sleep(1)
end = time.time()

merge_sort(array)

print(f"Total runtime of the program is {end - start} seconds")
