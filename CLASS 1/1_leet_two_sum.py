class Solution:
    def twosum(self, nums, target):
        pass


    # METHOD 1
    # def doublefor(self,nums, target):
    #     for i in range(int(len(nums)/2)):
    #         for j in range(len(nums)):
    #             if nums[i]+nums[j] == target :
    #                 print([i,j])


    #METHOD -2
    # def doublefor(self, nums, target):
    #     k = 0
    #     for element in nums:
    #         j = target - element
    #         k += 1
    #         tmp_nums = nums[k:] #creates a list of 1:last
    #         if j in tmp_nums:
    #             return [k - 1, tmp_nums.index(j) + k]
    
    #METHOD 3
    def doublefor(self, nums, target):
        import copy
        sort_nums = copy.deepcopy(nums)
        sort_nums.sort()
        i = 0
        j = len(sort_nums) - 1
        while i < j:
            if sort_nums [i] + sort_nums [j] == target:
                break
            elif sort_nums [i] + sort_nums [j] > target:
                j -= 1
            else:
                i += 1
        if i >= j:
            return []
        index1 = None
        index2 = None
        for k in range(len(nums)):
            if index1 is None and nums [k] == sort_nums [i]:
                index1 = k
            elif index2 is None and nums [k] == sort_nums [j]:
                index2 = k
        answer = [index1 + 1, index2 + 1]
        answer.sort()
        return answer

nums1=[2,7,11,4]
nums2=[3,2,4]
nums3=[3,3]
target=6



print(Solution().doublefor(nums1,target))
print(Solution().doublefor(nums2,target))
print(Solution().doublefor(nums3,target))



