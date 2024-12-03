#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>

using namespace std;


int solve(string line) {
	int result = 0;
	int n = line.size();
	for(int i{}; i < n; ++i) {
		int num1{}, num2{};
		bool valid = line.substr(i, 4) == "mul(";
		if(!valid) continue; 
		valid = false;
		int j{i+4};
		while(j < n && isdigit(line[j])) {
			num1 = num1 * 10 + (line[j++] - '0');
			valid = true;
		}
		if(!valid) continue;
		valid = j < n && line[j++] == ',';
		if(!valid) continue;
		valid = false;
		while(j < n && isdigit(line[j])) {
			num2 = num2 * 10 + (line[j++] - '0');
			valid = true;
		}
		if(!valid) continue;
		valid = line[j] == ')';
		if(valid) {
			result += num1 * num2;
		}
	}
	return result;
}


int main() {
  string line;
	int result{};
  while(getline(cin, line)) {
		result += solve(line);
  }
	cout << result << endl;
}

