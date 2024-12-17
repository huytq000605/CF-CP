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
using XY = pair<long long, long long>;

long long solve(vector<long long> registers, vector<int> program) {
  vector<int> output;
  for(int i{}; i < program.size();) {
    int instruction{program[i++]};
    int operand{program[i++]};
    int literal_operand = operand;
    int combo_operand = operand <= 3 ? operand: registers[operand-4];
    switch (instruction) {
      case 0:
        registers[0] = registers[0] / pow(2, combo_operand);
        break;
      case 1:
        registers[1] ^= literal_operand;
        break;
      case 2:
        registers[1] = combo_operand % 8;
        break;
      case 3:
        if(registers[0]) {
          i = literal_operand;
        }
        break;
      case 4:
        registers[1] ^= registers[2];
        break;
      case 5:
        output.emplace_back(combo_operand % 8);
        break;
      case 6:
        registers[1] = registers[0] / pow(2, combo_operand);
        break;
      case 7:
        registers[2] = registers[0] / pow(2, combo_operand);
        break;
    }
  }

  for(int i{}; i < 3; ++i) {
    cout << "Register " << i + 1 << " " << registers[i] << endl;
  }
  for(int t: output) {
    cout << t << ",";
  }
  cout << endl;

  return 0;
}


int main() {
  string line;
  char ctemp{};
  vector<long long> registers(3, 0);
  for(int i{}; i < 3; ++i) {
    getline(cin, line);
    sscanf(line.c_str(), "Register %c: %lld", &ctemp, &registers[i]);
  }
  getline(cin, line);
  getline(cin, line);
  vector<int> program;
  int v{};
  line = line.substr(9);
  istringstream ss(line);
  while(ss >> v) {
    program.emplace_back(v);
    ss >> ctemp;
  }

  cout << "Program: ";
  for(int i: program) {
    cout << i << " ";
  }
  cout << endl;
  
  // while(getline(cin, line)) {
  //   grid.emplace_back(line);
  // }
	cout << solve(registers, program) << endl;
}

