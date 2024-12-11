
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

using namespace std;
static constexpr array<pair<int, int>, 4> ds{{ {0,1}, {1,0}, {-1,0}, {0,-1} }};

long long solve(vector<long long> &stones) {
	int t{25};
	map<long long, long long> m;
	for(long long &stone: stones) ++m[stone];
	while(t--) {
		map<long long, long long> next_stones;
		for(auto [stone, count]: m) {
			// cout << stone << " ";
			if(stone == 0) next_stones[1] += count;
			else if((to_string(stone).size() & 1) == 0) {
				string ss = to_string(stone);
				long long left = stoi(ss.substr(0, ss.size() / 2));
				long long right = stoi(ss.substr(ss.size()/2, ss.size()/2));
				next_stones[left] += count;
				next_stones[right] += count;
			} else next_stones[stone * 2024] += count;
		}
		swap(m, next_stones);
	}
	long long result{};
	for(auto [_, count]: m) result += count;
	return result;
}

int main() {
  string line;
	vector<long long> stones;
  while(getline(cin, line)) {
		istringstream ss(line);
		long long stone{};
		while(ss >> stone) {
			stones.emplace_back(stone);
		}
  }
	cout << solve(stones) << endl;
}

