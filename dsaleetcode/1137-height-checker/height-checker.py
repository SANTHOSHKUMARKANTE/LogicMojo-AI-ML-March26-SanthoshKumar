# import copy

# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
        
#         dummy = copy.deepcopy(heights)
#         size = len(heights)

#         for i in range(size):
#             for j in range(size-i-1):
#                 if(heights[j] > heights[j+1]):
#                     heights[j],heights[j+1] = heights[j+1],heights[j]
#         print(" ".join(map(str,heights)))

#         count = 0
#         for i in range(size):
#             if(dummy[i] != heights[i]):
#                 count += 1
#         return count

# optimal approach

class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        dummy = sorted(heights)
        count = 0
        # size = len(heights)
        for i in range(len(heights)):
            if(dummy[i] != heights[i]):
                count += 1
        return count
