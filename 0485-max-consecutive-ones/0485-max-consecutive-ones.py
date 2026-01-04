class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maximum=0
        count=0
        for i in nums:
            if i==1:
                count+=1
                maximum=max(maximum,count)
            else:
                count=0
        return maximum