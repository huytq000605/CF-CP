
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>
#include <regex>

using namespace std;

int solve(vector<string>& matrix) {
	int m = matrix.size(), n = matrix[0].size();
	int result{};
	string XMAS = "XMAS";
	vector<pair<int, int>> ds{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

	for(int r{1}; r < m-1; ++r) {
		for(int c{1}; c < n-1; ++c) {
			if(matrix[r][c] == 'A') {
				bool dia1 = (matrix[r-1][c-1] == 'M' && matrix[r+1][c+1] == 'S') || (matrix[r-1][c-1] == 'S' && matrix[r+1][c+1] == 'M');
				bool dia2 = (matrix[r+1][c-1] == 'M' && matrix[r-1][c+1] == 'S') || (matrix[r+1][c-1] == 'S' && matrix[r-1][c+1] == 'M');
				if(dia1 && dia2) ++result;
			}
		}
	}

	return result;
}

int main() {
  string line;
	vector<string> matrix;
  while(getline(cin, line)) {
		matrix.emplace_back(line);
  }
	cout << solve(matrix) << endl;
}
