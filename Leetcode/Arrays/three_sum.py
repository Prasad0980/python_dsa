from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = list()
        target = None 
        for i in range(len(nums)):
            if target != nums[i]*-1:
                target = nums[i]*-1
            else:
                continue 
            l, h = i+1, len(nums)-1
            while h > l:
                s = nums[l] + nums[h]
                if s > target:
                    h -=1 
                elif s< target:
                    l +=1 
                else:
                    op.append([nums[i], nums[h], nums[l]])
                    #Comment: We add two conditions below to avoid the taking in of duplicates. 
                    #Comment2: We are moving l and h pointer if they have got same value ahead as one checked now.
                    #But we dont do it with an and condition. This still works.
                    #take for example the array [-4,-1,-1,0,1,2,5]
                    #For first iteration, target will be 4, l will be index 1 and h will be index 6
                    #We find a match in first go itself and then we see -1 is repeated. But 5 is not on h side.
                    #Things would have been very clear if both -1 and 5 were repeated so we increment l and decrement h to avoid duplicates.
                    #But even here when both are not repeated, we only increment l and leave h as it is.
                    #At first it might seem like we would miss out on some pairs as we move l without any checking. 
                    #But since we know, target is 4, l is -1 then h should be 5. So even though we skip one number (the next -1), we are not missing any pairs,
                    #This is because -1 will need only and only 5 as other number for 4 to be target. 
                    #Meaning iterating without skipping the other -1 would be useless because it would not find any pair anyway.
                    while h > l and nums[l] == nums[l+1]:
                        l +=1 
                    while h > l and nums[h] == nums[h-1]:
                        h -=1 
                    h -=1 
                    l +=1 
        return op
            

s = Solution()
print(s.threeSum([-2,0,0,2,2]))