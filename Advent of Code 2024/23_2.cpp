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

long long solve(vector<pair<string, string>> &edges)  {
  unordered_map<string, unordered_set<string>> graph;
  for(auto [u, v]: edges) {
    graph[u].emplace(v);
    graph[v].emplace(u);
  }

  vector<string> vertices;
  for(auto &[u, _]: graph) {
    vertices.emplace_back(u);
  }
  vector<string> cur;
  vector<string> result{};
  function<void(int)> dfs = [&](int i) {
    if(cur.size() > result.size()) {
      result = vector<string>(cur.begin(), cur.end());
    }
    if(i >= vertices.size()) return;

    string u = vertices[i];
    bool valid{true};
    for(auto v: cur) {
      if(graph[u].find(v) == graph[u].end()) {
        valid = false;
        break;
      }
    }
    if(valid) {
      cur.emplace_back(u);
      dfs(i+1);
      cur.pop_back();
    }
    dfs(i+1);
  };

  dfs(0);
  sort(result.begin(), result.end());
  for(auto u: result) {
    cout << u << ",";
  }
  cout << endl;

  return result.size();
}

int main() {
  string line;
  vector<pair<string, string>> edges;
  while(getline(cin, line)) {
    if(line == "") break;
    string u{}, v{};
    u = line.substr(0, 2);
    v = line.substr(3, 2);
    edges.emplace_back(u, v);
  }
  auto result = solve(edges);
  cout << "Result: " <<  result << endl;
}

