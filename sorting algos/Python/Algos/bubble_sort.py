# Bubble Sort
# It's

def bubble_sort(arr):
	for pAss in range(len(arr)):
		
		for i in range( (len(arr)-1) - pAss ):
			
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]

	print('Bubble Sort -', arr)


if __name__ == "__main__":
	arr=[9,8,12,9,3]
	bubble_sort(arr)
