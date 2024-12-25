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
static constexpr array<pair<int, int>, 4> ds{{ {1,0}, {0,1}, {0,-1}, {-1,0} }};
using XY = pair<int, int>;

template <typename T> class UF {
public:
  unordered_map<T, T> p;
  unordered_map<T, int> r;

  UF() {
  }

  T find(T u) {
    if(p.find(u) == p.end()) {
      p[u] = u;
      r[u] = 1;
    }
    if(p[u] != u) {
      p[u] = find(p[u]);
    }
    return p[u];
  }

  int uni(T u, T v) {
    u = find(u);
    v = find(v);
    if(u == v) return 0;
    if(r[u] < r[v]) swap(u, v);
    p[v] = u;
    r[u] += r[v];
    return 0;
  }
};

long long solve(vector<vector<int>> &locks, vector<vector<int>> &keys) {
  long long result{};
  for(auto &lock: locks) {
    // for(int i{}; i < 5; ++i) {
    //   cout << lock[i] << " ";
    // }
    // cout << endl;
    for(auto &key: keys) {
      bool fit{true};
      // for(int i{}; i < 5; ++i) {
      //   cout << key[i] << " ";
      // }
      // cout << endl;
      for(int i{}; i < 5; ++i) {
        if(lock[i] + key[i] > 5) fit = false;
      }

      if(fit) ++result;
    }
  }

  return result;
}

int main() {
  string line;
  vector<vector<int>> locks;
  vector<vector<int>> keys;
  vector<int> vals(5, 0);
  bool is_key{};
  bool determined{false};
  while(getline(cin, line)) {
    if(line == "") {
      determined = false;
      if(is_key) {
        keys.push_back(vals);
      } else {
        locks.push_back(vals);
      }
      for(int i{}; i < 5; ++i) vals[i] = 0;
      continue;
    }
    if(!determined) {
      determined = true;
      is_key = line[0] == '.';
      if(is_key) {
        for(int i{}; i < 5; ++i) vals[i] = -1;
      }
      continue;
    }
    for(int i{} ; i < 5; ++i) {
      vals[i] += line[i] == '#';
    }
  }

  auto result = solve(locks, keys);
  cout << "Result: " <<  result << endl;
}

