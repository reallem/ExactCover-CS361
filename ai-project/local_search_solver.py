
import random

def read_benchmark_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    X = set(map(int, lines[0].strip().split()))
    num_sets = int(lines[1].strip())
    S = [set(map(int, lines[i+2].strip().split())) for i in range(num_sets)]
    return X, S

def local_search_exact_cover(X, S, max_iterations=1000):
    def is_valid_solution(solution):
        union = set()
        for subset in solution:
            if not union.isdisjoint(subset):
                return False
            union.update(subset)
        return union == X

    def random_valid_solution():
        random_indices = list(range(len(S)))
        random.shuffle(random_indices)
        solution = []
        covered = set()
        for i in random_indices:
            if covered.issuperset(X):
                break
            if covered.isdisjoint(S[i]):
                solution.append(i)
                covered.update(S[i])
        return solution

    def get_neighbors(solution_indices):
        neighbors = []
        for i in range(len(S)):
            if i not in solution_indices:
                for j in range(len(solution_indices)):
                    new_solution = solution_indices[:]
                    new_solution[j] = i
                    if len(set(new_solution)) == len(new_solution):
                        neighbors.append(new_solution)
        return neighbors

    best_solution = random_valid_solution()
    best_score = len(set().union(*[S[i] for i in best_solution]))

    for _ in range(max_iterations):
        neighbors = get_neighbors(best_solution)
        improved = False
        for neighbor in neighbors:
            covered = set().union(*[S[i] for i in neighbor])
            if len(covered) > best_score and len(covered) == len(X) and is_valid_solution([S[i] for i in neighbor]):
                best_solution = neighbor
                best_score = len(covered)
                improved = True
                break
        if not improved:
            break

    return [S[i] for i in best_solution], best_score == len(X)

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python local_search_solver.py <benchmark_file>")
    else:
        filepath = sys.argv[1]
        X, S = read_benchmark_file(filepath)
        solution, is_exact = local_search_exact_cover(X, S)

        if solution:
            print("Solution found:" if is_exact else "Partial solution:")
            for subset in solution:
                print(subset)
        else:
            print("No solution found.")
