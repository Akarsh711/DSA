#Selection Sort

# In first iteration from start it get out the first number and check it
# with adjacent number, If second one is smaller then it take that one and finds other
# other smaller than that if it find it get that and then run till it find smaller
# number among them.

def selection_sort(arr):
	temp_arr = []#  optional array
	for i in range(len(arr)): # Pass
	    temp = i
	    for j in range(i+1, len(arr)): # Inner Iteration
	        if arr[temp] > arr[j]:
	            temp = j
	            
	    #optional to append
	    temp_arr.append(arr[temp]) # This practice is not good for memory 
	    # Swap the found minimum element with  
	    # the first element      
	    arr[i], arr[temp] = arr[temp], arr[i]
	print('Selection Sort - ', arr)
	print('temp_arr', temp_arr)
	print('==============================')
	
if __name__ == '__main__':
	arr =[5, 55, 45, 6, 7]
	selection_sort(arr)

