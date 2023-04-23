from populacao import Populacao
import algGenetico
from DadosModel import Dados

alg = algGenetico.GeneticAlgorithm(Populacao(100))

melhor_individuo = alg.run()

print(f' Tempo total ' + str(melhor_individuo.tempo))
print(f' Valor total ' + str(melhor_individuo.valor))
print(f' Peso total ' + str(melhor_individuo.peso))
print(f' Rota completa ' + str(melhor_individuo.rota_de_verdade()))
