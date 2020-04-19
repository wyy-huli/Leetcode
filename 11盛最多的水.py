# Leetcode
Leetcode-Python-Soultion
def maxArea(height):
    h = []
    i = 0
    j = len(height)-1
    while i < j:
        a = j -i
        if height[i] < height[j]:
            b = height[i]
            i += 1
        elif height[i] > height[j]:
            b = height[j]
            j -= 1
        else:
            b = height[i]
            i += 1
            j -= 1
        h.append(a*b)
    return max(h)
