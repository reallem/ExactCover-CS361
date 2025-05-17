
from queue import PriorityQueue

def read_benchmark_file(filepath):
    """Reads the benchmark file and returns X and S"""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    X = set(map(int, lines[0].strip().split()))
    num_sets = int(lines[1].strip())
    S = [set(map(int, lines[i+2].strip().split())) for i in range(num_sets)]
    
    return X, S

def max_ucs(X, S):
    """Implements the MAX-UCS algorithm to solve the exact cover problem"""
    # Priority Queue (maximize coverage, so use -len for priority)
    frontier = PriorityQueue()
    # Each node: (-covered_count, covered_set, selected_subsets, used_indices)
    frontier.put((-0, set(), [], set()))
    expanded_nodes = []

    while not frontier.empty():
        neg_count, covered, selected, used = frontier.get()
        expanded_nodes.append(selected)

        if covered == X:
            return selected, expanded_nodes

        for i, subset in enumerate(S):
            if i not in used and covered.isdisjoint(subset):
                new_covered = covered.union(subset)
                new_selected = selected + [subset]
                new_used = used.union({i})
                frontier.put((-len(new_covered), new_covered, new_selected, new_used))

    return None, expanded_nodes

# Example usage
if __name__ == "__main__":
    filename = "ECP_5.txt"  # Change this to the path of your benchmark file
    X, S = read_benchmark_file(filename)
    solution, expanded = max_ucs(X, S)

    if solution:
        print("Solution found:")
        for subset in solution:
            print(subset)
    else:
        print("No solution found.")

    print("\nExpanded nodes:")
    for node in expanded:
        print(node)
