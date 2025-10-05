#Part 2: Test with Random Numbers
import random
from algorithms import recursive_binary_search, iterative_binary_search, sequential_search


#This generates 20 random numbers between 1 and 100
arr = [random.randint(1, 100) for _ in range(20)]
#This sorts the array to prepare it for binary search algorithms.
arr.sort()


#This randomly selects a target value from the array or a value not in the array (e.g., 999) to test both found and not found scenarios with a 50% chance for each.
target = random.choice(arr) if random.random() < 0.5 else 999


# his prints the sorted array and the target value for reference.
print("Sorted Array:", arr)
print("Target:", target)


#This tests the recursive binary search function and prints the result.
index = recursive_binary_search(arr, target, 0, len(arr) - 1)
print(f"Recursive Binary Search: {target} {'found at index ' + str(index) if index != -1 else 'not found'}")


#This tests the iterative binary search function and prints the result.
index = iterative_binary_search(arr, target)
print(f"Iterative Binary Search: {target} {'found at index ' + str(index) if index != -1 else 'not found'}")


#This tests the sequential search function and prints the result.
index = sequential_search(arr, target)
print(f"Sequential Search: {target} {'found at index ' + str(index) if index != -1 else 'not found'}")