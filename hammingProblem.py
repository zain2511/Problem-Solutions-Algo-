    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = str(bin(x)[2:])
        b = str(bin(y)[2:])
        tempstr = ""
        if(len(a) > len(b)):
            diff = len(a) - len(b)
            for i in range(0, diff):
                tempstr += "0"
            b = tempstr + b    
        elif(len(a) < len(b)):    
            diff = len(b) - len(a)
            
            for i in range(0, diff):
                tempstr += "0"
            a = tempstr + a
        count = 0
        for i in range(len(a)):
            
            if a[i] != b[i]:
                count += 1
        return count  