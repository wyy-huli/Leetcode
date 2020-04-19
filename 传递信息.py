# Leetcode
Leetcode-Python-Soultion
BFS解法：
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        queue = collections.deque()
        queue.append(0)
        step = 0
        res = 0
        while queue and step <= k:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur == n - 1 and step == k:
                    res += 1
                for rel in relation:
                    if rel[0] != cur:
                        continue
                    nxt = rel[1]
                    queue.append(nxt)
            step += 1
        return res
DFS解法：
import collections
def numWways(n,relation,k):
    graph = collections.defaultdict(list)
    print(graph)
    for r in relation:
        graph[r[0]] = graph[r[0]] + [r[1]]
    res = 0
    print(graph)
    def dfs(curr, step):
        nonlocal res, n  #使用外层变量，nonlocal
        if curr == n - 1 and step == 0:
            res += 1
            return
        if not graph[curr] or not step:
            return
        for child in graph[curr]:
            dfs(child, step - 1)
    dfs(0, k)
    return res
