import numpy as np
class Solution(object):
    def countAndSay(self, n):
        nums = [1]
        num = 0 
        count = 0
        while count != n-1 :
            num = 0
            h = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,}
            for i in nums:
                h[str(i)] += 1
            indexes = np.unique(nums, return_index=True)[1]
            for j in [nums[index] for index in sorted(indexes)]:
                num = h[str(j)]*10 + num*100
                if h[str(j)] != 0:
                    num += j
            nums = list(map(int, str(num)))
            count += 1
        if n == 1 :
            return "1"
        else:
            return str(num)
            
            
                
                
            
                
       
        
