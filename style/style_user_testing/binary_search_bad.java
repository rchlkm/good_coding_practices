// Java implementation of iterative Binary Search 
class BinarySearch { 
    // Returns index of z if it is present in arr[], else return -1 
    int binarySearch(int arr[], int z) 
    { 
        int x = 0, y = arr.length - 1; 
        while (x <= y) { 
                int m = x + (y - x) / 2; 
                System.out.println("m: " + m);
              if (arr[m] == z) 
                  return m; 
  
            if (arr[m] < z) 
                x = m + 1; 
              else
                  y = m - 1; 
        } 
          return -1; 
    } 
}