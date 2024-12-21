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

long long solve(vector<string> &codes) {
  vector<string> numeric_keypad{
    "789", 
    "456", 
    "123", 
    ".0A"};
  unordered_map<char, pair<int, int>> numeric_map{
    {'7', {0, 0}},
    {'8', {0, 1}},
    {'9', {0, 2}},
    {'4', {1, 0}},
    {'5', {1, 1}},
    {'6', {1, 2}},
    {'1', {2, 0}},
    {'2', {2, 1}},
    {'3', {2, 2}},
    {'0', {3, 1}},
    {'A', {3, 2}},
  };
  vector<string> directional_keypad{
    ".^A", 
    "<v>"};
  unordered_map<char, pair<int, int>> directional_map{
    {'^', {0, 1}},
    {'A', {0, 2}},
    {'<', {1, 0}},
    {'v', {1, 1}},
    {'>', {1, 2}},
  };
  
  map<tuple<int, XY, XY>, long long> memo;
  auto cheapest = [&](int robot, pair<int, int> start, pair<int, int> dest, auto cheapest) -> long long {
    // if(robot == 0) 
    //   cout << "Robot: " << robot << " " << start.first << " " << start.second << " " << dest.first << " " << dest.second << endl;
    if(robot == 3) {
      return 1;
    }
    if(memo.find({robot, start, dest}) != memo.end()) {
      return memo[{robot, start, dest}];
    }

    vector<string>& keypad = robot == 0 ? numeric_keypad: directional_keypad;

    deque<pair<string, XY>> dq;
    dq.emplace_back("", start);
    vector<string> paths;
    while(!dq.empty()) {
      auto [path, pos] = dq.front(); dq.pop_front();
      if(pos == dest) {
        paths.emplace_back(path + 'A');
        continue;
      }
      if(keypad[pos.first][pos.second] == '.') continue;
      if(pos.first < dest.first) {
        dq.push_back({path + "v", {pos.first + 1, pos.second}});
      }
      if(pos.first > dest.first) {
        dq.push_back({path + "^", {pos.first - 1, pos.second}});
      }
      if(pos.second < dest.second) {
        dq.push_back({path + ">", {pos.first, pos.second + 1}});
      }
      if(pos.second > dest.second) {
        dq.push_back({path + "<", {pos.first, pos.second - 1}});
      }
    }

    long long result{LLONG_MAX};
    for(auto path: paths) {
      // cout << path << endl;
      char s = 'A';
      long long move{};
      for(char c: path) {
        move += cheapest(robot + 1, directional_map[s], directional_map[c], cheapest);
        s = c;
      }
      result = min(result, move);
    }

    memo[{robot, start, dest}] = result;
    return result;
  };
  
  long long result{};
  for(auto code: codes) {
    long long complexity = stoll(code.substr(0, 3));
    char start = 'A';
    long long move{};
    for(char c: code) {
      move += cheapest(0, numeric_map[start], numeric_map[c], cheapest);
      start = c;
    }
    cout << code << " " << move << endl;
    result += complexity * move;
  }
  return result;
}

int main() {
  string line;
  vector<string> codes;
  while(getline(cin, line)) {
    codes.emplace_back(line);
  }
  auto result = solve(codes);
  cout << "Result: " <<  result << endl;
}

