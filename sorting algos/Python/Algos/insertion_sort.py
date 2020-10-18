
def insertion_sort_mine(arr):
	current = 0	
	for i in range(1, len(arr)):
		current = arr[i] # 5, 3
		temp = i
		print(current)
		for j in range(i, -1, -1): # This loop waste it's first iteration and also it work wothout any j reach to 0  even array is sorted
			if current < arr[j]: # 7, 5, 7
				print(f'current - {current},{arr[i]}is less than previous arr[j] - {arr[j]}')
				arr[j+1] = arr[j] # slide previous element
				temp -= 1
		arr[temp] = current
	print(f'Insertion sort mine - {arr}')


def insertion_sort(arr):    
	for i in range(1, len(arr)):
		key = arr[i] # This var is required because arr[i] 's value keeps changing in while loop as that index's value changing when swapping / sliding caus
		j= i-1
		while j>=0 and key < arr[j]:
			arr[j+1] = arr[j] 
			j -= 1
		arr[j+1] = key
	print('insertion sort -',arr)


if __name__ == "__main__":
	arr=[9,8,12,9,3]	 # 8, 9 , 12 , 9
						 # 8, 9, _, 12
						 # 8, 9, 9, 12
	insertion_sort_mine(arr)
	insertion_sort(arr)


