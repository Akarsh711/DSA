# DSA
## Merge Sort
It is quite a recursivey algorith which gives you good test of recursion by having three functions,
two with same name and one with different name for merge.
```python 
 # Boiler Plate
 def mergeList(l, r):
  if l < r:
   mid = (l+r)//2
   mergeList(arr, l, mid)
   mergeList(arr, mid+1, r)
   merge(arr, l, mid, r)
```

The main Quesiton is which personally confuse me is : how to understand recursion or recursive call?
Ans : So, the best way of understanding is by using recursive tree (along with call stack personally recommended!)

## Here is Example
![Image Here](https://github.com/Akarsh711/DSA/blob/master/images/IMG_20201119_223602112.jpg)
Consider the list/array passed to the above function with ```l = 0```, and ```r = 1```

![Image Here](https://github.com/Akarsh711/DSA/blob/master/images/IMG_20201119_223822894.jpg)
If you look closely to above image then you will see that ```mL(0,0)``` is called by the ```mL(0,1)``` and
```mL(0,0)``` get's poped when it is running because condition ```if l < r ```  get's False
and same happens for mL(1,1) . 
So, when they both get poped then merge function called by main array ```[14, 19]```

