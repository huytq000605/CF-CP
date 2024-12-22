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

string ha(deque<int>& dq) {
  string result{};
  for(int num: dq) {
    result += to_string(num);
  }
  return result;
}

long long solve(vector<long long> &secrets)  {
  long long result{};
  const long long PRUNE = 16777216;
  unordered_map<string, long long> total_bananas;

  for(auto &secret: secrets) {
    unordered_map<string, long long> bananas;
    deque<int> dq;
    for(int t{}; t < 2000; ++t) {
      long long original = secret % 10;
      long long mul = secret * 64;
      secret ^= mul;
      secret %= PRUNE;
      long long div = secret / 32;
      secret ^= div;
      secret %= PRUNE;
      mul = secret * 2048;
      secret ^= mul;
      secret %= PRUNE;
      long long current = secret % 10;
      dq.emplace_back(current - original);
      if(dq.size() > 4) dq.pop_front();
      string h = ha(dq);
      if(bananas.find(h) == bananas.end()) {
        bananas[h] = current;
      }
    }

    for(auto [seq, banana]: bananas) {
      total_bananas[seq] += banana;
      result = max(result, total_bananas[seq]);
    }
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

