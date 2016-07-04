from Cadeia import *
from Chave import *
from EsquerdaDireitaCadeia import *
from Xor import *
from Matriz import *

def cifra(texto,key):
    #Calculo da chave
    chave = Chave()
    chave.setChave(key)
    #print("Chave Um")
    keyUm = chave.chaveUm()
    #print(keyUm)
    #print("Chave dois")
    keyDois = chave.chaveDois()
    #print(keyDois)


    #Cadeira
    cadeia = Cadeia()
    cadeia.setCadeia(texto)
    #Faz permutacao IP
    cadeia.permutacao(cadeia.getCadeia())
    #print("Permutacao IP")
    #print(cadeia.getPermutacao())

    esqDir = EsquedaDireitaCadeia()
    esquerda = esqDir.separaEsquerda(cadeia.getPermutacao())
    direita  = esqDir.seperaDireita(cadeia.getPermutacao())
    #print("esquerda")
    #print(esquerda)
    #print("Direita")
    #print(direita)

    ep =  cadeia.EP(direita)
    #print("EP")
    #print(ep)


    xor  = Xor()
    vetorXor = [0,0,0,0,0,0,0,0]
    for i in range(8):
        vetorXor[i] = xor.getXor(int(ep[i]),int(keyUm[i]))
    #print("XOR")
    #print(vetorXor)

    esquerda = esqDir.separaEsquerda(vetorXor)
    direita  = esqDir.seperaDireita(vetorXor)
    #print("Esquerda")
   # print(esquerda)
    #print("Direita")
    #print(direita)
    #print("")


    matriz = Matriz()
    s0 = matriz.matrizS0()
    s1 = matriz.matrizS1()

    p4 = matriz.p4(s0,s1,direita,esquerda)

    #print("P4")
    #print(p4)
    #print("")

    vetorP4 = [0,0,0,0]
    esquerda  = esqDir.separaEsquerda(cadeia.getPermutacao())
    for i in range(4):
        vetorP4[i] = xor.getXor(int(p4[i]),int(esquerda[i]))
    #print("Xor P4")
    #print(vetorP4)
    #print("")

    direita = esqDir.seperaDireita(cadeia.getPermutacao())
    #print("direita")
    #print(direita)
    #print("")

    ep = [0,0,0,0,0,0,0,0]
    ep[0] = vetorP4[3]
    ep[1] = vetorP4[0]
    ep[2] = vetorP4[1]
    ep[3] = vetorP4[2]
    ep[4] = vetorP4[1]
    ep[5] = vetorP4[2]
    ep[6] = vetorP4[3]
    ep[7] = vetorP4[0]
    #print("E/P")
    #print(ep)
    #print("")

    for i in range(8):
        vetorXor[i] = xor.getXor(int(ep[i]),int(keyDois[i]))
    #print(vetorXor)

    esquerda = esqDir.separaEsquerda(vetorXor)
    direita  = esqDir.seperaDireita(vetorXor)

    s0 = matriz.matrizS0()
    s1 = matriz.matrizS1()
    p4 = matriz.p4(s0,s1,direita,esquerda)
    #print(p4)

    vetorXorP4 = [0,0,0,0]
    direitaEsquerda = esqDir.seperaDireita(cadeia.getPermutacao())
    for i in range(4):
        vetorXorP4[i] = xor.getXor(int(p4[i]),int(direitaEsquerda[i]))
    #print(vetorXorP4)
    #print(vetorP4)

    concatena = vetorXorP4 + vetorP4
    #print(concatena)
    troca = [0,0,0,0,0,0,0,0]

    troca[0] = concatena[3]
    troca[1] = concatena[0]
    troca[2] = concatena[2]
    troca[3] = concatena[4]
    troca[4] = concatena[6]
    troca[5] = concatena[1]
    troca[6] = concatena[7]
    troca[7] = concatena[5]
    num = map(str,troca)
    num  = ''.join(num)
    num = int(num,2)
    print("Palavra cifrada")
    print(hex(num).split('x')[1])
    return troca

















