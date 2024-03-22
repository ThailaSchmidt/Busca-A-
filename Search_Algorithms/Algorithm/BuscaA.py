# Implementar heurística como função    def heuristica(estado: Estado)->int
# Implementar estrutura que armazena nós da árvore que ainda não foram analisados/expandidos
# Heap mínimo
# Lista de prioridades
# Lista simples com método de ordenação

import time

from Algorithm.Algorithm import Algorithm
from Problem.Jogo8.Estado import Estado
from Tree.Arvore import Arvore

class buscaA (Algorithm):
    def __init__(self, estado_inicial: Estado, objetivo: Estado):
        super().__init__("Busca A*", Arvore(estado_inicial), objetivo)



    def custo(self, nivel):
        while True:
            if ('fora do lugar'):
                h =+ 1
            else:
                break
        g = nivel
        novo_valor = h + g
        self.valor = novo_valor
        for filho in self.filhos:
            filho.custo(novo_valor)

    def busca_A(self):
        inicio = time.time()
        analisar = [self.arvore_busca]

        while True:
            # Se lista está vazia, instância não possui solução
            if not analisar:
                break
            # Expande quando g+h for o menor
            # h -> n de peças fora do lugar
            # g -> custo acumulado
            arvore = min(analisar, key=lambda x: x.custo())
            self.estados_analisados += 1
            


            # Verifica se estado analisado é objetivo
            if not self.eh_objetivo(arvore.estado):
                analisar.extend(self.expandir(arvore))
                analisar.custo(self, nivel)
            else:
                self.solucao = arvore.retornar_acoes()
                break
        fim = time.time()
        self.tempo_execucao = fim - inicio