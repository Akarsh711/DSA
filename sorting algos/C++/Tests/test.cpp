#include <iostream>

using namespace std;

int main(){
// array test
int arr[10];
for(int i = 0; i<11; i++){
    arr[i] = i;
    } // In C/CPP you can directly assign array like this way but that's not work with python
// printing array
for(int i=0; i<=11; i++){
    cout << arr[i] << "\n";
    }
}