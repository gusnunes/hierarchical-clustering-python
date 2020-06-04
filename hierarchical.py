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

def hierarchical(data):
    groups,size = inicial_groups(data)
    
    if size < 2:   # erro na funcao que calcula a matriz de distancia
        return groups

    medias = data   # as medias iniciais sao os dados iniciais
    print(f"\nGrupos iniciais: {groups}\n")

    cont = 0
    aux  = size-1
    while cont < aux:
        i,j = distance_matrix(medias,size)   # linha e coluna que representa menor valor na matriz de distancias
        
        if i < j:
            groups[i] = groups[i] + groups[j]
            groups.remove(groups[j])

            medias[i] = calc_media(groups[i])
            medias.remove(medias[j])
        else:
            groups[j] = groups[j] + groups[i]
            groups.remove(groups[i])

            medias[j] = calc_media(groups[j])
            medias.remove(medias[i])
        
        print(f"Agrupamento {cont+1}: {groups}")
        cont += 1
        size -= 1

def main():
    # dados constantes por enquanto
    data = [2, 4, 6.3, 9, 11.6]

    hierarchical(data)

main()