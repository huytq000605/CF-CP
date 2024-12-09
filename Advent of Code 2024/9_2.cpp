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
#include <tuple>

using namespace std;


long long solve(string& line) {
	vector<pair<int, int>> files;
	vector<pair<int, int>> free;

	vector<int> disk;
	
	for(int i{}, idx{}; i < line.size(); ++i) {
		int v = line[i] - '0';
		for(int j{}; j < v; ++j) disk.emplace_back(i & 1 ? -1: static_cast<int>(files.size()));
		if(i&1) free.emplace_back(idx, v);
		else files.emplace_back(idx, v);
		idx += v;
	}

	for(int i = files.size() - 1; i >= 0; --i) {
		auto &[file_idx, file_size] = files[i];
		for(auto &[free_idx, free_size]: free) {
			if(free_idx < file_idx && free_size >= file_size) {
				for(int k{}; k < file_size; ++k) {
					disk[free_idx++] = i;
					disk[file_idx++] = -1;
				}
				free_size -= file_size;
				break;
			}
		}
	}

	// for(int c: disk) cout << ((c == -1) ? '.' : static_cast<char>(c + '0'));
	// cout << endl;

	long long result{};
	for(int i{}; i < disk.size(); ++i) {
		if(disk[i] != -1) result += disk[i] * i;
	}
	return result;
}

int main() {
  string line;
  while(getline(cin, line)) {
		// istringstream ss(line);
  }
	cout << solve(line) << endl;
}
