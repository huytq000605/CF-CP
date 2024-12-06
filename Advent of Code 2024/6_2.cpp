#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>
#include <regex>
#include <array>
#include <set>

using namespace std;

int solve(vector<string> &matrix) {
	int m = matrix.size(), n = matrix[0].size();
	int result{};
	pair<int, int> start;
	array<pair<int, int>, 4> ds{{ {-1, 0}, {0, 1}, {1, 0}, {0, -1} }};

	for(int r{}; r < m; ++r) {
		for(int c{}; c < n; ++c) {
			if(matrix[r][c] == '^') {
				start = {r, c};
				break;
			}
		}
	}

	auto is_cycle = [&]() -> bool
	{
		vector<vector<int>> seen(m, vector<int>(n, 0));
		seen[start.first][start.second] |= (1 << 0);
		for (int i{}, r{start.first}, c{start.second}; r >= 0 && r < m && c >= 0 && c < n;)
		{
			int nr = r + ds[i].first, nc = c + ds[i].second;
			if (nr < 0 || nr >= m || nc < 0 || nc >= n)
				return false;
			if (seen[nr][nc] & (1 << i)) return true;
			if (matrix[nr][nc] == '#') {
				i = (i + 1) % 4;
				continue;
			}

			seen[nr][nc] |= (1 << i);
			r = nr;
			c = nc;
		}

		return false;
	};

	for(int r{}; r < m; ++r) {
		for(int c{}; c < n; ++c) {
			if(start != make_pair(r, c) && matrix[r][c] != '#') {
				matrix[r][c] = '#';
				if(is_cycle()) ++result;
				matrix[r][c] = '.';
			}
		}
	}

	return result;
}

int main() {
	bool rule{false};
  string line;
	vector<string> matrix;
  while(getline(cin, line)) {
		// istringstream ss(line);
		matrix.emplace_back(line);
  }
	cout << solve(matrix) << endl;
}
