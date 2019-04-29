# Python code to implement iterative Binary Search. It returns location of z in given array arr if present, else returns -1 
def binarySearch(arr, x, y, z): 
  
    while x <= y: 
  
        mid = x + (y - x)/2; 
        # print mid

        if arr[mid] == z: 
            return mid 
  
        elif arr[mid] < z: 
            x = mid + 1
  
        else: 
            y = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1