// cout and cin example from cplusplus.com
#include <iostream>	// cout and cin
#include <cstdlib> // EXIT_SUCCESS

int main()
{
	int i; 

	std::cout << "Enter an integer value: ";
	std::cin >> i;

	std::cout << "The value that you entered was: " << i << std::endl;
	std::cout << "Your value doubled: " << i * 2 << std::endl;

	std::cout << "Good Bye!" << std::endl;

	return EXIT_SUCCESS;
}
