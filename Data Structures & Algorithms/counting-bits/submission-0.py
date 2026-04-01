class Solution:
    def countBits(self, n: int) -> List[int]:
        def numberOfOnes(n):
            count = 0
            while n:
                if n & 1:
                    count +=1
                n = n >> 1
            return count
        res = [0]
        for i in range(1, n+1):
            res.append(numberOfOnes(i))


        return res