def inicial_groups(data):
    groups = [[i] for i in data]  # inicialmente os dados sao grupos isolados
    return groups

def hierarchical(data):
    groups = inicial_groups(data)
    print(f"\nGrupos iniciais: {groups}\n")
    return groups


def main():
    # dados constantes por enquanto
    data = [2, 4, 6.3, 9, 11.6]

    groups = hierarchical(data)
    print(groups)

main()