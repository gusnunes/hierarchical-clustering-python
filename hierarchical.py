def inicial_groups(data):
    size   = 0
    groups = []

    for i in data:   # inicialmente os dados sao grupos isolados
        groups.append([i])
        size += 1

    return groups,size

def distance_matrix(medias,size):   # procurar o menor valor na matriz de distancia
    menor  = abs(medias[1] - medias[0])   # primeira distancia da matriz
    row    = 1
    column = 0

    for i in range(2,size):
        for j in range(size):
            if j >= i:   # diagonal principal e acima(distancias repetidas e nulas)
                break
            distancia = abs(medias[i] - medias[j])
            if distancia < menor:
                menor  = distancia
                row    = i
                column = j
    
    return row,column

def calc_media(group):
    sum = size = 0
    for data in group:
        sum  += data
        size += 1
    
    media = sum/size
    return media

def agrupa_dados(groups,j,i):
    groups[j].extend(groups[i])
    groups.remove(groups[i])   # remove cluster antigo(foi agrupado em outro)

def remove_media(groups,medias,j,i):   # remove a media que fica sobrando(do cluster que foi agrupado)
    medias[j] = calc_media(groups[j])
    medias.remove(medias[i])

def hierarchical(data):
    groups,size = inicial_groups(data)
    
    if size < 2:   # erro na funcao que calcula a matriz de distancia
        return groups

    medias = data   # as médias iniciais sao os dados iniciais
    print(f"Clusters iniciais: {groups}\n")

    cont = 0
    qtd_clusters = size-1
    while cont < qtd_clusters:
        i,j = distance_matrix(medias,size)   # linha e coluna que representa menor valor na matriz de distancias
        agrupa_dados(groups,j,i)
        remove_media(groups,medias,j,i)

        print(f"{cont+1}º Agrupamento: {groups}")
        cont += 1
        size -= 1
         
def main():
    # dados constantes por enquanto
    data = [2, 4, 6.3, 9, 11.6]
    hierarchical(data)

main()