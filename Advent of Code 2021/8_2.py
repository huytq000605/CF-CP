import sys
import collections
import math
import itertools
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


def main():
	lines = sys.stdin.read().splitlines()
	print(solve(lines))

class BreakOutException(Exception):
	pass

def sort_string(s):
	return "".join(sorted(s))

def solve(lines):
	nums = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
	arr = ["a", "b", "c", "d", "e", "f", "g"]
	finalResult = 0
	for line in lines:
		before, after = line.split("|")
		before = before.split()
		after = after.split()

		for i, word in enumerate(before):
			before[i] = sort_string(word)
		
		for i, word in enumerate(after):
			after[i] = sort_string(word)

		for arr1 in itertools.permutations(arr, len(arr)):
			try: 
				mappingLetter = {arr[i]: arr1[i] for i in range(len(arr))}
				newNums = []
				for num in nums:
					newNum = ""
					for l in num:
						newNum += mappingLetter[l]
					newNum = sort_string(newNum)
					newNums.append(newNum)

				newNums = {newNums[i]: i for i in range(len(nums))}
				result = 0
				
				for word in before:
					word = sort_string(word)
					if word not in newNums:
						raise BreakOutException
				
				for word in after:
					word = sort_string(word)
					if word not in newNums:
						raise BreakOutException
					else:
						result = result * 10
						result += newNums[word]
				finalResult += result
			except BreakOutException:
				continue
		


	return finalResult




if __name__ == "__main__":
	main()
