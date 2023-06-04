#return num of unique paths

class Solution:
    def uniquePaths(m: int, n: int) -> int:
        d = {}
        d[0] = 0
        def up(a,b):
            if a == 1 and b == 1:
                d[0] = d[0] + 1
            else:
                if a > 0:
                    up(a-1,b)
                if b > 0:
                    up(a,b-1)
        up(m,n)
        return d[0]
        

    print(uniquePaths(3,7))
