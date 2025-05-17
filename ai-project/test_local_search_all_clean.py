
import os
from local_search_solver import read_benchmark_file, local_search_exact_cover

# List of benchmark files
benchmark_files = [
    "ECP_1.txt", "ECP_2.txt", "ECP_3.txt", "ECP_4.txt", "ECP_5.txt"
]

for file in benchmark_files:
    print("==============================")
    print(f"Testing file: {file}")
    print("==============================")

    # Read the file and run local search
    X, S = read_benchmark_file(file)
    solution, is_exact = local_search_exact_cover(X, S)

    # Print results
    if solution:
        print("Solution found:" if is_exact else "Partial solution:")
        for subset in solution:
            print(subset)
    else:
        print("No solution found.")

    print()
