#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	vector<int> A;
	unordered_map<int, int> B;
	int a{}, b{};
	int result{};
	while(cin >> a >> b) {
		A.emplace_back(a);
		B[b]++;
	}
	for(int i{}; i < A.size(); ++i) {
		result += A[i] * B[A[i]];
	}
	cout << result << endl;
}