# Binary Search 
# Algo Complexity : n(log2(n)) or n(log(n))
# To Implement that search our array must be sorted
class sol():

    def binarySearchRecursive2(self, arr, x, *args):
        if(left> right):
            return False
        
        self.mid = (left + right) / 2

        if arr[mid] == x:
            return True
        
        if x < arr[mid]:
            return  binarySearchRecursive2(arr, x, left, mid -1 )
        else:
            return binarySearchRecursive2(arr, x, mid+1, right)

        
    def binarySearchRecursive(self, arr, x, *args):
        return binarySearchRecursive2(arr ,x, 0, len(arr) -1)


if __name__ == "__main__":
    arr = [1,3,4,5,13,20,25,40, 42, 44, 53]

    obj = sol()
    obj.binarySearchRecursive(arr, 20)
