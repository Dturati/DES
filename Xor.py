class Xor:
    def getXor(self,n1,n2):
        if(n1 == 0 and n2 == 0):
            return 0
        elif(n1 == 0 and n2 == 1):
            return 1
        elif(n1 == 1 and n2 == 0):
            return 1
        elif(n1 == 1 and n2 == 1):
            return 0