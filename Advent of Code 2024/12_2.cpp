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
#include <numeric>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;
static constexpr array<pair<int, int>, 4> ds{{ {0,1}, {1,0}, {-1,0}, {0,-1} }};

long long solve(vector<string> &grid) {
	int m = grid.size(), n = grid[0].size();

	vector<vector<bool>> seen(m, vector<bool>(n));
	auto cal = [&](int r, int c) -> pair<long long, long long> {
		seen[r][c] = true;
		deque<pair<int, int>> dq;
		dq.emplace_back(r, c);
		long long s{};
		map<pair<int, int>, set<pair<int, int>>> direction_to_adj_sides;

		while(!dq.empty()) {
			auto [r, c] = dq.front();
			s += 1;
			dq.pop_front();
			for(auto [dr, dc]: ds) {
				int nr = r + dr, nc = c + dc;
				if(nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] != grid[r][c]) {
					// For each direction, store all the outside cell
					direction_to_adj_sides[{dr, dc}].emplace(nr, nc);
					continue;
				}
				if(seen[nr][nc]) continue;
				seen[nr][nc] = true;
				dq.emplace_back(nr, nc);
			}
		}

		long long sides{};
		for(auto &[direction, adj_sides]: direction_to_adj_sides) {
			// For each direction, bfs all outside cells, each group will be a side
			set<pair<int, int>> seen_sides;
			for(auto [r, c]: adj_sides) {
				// cout << "direction " << direction.first << " " << direction.second << " " << r << " " << c << endl;
				if(seen_sides.find({r, c}) != seen_sides.end()) continue;
				deque<pair<int, int>> dq;
				dq.emplace_back(r, c);
				++sides;
				while(!dq.empty()) {
					auto [r, c] = dq.front();
					dq.pop_front();
					for(auto [dr, dc]: ds) {
						int nr = r + dr, nc = c + dc;
						if(adj_sides.find({nr, nc}) != adj_sides.end() &&
							seen_sides.find({nr, nc}) == seen_sides.end()) {
							seen_sides.emplace(nr, nc);
							dq.emplace_back(nr, nc);
						}
					}
				}

			}
		}

		return {s, sides};
	};

	long long result{};
	for(int r{}; r < m; ++r) {
		for(int c{}; c < n; ++c) {
			if(seen[r][c]) continue;
			auto [s, p] = cal(r, c);
			cout << grid[r][c] << " " << s << " " << p << endl;
			result += s * p;
		}
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

