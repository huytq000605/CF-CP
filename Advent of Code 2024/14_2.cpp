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
using XY = pair<long long, long long>;

int R{103}, C{101};

int find_biggest_group(vector<vector<int>> &grid) {
  vector<vector<int>> seen(R, vector<int>(C));
  auto dfs = [&](int r, int c, auto dfs) -> int {
    int result{1};
    for(auto [dr, dc]: ds) {
      int nr = r + dr;
      int nc = c + dc;
      if(nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
      if(grid[nr][nc] == 0 || seen[nr][nc]) continue;
      seen[nr][nc] = 1;
      result += dfs(nr, nc, dfs);
    }
    return result;
  };
  int result{};
  for(int r{}; r < R; ++r) {
    for(int c{}; c < C; ++c) {
      if(seen[r][c]) continue;
      seen[r][c] = 1;
      result = max(result, dfs(r, c, dfs));
    }
  }
  return result;
}

long long solve(vector<pair<XY, XY>> robots) {
  int t{1};
  while(t < 10000) {
    for(auto &[p, v]: robots) {
      p.first = (p.first + v.first + R) % R;
      p.second = (p.second + v.second + C) % C;
    }

    vector<vector<int>> grid(R, vector<int>(C));
    for(auto &[p, v]: robots) {
      grid[p.first][p.second] += 1;
    }

    int sz = find_biggest_group(grid);
    if(sz > 20) {
        for(auto &r: grid) {
           for(auto c: r) {
               if(c != 0) cout << c << " ";
               else cout << ". ";
             }
           cout << endl;
         }
      return t;
    }
    ++t;
  }
  return -1;
}


int main() {
  string line;
  vector<pair<XY, XY>> robots;
  while(getline(cin, line)) {
    int x{}, y{}, vx{}, vy{};
		sscanf(line.c_str(), "p=%d,%d v=%d,%d", &x, &y, &vx, &vy);
    robots.push_back({{y, x}, {vy, vx}});
  }
	cout << solve(robots) << endl;
}

