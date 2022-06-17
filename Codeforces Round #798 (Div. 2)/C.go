package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func print(a ...interface{})            { fmt.Println(a...) }
func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f+"\n", a...) }

func main() {
	defer writer.Flush()

	var testcases int
	scanf("%d", &testcases)
	for i := 0; i < testcases; i++ {
		var n int
		scanf("%d", &n)
		tree := make([][]int, n)
		for j := 0; j < n; j++ {
			tree[j] = make([]int, 0)
		}
		for j := 0; j < n-1; j++ {
			var u, v int
			scanf("%d %d", &u, &v)
			tree[u-1] = append(tree[u-1], v-1)
			tree[v-1] = append(tree[v-1], u-1)
		}
		print(solve(tree, n))
	}
}

func max(nums ...int) int {
	result := math.MinInt32
	for _, num := range nums {
		if num > result {
			result = num
		}
	}
	return result
}

func solve(tree [][]int, n int) int {
	count := make([]int, n)
	var count_child_node func(int, int) int
	count_child_node = func(node, parent int) int {
		children := make([]int, 0)
		result := 0
		for _, child := range tree[node] {
			if child == parent {
				continue
			}
			result += count_child_node(child, node)
			result += 1
			children = append(children, child)
		}
		tree[node] = children
		count[node] = result
		return result
	}
	count_child_node(0, -1)

	var dfs func(int) int
	dfs = func(node int) int {
		children := tree[node]
		switch len(children) {
		case 0:
			return 0
		case 1:
			return count[tree[node][0]]
		case 2:
			return max(count[children[0]]+dfs(children[1]), count[children[1]]+dfs(children[0]))
		default:
			return 0
		}
	}
	return dfs(0)
}
