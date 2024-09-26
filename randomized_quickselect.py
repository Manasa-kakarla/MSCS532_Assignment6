import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot_value = arr[pivot_index]
    
    # Move the pivot to the end
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low
    
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    
    # Move the pivot to its final place
    arr[store_index], arr[high] = arr[high], arr[store_index]
    
    return store_index

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = randomized_partition(arr, low, high)

    # The pivot is in its final sorted position
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k)

def quickselect(arr, k):
    if k < 0 or k >= len(arr):
        raise IndexError("k is out of bounds")
    return randomized_select(arr, 0, len(arr) - 1, k)

# Example usage
arr = [3, 1, 2, 5, 4, 6, 8, 7, 9, 10]
k = 8  # Find the 5th smallest element (0-based index)
result = quickselect(arr, k)
print(f"The {k}th smallest element is: {result}")
