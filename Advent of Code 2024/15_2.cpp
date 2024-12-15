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

vector<string> scale_grid(vector<string>& grid) {
  vector<string> new_grid;
  for(auto &r: grid) {
    string new_r;
    for(auto c: r) {
      if(c == '#') new_r += "##";
      else if(c == 'O') new_r += "[]";
      else if(c == '.') new_r += "..";
      else if(c == '@') new_r += "@.";
    }
    new_grid.emplace_back(new_r);
  }
  return new_grid;
}

long long solve(vector<string>& grid, vector<pair<int, int>> &commands) {
  grid = scale_grid(grid);
  int m = grid.size(), n = grid[0].size();
  pair<int, int> robot{-1, -1};
  for(int r{}; r < m && robot == make_pair(-1, -1); ++r) {
    for(int c{}; c < n; ++c) {
      if(grid[r][c] == '@') {
        robot = {r, c};
      }
    }
  }

  function<bool(int, int, int, int)> can_move = [&](int r, int c, int dr, int dc) -> bool {
    int nr = r + dr, nc = c + dc;
    if(grid[nr][nc] == '#') return false;
    else if(grid[nr][nc] == '.') return true;
    else if(dc == 0 && grid[nr][nc] == '[') {
      return can_move(nr, nc, dr, dc) && can_move(nr, nc+1, dr, dc);
    } else if(dc == 0 && grid[nr][nc] == ']') {
      return can_move(nr, nc, dr, dc) && can_move(nr, nc-1, dr, dc);
    } else {
      return can_move(nr, nc, dr, dc);
    }
  };

  function<void(int, int, int, int)> move = [&](int r, int c, int dr, int dc) {
    int nr = r + dr, nc = c + dc;
    if(dc == 0 && grid[nr][nc] == '[') {
      move(nr, nc, dr, dc);
      move(nr, nc+1, dr, dc);
    } else if(dc == 0 && grid[nr][nc] == ']') {
      move(nr, nc, dr, dc);
      move(nr, nc-1, dr, dc);
    } else if(grid[nr][nc] == '.') {
      
    } else {
      move(nr, nc, dr, dc);
    }
    swap(grid[r][c], grid[nr][nc]);
  };

  int t{};
  auto [r, c] = robot;
  for(auto [dr, dc]: commands) {
    int nr = r + dr, nc = c + dc;
    bool ok = can_move(r, c, dr, dc);
    if(ok) {
      move(r, c, dr, dc);
      r = nr, c = nc;
    }
  }

  for(auto &r: grid) {
   for(auto c: r) {
     cout << c << " ";
   }
   cout << endl;
  }
  
  long long result{};
  for(int r{}; r < m; ++r) {
    for(int c{}; c < n; ++c) {
      if(grid[r][c] == '[') {
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

