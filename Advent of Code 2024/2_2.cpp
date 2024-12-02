#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>

using namespace std;

bool check(vector<int> &A) {
  for(int remove = -1; remove < static_cast<int>(A.size()); ++remove) {
    vector<int> first2;
    int prev{};
    bool valid{true};
    for(int i{}; i < A.size(); ++i) {
      if(i == remove) continue;
      if(first2.size() < 2) first2.emplace_back(A[i]);
      if(first2.size() >= 2) {
        if(abs(A[i] - prev) < 1 || abs(A[i] - prev) > 3) {
          valid = false;
          break;
        }
        if(A[i] < prev != first2.back() < first2.front()) {
          valid = false;
          break;
        }
      }
      prev = A[i];
    }

    if(valid) {
      return true;
    }
  }

  return false;
}


int main() {
  string line;
  int result{};
  while(getline(cin, line)) {
    istringstream streamin(line);
    vector<int> l;
    int a{};
    while(streamin >> a) l.emplace_back(a);
    if(check(l)) {
      ++result;
      cout << line << endl;
    }
  }
  cout << result << endl;
}

