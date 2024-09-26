def median_of_medians(arr, k):
    if len(arr) < 10:
        return sorted(arr)[k]  # Use a simple sort for small arrays

    # Step 1: Divide arr into subarrays of length 5
    subarrays = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = []

    # Step 2: Find the median of each subarray
    for subarray in subarrays:
        medians.append(sorted(subarray)[len(subarray) // 2])

    # Step 3: Recursively find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Step 4: Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)

    # Determine the position of the pivot
    if k < len(low):
        return median_of_medians(low, k)  # k-th smallest is in the lower part
    elif k < len(low) + pivot_count:
        return pivot  # k-th smallest is the pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)  # k-th smallest is in the upper part

# Example usage
arr = [3, 1, 2, 5, 4, 6, 8, 7, 9, 10]
k = 5  # Find the 5th smallest element (0-based index)
result = median_of_medians(arr, k)
print(f"The {k}th smallest element is: {result}")
