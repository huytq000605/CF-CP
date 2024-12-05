#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>
#include <regex>

using namespace std;

int solve(unordered_map<int, vector<int>> &graph, vector<vector<int>> &rules) {

	auto valid = [&](vector<int> &rule) {
		int n = rule.size();
		int prev{-1};
		bool valid{true};
		for(int i{}; i < n; ++i) {
			for(int j{i+1}; j < n; ++j) {
				int u = rule[i], v = rule[j];
				if(find(graph[v].begin(), graph[v].end(), u) != graph[v].end()) {
					swap(rule[i], rule[j]);
					valid = false;
				}
			}
		}
		return valid;
	};

	int result{};
	for(auto &rule: rules) {
		if(!valid(rule)) {
			result += *(rule.begin() + rule.size() / 2);
		}
	}
	return result;
}

int main() {
	unordered_map<int, vector<int>> graph;
	vector<vector<int>> rules;
	bool rule{false};
  string line;
  while(getline(cin, line)) {
		istringstream ss(line);
		if(line == "") {
			rule = true;
			continue;
		}
		if(!rule) {
			int u{}, v{};
			char c{};
			ss >> u >> c >> v;
			graph[u].emplace_back(v);
		} else {
			int num{};
			vector<int> nums{};
			while(ss >> num) {
				nums.emplace_back(num);
				char a{};
				ss >> a;
			}
			rules.push_back(nums);
		}
  }
	cout << solve(graph, rules) << endl;
}
