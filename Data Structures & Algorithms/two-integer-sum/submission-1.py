class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum={}
        out=[]
        for  i, num in enumerate(nums):
            if target-num in sum:
                return [sum[target-num],i]

            sum[num]=i

        return out


        