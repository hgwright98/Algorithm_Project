#Part 3: Measure and Compare Runtime Growth
import random
import time
from algorithms import recursive_binary_search, iterative_binary_search, sequential_search


#This section measures and compares the runtime of three search algorithms: recursive binary search, iterative binary search, and sequential search. It generates sorted arrays of varying sizes, performs each search multiple times, and calculates the average runtime for each algorithm.
data_sizes = [5000, 50000, 100000, 150000, 1000000]


#This loop iterates over different sizes of data to test the performance of each search algorithm.
for N in data_sizes:
    #This initializes total time counters for each search algorithm.
    total_rbs = total_ibs = total_seq = 0


    #This inner loop runs the search tests multiple times to get an average runtime for each algorithm.
    for _ in range(10):  #This repeats 10 times for average
        arr = sorted([random.randint(1, 1_000_000) for _ in range(N)]) #This generates a sorted array of N random integers.
        target = random.randint(1, 1_000_000) #This selects a random target value to search for in the array.


        #This is the Recursive Binary Search
        start = time.perf_counter() #This records the start time of the search.
        recursive_binary_search(arr, target, 0, len(arr) - 1) #This performs the recursive binary search.
        total_rbs += (time.perf_counter() - start) * 1_000_000 #This calculates the elapsed time in microseconds and adds it to the total.


        #This is the Iterative Binary Search
        start = time.perf_counter() #This records the start time of the search.
        iterative_binary_search(arr, target) #This performs the iterative binary search.
        total_ibs += (time.perf_counter() - start) * 1_000_000 #This calculates the elapsed time in microseconds and adds it to the total.


        #This is the Sequential Search
        start = time.perf_counter() #This records the start time of the search.
        sequential_search(arr, target) #This performs the sequential search.
        total_seq += (time.perf_counter() - start) * 1_000_000 #This calculates the elapsed time in microseconds and adds it to the total.

        #This prints average times for each algorithm
    print(f"\nN = {N}")
    print(f"Average Recursive Binary Search time: {total_rbs / 10:.2f} μs")
    print(f"Average Iterative Binary Search time: {total_ibs / 10:.2f} μs")
    print(f"Average Sequential Search time: {total_seq / 10:.2f} μs")