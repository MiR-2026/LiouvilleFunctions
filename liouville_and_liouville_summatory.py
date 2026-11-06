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
