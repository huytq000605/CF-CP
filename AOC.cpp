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

  auto find_best_time = [&]() -> long long {
    deque<pair<int, int>> dq;
    dq.emplace_back(sr, sc);
    vector<vector<bool>> seen(m, vector<bool>(n));
    seen[sr][sc] = false;
    int s{};
    while(!dq.empty()) {
      int t = dq.size();
      while(t--) {
        auto [r, c] = dq.front(); dq.pop_front();
        if(grid[r][c] == 'E') {
          return s;
          break;
        }
        for(auto [dr, dc]: ds) {
          int nr = r + dr, nc = c + dc;
          if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
          if(grid[nr][nc] == '#') continue;
          if(seen[nr][nc]) continue;
          seen[nr][nc] = true;
          dq.emplace_back(nr, nc);
        }
      }
      ++s;
    }

    return -1;
  };

  long long best_time = find_best_time();
  cout << "best_time " << best_time << endl;

  set<pair<XY, XY>> result;
  vector<vector<bool>> seen(m, vector<bool>(n));
  seen[sr][sc] = true;
  int s{};
  vector<XY> cheats;
  vector<vector<int>> memo(m, vector<int>(n, 0));
  function<void(int, int, int)> dfs = [&](int r, int c, int cheat) {
    if(grid[r][c] == 'E') {
      cout << cheats.size() << endl;
      result.insert({cheats[0], cheats[1]});
      return;
    }
    if(s > best_time - 76) return;
    if(cheat == 21) memo[r][c] = 1;
    
    for(auto [dr, dc]: ds) {
      int nr = r + dr;
      int nc = c + dc;
      if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
      if(seen[nr][nc]) continue;
      seen[nr][nc] = true;
      ++s;
      if(cheat == 21) {
        if(grid[nr][nc] == '#') {
          cheats.emplace_back(nr, nc);
          dfs(nr, nc, 20);
          cheats.pop_back();
        }
        dfs(nr, nc, cheat);
      } else {
        if(cheat) {
          if(cheat == 1) cheats.emplace_back(nr, nc);
          dfs(nr, nc, cheat - 1);
          if(cheat == 1) cheats.pop_back();

        } else {
          if(grid[nr][nc] != '#') dfs(nr, nc, 0);
        }
      }
      seen[nr][nc] = false;
      --s;
    }
  };
  dfs(sr, sc, 21);

  for(auto cheat: result) {
    auto [c1, c2] = cheat;
    char cell1 = grid[c1.first][c1.second];
    char cell2 = grid[c2.first][c2.second];
    grid[c1.first][c1.second] = '1';
    grid[c2.first][c2.second] = '2';
    cout << c1.first << " " << c1.second << " " << c2.first << " " << c2.second << endl;
    // for(auto &r: grid) {
    //   cout << r << endl;
    // }
    cout << "----------------------" << endl;
    grid[c1.first][c1.second] = cell1;
    grid[c2.first][c2.second] = cell2;
  }
  return static_cast<long long>(result.size());
}

long long solve(unordered_set<string>& towels, vector<string>& patterns) {
  long long result{};

  for(string &pattern: patterns) {
    vector<long long> dp(pattern.size(), -1);
    result += ways(towels, pattern);
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

