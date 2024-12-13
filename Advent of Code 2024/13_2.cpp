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
using XY = pair<long long, long long>;

long long solve(XY A, XY B, XY P) {
	// A.first * TA + B.first * TB = P.first
	// A.second * TA + B.second * TB = P.second
	// A.first * A.second * TA + B.first * A.second * TB = P.first * A.second
	// A.first * A.second * TA + B.second * A.first * TB = P.second * A.first
	// (B.first * A.second - B.second * A.first) * TB = P.first * A.second - P.second * A.first
	if((static_cast<long double>(A.second) / A.first) == (static_cast<long double>(B.second) / B.first)) {
		cout << "WTF" << endl;
		return 0;
	}
	long double ftB = static_cast<long double>(P.first * A.second - P.second * A.first) / (B.first * A.second - B.second * A.first);
	long long tB = (P.first * A.second - P.second * A.first) / (B.first * A.second - B.second * A.first);
	if(static_cast<long double>(tB) != ftB) return 0;
	long long tA = (P.first - B.first * tB) / A.first;
	long double ftA = static_cast<long double>(P.first - B.first * tB) / A.first;
	if(static_cast<long double>(tA) != ftA) return 0;
	if(tA < 0  || tB < 0) return 0;
	return 3 * tA + tB;
}


int main() {
  string line;
	long long result{};
  while(getline(cin, line)) {
		if(line == "") continue;
		long long xa{}, ya{}, xb{}, yb{}, xp{}, yp{};
		sscanf(line.c_str(), "Button A: X+%lld, Y+%lld", &xa, &ya);
		getline(cin, line);
		sscanf(line.c_str(), "Button B: X+%lld, Y+%lld", &xb, &yb);
		getline(cin, line);
		sscanf(line.c_str(), "Prize: X=%lld, Y=%lld", &xp, &yp);
		// cout << xa << " " << ya << " " << xb << " " << yb << " " << xp << " " << yp << endl;
		xp += 10000000000000;
		yp += 10000000000000;
		long long res = solve({xa, ya}, {xb, yb}, {xp, yp});
		cout << res << endl;
		result += res;
  }
	cout << result << endl;
}

