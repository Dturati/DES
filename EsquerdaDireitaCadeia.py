class EsquedaDireitaCadeia:
    direita = [0,0,0,0]
    esquerda = [0,0,0,0]

    def separaEsquerda(self,cadeia):
        for i in range(4):
            self.esquerda[i] = cadeia[i]
        return self.esquerda

    def seperaDireita(self,cadeia):
        for i in range(4,8):
            self.direita[i-4] = cadeia[i]
        return self.direita
