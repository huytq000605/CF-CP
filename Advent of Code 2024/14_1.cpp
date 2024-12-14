
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

long long solve(vector<pair<XY, XY>> robots) {
  int R{103}, C{101};
  for(auto &[p, v]: robots) {
    // cout << p.first << " " << p.second << endl;
    // cout << v.first << " " << v.second << endl;
    // cout << "-----------" << endl;
    int t{100};
    while(t--) {
      p.first = (p.first + v.first + R) % R;
      p.second = (p.second + v.second + C) % C;
    }
  }

  vector<vector<int>> grid(R, vector<int>(C));
  for(auto &[p, v]: robots) {
    cout << p.first << " " << p.second << endl;
    grid[p.first][p.second] += 1;
  }

  // for(auto &r: grid) {
  //   for(auto c: r) {
  //     if(c != 0) cout << c << " ";
  //     else cout << ". ";
  //   }
  //   cout << endl;
  // }
  //
  
  int u{}, v{}, w{}, z{};
  for(int r{}; r < R; ++r) {
    for(int c{}; c < C; ++c) {
        if(r < R/2 && c < C/2) u += grid[r][c];
        else if(r < R/2 && c > C/2) v += grid[r][c];
        else if(r > R/2 && c < C/2) w += grid[r][c];
        else if(r > R/2 && c > C/2) z += grid[r][c];
    }
  }

  cout << u << " " << v << " " << w << " " << z << endl;
  
  return u*v*w*z;
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

