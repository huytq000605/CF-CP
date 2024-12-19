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

long long ways(unordered_set<string>& towels, string& pattern) {
  vector<long long> dp(pattern.size() + 1, 0);
  dp[0] = 1;
  for(int i{}; i < pattern.size(); ++i) {
    string s{};
    for(int j{i}; j < pattern.size(); ++j) {
      s += pattern[j];
      if(towels.find(s) != towels.end()) {
        dp[j+1] += dp[i];
      }
    }
  }
  
  return dp.back();
}

long long solve(unordered_set<string>& towels, vector<string>& patterns) {
  long long result{};

  for(string &pattern: patterns) {
    vector<long long> dp(pattern.size(), -1);
    result += ways(towels, pattern);
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

