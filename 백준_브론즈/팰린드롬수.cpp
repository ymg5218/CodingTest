#include <iostream>
using namespace std;

int main() {
	int num;

	while (true) {
		cin >> num;
		if (num == 0) {
			break;
		}
		stringstream str_num;
		str_num << num;

		int left = 0;
		int right = sizeof(str_num) - 1;
		
		bool is_valid = true;

		while (left < right) {
			if (str_num[left] != str_num[right]) {
				is_valid = false;
				break;
			}
		}

		if (is_valid) {
			cout << "yes" << endl;
		}
		else {
			cout << "no" << endl;
		}

	}

	return 0;
}