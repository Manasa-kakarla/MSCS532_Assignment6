import time
import random

# Implementation of Median of Medians (Deterministic Selection)
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    # Divide arr into sublists of length 5
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    
    # Find the median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)

    # Determine the rank of the pivot
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot  # pivot is the k-th element
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

# Implementation of Randomized Quickselect
def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)

    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + pivot_count:
        return pivot  # pivot is the k-th element
    else:
        return randomized_quickselect(high, k - len(low) - pivot_count)

# Function to time the execution of an algorithm
def time_algorithm(algorithm, arr, k):
    start_time = time.time()
    result = algorithm(arr, k)
    end_time = time.time()
    return end_time - start_time

# Define input sizes and distributions
sizes = [100, 1000, 10000, 100000]
distributions = {
    'random': lambda n: [random.randint(1, 10000) for _ in range(n)],
    'sorted': lambda n: list(range(n)),
    'reverse_sorted': lambda n: list(range(n, 0, -1)),
    'duplicates': lambda n: [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]
}

# Results dictionary
results = {}

# Run the experiments
for size in sizes:
    results[size] = {}
    for dist_name, dist_func in distributions.items():
        arr = dist_func(size)
        k = size // 2  # Selecting the median-like element

        # Timing the deterministic algorithm
        time_deterministic = time_algorithm(median_of_medians, arr.copy(), k)
        # Timing the randomized algorithm
        time_randomized = time_algorithm(randomized_quickselect, arr.copy(), k)

        results[size][dist_name] = {
            'deterministic': time_deterministic,
            'randomized': time_randomized
        }

# Print results
for size, data in results.items():
    print(f"Results for size {size}:")
    for dist, times in data.items():
        print(f"  Distribution: {dist}, Deterministic: {times['deterministic']:.6f}s, Randomized: {times['randomized']:.6f}s")
