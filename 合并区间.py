# Leetcode
Leetcode-Python-Soultion
def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    h =[]
    h.append(intervals[0])
    for  interval in intervals:
        if interval[0] > h[-1][1]:#可以加一个if判断是否等于h【-1】
            h.append(interval)
        else:
            h[-1][1] = max(interval[1],h[-1][1])
    return  h
