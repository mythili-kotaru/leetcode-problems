# Letter Combinations of a Phone Number (LeetCode 17)
# ---------------------------------------------------
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. The mapping follows a
# classic telephone keypad.
#
# Example:
#   Input: "23"
#   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Constraints:
#   1 <= len(digits) <= 4
#   digits[i] is a digit in the range ['2','9'].
# ---------------------------------------------------

def telephoneNumber(digits: str) -> list[str]:
    """Return all possible letter combinations for the input digits.

    The algorithm uses depth‑first search (backtracking). For each digit we
    iterate over its possible letters, appending to a temporary combination
    list. When the combination length equals the input length we join the
    characters and store the result.
    """
    if not digits:
        return []

    # Mapping from digit to its corresponding letters
    digit_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    res: list[list[str]] = []

    def dfs(comb: list[str], idx: int) -> None:
        # If the combination is complete, add to results
        if idx == len(digits):
            res.append(''.join(comb))
            return
        # Iterate over possible letters for the current digit
        for ch in digit_map[digits[idx]]:
            comb.append(ch)
            dfs(comb, idx + 1)
            comb.pop()

    dfs([], 0)
    return res

# ---------------------------------------------------
# Simple sanity tests (run with `python3 telephone_number.py`)
if __name__ == "__main__":
    assert sorted(telephoneNumber("23")) == sorted([
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
    ])
    assert sorted(telephoneNumber("2")) == sorted(["a", "b", "c"])
    assert telephoneNumber("") == []
    print("All tests passed!")
