# ============================================================
# 22. Generate Parentheses
# ============================================================
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# Example 1: n = 3 → ["((()))","(()())","(())()","()(())","()()()"]
# Example 2: n = 1 → ["()"]
#
# Constraints: 1 <= n <= 8
# ============================================================


# ---- Solution: Backtracking (DFS) ----
def paranthesis(n: int) -> list[str]:
    res = []

    def dfs(closeN: int, openN: int, comb: list[str]) -> None:
        # Base case: used n open and n close parens → valid combination
        if openN == closeN == n:
            res.append(''.join(comb))
            return

        # Add '(' as long as we haven't used all n open parens
        if openN < n:
            comb.append('(')
            dfs(closeN, openN + 1, comb)
            comb.pop()

        # Add ')' only if there is an unmatched '(' to close
        if closeN < openN:
            comb.append(')')
            dfs(closeN + 1, openN, comb)
            comb.pop()

    dfs(0, 0, [])
    return res


# ============================================================
# Notes
# ============================================================
# Approach: Backtracking
#   - Track two counters: openN (open parens placed) and
#     closeN (close parens placed).
#   - Rule 1: Add '(' whenever openN < n.
#   - Rule 2: Add ')' only when closeN < openN (there is an
#     unmatched '(' available to close).
#   - These two rules guarantee every generated string is valid
#     without needing any post-generation filtering.
#
# Complexity Analysis:
#   - Time: O(4^N / √N)
#     The number of valid combinations equals the Nth Catalan
#     number:  C(N) = C(2N, N) / (N+1) ≈ 4^N / (N^(3/2) * √π)
#     Building each combination takes O(N) work (string join),
#     so total time ≈ O(4^N / √N).
#
#     Note: This is NOT simply "2 choices at each step = 2^(2N)".
#     The pruning constraints reduce the actual branching factor
#     below 2, and the resulting count is the Catalan number.
#
#   - Auxiliary Space: O(N)
#     The recursion stack goes at most 2N levels deep (one level
#     per character added). The `comb` list is at most length 2N.
#     Both are O(N). The output list is excluded from auxiliary
#     space (it is the required output).
# ============================================================


# ---- Tests ----
assert sorted(paranthesis(1)) == ["()"]
assert sorted(paranthesis(2)) == sorted(["(())", "()()"])
assert sorted(paranthesis(3)) == sorted(["((()))","(()())","(())()","()(())","()()()"])
print("All tests passed!")
