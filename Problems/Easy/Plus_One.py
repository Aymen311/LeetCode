class Solution(object):
    def plusOne(self, digits):
        string = ''.join(map(str,digits))
        k = str(int(string)+1)
        k = k.zfill(len(string))
        return [int(x) for x in k ]
