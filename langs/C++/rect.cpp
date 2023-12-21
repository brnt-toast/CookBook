#include <iostream>

class Rectangle {
	int width, height;

	public:
		void set_values (int, int);

		int area(){
			return width * height;
		}
};

void Rectangle::set_values (int x, int y) {
	width = x;
	height = y;
}

int main() {
	Rectangle rect;
	
	rect.set_values (3,4);

	std::cout << "area: " << rect.area() << std::endl;

	return 0;
}
