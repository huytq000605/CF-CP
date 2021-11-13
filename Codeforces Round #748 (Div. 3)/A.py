def main():
	numOfTestcases = int(input())
	for i in range(numOfTestcases):
		print(solve(list(map(int, input().split()))))
 
def solve(votes):
	maxVote = max(*votes)
	flag = False
	dupplicate = False
	for vote in votes:
		if vote == maxVote and flag:
			dupplicate = True
		elif vote == maxVote:
			flag = True
		
	result = [0] * 3
	for i, vote in enumerate(votes):
		if vote < maxVote:
			result[i] = maxVote - vote + 1
		elif vote == maxVote and dupplicate:
			result[i] =  1
	return " ".join([str(result[i]) for i in range(len(result))])
 
 
if __name__ == "__main__":
	main()