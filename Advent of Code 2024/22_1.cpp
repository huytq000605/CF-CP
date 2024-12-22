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

long long solve(vector<long long> &secrets)  {
  long long result{};
  const long long PRUNE = 16777216;
  for(auto &secret: secrets) {
    for(int t{}; t < 2000; ++t) {
      long long mul = secret * 64;
      secret ^= mul;
      secret %= PRUNE;
      long long div = secret / 32;
      secret ^= div;
      secret %= PRUNE;
      mul = secret * 2048;
      secret ^= mul;
      secret %= PRUNE;
      // cout << secret << endl;
    }

    result += secret;
  }

  return result;
}

int main() {
  string line;
  vector<long long> secrets;
  while(getline(cin, line)) {
    long long secret;
    sscanf(line.c_str(), "%lld", &secret);
    secrets.emplace_back(secret);
  }
  auto result = solve(secrets);
  cout << "Result: " <<  result << endl;
}

