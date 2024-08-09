class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2**31 or x >= (2**31)-1 or x == 0:
            return 0
            
        isNegative = x < 0
        x = abs(x)
        hh = 0

        while x != 0 and x > 0:
            d = x%10
            hh = hh*10 + d
            x = x//10
        if hh <= -2**31 or hh >= (2**31) -1:
            return 0

        if isNegative:
            hh = hh * (-1)
        return hh
