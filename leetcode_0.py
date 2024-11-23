from typing import List

class Solution:
    def search(self,nums:List[int],target:int) ->int:
        high=len(nums)-1
        low=0
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                low=mid+1
            else:
                high=mid-1
        return -1

if __name__=="__main__":
    solution=Solution()

    nums1=[-1,0,3,5,9,12]
    target1=9
    result1=solution.search(nums1,target1)
    print(f" searching for {target1} in {nums1}:Index {result1}")
