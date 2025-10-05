#This function performs a recursive binary search on a sorted array to find the index of the target value.
#It takes the array, target value, and the current low and high indices as parameters.
def recursive_binary_search(arr, target, low, high):
   #This checks if the low index has exceeded the high index, indicating that the target is not present in the array.
   if low > high:
       return -1
   #This calculates the median index of the current search range.
   mid = (low + high) // 2
   #This compares the median element with the target value and decides whether to return the index or search further.
   if arr[mid] == target:
       return mid
   #This recursively searches the left half if the target is less than the median element.
   elif arr[mid] > target:
       return recursive_binary_search(arr, target, low, mid - 1)
   #This recursively searches the right half if the target is greater than the median element.
   else:
       return recursive_binary_search(arr, target, mid + 1, high)


#This function performs an iterative binary search on a sorted array to find the index of the target value.
#It takes the array and target value as parameters.
def iterative_binary_search(arr, target):
   #This initializes the low and high indices for the search range.
   low = 0
   high = len(arr) - 1
   #This loop continues until the low index exceeds the high index, indicating that the target is not present in the array.
   while low <= high:
       #This calculates the median index of the current search range.
       mid = (low + high) // 2
       #This compares the median element with the target value and adjusts the search range accordingly.
       if arr[mid] == target:
           return mid
       elif arr[mid] < target:
           #This narrows the search to the right half if the target is greater than the median.
           low = mid + 1
       else:
           #This narrows the search to the left half if the target is less than the median.
           high = mid - 1
   #This returns -1 if the target is not found in the array.
   return -1


#This function performs a sequential search on an array to find the index of the target value.
#It takes the array and target value as parameters.
def sequential_search(arr, target):
   #This iterates through each element in the array and checks if it matches the target value.
   for i in range(len(arr)):
       #This returns the index if the target is found.
       if arr[i] == target:
           return i
   #This returns -1 if the target is not found after scanning the entire array.
   return -1