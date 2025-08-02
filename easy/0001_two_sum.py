# 0001. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/

"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
