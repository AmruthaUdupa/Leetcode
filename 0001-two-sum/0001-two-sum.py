class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution={}
        for i, num in enumerate(nums):
            comp=target-num
            if comp in solution:
                return[solution[comp],i]
            solution[num]=i

            