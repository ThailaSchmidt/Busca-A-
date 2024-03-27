# Implementar heurística como função    def heuristica(estado: Estado)->int
# Implementar estrutura que armazena nós da árvore que ainda não foram analisados/expandidos
# Heap mínimo
# Lista de prioridades
# Lista simples com método de ordenação

import time

from Algorithm.Algorithm import Algorithm
from Problem.Jogo8.Estado import Estado
from Tree.Arvore import Arvore
from Algorithm.PriorityQueue import PriorityQueue #lista de prioridade para descobrir nó de menor custo

class buscaA (Algorithm):
    def __init__(self, estado_inicial: Estado, objetivo: Estado):
        super().__init__("Busca A*", Arvore(estado_inicial, 0), objetivo)

    def busca_A(self):
        inicio = time.time()
        analisar = PriorityQueue()
        analisar.inserir((self.arvore_busca.custo, self.arvore_busca)) 
        
        while True:
            # Se lista está vazia, instância não possui solução
            if not analisar:
                break
            # Expande quando o custo for o menor
            _, arvore = analisar.remover_min()  # Obtém o nó com menor custo
            self.estados_analisados += 1
            # Verifica se estado analisado é objetivo
            if not self.eh_objetivo(arvore.estado):
                for filho in self.expandir(arvore): # Calcula o custo do filho
                    analisar.inserir((filho.custo, filho)) # Adiciona o filho à fila de prioridades com seu custo
            else:
                self.solucao = arvore.retornar_acoes()
                break
        fim = time.time()
        self.tempo_execucao = fim - inicio