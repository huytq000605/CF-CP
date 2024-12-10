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
static constexpr array<pair<int, int>, 4> ds{{ {0,1}, {1,0}, {-1,0}, {0,-1} }};

long long solve(vector<string>& grid) {
	int m = static_cast<int>(grid.size()), n = static_cast<int>(grid[0].size());
	vector<pair<int, int>> starts;
	for(int r{}; r < m; ++r) {
		for(int c{}; c < n; ++c) {
			if(grid[r][c] == '0') starts.emplace_back(r, c);
		}
	}

	long long result{};
	for(auto [r, c]: starts) {
		set<pair<int, int>> top;
		set<pair<int, int>> seen;
		deque<pair<int, int>> dq{{ {r, c} }};
		while(!dq.empty()) {
			auto [r, c] = dq.front();
			if(grid[r][c] == '9') {
				top.emplace(r, c);
			}
			dq.pop_front();
			for(auto [dr, dc]: ds) {
				int nr = r + dr, nc = c + dc;
				if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
				if(grid[r][c]+1 != grid[nr][nc]) continue;
				if(seen.find({nr, nc}) != seen.end()) continue;
				seen.emplace(nr, nc);
				dq.emplace_back(nr, nc);
			}
		}
		result += top.size();
	}

	return result;
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

