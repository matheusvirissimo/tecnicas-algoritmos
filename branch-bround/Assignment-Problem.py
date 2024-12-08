import sys
from typing import List, Tuple

class Tarefas:
    def __init__(self, n: int, t: int, pesos: List[List[int]]):
        self.n_pessoas = n
        self.n_tarefas = t
        self.pesos = pesos
        self.custo_min = float('inf')
        self.state_min = [0] * n

def nova_tarefa(n: int, t: int, pesos: List[List[int]]) -> Tarefas:
    return Tarefas(n, t, pesos)

def manipular_tarefa() -> Tarefas:
    n = int(input("\nQuantidade de pessoas e tarefas "))
    pesos = []

    for i in range(n):
        col = []
        for j in range(n):
            cost = int(input(f"\nCusto de pessoas {i} para executar tarefas {j}: "))
            col.append(cost)
        pesos.append(col)

    return nova_tarefa(n, n, pesos)

def imprimir_respostas(t: Tarefas):
    print("\nSolução ótima", t.state_min)
    print("Custo mínimo: ", t.custo_min)

def imprimir_tabela(t: Tarefas):
    print("\n         TAREFAS")
    print("         |", " | ".join(map(str, range(t.n_tarefas))), "|")
    print("        " + "-----" * t.n_tarefas)

    for i in range(t.n_pessoas):
        col = " | ".join(map(str, t.pesos[i]))
        print(f"Person {i} | {col} |")

def imprimir_menu():
    print("\n\n=====   MENU   =====")
    print("1. Criar uma tabela de tarefas")
    print("2. Ver a tabela de tarefas")
    print("3. Solução ótima")

def state_valido(state: List[int], profundidade: int) -> bool:
    return len(state[:profundidade + 1]) == len(set(state[:profundidade + 1]))

def calcular_custo(t: Tarefas, state: List[int], profundidade: int) -> int:
    return sum(t.pesos[i][state[i]] for i in range(profundidade + 1))

def branch(state: List[int], tamanho: int, profundidade: int):
    state[profundidade] += 1
    for i in range(profundidade + 1, tamanho):
        state[i] = 0

def backtrack(state: List[int], tamanho: int, profundidade: int) -> Tuple[List[int], int, bool]:
    while state[profundidade] == tamanho - 1:
        profundidade -= 1
        if profundidade < 0:
            return state, profundidade, False

    branch(state, tamanho, profundidade)
    return state, profundidade, True

def assignment_problem(t: Tarefas):
    if not t.pesos:
        print("\nNenhuma tarefa foi adicionada.")
        return

    state_atual = [0] * t.n_pessoas
    profundidade = 0

    while True:
        derivou = False

        if state_valido(state_atual, profundidade):
            if profundidade < t.n_pessoas - 1:
                derivou = True
            else:
                custo_solucao = calcular_custo(t, state_atual, profundidade)

                if custo_solucao < t.custo_min:
                    t.custo_min = custo_solucao
                    t.state_min = state_atual[:]

        if derivou:
            profundidade += 1
        else:
            if state_atual[profundidade] + 1 == t.n_tarefas:
                state_atual, profundidade, more = backtrack(state_atual, t.n_pessoas, profundidade)
                if not more:
                    break
            else:
                branch(state_atual, t.n_pessoas, profundidade)

def main():
    tarefas = nova_tarefa(0, 0, [])

    while True:
        imprimir_menu()
        escolha = int(input())

        if escolha == 1:
            tarefas = manipular_tarefa()
        elif escolha == 2:
            imprimir_tabela(tarefas)
        elif escolha == 3:
            assignment_problem(tarefas)
            imprimir_respostas(tarefas)
        else:
            sys.exit()

if __name__ == "__main__":
    main()
