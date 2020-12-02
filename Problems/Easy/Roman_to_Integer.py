class Solution:
    def romanToInt(self, s: str) -> int:
        h = {73: 1, 86: 5, 88: 10, 76: 50, 67: 100, 68: 500, 77: 1000};
        sum = 0;
        i = 0
        sub = False
        while i != len(s):
            if i+1 == len(s):
                 suiv = s[-1]
            elif i == len(s):
                suiv = s[i]
            else:
                suiv = s[i+1]
            if ((s[i] == 'I' and (suiv == 'V' or suiv == 'X')) or (s[i] == 'X' and (suiv == 'L' or suiv == 'C')) or (
                    s[i] == 'C' and (suiv == 'D' or suiv == 'M'))):
                sum = sum + h[ord(suiv)] - h[ord(s[i])]
                i+=2
            else:
                sum += h[ord(s[i])]
                i+=1
        return sum
