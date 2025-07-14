def multiply_iterative(N, M):
    """
    Multiplies two non-negative integers N and M using iterative addition.

    Args:
        N: The first non-negative integer (multiplicand).
        M: The second non-negative integer (multiplier).

    Returns:
        The product of N and M.

    Raises:
        ValueError: If N or M are negative.
    """
    if N < 0 or M < 0:
        raise ValueError("Both N and M must be non-negative for this multiplication method.")

    product = 0
    # Add N to itself M times
    for _ in range(M):
        product += N
    return product

def multiply_nim_inspired_bitwise(N, M):
    """
    Multiplies two non-negative integers N and M using a bit-wise approach,
    often called Russian Peasant Multiplication. This method is "Nim-inspired"
    in the sense that it relies on bit manipulations, similar to how bitwise
    operations are fundamental in understanding games like Nim (e.g., Nim-sum).

    Args:
        N: The first non-negative integer (multiplicand).
        M: The second non-negative integer (multiplier).

    Returns:
        The product of N and M.

    Raises:
        ValueError: If N or M are negative.
    """
    if N < 0 or M < 0:
        raise ValueError("Both N and M must be non-negative for this multiplication method.")

    result = 0
    current_N = N
    current_M = M

    # Loop while the multiplier (current_M) is greater than 0
    while current_M > 0:
        # If the least significant bit of current_M is 1 (i.e., current_M is odd)
        # then add current_N to the result. This means this power of 2 contributes.
        if current_M & 1:  # Bitwise AND with 1 checks the last bit
            result += current_N
        
        # Double current_N (equivalent to multiplying by 2, or left-shifting by 1 bit)
        current_N <<= 1
        
        # Halve current_M (equivalent to integer division by 2, or right-shifting by 1 bit)
        current_M >>= 1
        
    return result

# --- Main part of the program to test the functions ---
if __name__ == "__main__":
    print("--- Multiplication using Iterative Addition ---")
    
    test_cases_iterative = [
        (5, 7),
        (0, 10),
        (12, 0),
        (9, 3)
    ]

    for n_val, m_val in test_cases_iterative:
        try:
            product = multiply_iterative(n_val, m_val)
            print(f"  {n_val} * {m_val} = {product}")
        except ValueError as e:
            print(f"  Error for {n_val} * {m_val}: {e}")

    print("\n--- Multiplication using Nim-Inspired Bitwise (Russian Peasant) Method ---")

    test_cases_bitwise = [
        (5, 7),
        (0, 10),
        (12, 0),
        (9, 3),
        (13, 11), # Example where both N and M are non-powers of 2
        (25, 6)
    ]

    for n_val, m_val in test_cases_bitwise:
        try:
            product = multiply_nim_inspired_bitwise(n_val, m_val)
            print(f"  {n_val} * {m_val} = {product}")
        except ValueError as e:
            print(f"  Error for {n_val} * {m_val}: {e}")

    print("\n--- Testing with Negative Inputs (Expected Errors) ---")
    try:
        print(f"  -5 * 3 (iterative): {multiply_iterative(-5, 3)}")
    except ValueError as e:
        print(f"  Caught error for -5 * 3 (iterative): {e}")

    try:
        print(f"  7 * -4 (bitwise): {multiply_nim_inspired_bitwise(7, -4)}")
    except ValueError as e:
        print(f"  Caught error for 7 * -4 (bitwise): {e}")