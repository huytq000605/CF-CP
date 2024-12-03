
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>
#include <regex>

using namespace std;


pair<int, bool> solve(string line, bool enabled) {
	int result = 0;
	int n = line.size();
	for(int i{}; i < n; ++i) {
		if(line.substr(i, 7) == "don't()") {
			i = i + 6;
			enabled = false;
		}
		else if(line.substr(i, 4) == "do()") {
			i = i + 3;
			enabled = true;
		} else {
			int num1{}, num2{};
			bool valid = line.substr(i, 4) == "mul(";
			if (!valid) continue;
			valid = false;
			int j{i + 4};
			while (j < n && isdigit(line[j]))
			{
				num1 = num1 * 10 + (line[j++] - '0');
				valid = true;
			}
			if (!valid) continue;
			valid = j < n && line[j++] == ',';
			if (!valid) continue;
			valid = false;
			while (j < n && isdigit(line[j]))
			{
				num2 = num2 * 10 + (line[j++] - '0');
				valid = true;
			}
			if (!valid) continue;
			valid = line[j] == ')';
			if (valid && enabled)
			{
				result += num1 * num2;
			}
		}
	}
	return {result, enabled};
}


int main() {
  string line;
	int result{};
	bool enabled{true};
  while(getline(cin, line)) {
		auto [res, nenabled] = solve(line, enabled);
		result += res;
		enabled = nenabled;
  }
	cout << result << endl;
}
