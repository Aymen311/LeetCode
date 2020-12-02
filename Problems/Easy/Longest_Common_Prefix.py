class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:   
        if (len(strs) > 0 and len(strs) <= 200):
            pref = strs[0]
            for item in range(1, len(strs)):
                
                word2 = strs[item]
                pref1 = ''
                same = True
                for i,j in zip(pref, word2):
                    if i == j and same:
                        pref1 += i
                        same = True
                    else:
                        same = False
                pref = pref1
            return pref
        else:
            return ""
    
