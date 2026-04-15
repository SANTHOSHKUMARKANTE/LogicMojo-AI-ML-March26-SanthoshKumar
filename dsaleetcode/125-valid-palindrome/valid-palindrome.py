#As a begineer this is my solution
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         res = []

#         for char in s:
#             if(char.isalpha()):
#                 res.append(char)
#         final = res[::-1]
#         if(final == res):
#             return True
#         return False

# Optimised solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = s.lower()

        while(left < right):
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
