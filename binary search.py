We have created a function called binary_search() function which takes two arguments - a list to sorted and a number to be searched.
We have declared two variables to store the lowest and highest values in the list. The low is assigned initial value to 0, high to len(list1) - 1 and mid as 0.
Next, we have declared the while loop with the condition that the lowest is equal and smaller than the highest The while loop will iterate if the number has not been found yet.
In the while loop, we find the mid value and compare the index value to the number we are searching for.
If the value of the mid-index is smaller than n, we increase the mid value by 1 and assign it to The search moves to the left side.
Otherwise, decrease the mid value and assign it to the high. The search moves to the right side.
If the n is equal to the mid value then return mid.
This will happen until the low is equal and smaller than the high.
If we reach at the end of the function, then the element is not present in the list. We return -1 to the calling function.

code:
  # Iterative Binary Search Function method Python Implementation  
# It returns index of n in given list1 if present,   
# else returns -1   
def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < n:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif list1[mid] > n:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  
  
  
# Initial list1  
list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 45  
  
# Function call   
result = binary_search(list1, n)  
  
if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1")  
