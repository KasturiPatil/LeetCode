class Solution:
    def findNumbers(self, A) -> int:
        count=0
        for i in A:
            res = list(map(int, str(i)))
            z=len(res)
            if z%2==0:
                count +=1
        return count
