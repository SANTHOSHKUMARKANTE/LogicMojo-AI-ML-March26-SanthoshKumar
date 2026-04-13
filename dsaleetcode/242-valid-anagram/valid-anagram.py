#As a begineer my solution

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         freq = {}

#         if(len(s) != len(t)):
#             return False
        
#         for char in s:
#             freq[char] = freq.get(char,0) + 1

#         for char in t:
#             if char not in freq:
#                 return False
#             freq[char] -= 1
#             if(freq[char] < 0):
#                 return False
    
#         return True

#optimised solution

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        