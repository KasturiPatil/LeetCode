class Solution:
    def removeDuplicates(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a= [str(i) for i in nums]
        a=set(a)
        nums.clear()
        for i in a:
            nums.append(int(i))
        nums.sort()
        return len(nums)

