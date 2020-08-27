class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        a,n = 0,len(nums)
        for i in range (0,n):
            a^=nums[i]
        b,c = 0,0
        mask = a & (-a)
        for i in range(len(nums)):
            if(nums[i] & mask == 0):
                b^=nums[i]
            else:
                c^=nums[i]
        return b,c
