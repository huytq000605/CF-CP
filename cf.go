package main

import (
	"fmt"
	"bufio"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func print(a ...interface{}) { fmt.Println(a...) }
func scanf(f string, a ...interface{}) { fmt.Fscanf(reader, f + "\n", a...) }

func main() {
	defer writer.Flush()

	var testcases int
	scanf("%d", &testcases)
	for i := 0; i < testcases; i++ {
		scanf("%s")
		var vertices, edges int
		scanf("%d %d", &vertices, &edges)
		graph := make([][][]int, vertices + 1)
		for i := range(graph) {
			graph[i] = make([][]int, 0)
		}
		for j := 0; j < edges; j++ {
			var u, v, w int
			scanf("%d %d %d", &u, &v, &w)
			graph[u] = append(graph[u], []int{v, w})
			graph[v] = append(graph[v], []int{u, w})
		}
		print(solve(graph, vertices))
	}
}

func solve(graph [][][]int, vertices int) int {
	result := (1<<30) - 1
	notInAns := 0
	for i := 30; i >= 0; i-- {
		stack := []int{1}
		seen := make(map[int]struct{})
		notInAns |= (1<<i)
		for len(stack) > 0 {
			current := stack[len(stack) - 1]
			stack = stack[:len(stack) - 1]
			for _, data := range graph[current] {
				next, weight := data[0], data[1]
				if _, found := seen[next]; found {
					continue
				}
				if weight & notInAns != 0 {
					continue
				}
				stack = append(stack, next)
				seen[next] = struct{}{}
			}
		}
		notInAns &= ^(1<<i)
		if len(seen) == vertices {
			notInAns |= (1<<i)
			result &= ^(1<<i)
		}
	}
	return result
}