# As a begineer this is my solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dici = {}

        for key in nums:
            dici[key] = dici.get(key,0) + 1

        res = [True for val in dici.values() if val > 1]
        
        if(True in res):
            return True
        return False


# solution of precise and optimsed