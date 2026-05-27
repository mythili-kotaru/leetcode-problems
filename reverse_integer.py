# ============================================================
# 7. Reverse Integer
# ============================================================
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer
# range [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers
# (signed or unsigned).
#
# Example 1:
#   Input: x = 123
#   Output: 321
#
# Example 2:
#   Input: x = -123
#   Output: -321
#
# Example 3:
#   Input: x = 120
#   Output: 21
#
# Constraints:
#   -2^31 <= x <= 2^31 - 1
# ============================================================


# ---- Solution: Digit Popping with Overflow Prevention ----
def reverse(x: int) -> int:
    """Reverse the digits of a signed 32-bit integer.

    Returns 0 if the reversed integer overflows the 32-bit signed range.
    """
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    res = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    while x != 0:
        pop = x % 10
        x //= 10
        
        # Check for 32-bit overflow before multiplying by 10.
        # INT_MAX // 10 is 214748364.
        if (res > INT_MAX // 10) or (res == INT_MAX // 10 and pop > 7):
            return 0
        
        res = res * 10 + pop
        
    return sign * res


# ============================================================
# Notes
# ============================================================
# Approach: Mathematical Digit Reversal
#   - We pop the last digit of the number using modulo (`x % 10`) and push it 
#     to the end of `res` (`res = res * 10 + pop`).
#   - To handle negative numbers in Python correctly, we extract the sign and 
#     work with the absolute value since Python's standard floor division (`//`) 
#     and modulo (`%`) behave differently on negative operands (e.g. `-123 // 10` 
#     is `-13` in Python, not `-12`).
#
# Overflow Checking under Constraints:
#   - The problem constraints specify that we cannot store 64-bit integers.
#   - Therefore, checking `res > INT_MAX` at the very end is technically a violation.
#   - To strictly obey this, we check for overflow *before* we perform the 
#     multiplication step:
#     1. If `res > INT_MAX // 10`, then `res * 10` will definitely overflow.
#     2. If `res == INT_MAX // 10`, it will overflow if `pop > 7` (since `INT_MAX` is 2147483647).
#
# Complexity Analysis:
#   - Time Complexity: O(log10(x))
#     The number of digits in x is approximately log10(x). We divide x by 10 
#     in each step, so the loop runs O(log10(x)) times.
#   - Space Complexity: O(1)
#     We use a constant amount of memory for auxiliary variables.
# ============================================================


# ---- Tests ----
if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
    assert reverse(0) == 0
    # Boundary testing: 32-bit limits
    assert reverse(1534236469) == 0  # Overflows when reversed (9646324351 > 2^31 - 1)
    assert reverse(-2147483648) == 0  # Underflows/overflows absolute limits
    print("All tests passed!")
