def firstBadversion(n):
    l,r = 1,n
    while l <= r:
        mid = (r+l) //2
        if not isBadversion(mid):
            l = mid+1
        else isBadversion(mid):
            r = mid
    return l
