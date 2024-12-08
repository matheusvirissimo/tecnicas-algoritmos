import heapq
from collections import defaultdict # namedtuple

# Estrutura para um nó da árvore
class No:
    def __init__(self, caracter, frequencia):
        self.caracter = caracter
        self.frequencia = frequencia
        self.esq = None
        self.dir = None

    # Comparadores para usar com heapq
    def __lt__(self, other):
        return self.frequencia < other.frequencia

# Função para construir o heap mínimo
def build_min_heap(caracteres, frequencias):
    heap = []
    for char, freq in zip(caracteres, frequencias):
        heapq.heappush(heap, No(char, freq))
    return heap

# Função principal do algoritmo de Huffman
def huffman_algoritmo(caracteres, frequencias):
    heap = build_min_heap(caracteres, frequencias)
    
    # Construir a árvore de Huffman
    while len(heap) > 1:
        esq = heapq.heappop(heap)
        dir = heapq.heappop(heap)
        merged = No('$', esq.frequencia + dir.frequencia)
        merged.esq = esq
        merged.dir = dir
        heapq.heappush(heap, merged)
    
    # Raiz da árvore de Huffman
    raiz = heap[0]
    return raiz

# Função para gerar os códigos (binários) a partir da árvore
def gerar_codigo(no, codigo_atual="", codigo=None):
    if codigo is None:
        codigo = {}
    
    if no is None:
        return codigo
    
    # Nó folha
    if no.caracter != '$':
        codigo[no.caracter] = codigo_atual
    
    gerar_codigo(no.esq, codigo_atual + "0", codigo)
    gerar_codigo(no.dir, codigo_atual + "1", codigo)
    
    return codigo

# Função para calcular frequências dos caracteres na string
def calcular_frequencia(string):
    frenquencia_map = defaultdict(int)
    for char in string:
        frenquencia_map[char] += 1
    
    caracteres = list(frenquencia_map.keys())
    frequencias = list(frenquencia_map.values())
    return caracteres, frequencias

# Função principal
def main():
    tamanho = int(input("Tamanho máximo da string: "))
    
    if tamanho > 10000:
        print("Tamanho muito grande.")
        return
    
    string = input("Digite a string: ").strip()
    
    if len(string) > tamanho:
        print("A frase digitada excede o máximo possível.")
        return
    
    caracteres, frequencias = calcular_frequencia(string)
    raiz = huffman_algoritmo(caracteres, frequencias)
    codigo = gerar_codigo(raiz)
    
    print("\nCódigos de Huffman:")
    for char, code in codigo.items():
        print(f"{char}: {code}")

if __name__ == "__main__":
    main()
