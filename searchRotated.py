class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0; r=len(nums)-1
        while (l<=r):
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[l]<=nums[mid]:
                if target>nums[mid] or target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if target>nums[mid] and target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
            

        
