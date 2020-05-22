# Leetcode
Leetcode-Python-Soultion
def spiraOrder(matrix):
    res = []
    while matrix:
        res += list(matrix.pop(0))
        matrix = list(zip(*matrix))[::-1] #将矩阵逆时针反转
    return res
