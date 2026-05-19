# ============================================================
# Reverse Integer
# ============================================================
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit
# integer range [-2^31, 2^31 - 1], return 0.
#
# Example 1: x = 123  → 321
# Example 2: x = -123 → -321
# Example 3: x = 120  → 21
#
# Constraints: -2^31 <= x <= 2^31 - 1
# ============================================================


# ---- Solution: Build reversed number digit by digit ----
def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0

    while x > 0:
        rev = rev * 10 + x % 10   # BUG FIX: was `x * 10` — must build up `rev`, not multiply x
        x = x // 10

    rev = sign * rev              # BUG FIX: apply sign (was missing entirely)

    if rev < -(2**31) or rev > 2**31 - 1:
        return 0

    return rev


# ============================================================
# Notes
# ============================================================
# Approach: Extract digits from the right, build reversed number from the left
#   - `x % 10`  → gives the last (rightmost) digit of x
#   - `x // 10` → strips that digit off x
#   - `rev * 10 + digit` → appends that digit to the right of rev
#
# Trace for x = 123:
#   x=123, rev=0  → digit=3, rev=0*10+3=3,    x=12
#   x=12,  rev=3  → digit=2, rev=3*10+2=32,   x=1
#   x=1,   rev=32 → digit=1, rev=32*10+1=321,  x=0
#   loop ends → rev=321 ✓
#
# Bug fixes:
#   1. `rev = x * 10 + x % 10` → `rev = rev * 10 + x % 10`
#      (was multiplying x instead of accumulating into rev)
#   2. `sign` was computed but never applied to the result
#
# Time Complexity:  O(log x) — the loop runs once per digit, and the
#                   number of digits in x is ⌊log₁₀(x)⌋ + 1
#                   (your "O(N) over every digit" intuition is right;
#                   O(log x) is just the formal way to say it when
#                   N = the numeric value of x, not the digit count)
# Space Complexity: O(1) — only a few integer variables, no extra storage
# ============================================================


# ---- Tests ----
assert reverse(123) == 321
assert reverse(-123) == -321
assert reverse(120) == 21
assert reverse(0) == 0
assert reverse(2**31 - 1) == 0   # edge: overflows on reverse
assert reverse(-2**31) == 0      # edge: overflows on reverse
print("All tests passed!")
