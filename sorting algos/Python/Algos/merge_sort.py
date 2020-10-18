# Merge Sort by me @Akarsh

def merge(arr, l, mid, r):
	print('mid, l',mid, l)
	n1 = mid - l + 1
	n2 = r - mid 
	
	# print('n1, n2', n1, n2)
	temp_l = [0] * n1
	temp_r = [0] * n2
	for i in range(0, n1):
		temp_l[i] = arr[l+i]
		print('l+i', l+i,i)

	for j in range(0, n2):
		temp_r[j] = arr[mid + 1 + j]

	print('temp_l, temp_r',temp_l,temp_r)


	i = 0
	j = 0 
	k = l

	while i < n1 and j < n2:
		if temp_l[i] <= temp_r[j]:
			arr[k] = temp_l[i]
			i+=1
		else:
			arr[k] = temp_r[j]
			j+=1
		k+=1

	while i < n1:
		arr[k] = temp_l[i]
		i+=1
		k+=1

	while j < n2:
		arr[k] = temp_r[j]
		j+=1
		k+=1

def merge_sort(arr, l, r):
	if l < r:
		mid = (l+r)//2
		print('mid_fresh',mid)
		merge_sort(arr, l, mid)
		merge_sort(arr, mid+1, r)
		merge(arr, l, mid, r)



if __name__ =="__main__":
	arr = [9,6,3,7]
	merge_sort(arr, 0, len(arr)-1)
	print(arr)

# Python program for implementation of MergeSort 
  
# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
# def merge(arr, l, m, r): 
#     n1 = m - l + 1
#     n2 = r- m 
#     print('l, m, r',l, m, r )
#     print('n1, n2',n1, n2)
#     # create temp arrays 
#     L = [0] * (n1)
#     R = [0] * (n2)
#     # Copy data to temp arrays L[] and R[] 
#     for i in range(0 , n1): 
#         L[i] = arr[l + i]
 
#     for j in range(0 , n2):
#         R[j] = arr[m + 1 + j]
#         print('L , R',L, R)

#     # Merge the temp arrays back into arr[l..r] 
#     i = 0     # Initial index of first subarray 
#     j = 0     # Initial index of second subarray 
#     k = l     # Initial index of merged subarray 
  
#     while i < n1 and j < n2 : 
#         if L[i] <= R[j]:
#             arr[k] = L[i] 
#             i += 1
#         else: 
#             arr[k] = R[j] 
#             j += 1
#         k += 1
  
#     # Copy the elements of L[], if there 
#     # are any 
#     while i < n1: 
#         arr[k] = L[i] 
#         i += 1
#         k += 1
  
#     # Copy the remaining elements of R[], if there 
#     # are any 
#     while j < n2: 
#         arr[k] = R[j] 
#         j += 1
#         k += 1
  
# # l is for left index and r is right index of the 
# # sub-array of arr to be sorted 
# def mergeSort(arr,l,r): 
#     if l < r: 
  
#         # Same as (l+r)//2, but avoids overflow for 
#         # large l and h
#         m = (l+(r-1))//2
  
#         # Sort first and second halves 
#         mergeSort(arr, l, m) 
#         mergeSort(arr, m+1, r) 
#         merge(arr, l, m, r) 
  
  
# # Driver code to test above 
# arr = [12, 11, 13, 5] 
# n = len(arr) 
# print ("Given array is") 
# for i in range(n): 
#     print ("%d" %arr[i]) 
  
# mergeSort(arr,0,n-1) 
# print ("\n\nSorted array is") 
# for i in range(n): 
#     print ("%d" %arr[i]), 
