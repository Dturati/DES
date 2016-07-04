import ast
class Chave:
    chave = [0,0,0,0,0,0,0,0,0,0]
    ladoEsquerdoChave = [0,0,0,0,0]
    ladoDireitoChave = [0,0,0,0,0]
    chavePermutada = [0,0,0,0,0,0,0,0,0,0]
    keyUm   = [0,0,0,0,0,0,0,0]
    keyDois = [0,0,0,0,0,0,0,0]

    def setChave(self,chave):
        self.chave = map(str,str(chave))

    def getChave(self):
        return self.chave

    def chaveUm(self):
     self.chavePermutada[0] = self.chave[2]
     self.chavePermutada[1] = self.chave[4]
     self.chavePermutada[2] = self.chave[1]
     self.chavePermutada[3] = self.chave[6]
     self.chavePermutada[4] = self.chave[3]
     self.chavePermutada[5] = self.chave[9]
     self.chavePermutada[6] = self.chave[0]
     self.chavePermutada[7] = self.chave[8]
     self.chavePermutada[8] = self.chave[7]
     self.chavePermutada[9] = self.chave[5]
     #print("Chave permutada")
     #print(self.chavePermutada)
     self.ladoEsquerdoChave = self.ladoEsquerdo()
     self.ladoDireitoChave  = self.ladoDireito()
     #print(self.ladoEsquerdoChave)
     #print(self.ladoDireitoChave)
     contetena = self.ladoEsquerdoChave + self.ladoDireitoChave
     self.keyUm[0] = contetena[5]
     self.keyUm[1] = contetena[2]
     self.keyUm[2] = contetena[6]
     self.keyUm[3] = contetena[3]
     self.keyUm[4] = contetena[7]
     self.keyUm[5] = contetena[4]
     self.keyUm[6] = contetena[9]
     self.keyUm[7] = contetena[8]
     return self.keyUm



    def chaveDois(self):
        ladoEsquerdoChavedois = self.ladoEsquerdo()
        ladoDiretoChaveDois   = self.ladoDireito()

        for i in range(4):
            troca = ladoEsquerdoChavedois[i]
            ladoEsquerdoChavedois[i] = ladoEsquerdoChavedois[i+1]
            ladoEsquerdoChavedois[i+1] = troca

        for i in range(4):
            troca = ladoEsquerdoChavedois[i]
            ladoEsquerdoChavedois[i] = ladoEsquerdoChavedois[i+1]
            ladoEsquerdoChavedois[i+1] = troca

        for i in range(4):
            troca = ladoDiretoChaveDois[i]
            ladoDiretoChaveDois[i] = ladoDiretoChaveDois[i+1]
            ladoDiretoChaveDois[i+1] = troca

        for i in range(4):
            troca = ladoDiretoChaveDois[i]
            ladoDiretoChaveDois[i] = ladoDiretoChaveDois[i+1]
            ladoDiretoChaveDois[i+1] = troca

        concatena = ladoEsquerdoChavedois + ladoDiretoChaveDois

        self.keyDois[0] = concatena[5]
        self.keyDois[1] = concatena[2]
        self.keyDois[2] = concatena[6]
        self.keyDois[3] = concatena[3]
        self.keyDois[4] = concatena[7]
        self.keyDois[5] = concatena[4]
        self.keyDois[6] = concatena[9]
        self.keyDois[7] = concatena[8]

        return self.keyDois




    def ladoEsquerdo(self):
        #sepera lado esquerdo da chave
        #print("lado Esquerdo")
        for i in range(5):
            self.ladoEsquerdoChave[i] = self.chavePermutada[i]

        for i in range(4):
            troca = self.ladoEsquerdoChave[i]
            self.ladoEsquerdoChave[i] = self.ladoEsquerdoChave[i+1]
            self.ladoEsquerdoChave[i+1] = troca
        #print(self.ladoEsquerdoChave)
        return self.ladoEsquerdoChave




    def ladoDireito(self):
        #print("lado Direito")
        for i in range(5,10):
            self.ladoDireitoChave[i-5] = self.chavePermutada[i]
        for i in range(4):
            troca = self.ladoDireitoChave[i]
            self.ladoDireitoChave[i] = self.ladoDireitoChave[i+1]
            self.ladoDireitoChave[i+1] = troca
        #print(self.ladoDireitoChave)
        return self.ladoDireitoChave