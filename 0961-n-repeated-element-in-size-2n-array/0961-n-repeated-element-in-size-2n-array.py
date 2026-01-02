class Solution(object):
    def repeatedNTimes(self, nums):
        seen =set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return i


        