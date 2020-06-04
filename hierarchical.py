def inicial_groups(data):
    size   = 0
    groups = []

    for i in data:   # inicialmente os dados sao grupos isolados
        groups.append([i])
        size += 1

    return groups,size

def hierarchical(data):
    groups,size = inicial_groups(data)
    print(f"\nGrupos iniciais: {groups}\n")

    return groups


def main():
    # dados constantes por enquanto
    data = [2, 4, 6.3, 9, 11.6]

    groups = hierarchical(data)
    print(groups)

main()