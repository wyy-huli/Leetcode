# Leetcode
Leetcode-Python-Soultion
贪心算法
def findContentChildren(g,s):
    s.sort()
    g.sort()
    i = 0 #孩子i
    j = 0#饼干j
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j+=1
    return i
