class Item:
    def __init__(self, peso, valor, nome):
        self.peso = peso
        self.valor = valor
        self.nome = nome
        self.rel_value = valor / peso

    def __str__(self):
        return f"{self.nome}: Total valor: {self.valor:.2f}\n Peso: {self.peso:.2f}\n Valor por peso: {self.rel_value:.2f}"


class Armazenamento:
    def __init__(self, tamanho, itens):
        self.tamanho = tamanho
        self.itens = itens

    def __str__(self):
        arm_itens = "\n".join(str(item) for item in self.itens)
        return f"\nESPAÇO:\nTAMANHO: {self.tamanho}\n{arm_itens}"


class Knapsack:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.peso = 0
        self.valor = 0

    def __str__(self):
        return f"\nESTADO DO KNAPSACK:\n Peso: {self.peso:.2f}\n Valor: {self.valor:.2f}"


def criar_knapsack():
    capacidade = float(input("\nCapacidade do Knapsack: "))
    return Knapsack(capacidade)


def criar_armazenamento():
    tamanho = int(input("\nNúmeros de itens armazenados: "))
    itens = []

    print("\nOBS: O VALOR MÁXIMO PARA O NOME DOS ITENS É DE 12 CARACTERES\n")

    for i in range(tamanho):
        nome = input(f"Nome do item {i + 1}: ")
        peso = float(input(f"peso do '{nome}' disponível: "))
        valor = float(input(f"Valor total do '{nome}': "))
        itens.append(Item(peso, valor, nome))

    return Armazenamento(tamanho, itens)


def ordenar_armazenamento(armazenamento):
    # Sort the itens in descending order by their relative valor
    armazenamento.itens.sort(key=lambda item: item.rel_value, reverse=True)


def fractional_knapsack(knapsack, armazenamento):
    cheio = False

    # Sort itens by relative valor
    ordenar_armazenamento(armazenamento)

    i = 0
    while not cheio and i < armazenamento.tamanho:
        item_atual = armazenamento.itens[i]

        # If the knapsack can hold all of the current highest valor item
        if knapsack.capacidade - knapsack.peso >= item_atual.peso:
            print(f"\n {item_atual.peso:.2f} do item '{item_atual.nome}' foi adicionado a mochila")
            knapsack.valor += item_atual.valor
            knapsack.peso += item_atual.peso
        else:
            # If it can only hold a fraction of the current item
            frac = (knapsack.capacidade - knapsack.peso) / item_atual.peso
            knapsack.valor += frac * item_atual.valor
            knapsack.peso += frac * item_atual.peso
            cheio = True
            print(f"\n {frac * item_atual.peso:.2f} do item '{item_atual.nome}' foi adicionado na mochila")

        i += 1

    if knapsack.peso < knapsack.capacidade:
        print("\nTodos os itens cabem na mochila!")
    else:
        print("\nA mochila está cheia!")
    print(knapsack)


def main():
    knapsack = criar_knapsack()
    armazenamento = criar_armazenamento()
    fractional_knapsack(knapsack, armazenamento)


if __name__ == "__main__":
    main()
