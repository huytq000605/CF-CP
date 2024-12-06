#include <stdio.h>
#include <iostream>

using namespace std;

void show_bytes(unsigned char* start, size_t len) {
	for(int i{}; i < len; ++i) {
		printf("%.2x ", start[i]);
	}
	cout << endl;
}

int main() {
	int a{0x12345678};
	cout << a << endl;
	show_bytes((unsigned char*)(&a), sizeof(0x12345678));

	cout << "DONE" << endl;
	return 0;
}