class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(N) — we iterate through the string once.
        Space Complexity: O(N) — the stack can hold at most N/2 characters in the worst case.
        """
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
