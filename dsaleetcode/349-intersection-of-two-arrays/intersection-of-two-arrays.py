#as a begineer this is my solution
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         if(len(nums1) > len(nums2)):
#             res = []
#             size = len(nums2)

#             for i in nums2:
#                 if i in nums1 and i not in res:

#                     res.append(i)
#         else:
#             res = []
#             size = len(nums1)

#             for i in nums1:
#                 if i in nums2 and i not in res:
#                     res.append(i)
#         return res
# Optimal solution
class Solution:
     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #remove duplicates in the lists bu converting into the sets

        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)