#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	vector<int> A, B;
	int a{}, b{};
	int result{};
	while(cin >> a >> b) {
		A.emplace_back(a);
		B.emplace_back(b);
	}
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());
	for(int i{}; i < A.size(); ++i) {
		result += abs(A[i] - B[i]);
	}
	cout << result << endl;
}