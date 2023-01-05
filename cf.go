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
func max(nums ...int64) int64 {
  result := nums[0]
	for _, num := range nums {
		if num > result {
			result = num
		}
	}
	return result
}

func min(nums ...int64) int64 {
  result := nums[0]
  for _, num := range nums {
    if num < result {
      result = num
    }
  }
  return result
}

func main() {
	defer writer.Flush()

	var testcases int64
	scanf("%d", &testcases)
  var i int64
	for i = 0; i < testcases; i++ {
		var n, k int64
		scanf("%d %d", &n, &k)
    graph := make([][]int64, n)
    var j int 64
    for j = 2; j < n+1; j++ {
      graph[j] = make([]int, 0)
      var p int64
      scanf("%d", &p)
      graph[p-1] = append(graph[p-1], j)
    }

		print(solve(n, k, graph))
	}
}

func dfs(u) {

}

func solve(n, k int64, graph [][]int64) int64 {

}
