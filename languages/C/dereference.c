#include <stdio.h>

int main(){
	int num = 42;
	int* ptr = &num; // pointer varible storing the address of num

	printf("%d\n", num); // 42
	printf("%p\n", &num); // memory address of num 
	printf("%p\n", ptr);
	printf("%d\n", *ptr); // dereference

	return 0;
}
