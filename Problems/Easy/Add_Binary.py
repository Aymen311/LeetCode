class Solution(object):
    def addBinary(self, a, b):
        ret = '0'
        a = a.zfill(max(len(a),len(b)))
        b = b.zfill(max(len(a),len(b)))
        l3 = ['0' for i in range(0, max(len(a), len(b)) + 1)]
        l1 = [i for i in a]
        l2 = [i for i in b]


        for i in range(len(l2)-1, -1, -1):
            if l1[i] == l2[i] == '1' and ret == '1':
                l3[i + 1] = '1'
                ret = '1'
            elif l1[i] == l2[i] == '1' and ret == '0':
                l3[i + 1] = '0'
                ret = '1'
            elif ((l1[i] == '1' and l2[i] == '0') or (l1[i] == '0' and l2[i] == '1')) and ret == '1':
                l3[i + 1] = '0'
                ret = '1'
            elif ((l1[i] == '1' and l2[i] == '0') or (l1[i] == '0' and l2[i] == '1')) and ret == '0':
                l3[i + 1] = '1'
                ret = '0'
            elif l1[i] == l2[i] == '0' and ret == '0':
                l3[i + 1] = '0'
                ret = '0'
            elif l1[i] == l2[i] == '0' and ret == '1':
                l3[i + 1] = '1'
                ret = '0'
        l3[0] = ret
        return str(int(''.join(map(str, l3))))


print(Solution().addBinary("1010", "1011"))
