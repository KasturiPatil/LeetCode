class Solution:
    def countSegments(self, A) -> int:
        ans=[]
        if A.isspace():
            return 0
        elif not A:
            return 0
        new=A.split(" ")
        for i in new:
            if i == '':
                continue
            else:
                ans.append(i)
        print(ans)
        return len(ans)
