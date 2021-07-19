class Solution:
    def twosum(self, nums, target):
        pass


    def doublefor(self,nums, target):
        for i in range(len(nums)/2):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target :
                    print([i,j])

nums=[2,7,11,15]
target=9


Solution.doublefor(nums,target)



