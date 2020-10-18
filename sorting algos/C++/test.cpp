#include <iostream>
#include <stdio.h>
#include <typeinfo>
using namespace std;

void test(int arr[], int integer){
   	printf("\narrr %d",arr);
   	cout << typeid(integer).name() <<endl;Î	
	cout << "integer we gave"<<integer;

}

int main(){
	int A[] = {4,6,3,2};
	test(A, 223);

}
