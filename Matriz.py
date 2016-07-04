class Matriz:
    s0 = [[]]
    sq = [[]]
    def matrizS0(self):
        s0 = [[1,0,3,2],
             [3,2,1,0],
             [0,2,1,3],
             [3,1,3,2]]

        return s0

    def matrizS1(self):
        s1 = [[0,1,2,3],
             [2,0,1,3],
             [3,0,1,0],
             [2,1,0,3]]
        return s1

    def p4(self,s0,s1,direta,esquerda):
        s0n1 =  str(esquerda[0]) + str(esquerda[3])
        s0n1 = int(s0n1,2)
        s0n2 = str(esquerda[1]) + str(esquerda[2])
        s0n2 = int(s0n2,2)

        rs1 = s0[s0n1][s0n2]
        rs1 = "{0:b}".format(rs1)
        if(rs1 == '1'):
            rs1 = "0" + rs1
        elif(rs1 == '0'):
            rs1 = "0" + "0"
        s1n1 =  str(direta[0]) + str(direta[3])
        s1n1 = int(s1n1,2)
        s1n2 = str(direta[1]) + str(direta[2])
        s1n2 = int(s1n2,2)

        rs2 = s1[s1n1][s1n2]
        rs2 = "{0:b}".format(rs2)

        if(rs2 == '1'):
            rs2 = "0" + rs2
        elif(rs2 == "0"):
            rs2 = "0" + "0"
        p4 = rs1 + rs2
        p4Res = [0,0,0,0]
        p4Res[0] = p4[1]
        p4Res[1] = p4[3]
        p4Res[2] = p4[2]
        p4Res[3] = p4[0]
        return p4Res










