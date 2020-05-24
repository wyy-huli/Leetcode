# Leetcode
Leetcode-Python-Soultion
import collections
def majorityElement(nums):
    if nums == []: return
    h = collections.Counter(nums)
    for key in h:
        if h[key] > len(nums)//2:
            return key
