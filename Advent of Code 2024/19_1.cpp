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

bool possible(unordered_set<string>& towels, string& pattern, int i = 0) {
  if(i >= pattern.size()) return true;
  for(int j{i}; j < pattern.size(); ++j) {
    if(towels.find(pattern.substr(i, j - i + 1)) != towels.end()) {
      if(possible(towels, pattern, j+1)) return true;
    }
  }
  
  return false;
}

long long solve(unordered_set<string>& towels, vector<string>& patterns) {
  long long result{};

  for(string &pattern: patterns) {
    if(possible(towels, pattern)) ++result;
  }
  
  return result;
} 


int main() {
  string line;

  unordered_set<string> towels;
  getline(cin, line);
  string towel{};
  istringstream ss(line);
  while(ss >> towel) {
    if(towel.back() == ',') towel = towel.substr(0, towel.size() - 1);
    towels.emplace(towel);
  }

  getline(cin, line);
  
  vector<string> patterns;
  while(getline(cin, line)) {
    patterns.emplace_back(line);
  }

  cout << solve(towels, patterns) << endl;

  return 0;
}

