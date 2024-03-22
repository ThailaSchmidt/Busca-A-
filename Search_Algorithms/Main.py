from Algorithm.BFS import BFS
from Problem.Jogo8.Complexidade import Complexidade
from Problem.Jogo8.Jogo8 import Jogo8

instancia = Jogo8(3, Complexidade.Dificil)
print(instancia.estado_inicial)
bfs = BFS(instancia.estado_inicial, instancia.estado_final)
bfs.encontrar_solucao()
print(f"Solução Ótima: {bfs.solucao}")
print(f"Custo da S*: {len(bfs.solucao)}")
print(f"Tempo de execução: {bfs.tempo_execucao:.2f}s")
print(f"Quantidade de estados analisados: {bfs.estados_analisados}")
