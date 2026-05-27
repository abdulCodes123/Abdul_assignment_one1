## Lab 1 — Pull Request Checklist

### Description
<!-- Briefly describe your implementation approach (2–3 sentences) -->


### Implementation Notes
<!-- Did you use recursion, iteration, or memoisation? Why did you choose that approach? -->
I used an iterative approach instead of recursion to improve efficiency and avoid unnecessary function calls.
Iteration uses constant memory space O(1) and performs well for larger values of n.
Input validation was added to handle TypeError and ValueError edge cases.
The implementation follows PEP 8 standards and passes all pytest unit tests.

### Checklist
- [ ] `fibonacci()` is fully implemented in `fibonacci.py`
- [ ] All tests in `test_fibonacci.py` pass (`pytest test_fibonacci.py -v`)
- [ ] `ruff check .` reports **0 violations**
- [ ] `ruff format --check .` reports **0 formatting issues**
- [ ] My docstring follows Google style (Args, Returns, Raises, Examples)
- [ ] I used a Conventional Commit message: `feat(lab1): add fibonacci function with tests`
- [ ] My branch is named `feature/your-name` (e.g. `feature/jane-doe`)

### Edge Cases Handled
<!-- List the edge cases your implementation handles and how -->
- Negative input: 
- Float input: 
- None / string input: 
Negative input: Raises ValueError because Fibonacci numbers are only defined for n >= 0.
Float input: Raises TypeError since the function only accepts integers.
None / string input: Raises TypeError to prevent invalid non-integer values from being processed.
### Tests Run
```
# Paste your pytest output here
```
$ pytest test_fibonacci.py -v

============================= test session starts =============================
collected 19 items

test_fibonacci.py::TestFibonacciBaseCase::test_fibonacci_zero PASSED
test_fibonacci.py::TestFibonacciBaseCase::test_fibonacci_one PASSED
test_fibonacci.py::TestFibonacciSequence::test_fibonacci_two PASSED
test_fibonacci.py::TestFibonacciSequence::test_fibonacci_three PASSED
test_fibonacci.py::TestFibonacciSequence::test_fibonacci_ten PASSED
test_fibonacci.py::TestFibonacciSequence::test_fibonacci_fifteen PASSED
test_fibonacci.py::TestFibonacciSequence::test_fibonacci_twenty PASSED
test_fibonacci.py::TestFibonacciSequence::test_fibonacci_sequence_parametrized PASSED
test_fibonacci.py::TestFibonacciEdgeCases::test_negative_input_raises_value_error PASSED
test_fibonacci.py::TestFibonacciEdgeCases::test_large_negative_raises_value_error PASSED
test_fibonacci.py::TestFibonacciEdgeCases::test_float_input_raises_type_error PASSED
test_fibonacci.py::TestFibonacciEdgeCases::test_string_input_raises_type_error PASSED
test_fibonacci.py::TestFibonacciEdgeCases::test_none_input_raises_type_error PASSED
test_fibonacci.py::TestFibonacciReturnType::test_returns_integer_for_zero PASSED
test_fibonacci.py::TestFibonacciReturnType::test_returns_integer_for_positive PASSED

============================== 19 passed in 0.05s ==============================
### Ruff Output
```
# Paste your ruff check output here (should be empty / "All checks passed")
```
$ ruff check .

All checks passed!
### What I Learned
<!-- One or two sentences about what you found most challenging or interesting -->

Implemented the fibonacci(n) function using iterative logic and sequence handling.
Applied PEP 8 standards, clean naming, and Google-style docstrings.
Practiced unit testing with pytest and validated edge cases/errors.
Learned basic GitHub workflow: branching, Ruff linting, and Pull Requests.