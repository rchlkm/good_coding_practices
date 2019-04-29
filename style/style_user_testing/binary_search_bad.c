// C program to implement iterative Binary Search 
#include <stdio.h> 
  
// A iterative binary search function. It returns location of z in given array arr[l..r] if present, otherwise -1 
int binarySearch(int arr[], int x, int y, int z) 
{ 
    while (x <= y) { 
          int m = x + (y - x) / 2; 
  
            //printf("%d\n", m);
          //printf("%d, %d", x, y);
        if (arr[m] == z) 
            return m; 
  
            if (arr[m] < z) 
                x = m + 1; 
  
            else
              y = m - 1; 
    } 
    return -1; 
} 