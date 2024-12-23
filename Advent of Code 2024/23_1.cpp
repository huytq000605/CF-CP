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

class UF {
public:
  int n{};
  vector<int> p;
  vector<int> r;

  UF(int _n): n(_n) {
    p.resize(n, 0);
    r.resize(n, 1);
    for(int i{}; i < n; ++i) {
      p[i] = i;
    }
  }

  int find(int u) {
    if(p[u] != u) {
      p[u] = find(p[u]);
    }
    return p[u];
  }

  int uni(int u, int v) {
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
  // unordered_map<string, int> name_mapping;
  // unordered_map<int, string> inverse_name_mapping;
  // for(auto [u, v]: edges) {
  //   if(name_mapping.find(u) == name_mapping.end()) {
  //     name_mapping[u] = static_cast<int>(name_mapping.size());
  //     inverse_name_mapping[name_mapping[u]] = u;
  //   }
  //   if(name_mapping.find(v) == name_mapping.end()) {
  //     name_mapping[v] = static_cast<int>(name_mapping.size());
  //     inverse_name_mapping[name_mapping[v]] = v;
  //   }
  // }
  // auto uf = UF(static_cast<int>(name_mapping.size()));
  // for(auto [u, v]: edges) {
  //   uf.uni(name_mapping[u], name_mapping[v]);
  // }
  //
  
  unordered_map<string, unordered_set<string>> graph;
  for(auto [u, v]: edges) {
    graph[u].emplace(v);
    graph[v].emplace(u);
  }

  long long result{};
  set<tuple<string, string, string>> s;
  for(auto [u, vs]: graph) {
    if(u[0] == 't') {
      for(auto v1: graph[u]) {
        for(auto v2: graph[u]) {
          if(v1 == v2) continue;
          if(graph[v1].find(v2) != graph[v1].end()) {
            vector<string> scc{u, v1, v2};
            sort(scc.begin(), scc.end());
            s.emplace(scc[0], scc[1], scc[2]);
          }
        }
      }
    }
  }

  return s.size();
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

