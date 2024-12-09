
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

using namespace std;


long long solve(string& line) {
	vector<int> disk;
	
	for(int i{}, id{}; i < line.size(); ++i) {
		for(int j{}; j < line[i] - '0'; ++j) {
			disk.emplace_back(i & 1 ? -1 : id);
		}
		if(i&1) ++id;
	}
	for(int i = disk.size() - 1, j{}; i >= 0 && i > j; --i) {
		while(j < disk.size() && disk[j] != -1) ++j;
		if(disk[i] != -1 && j < i) { swap(disk[i], disk[j++]); }
	}
	
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
