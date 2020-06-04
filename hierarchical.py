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
            if i >= j:   # diagonal principal e acima(distancias repetidas e nulas)
                break
            
            distancia = abs(medias[i] - medias[j])
            if distancia < menor:
                row    = i
                column = j
    
    return row,column

def hierarchical(data):
    groups,size = inicial_groups(data)
    
    if size < 2:   # erro na funcao que calcula a matriz de distancia
        return groups

    medias = data   # a media inicial sao os dados iniciais
    print(f"\nGrupos iniciais: {groups}\n")

    cont = 1
    while cont < size:
        i,j = distance_matrix(medias,size)
        if i < j:
            groups[i] = groups[i] + groups[j]
            groups.remove(groups[j])
        else:
            groups[j] = groups[j] + groups[i]
            groups.remove(groups[i])
        
        print(f"Agrupamento {cont}: {groups}")

        cont += 1

    return groups


def main():
    # dados constantes por enquanto
    data = [2, 4, 6.3, 9, 11.6]

    groups = hierarchical(data)
    print(groups)

main()