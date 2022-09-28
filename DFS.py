import copy

estadoI = [
[2, 8, 3], 
[1, 6, 4],  
[7, 0, 5]
]

estadoF = [
[1, 2, 3], 
[8, 0, 4],  
[7, 6, 5]
]

def gerar_filhos(estado):
    aux = []
    nlinha = len(estado)
    ncoluna = len(estado[0])
    filhos = []
    for i in range(nlinha):
        for j in range(ncoluna):
            if estado[i][j] == 0:
                #print(estadoI[i][j])
                #print(i, j)
                #avaliar possibilidades de movimento
                if(i > 0): #posso mover para cima
                    aux = copy.deepcopy(estado)
                    aux[i][j] = aux[i-1][j] #a posiçao em que estava o 0 recebeu o numero de cima
                    aux[i-1][j] = 0 #o numero que estava em cima recebeu o 0
                    #verificar se o estado existe em abertos e fechados (nao adicionar eles)
                    #coloque os filhos a diretia em abertos
                    filhos.append(aux)
                if(j>=0 and j<2): #pode mover para direita
                    aux = copy.deepcopy(estado)
                    aux[i][j] = aux[i][j+1] #a posiçao em que estava o 0 recebeu o numero da direita
                    aux[i][j+1] = 0  #o numero que estava a direita recebeu o 0
                    #verificar se o estado existe em abertos e fechados (nao adicionar eles)
                    #coloque os filhos a diretia em abertos
                    filhos.append(aux)
                if(j<=2 and j>0): #pode movar para esquerda
                    aux = copy.deepcopy(estado)
                    aux[i][j] = aux[i][j-1] #a posiçao em que estava o 0 recebeu o numero da esquerda
                    aux[i][j-1] = 0  #o numero que estava a esquerda recebeu o 0
                    #verificar se o estado existe em abertos e fechados (nao adicionar eles)
                    #coloque os filhos a diretia em abertos
                    filhos.append(aux)
                if(i < 2): #pode mover para baixo
                    aux = copy.deepcopy(estado)
                    aux[i][j] = aux[i+1][j] #a posiçao em que estava o 0 recebeu o numero de baixo
                    aux[i+1][j] = 0 #o numero que estava em baixo recebeu o 0
                    #verificar se o estado existe em abertos e fechados (nao adicionar eles)
                    #coloque os filhos a diretia em abertos
                    filhos.append(aux)   
                return filhos



def DFS (inicial):
    abertos = [inicial]
    fechados = []
    geracao = []
    while abertos != []:
        X  = abertos.pop(0)
        if X == estadoF:
            print("chegamos")
            print(X)
            return True
        else:
            geracao = gerar_filhos(X)
            fechados.append(X)
            for i in geracao:
                if i not in abertos and i not in fechados:
                  abertos.insert(0,i)
    print("nao chegamos")
    return False

                    
