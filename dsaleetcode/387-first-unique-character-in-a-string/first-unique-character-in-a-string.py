class Solution:
    def firstUniqChar(self, s: str) -> int:
        dici = {}

        for key in s:
            dici[key] = dici.get(key,0)+1
        for key in dici:
            if(dici[key] == 1):
                return s.index(key)
        return -1