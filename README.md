
# Exact Cover Problem Solver

This project solves the **Exact Cover Problem** using two different algorithms:
- **MAX-UCS**: A modified Uniform Cost Search that guarantees exact solutions.
- **Local Search**: A faster, heuristic method using Hill Climbing.

## 🔍 Problem Description
Given a set `X` and a collection `S` of subsets of `X`, the goal is to select a sub-collection `S*` such that:
- The union of all subsets in `S*` equals `X`.
- No two subsets in `S*` overlap (are disjoint).

## 🛠️ Algorithms Implemented
- `max_ucs_solver.py`: Implements the MAX-UCS algorithm.
- `local_search_solver.py`: Implements a Local Search with Hill Climbing.
- `test_local_search_all.py`: Runs Local Search on all benchmarks.
- `ECP_x.txt`: Benchmark input files for testing.

## 📊 Benchmark Files
We tested both algorithms on five benchmark files:
- `ECP_1.txt` to `ECP_5.txt`

## 📈 Results Summary

| File      | MAX-UCS Result | Local Search Result |
|-----------|----------------|----------------------|
| ECP_1     | ✅ Exact        | ✅ Exact             |
| ECP_2     | ✅ Exact        | ✅ Exact             |
| ECP_3     | ✅ Exact        | ❌ Partial           |
| ECP_4     | ❌ No Solution  | ❌ Partial           |
| ECP_5     | ❌ No Solution  | ❌ Partial           |

## 📦 Project Includes
- Python source code for both algorithms
- Benchmark files for testing

## 👨‍💻 How to Run
```bash
python local_search_solver.py ECP_1.txt
python test_local_search_all.py
```

## 📬 Contact
For questions or contributions, feel free to open an issue or fork the repo.
