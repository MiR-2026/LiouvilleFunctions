def liouville_single(n: int) -> int:
    if n < 1:
        raise ValueError("Liouville function is only defined for positive integers.")
    if n == 1:
        return 1
    omega = 0
    d = 2 
    while d * d <= n:
        while n % d == 0:
            omega += 1
            n //= d
        d += 1
    if n > 1:
        omega += 1
    return 1 if omega % 2 == 0 else -1

def liouville_summatory_range(start: int, end: int) -> int:
    if start < 1 or end < 1:
        raise ValueError("The range must consist of positive integers starting from 1.")
    if start > end:
        raise ValueError("The start of the range cannot be greater than the end.")
    total_sum = 0
    for n in range(start, end + 1):
        total_sum += liouville_single(n)
    return total_sum

# Test suite covering both Liouville functions
if __name__ == "__main__":
    print("Running inline tests...")

    # Fix 1 & 2: Added explicit lists to the iterations
    assert liouville_single(1) == 1, "Base case n=1 failed"
    
    for prime in [2, 3, 5, 7, 11, 13]:
        assert liouville_single(prime) == -1, f"Failed for prime {prime}"
        
    for square in [4, 9, 16, 25]:
        assert liouville_single(square) == 1, f"Failed for square {square}"
        
    # Fix 3: Replaced broken loop syntax with direct assertions
    assert liouville_single(8) == -1, "Failed for 8 (omega=3)"
    assert liouville_single(12) == -1, "Failed for 12 (omega=3)"

    assert liouville_summatory_range(1, 4) == 0, "Range 1-4 sum failed"
    assert liouville_summatory_range(1, 1) == 1, "Single element range failed"

    # Fix 4: Reliable exception checking pattern
    raised_single_error = False
    try:
        liouville_single(0)
    except ValueError:
        raised_single_error = True
    assert raised_single_error, "liouville_single(0) failed to raise ValueError"

    raised_range_error = False
    try:
        liouville_summatory_range(5, 2)
    except ValueError:
        raised_range_error = True
    assert raised_range_error, "Inverted range failed to raise ValueError"

    print("All tests passed successfully!")
