from Problem.Jogo8.Estado import Estado
from Problem.Jogo8.Acao import Acao


class Arvore:
    def __init__(self, estado: Estado, pai: 'Arvore' = None, acao: Acao = None):
        self.estado = estado
        self.filhos = []
        self.pai = pai
        self.acao = acao

    def adicionar_filho(self, estado: Estado, acao: Acao) -> 'Arvore':
        novo_filho = Arvore(estado, self, acao)
        self.filhos.append(novo_filho)
        return novo_filho

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
