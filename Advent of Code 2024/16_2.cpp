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
#include <queue>
#include <tuple>

using namespace std;
static constexpr array<pair<int, int>, 4> ds{{ {0,1}, {1,0}, {0,-1}, {-1,0} }};
using XY = pair<long long, long long>;

long long solve(vector<string>& grid) {
  int m = grid.size(), n = grid[0].size();
  int sr{-1}, sc{-1}, er{-1}, ec{-1};
  for(int r{}; r < m; ++r) {
    for(int c{}; c < n; ++c) {
      if(grid[r][c] == 'S') {
        sr = r;
        sc = c;
      }

      if(grid[r][c] == 'E') {
        er = r;
        ec = c;
      }
    }
  }

  auto dijkstra = [&](int sr, int sc, int sdi) {
    priority_queue<tuple<long long, XY, int>, 
    vector<tuple<long long, XY, int>>,
    decltype([](auto t1, auto t2) -> bool {
        return get<0>(t1) > get<0>(t2);
    })> pq;
    vector<vector<vector<long long>>> seen(m, vector<vector<long long>>(n, vector<long long>(4, LLONG_MAX)));

    pq.push({0, {sr, sc}, sdi});
    seen[sr][sc][0] = 0;

    while(!pq.empty()) {
      auto [s, pos, di] = pq.top();
      pq.pop();
      auto [r, c] = pos;
      // following the direction
      int nr = r + ds[di].first, nc = c + ds[di].second;
      if(grid[nr][nc] != '#' && s + 1 < seen[nr][nc][di]) {
        seen[nr][nc][di] = s + 1;
        pq.push({s+1, {nr, nc}, di});
      }

      // turn 90*
      for(int ndi: {(di-1+4)%4, (di+1)%4}) {
        if(s + 1000 < seen[r][c][ndi]) {
          seen[r][c][ndi] = s + 1000;
          pq.push({s+1000, {r, c}, ndi});
        }
      }
    }

    return seen;
  };

	// sS[r][c][di] = shorest path from S to [r,c] when heading at ds[di] direction
  auto sS = dijkstra(sr, sc, 0);
  // auto sE = dijkstra(er, ec, 2);

	long long best_path{LLONG_MAX};
  for(int di{}, distance{}; di < 4; ++di) {
    best_path = min(best_path, sS[er][ec][di]);
  }

	set<pair<int, int>> result;
  auto dfs = [&](int r, int c, int di, long long cost, auto dfs) -> bool {
    if(grid[r][c] == '#' || cost > best_path || cost > sS[r][c][di]) return false;
    if(grid[r][c] == 'E') return true;
    bool res = dfs(r + ds[di].first, c + ds[di].second, di, cost + 1, dfs);
    res |= dfs(r, c, (di-1+4) % 4, cost + 1000, dfs);
    res |= dfs(r, c, (di+1) % 4, cost + 1000, dfs);

    if(res) {
      result.emplace(r, c);
      return true;
    }

    return false;
  };
  dfs(sr, sc, 0, 0, dfs);

  return result.size() + 1;
}


int main() {
  string line;
  vector<string> grid;
  while(getline(cin, line)) {
    grid.emplace_back(line);
  }
	cout << solve(grid) << endl;
}

