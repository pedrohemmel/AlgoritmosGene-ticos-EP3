import copy
from DadosModel import Dados
from individuo import Individuo


class Populacao:
    def __init__(self, tamanho):
        self.n = tamanho
        self.populacao = [Individuo(Dados()) for i in range(tamanho)]

    def fitness_populacao(self):
        fitness_list = []
        for individuo in self.populacao:
            fitness = individuo.fitness()
            fitness_list.append(fitness)
        return fitness_list

    def mutacao(self):
        mutados = []
        for individuo in copy.deepcopy(self.populacao):
            mutado = individuo.mutacao()
            mutados.append(mutado)
        return mutados

    def crossover(self):
        nova_populacao = []
        nova_rota = []

        meio = len(self.populacao) // 2

        pop_esquerda = self.populacao[meio:]
        pop_direita = self.populacao[:meio]

        for i in range(meio):
            rota_esquerda = pop_esquerda[i].rota_de_verdade()
            rota_direita = pop_direita[i].rota_de_verdade()

            rota_esquerda = rota_direita[:len(rota_direita) // 2]
            rota_direita = rota_esquerda[len(rota_esquerda) // 2:]
            for cidade in Dados().load_cities():
                if rota_direita.count(cidade) == 1 and cidade not in rota_esquerda:
                    rota_final = (rota_direita + rota_esquerda)
                elif rota_esquerda.count(cidade) == 1 and cidade not in rota_direita:
                    rota_final = (rota_direita + rota_esquerda)

            
            nova_rota.append(rota_final)

        for rota in nova_rota:
            nova_populacao.append(Individuo(Dados(), rota))

        return nova_populacao

    def top_individuo(self):
        return max(self.populacao, key=lambda x: x.fitness())

    def top_fitness(self):
        return self.top_individuo().fitness()

    def sort_pop(self, populacao):
        sorted_pop = [populacao[0]]

        for i in range(1, len(populacao)):
            for j in range(len(sorted_pop)):
                if populacao[i].fitness() > sorted_pop[j].fitness():
                    sorted_pop.insert(j, populacao[i])
                    break
                elif j == len(sorted_pop) - 1:
                    sorted_pop.append(populacao[i])
                    break
        return sorted_pop

    def selecionar(self, pop_mutada, pop_crossover):
        pop_total = self.populacao + pop_mutada + pop_crossover
        nova_populacao = self.sort_pop(pop_total)
        self.populacao = nova_populacao[:self.n]
        