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

	var testcases int64
	scanf("%d", &testcases)
  var i int64
	for i = 0; i < testcases; i++ {
		var n, x, y int64
		scanf("%d %d %d", &n, &x, &y)
    var a, b string
    scanf("%s", &a)
    scanf("%s", &b)

		print(solve(n, x, y, a, b))
	}
}

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

func solve(n, x, y int64, a, b string) int64 {
  diffs := make([]int64, 0, n)
  var i int64
  for i = 0; i < n; i++ {
    if a[i] != b[i] {
      diffs = append(diffs, i)
    }
  }

  m := int64(len(diffs))

  if m % 2 == 1 {
    return -1
  }

  if x >= y {
    if m == 2 && diffs[0] + 1 == diffs[1] {
      return min(x, y*2)
    }
    return y * m / 2
  }

  dp := make([][]int64, m)
  for i = 0; i < m; i++ {
    dp[i] = make([]int64, m)
    var j int64
    for j = 0; j < m; j++ {
      dp[i][j] = -1
    }
  }
  var dfs func(i, drop int64) int64
  dfs = func(i, drop int64) int64 {
    if i >= m {
      if drop == 0 {
        return 0
      }
      return math.MaxInt64
    }
    if dp[i][drop] != -1 {
      return dp[i][drop]
    }
    result := dfs(i+1, drop+1)
    if drop > 0 {
      this := dfs(i+1, drop-1)
      if this != math.MaxInt64 {
        result = min(result, this + y)
      }
    }
    if i < m-1 {
      this := dfs(i+2, drop)
      if this != math.MaxInt64 {
        result = min(result, this + min(y, x * (diffs[i+1] - diffs[i])))
      }
    }
    dp[i][drop] = result
    return result
  }
  res := dfs(0, 0)
  return res
}

