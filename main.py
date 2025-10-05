#Part 1: Test with Small List
from algorithms import recursive_binary_search, iterative_binary_search, sequential_search
#This is a small sorted array to test the search algorithms
arr = [3, 5, 8, 12, 14, 18, 21]
#This sorts the array to ensure it is in ascending order for binary search algorithms
arr.sort()


target1 = 12  # This is the target that is present in the array
target2 = 9   # This is the target that is not present in the array


#This tests each search algorithm with both targets and prints the results
for target in [target1, target2]:
    #This prints the target being searched for as a title
    print("\nTarget:", target)
    #This tests the recursive binary search
    index = recursive_binary_search(arr, target, 0, len(arr) - 1)
    print(f"Recursive Binary Search: {target} {'found at index ' + str(index) if index != -1 else 'not found'}")
    #This tests the iterative binary search
    index = iterative_binary_search(arr, target)
    print(f"Iterative Binary Search: {target} {'found at index ' + str(index) if index != -1 else 'not found'}")
    #This tests the sequential search
    index = sequential_search(arr, target)
    print(f"Sequential Search: {target} {'found at index ' + str(index) if index != -1 else 'not found'}")