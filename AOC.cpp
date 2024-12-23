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

vector<vector<string*>> combinations(vector<string>& vertices, int n) {
  vector<vector<string*>> result;
  vector<string*> cur;
  cur.emplace_back(&vertices[0]);

  function<void(int)> dfs = [&](int i) {
    if(i == n) {
      result.push_back(cur);
      return;
    }

    for(int j{i}; j < vertices.size(); ++j) {
      if(cur.size() < n) {
        cur.emplace_back(&vertices[i]);
        dfs(j+1);
        cur.pop_back();
      }
    }
  };

  return result;
}

long long solve(vector<pair<string, string>> &edges)  {
  unordered_map<string, unordered_set<string>> graph;
  unordered_set<string> svertices;
  UF<string> uf{};
  for(auto [u, v]: edges) {
    graph[u].emplace(v);
    graph[v].emplace(u);
    svertices.emplace(u);
    svertices.emplace(v);
    uf.uni(u, v);
  }

  int scc{};
  for(auto u: svertices) {
    if(u == uf.find(u)) ++scc;
  }
  cout << "scc: " << scc << endl;
  
  vector<string> vertices(svertices.begin(), svertices.end());
  cout << vertices.size() << endl;

  return 0;
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

