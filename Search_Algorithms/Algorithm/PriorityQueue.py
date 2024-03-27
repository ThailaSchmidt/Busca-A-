class PriorityQueue:
    def __init__(self):
        self.heap = []

    def pai(self, i):
        return (i - 1) // 2

    def filho_esquerdo(self, i):
        return 2 * i + 1

    def filho_direito(self, i):
        return 2 * i + 2

    def inserir(self, no):
        self.heap.append(no)
        indice = len(self.heap) - 1
        while indice != 0 and self.heap[self.pai(indice)][0] > self.heap[indice][0]:
            self.heap[indice], self.heap[self.pai(indice)] = self.heap[self.pai(indice)], self.heap[indice]
            indice = self.pai(indice)

    def heapify_para_baixo(self, i):
        menor = i
        esq = self.filho_esquerdo(i)
        dir = self.filho_direito(i)

        if esq < len(self.heap) and self.heap[esq][0] < self.heap[menor][0]:
            menor = esq
        if dir < len(self.heap) and self.heap[dir][0] < self.heap[menor][0]:
            menor = dir
        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self.heapify_para_baixo(menor)

    def remover_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_para_baixo(0)
        return raiz

    def tamanho(self):
        return len(self.heap)

    def mostrar(self):
        return self.heap
    
    def get(self):
        return self.heap[0]
