class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dici = {}

        for key in nums:
            dici[key] = dici.get(key,0) + 1

        print(dici.values())

        res = [True for val in dici.values() if val > 1]
        
        if(True in res):
            return True
        return False