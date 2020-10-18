void quick(int A[], int N, int BEG, int END, int *LOCPTR){
	int LEFT, RIGHT, temp;
	LEFT = BEG; RIGHT = END;
	*LOCPTR = BEG;

	while(LEFT<RIGHT){
		// step2:
		//scanning from right to *LOCPTR
		while(A[*LOCPTR] <= A[RIGHT] && *LOCPTR!=RIGHT)
			RIGHT--;
		if(*LOCPTR == RIGHT)
			return;
		if(A[*LOCPTR] > A[RIGHT]){
			// swapping
			temp = A[*LOCPTR];
			A[*LOCPTR] = A[RIGHT];
			A[RIGHT] = temp;
			*LOCPTR = RIGHT;
		}
		//we should not use goto
		// goto step3;

		// step3:
		while(A[LEFT] <= A[*LOCPTR] && LEFT != *LOCPTR)
			LEFT++;
		if(*LOCPTR == LEFT)
			return;
		if(A[LEFT] > A[*LOCPTR]){
			// swapping
			temp = A[LEFT];
			A[LEFT] = A[*LOCPTR];
			A[*LOCPTR] = temp;
			*LOCPTR = LEFT;
		}
		// goto step2;
	}
}


void quick_sort(int A[], int N){
	int BEG, END, LOC, TOP;

	// creating stack
	TOP = -1;
	int LOWER[10], UPPER[10];

	// putting values in stack
	if(N > 1){
		TOP++;
		LOWER[TOP] = 0;
		UPPER[TOP] = N-1;
	}
	while(TOP != -1){
		BEG = LOWER[TOP];
		END = UPPER[TOP];
		TOP--;
		quick(A, N, BEG, END, &LOC);
		if(BEG<LOC-1){
			TOP++;
			LOWER[TOP] = BEG;
			UPPER[TOP] = LOC - 1;
		}
		if(LOC+1 < END){
			TOP++;
			LOWER[TOP] = LOC + 1;
			UPPER[TOP] = END;
		}
	}
}

#include <stdio.h>
#include <conio.h>

int main()
{
	int A[] = {30, 20, 10, 8, 5, 3, 8, 3};
	int i;
	quick_sort(A, 8);
	for(i=0; i<=7; i++){
		printf("%d ,", A[i]);
	}
	getch();
}