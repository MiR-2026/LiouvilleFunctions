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
