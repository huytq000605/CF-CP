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


long long solve(vector<XY>& bytes) {
  int m{71}, n{71};
  int first_bytes{1024};
  vector<vector<int>> grid(m, vector<int>(n, 0));
  for(auto [x, y]: bytes) {
    grid[x][y] = 1;
    first_bytes--;
    if(!first_bytes) break;
  }
  for(auto &r: grid) {
    for(auto c: r) {
      cout << c;
    }
    cout << endl;
  }
  priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, 
      decltype([](auto t1, auto t2) -> bool {
          return get<0>(t1) > get<0>(t2);
        })> pq;
  vector<vector<int>> distances(m, vector<int>(n, INT_MAX));

  pq.emplace(0, 0, 0);
  distances[0][0] = 0;
  while(!pq.empty()) {
    auto [s, r, c] = pq.top();
    if(r == m-1 && c == n-1) {
      return s;
    }
    pq.pop();
    for(auto [dr, dc]: ds) {
      int nr = r + dr, nc = c + dc;
      if(nr < 0 || nr >= m || nc < 0 || nc >= n) {
        continue;
      }
      if(grid[nr][nc] == 1 || s + 1 >= distances[nr][nc]) continue;
      distances[nr][nc] = s + 1;
      pq.emplace(s+1, nr, nc);
    }
  }
  
  return -1;
}


int main() {
  string line;
  vector<XY> bytes;
  while(getline(cin, line)) {
    int x{}, y{};
    sscanf(line.c_str(), "%d,%d", &x, &y);
    bytes.emplace_back(y, x);
  }

  cout << solve(bytes) << endl;
}

