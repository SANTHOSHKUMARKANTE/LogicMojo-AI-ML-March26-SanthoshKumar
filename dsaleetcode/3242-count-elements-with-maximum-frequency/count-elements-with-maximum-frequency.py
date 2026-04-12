# As a begineer this is my level solution

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dici = {}
        
        for i in nums:
            if i in dici:
                dici[i] += 1
            else:
                dici[i] = 1
        max_count = max(dici.values())
        res = 0
        for key in dici:
            if(dici[key] == max_count):
                res += dici[key]
        return res

# how can we make more concise and precise way of optimal solution

# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         dici = {}
        
#         for i in nums:
#             dici[i] = dici.get(i,0) + 1
#         max_count = max(dici.values())
#         res = 0
        
#         return sum(val for val in dici.values() if dici[val] == max_count)
