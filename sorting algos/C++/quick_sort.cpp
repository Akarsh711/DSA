# include<stdio.h>

void quicksort(int arr[],int first,int last){
    
    int i, j, pivot, temp;
    if(first<last){
        pivot= last;
        i=first;
        j=last;

        while(i<j){
            while(arr[i]<=arr[pivot]&&i<last)
                i++;
            while(arr[j]>arr[pivot])
                j--;
            if(i<j){
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }

        temp=arr[pivot];
        arr[pivot]=arr[j];
        arr[j]=temp;
        quicksort(arr,first,j-1);
        quicksort(arr,j+1,last);
        int count = 5;
        for(i=0;i<count;i++)
            printf("%d ,",arr[i]);
        printf("\n");
    }
}

int main(){
    int i, count;
    int arr[] = {8, 5, 0, 3, 4};
    count = 5;
    quicksort(arr,0,count-1);

    for(i=0;i<count;i++)
        printf("%d",arr[i]);
    return 0;
    }
