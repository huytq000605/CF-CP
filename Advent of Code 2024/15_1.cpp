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

long long solve(vector<string>& grid, vector<pair<int, int>> &commands) {
  int m = grid.size(), n = grid[0].size();
  pair<int, int> robot{-1, -1};
  for(int r{}; r < m && robot == make_pair(-1, -1); ++r) {
    for(int c{}; c < n; ++c) {
      if(grid[r][c] == '@') {
        robot = {r, c};
      }
    }
  }

  auto move = [&](int r, int c, int dr, int dc) -> bool {
    int rr = r, cc = c;
    while(r >= 0 && r < m && c >= 0 && c < n) {
      if(grid[r][c] == '#') return false;
      if(grid[r][c] == '.') {
        while(r != rr || c != cc) {
          swap(grid[r][c], grid[r - dr][c - dc]);
          r -= dr;
          c -= dc;
        }
        return true;
      }
      r += dr;
      c += dc;
    }
    return false;
  };

  int t{};
  auto [r, c] = robot;
  for(auto [dr, dc]: commands) {
    int nr = r + dr, nc = c + dc;
    bool moved = move(r, c, dr, dc);
    if(moved) {
      r = nr, c = nc;
    }
  }

  // for(auto &r: grid) {
  //   for(auto c: r) {
  //     cout << c << " ";
  //   }
  //   cout << endl;
  // }
  //
  long long result{};
  for(int r{}; r < m; ++r) {
    for(int c{}; c < n; ++c) {
      if(grid[r][c] == 'O') {
        result += r * 100 + c;
      }
    }
  }

  return result;
}


int main() {
  string line;
  vector<string> grid;
  bool input_grid = true;
  vector<pair<int, int>> commands;
  while(getline(cin, line)) {
    if(line == "") {
      input_grid = false;
      continue;
    }
    if(input_grid) grid.emplace_back(line);
    else {
      for(char c: line) {
        switch(c) {
          case 'v':
            commands.emplace_back(1, 0);
            break;
          case '^':
            commands.emplace_back(-1, 0);
            break;
          case '>':
            commands.emplace_back(0, 1);
            break;
          case '<':
            commands.emplace_back(0, -1);
            break;
        }
      }
    }
  }
	cout << solve(grid, commands) << endl;
}

