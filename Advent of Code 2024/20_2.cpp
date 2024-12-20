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
#include <climits>

using namespace std;
static constexpr array<pair<int, int>, 4> ds{{ {0,1}, {1,0}, {0,-1}, {-1,0} }};
using XY = pair<int, int>;


long long solve(vector<string>& grid) {
  int m = grid.size(), n = grid[0].size();
  int sr{}, sc{}, er{}, ec{};
  for(int r{}; r < m; ++r) {
    for(int c{}; c < n; ++c) {
      if(grid[r][c] == 'S') {
        sr = r; sc = c;
      } else if(grid[r][c] == 'E') {
        er = r, ec = c;
      }
    }
  }

  auto find_best_time = [m, n, &grid](int sr, int sc) -> vector<vector<long long>> {
    deque<pair<int, int>> dq;
    dq.emplace_back(sr, sc);
    vector<vector<long long>> dist(m, vector<long long>(n, LLONG_MAX));
    dist[sr][sc] = 0;
    long long s{};
    while(!dq.empty()) {
      int t = dq.size();
      while(t--) {
        auto [r, c] = dq.front(); dq.pop_front();
        for(auto [dr, dc]: ds) {
          int nr = r + dr, nc = c + dc;
          if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
          if(grid[nr][nc] == '#') continue;
          if(s+1 >= dist[nr][nc]) continue;
          dist[nr][nc] = s+1;
          dq.emplace_back(nr, nc);
        }
      }
      ++s;
    }

    return dist;
  };

  auto from_start = find_best_time(sr, sc);
  auto from_end = find_best_time(er, ec);
  long long d{from_start[er][ec]};
  cout << d << endl;
  long long result{};

  const int MAX_CHEAT = 20;
  const int SAVE = 100;
  for(int r1{}; r1 < m; ++r1) {
    for(int c1{}; c1 < n; ++c1) {
      if(grid[r1][c1] == '#') continue;
      for(int dr{-MAX_CHEAT}; dr <= MAX_CHEAT; ++dr) {
        for(int dc{-MAX_CHEAT}; dc <= MAX_CHEAT;  ++dc) {
          if(abs(dr) + abs(dc) > MAX_CHEAT) continue;
          int r2{r1+dr}, c2{c1+dc};
          if(r2 < 0 || r2 >= m || c2 < 0 || c2 >= n || grid[r2][c2] == '#') continue;
          if(from_start[r1][c1] + abs(dr) + abs(dc) + from_end[r2][c2] <= d - SAVE) {
            ++result;
          }
        }
      }
    }
  }
  return result;
}

int main() {
  string line;
  vector<string> grid;
  while(getline(cin, line)) {
    grid.emplace_back(line);
  }
  cout << solve(grid) << endl;
}

