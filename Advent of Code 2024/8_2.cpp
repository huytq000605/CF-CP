#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>
#include <regex>
#include <array>
#include <set>
#include <math.h>

using namespace std;


long long solve(vector<string>& grid) {
	int m = grid.size(), n = grid[0].size();
	set<pair<int, int>> result;
	unordered_map<char, vector<pair<int, int>>> um;
	for(int r{}; r < m; ++r) {
		for(int c{}; c < n; ++c) {
			if(isalpha(grid[r][c]) || isdigit(grid[r][c])) {
				um[grid[r][c]].emplace_back(r, c);
				result.emplace(r, c);
			}
		}
	}

	for(auto [c, A]: um) {
		int k = A.size();
		for(int i{}; i < k; ++i) {
			for(int j{i+1}; j < k; ++j) {
				auto [r1, c1] = A[i];
				auto [r2, c2] = A[j];
				int r3 = r1 + (r1 - r2), c3 = c1 + (c1 - c2);
				while(r3 >= 0 && r3 < m && c3 >= 0 && c3 < n) {
					result.emplace(r3, c3);
					r3 += (r1 - r2);
					c3 += (c1 - c2);
				}
				int r4 = r2 + (r2 - r1), c4 = c2 + (c2 - c1);
				while(r4 >= 0 && r4 < m && c4 >= 0 && c4 < n) {
					result.emplace(r4, c4);
				 	r4 += (r2 - r1);
					c4 += (c2 - c1);
				}
			}
		}
	}

	return result.size();
}

int main() {
  string line;
	vector<string> grid;
  while(getline(cin, line)) {
		// istringstream ss(line);
		grid.emplace_back(line);
  }
	cout << solve(grid) << endl;
}
