# rubocop: disable all
require 'set'

def get_ints
  gets.split(' ').map(&:to_i)
end

def get_str
  gets
end

def get_int
  gets.to_i
end

def main
  testcases = gets.to_i
  testcases.downto(1) do
    gets
    vertices, edges = get_ints
    graph = Array.new(edges + 1).map {Array.new}
    edges.downto(1) do
      u, v, w = get_ints
      graph[u].push([v, w])
      graph[v].push([u, w])
    end
    puts solve(graph, vertices)
  end
end

def solve(graph, vertices)
	not_in_ans = 0
	ans = (1<<30) - 1
	30.downto(0) do |i|
		not_in_ans |= (1<<i)
		seen = Set[1]
		stack = [1]
		while stack.length > 0 do
			cur_node = stack.pop
			graph[cur_node].each do |next_node, weight|
				next if ( (seen.include?(next_node)) || ((weight & not_in_ans) != 0) )
				seen << next_node
				stack << next_node
			end
		end
		not_in_ans &= ~(1<<i)
		if seen.length == vertices
			not_in_ans |= (1<<i)
			ans &= ~(1<<i)
		end
	end

	ans
end

main
