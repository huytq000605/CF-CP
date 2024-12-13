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

using namespace std;
static constexpr array<pair<int, int>, 4> ds{{ {0,1}, {1,0}, {-1,0}, {0,-1} }};
using XY = pair<int, int>;

long long solve(XY A, XY B, XY P, int tapA, int tapB, map<tuple<int, int, int, int>, long long>& memo) {
	if(memo.find({P.first, P.second, tapA, tapB}) != memo.end()) {
		return memo[{P.first, P.second, tapA, tapB}];
	}
	if(P.first < 0 || P.second < 0) return 500;
	if(P.first == 0 && P.second == 0) return 0;
	int rA{500}, rB{500};
	if(tapA != 100) rA = solve(A, B, {P.first - A.first, P.second - A.second}, tapA + 1, tapB, memo) + 3;
	if(tapB != 100) rB = solve(A, B, {P.first - B.first, P.second - B.second}, tapA, tapB + 1, memo) + 1;
	memo[{P.first, P.second, tapA, tapB}] = min(rA, rB);
	return memo[{P.first, P.second, tapA, tapB}];
}


int main() {
  string line;
	long long result{};
  while(getline(cin, line)) {
		if(line == "") continue;
		int xa{}, ya{}, xb{}, yb{}, xp{}, yp{};
		sscanf(line.c_str(), "Button A: X+%d, Y+%d", &xa, &ya);
		getline(cin, line);
		sscanf(line.c_str(), "Button B: X+%d, Y+%d", &xb, &yb);
		getline(cin, line);
		sscanf(line.c_str(), "Prize: X=%d, Y=%d", &xp, &yp);
		// cout << xa << " " << ya << " " << xb << " " << yb << " " << xp << " " << yp << endl;
		map<tuple<int, int, int, int>, long long> memo{};
		long long res = solve({xa, ya}, {xb, yb}, {xp, yp}, 0, 0, memo);
		cout << res << endl;
		result += (res >= 500) ? 0: res;
  }
	cout << result << endl;
}

