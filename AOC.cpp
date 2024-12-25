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

long long solve(unordered_map<string, long long> &wires) {
  vector<string> wire_names;
  for(auto [k, v]: wires) {
    if(k[0] == 'z') {
      wire_names.emplace_back(k);
    }
  }
  sort(wire_names.begin(), wire_names.end());
  long long power{1};
  long long result{};
  for(auto k: wire_names) {
    // cout << k << " " << wires[k] << " " << power << endl;
    result += wires[k] * power;
    power <<= 1;
  }
  return result;
}

int main() {
  string line;
  unordered_map<string, long long> wires;
  unordered_map<string, tuple<string, string, string>> equations;
  bool direct_value{true};
  while(getline(cin, line)) {
    if(line == "") {
      direct_value = false;
      continue;
    }
    istringstream ss(line);
    if(direct_value) {
      string wire{};
      long long v{};
      ss >> wire >> v;
      wires[wire.substr(0, wire.size() - 1)] = v;
    } else {
      string wire1{}, wire2{}, op{}, wire{}, strtemp{};
      ss >> wire1 >> op >> wire2 >> strtemp >> wire;
      equations[wire] = {wire1, wire2, op};
    }
  }

  function<long long(const string &)> find = [&](const string& wire) {
    if(wires.find(wire) != wires.end()) return wires[wire];
    auto &[wire1, wire2, op] = equations[wire];
    long long res{};
    if(op == "XOR") {
        res = find(wire1) ^ find(wire2);
    } else if(op == "OR") {
        res = find(wire1) | find(wire2);
    } else if(op == "AND") {
        res = find(wire1) & find(wire2);
    }
    wires[wire] = res;
    return res;
  };
  for(auto &[wire, _]: equations) {
    find(wire);
  }
  cout << wires.size() << endl;

  auto result = solve(wires);
  cout << "Result: " <<  result << endl;
}

