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
  int sr{-1}, sc{-1};
  for(int r{}; r < m && sr == -1; ++r) {
    for(int c{}; c < n; ++c) {
      if(grid[r][c] == 'S') {
        sr = r;
        sc = c;
        break;
      }
    }
  }

  priority_queue<tuple<long long, XY, int>, 
    vector<tuple<long long, XY, int>>,
    decltype([](auto t1, auto t2) -> bool {
        return get<0>(t1) > get<0>(t2);
    })> pq;
  
  pq.push({0, {sr, sc}, 0});
  vector<vector<vector<long long>>> seen(m, vector<vector<long long>>(n, vector<long long>(4, LLONG_MAX)));
  seen[sr][sc][0] = 0;
  while(!pq.empty()) {
    auto [s, pos, di] = pq.top();
    pq.pop();
    auto [r, c] = pos;
    cout << r << " " << c << " " << di << endl;
    if(grid[r][c] == 'E') return s;
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

  return -1;
}


int main() {
  string line;
  vector<string> grid;
  while(getline(cin, line)) {
    grid.emplace_back(line);
  }
	cout << solve(grid) << endl;
}

