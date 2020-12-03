class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        try:
            return len(words[-1])
        except IndexError:
            return 0
        
    
        
