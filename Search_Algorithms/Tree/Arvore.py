from Problem.Jogo8.Estado import Estado
from Problem.Jogo8.Acao import Acao
from Algorithm.PriorityQueue import PriorityQueue

class Arvore:
    def __init__(self, estado: Estado, nivel: int, pai: 'Arvore' = None, acao: Acao = None):
        self.estado = estado
        self.nivel = nivel #seria o g
        self.filhos = []
        self.pai = pai
        self.acao = acao
        self.custo = self.calcular_custo() 

    def adicionar_filho(self, estado: Estado, acao: Acao, lista_prioridade: PriorityQueue) -> 'Arvore':
        novo_filho = Arvore(estado, self.nivel + 1, self, acao)  # add +1 nivel
        self.filhos.append(novo_filho)
        return novo_filho
    
    def calcular_custo(self) -> int:
        heuristica = self.calcular_heuristica()
        custo = self.nivel + heuristica #h+g
        return custo
    
    def calcular_heuristica(self) -> int:
        heuristica = 0
        estado_atual = self.estado
        for i in range(len(estado_atual.tabuleiro)):
            if estado_atual.tabuleiro[i] != i + 1:  #comparando com o valor esperado na posição
                heuristica += 1
        return heuristica
    
    def retornar_acoes(self) -> list[Acao]:
        acoes = []
        arvore = self
        while True:
            if arvore.acao is None:
                break
            acoes.append(arvore.acao)
            arvore = arvore.pai
        acoes.reverse()
        return acoes
