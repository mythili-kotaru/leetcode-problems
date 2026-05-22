def combinationSum(nums, target):
    res = []

    def dfs(i, comb, total):
        # Base Case 1: We found a valid combination
        if total == target:
            res.append(comb[:])  # Append a copy of the list
            return
        
        # Base Case 2: We went over the target or ran out of numbers
        if total > target or i >= len(nums):
            return

        # Decision 1: Include nums[i]. We can reuse it, so 'i' stays the same.
        comb.append(nums[i])
        dfs(i, comb, total + nums[i])
        
        # Backtrack: Clean up the state before trying the next decision
        comb.pop()

        # Decision 2: Exclude nums[i] and move on to the next number
        dfs(i + 1, comb, total)
    
    dfs(0, [], 0)
    return res