# Liouville Function and Liouville Summatory Function - Python Implementation with Test Suite

A simple Python implementation of the **Liouville function** and its **summatory function**, allowing calculations for individual integers or a specified range.

## Mathematical Definition

The Liouville function is defined as:
<br><img width="136" height="32" alt="image" src="https://github.com/user-attachments/assets/c531b3a6-a5b3-44ad-a625-ab9bbb447ed7" />

where Ω(n) is the total number of prime factors of n, counted with multiplicity.

The summatory function is:
<br><img width="147" height="71" alt="image" src="https://github.com/user-attachments/assets/d20e48fd-a09c-41e1-8e4f-8b30a588e707" />
<br>The floor brackets in this function represent the greatest integer less than or equal to N. This ensures that the upper limit of the summation index remains an integer.

## Features

- Calculates the Liouville function for a positive integer.
- Calculates the sum of Liouville values over an inclusive range.
- Uses trial division for prime factorisation.
- Validates inputs and handles invalid values.
- Includes an inline test suite using Python assertions.

## Usage

**1. Clone the repository**

```bash
git clone <repository-url>
cd <repository-folder>
```

**2. Run the program**

```bash
python liouville_and_liouville_summatory.py
```

**3. Import and use the functions**

```python
from liouville_and_liouville_summatory import (
    liouville_single,
    liouville_summatory_range
)

print(liouville_single(12))
print(liouville_summatory_range(1, 10))
```

## Testing

Run the Python file to execute the included tests:

```bash
python liouville_and_liouville_summatory.py
```

The tests cover:
- The base case \(n=1\).
- Prime numbers and prime squares.
- Composite numbers.
- Summatory calculations over different ranges.
- Invalid inputs and ranges.

A successful run prints:

```text
All tests passed successfully!
```

### Extending the Tests

You can add more tests by inserting additional `assert` statements inside the existing `if __name__ == "__main__":` test block.

For example:

```python
assert liouville_single(36) == 1
assert liouville_single(72) == -1

assert liouville_summatory_range(1, 5) == -1
assert liouville_summatory_range(2, 5) == -2
```

To test invalid inputs, use a `try-except` block and assert that a `ValueError` is raised.

After adding tests, run the Python file again to check that they pass. Keep new tests inside the existing test block rather than creating a separate one.

## Requirements

- Python 3
- No external libraries required.
