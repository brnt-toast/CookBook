#include <stdio.h>

int sum(int k);

int sum(int k){
	if ( k > 0){
		return k + sum(k -1);
	} else {
		return 0;
	}
}

int main() {
	int result = sum(10);

	printf("%d\n", result);

	return 0;
}
