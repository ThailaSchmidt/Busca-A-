from abc import abstractmethod

from Problem.Jogo8.Acao import Acao
from Problem.Jogo8.Estado import Estado
from Problem.Jogo8.Jogo8 import Jogo8
from Tree.Arvore import Arvore
from Algorithm.PriorityQueue import PriorityQueue

class Algorithm:
    def __init__(self, nome: str, arvore_busca: Arvore, objetivo: Estado):
        self.nome = nome
        self.arvore_busca = arvore_busca
        self.objetivo = objetivo
        self.solucao = None
        self.tempo_execucao = None
        self.estados_analisados = 0

    @abstractmethod
    def encontrar_solucao(self):
        pass

    @staticmethod
    def expandir(arvore: Arvore) -> list[Arvore]:
        estados_expandidos = []
        for acao in Acao:
            # Otimização — Não repetir ação inversa da última usada
            if arvore.pai is None or acao != arvore.acao.inversa():
                novo_estado = Jogo8.transicao(arvore.estado, acao)
                # Testa se a ação foi válida
                if novo_estado != arvore.estado:
                    estados_expandidos.append(arvore.adicionar_filho(novo_estado, acao, PriorityQueue))
        return estados_expandidos

    def eh_objetivo(self, estado_atual: Estado) -> bool:
        return estado_atual == self.objetivo
