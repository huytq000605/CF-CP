
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <sstream>
#include <regex>

using namespace std;

int solve(vector<string>& matrix) {
	int m = matrix.size(), n = matrix[0].size();
	int result{};
	string XMAS = "XMAS";
	vector<pair<int, int>> ds{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

	for(int r{}; r < m; ++r) {
		for(int c{}; c < n; ++c) {
			if(matrix[r][c] == 'X') {
				for (auto &[dr, dc] : ds)
				{
					int rr{r}, cc{c}, ii{0};
					while (ii < XMAS.size())
					{
						if (rr < 0 || rr >= m || cc < 0 || cc >= n)
							break;
						if (matrix[rr][cc] != XMAS[ii])
							break;
						++ii;
						rr += dr;
						cc += dc;
					}
					result += ii == XMAS.size();
				}
			}
		}
	}

	return result;
}

int main() {
  string line;
	vector<string> matrix;
  while(getline(cin, line)) {
		matrix.emplace_back(line);
  }
	cout << solve(matrix) << endl;
}
