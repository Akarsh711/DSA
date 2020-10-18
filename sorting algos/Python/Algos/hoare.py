# Hoare Implementation of Quick Sort
# Consider :-Gayle Laakmann McDowell
from math import ceil

only_once = True
def partition(arr, l, h):
        
    global only_once
    if only_once:
       print("if chala")
       pivot = arr[3]
       only_once = False
    else:
       print("else chala")
       pivot = arr[l]

    # pivot = arr[l + h-1]//2
    i = l - 1 
    j = h + 1
      
    while (True):
        print(pivot) 
        print("ye chal ra aur arr hai ", arr)
        # Find leftmost element greater than  
        # or equal to pivot  
        i += 1
        while (arr[i] < pivot): 
            i += 1
              
        # Find rightmost element smaller than  
        # or equal to pivot  
        j -= 1
        while (arr[j] > pivot): 
            j -= 1
              
        # If two pointers met.
        print("jate jjate", i, j)
        if (i >= j): 
            return j  
          
        arr[i], arr[j] = arr[j], arr[i] 

def quicksort(arr, l, h):
    if l< h:
        p = partition(arr, l, h)

        quicksort(arr, l, p)
        quicksort(arr, p+1, h) 

if __name__ == "__main__":
    arr = [4,58,3,6,57,7]
    n = len(arr)
    quicksort(arr, 0, n-1)
    print('quick sort "Hoare Partition"-',arr)

