# LeetCode Practice (Python)

Solving LeetCode problems in Python, organized by topic.

## Structure

```
solutions/          ← your code
  arrays/
  strings/
  linked_list/
  trees/
  graphs/
  dynamic_programming/
  sorting/
  binary_search/
  stack_queue/

tests/              ← pytest test files (mirrors solutions/)
```

## Setup

```bash
pip install -r requirements.txt
```

## How to Run Tests

```bash
# Run all tests
pytest

# Run tests for a specific problem
pytest tests/arrays/test_lc0001_two_sum.py

# Run only solution1 tests
pytest tests/arrays/test_lc0001_two_sum.py::TestSolution1

# Run a single test
pytest tests/arrays/test_lc0001_two_sum.py::TestSolution1::test_basic

# Verbose output
pytest -v
```

## Progress

| # | Problem | Topic | Difficulty | Status |
|---|---------|-------|------------|--------|
| 1 | Two Sum | Arrays | Easy | 🔄 In Progress |
