#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>
#include <regex>
#include <array>
#include <set>

using namespace std;


long long solve(vector<vector<long long>> &equations) {
	auto possible = [](vector<long long> &eq) -> bool {
		long long target = eq[0];
		auto dfs = [&](long long cur, int i, auto dfs) -> bool {
			if(i >= eq.size()) return cur == target;
			return dfs(cur * eq[i], i+1, dfs) || dfs(cur + eq[i], i+1, dfs);
		};
		return dfs(eq[1], 2, dfs);
	};

	long long result{};
	for(auto &eq: equations) {
		if(possible(eq)) result += eq[0];
	}
	return result;
}

int main() {
	bool rule{false};
  string line;
	vector<vector<long long>> equations;
  while(getline(cin, line)) {
		char c{};
		long long a{};
		vector<long long> equation;
		istringstream ss(line);
		ss >> a >> c;
		equation.emplace_back(a);
		while(ss >> a) {
			equation.emplace_back(a);
		}
		equations.push_back(equation);
  }
	cout << solve(equations) << endl;
}
