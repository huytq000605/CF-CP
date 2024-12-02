#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>

using namespace std;

int main() {
  string line;
  int result{};
  while(getline(cin, line)) {
    istringstream is(line);
    int a{}, b{}, c{};
    is >> a >> b;
    if(abs(a - b) < 1 || abs(a-b) > 3) continue;
    bool valid{true};
    while(is >> c) {
      if(a < b != b < c) {
        valid = false;
        break;
      }
      if(abs(b-c) < 1 | abs(b-c) > 3) {
        valid = false;
        break;
      }
      b = c;
    }
    if(valid) ++result;
    cout << line << " " << valid << endl;
  }
  cout << result << endl;
}

