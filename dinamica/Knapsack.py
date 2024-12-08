def criar_tabela(m, n):
    # Cria uma tabela de (m+1) x (n+1) inicializada com zeros
    return [[0 for _ in range(n + 1)] for _ in range(m + 1)]

def valor_max(a, b):
    # Retorna o maior valor entre a e b
    return max(a, b)

def knapsack(capacidade, n, valores, pesos):
    # Cria uma tabela para armazenar os resultados
    table = criar_tabela(n, capacidade)

    # Preenche a tabela utilizando a abordagem bottom-up
    for i in range(1, n + 1):
        for j in range(1, capacidade + 1):
            if pesos[i - 1] <= j:
                table[i][j] = valor_max(table[i - 1][j], table[i - 1][j - pesos[i - 1]] + valores[i - 1])
            else:
                table[i][j] = table[i - 1][j]

    # Retorna o valor máximo obtido
    return table[n][capacidade]

def main():
    # Entrada da capacidade e número de itens
    capacidade = int(input("Knapsack's capacidade: "))
    n = int(input("Number of items: "))

    valores = []
    pesos = []

    # Entrada dos valores e pesos dos itens
    for i in range(n):
        valor = int(input(f"Valor do item {i}: "))
        peso = int(input(f"Peso do item {i}: "))
        valores.append(valor)
        pesos.append(peso)

    # Resolve o problema e imprime o resultado
    resposta = knapsack(capacidade, n, valores, pesos)
    print(f"\nMaximum valor: {resposta}")

if __name__ == "__main__":
    main()
