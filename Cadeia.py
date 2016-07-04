class Cadeia:
    permutas = [0,0,0,0,0,0,0,0]
    cadeia = 0
    ep = [0,0,0,0,0,0,0,0]
    def setCadeia(self,cadeia):
        self.cadeia = cadeia

    def getCadeia(self):
        return self.cadeia


    def permutacao(self,vetor):
        self.permutas[0] = vetor[1]
        self.permutas[1] = vetor[5]
        self.permutas[2] = vetor[2]
        self.permutas[3] = vetor[0]
        self.permutas[4] = vetor[3]
        self.permutas[5] = vetor[7]
        self.permutas[6] = vetor[4]
        self.permutas[7] = vetor[6]

    def getPermutacao(self):
        return self.permutas

    def EP(self,chave):
        self.ep[0] = chave[3]
        self.ep[1] = chave[0]
        self.ep[2] = chave[1]
        self.ep[3] = chave[2]
        self.ep[4] = chave[1]
        self.ep[5] = chave[2]
        self.ep[6] = chave[3]
        self.ep[7] = chave[0]
        return  self.ep
