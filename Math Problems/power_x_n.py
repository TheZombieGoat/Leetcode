#Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n *= -1
        result = self.myPow(x, n // 2)
        if n % 2 == 0:
            return result*result
        else:
            return x*result*result
