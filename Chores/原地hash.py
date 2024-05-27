# 给你一个整数数组（有负数），找到这个数组中不存在的最小正整数
nums = [2,3,4,1,1]
def first_missing_positive(nums):
    n = len(nums)
    
    # Step 1: Mark numbers (num < 1 or num > n) with a special marker number (n+1)
    # We can ignore those because if all numbers are in range 1 to n, the missing number is n+1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Step 2: Mark each number that appears in the array
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first cell which isn't negative (i.e. the smallest missing positive)
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    # Step 4: If no cell is found, it means numbers 1 to n are present, so return n+1
    return n + 1

# Example usage:
print(first_missing_positive(nums))  # Output: 5
