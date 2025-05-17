
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

## 📈 Results Comparison: Local Search vs. MAX-UCS

| File       | Local Search Result                      | MAX-UCS Result                            | Exact Cover Found?     |
|------------|-------------------------------------------|--------------------------------------------|-------------------------|
| ECP_1.txt  | ✅ `{3}, {2, 4}, {1, 5}`                  | ✅ `{3}`                                   | ✅ Both correct         |
| ECP_2.txt  | ✅ `{1, 4}, {3, 5, 6}, {2, 7}`            | ✅ `{1, 4}, {3, 5, 6}, {2, 7}`              | ✅ Matching             |
| ECP_3.txt  | ❌ Partial solution                       | ✅ Full solution                            | ❌ Only MAX-UCS correct |
| ECP_4.txt  | ❌ Partial solution                       | ✅ `{1,10,5}, {9,7}, {4,6}` (disjoint sets) | ✅ Only MAX-UCS correct |
| ECP_5.txt  | ❌ Partial solution                       | ✅ `{1–5}, {6–10}, ..., {26–30}`           | ✅ Only MAX-UCS correct |

### 🔍 Observations:
- **MAX-UCS** consistently finds exact covers in all benchmark files.
- **Local Search** only succeeded on smaller inputs (ECP_1, ECP_2).
- This highlights the trade-off:
  - **MAX-UCS** = accurate but slower.
  - **Local Search** = faster but not always complete.

## 📦 Project Includes
- Python source code for both algorithms
- Benchmark files for testing
- PowerPoint presentation (`.pptx`)
- Project report (optional)

## 👨‍💻 How to Run
```bash
python local_search_solver.py ECP_1.txt
python test_local_search_all.py
```

## 📬 Contact
For questions or contributions, feel free to open an issue or fork the repo.
