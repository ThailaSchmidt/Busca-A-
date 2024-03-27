from Algorithm.BuscaA import buscaA
from Problem.Jogo8.Complexidade import Complexidade
from Problem.Jogo8.Jogo8 import Jogo8

instancia = Jogo8(4, Complexidade.Dificil)
print(instancia.estado_inicial)

busca_a = buscaA(instancia.estado_inicial, instancia.estado_final) 
busca_a.busca_A()  

print(f"Solução Ótima: {busca_a.solucao}")
print(f"Custo da S*: {len(busca_a.solucao)}")
print(f"Tempo de execução: {busca_a.tempo_execucao:.2f}s")
print(f"Quantidade de estados analisados: {busca_a.estados_analisados}")
print(instancia.estado_final)