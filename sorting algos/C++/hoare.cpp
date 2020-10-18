#include <iostream>
#include <cmath>
#include <stdio.h>

using namespace std;
int partition(int [], int, int);
void quicksort(int A[] ,int lo, int hi){
	int l, h, p;
	l = lo;
	h = hi;
	
	if (l<h){
	p = partition(A, lo, hi);
        quicksort(A, l, p);
        quicksort(A, p+1, h);
	}
}

int partition(int A[],int lo, int hi){
    int pivot = ceil(A[lo + hi]/2);
    int i, j, temp;
    i = lo -1;
    j = hi +1;
    
    bool check = true; // Reflect true as 1, and 0 for false
    while(true){
        while(A[i] < pivot) //scaning from left to pivot
            i ++;
        
	
        while(A[j] > pivot) // scanning from right to pivot
            j --;

        if(i == j) // if we found both side pointer equal then get out from loop
            return 0;
        
        //now swap 
        temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
    
    return pivot;
}


int main(){	
    int Arr[] = {4,5,3,2,6,8,1,3};
    quicksort(Arr, 0, 7);
    for (int i=0; i<=7; i++){
    	cout << Arr[i];
    }	
    return 0;
}
