def criar_matriz(m, n):   # Cria uma matriz inicializada com zeros para armazenar os valores da subsequência
    return [[0] * (n + 1) for _ in range(m + 1)]


def subsequence(s1, s2):

    # Calcula o tamanho da subsequência comum mais longa (LCS) entre duas strings.
    m = len(s1)
    n = len(s2)

    tabela = criar_matriz(m, n)

    # Acho que dá pra fazer com Set para diminuir a complexidade do algoritmo

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1])

    return tabela[m][n]


def main():
    valor_max = int(input("Tamanho máximo da string: "))

    if valor_max > 1000000:
        print("Valor máximo excedido.")
        return

    str1 = input("Primeira string: ")
    str2 = input("Segunda string: ")

    resposta = subsequence(str1, str2)
    print(f"\nA maior subsequência comum entre as string é: {resposta}")


if __name__ == "__main__":
    main()
