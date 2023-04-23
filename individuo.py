from DadosModel import Dados
import numpy as np
import random
import copy

class Individuo:
    def __init__(self, dados: Dados, rota=None):
        self.dados = dados
        self.rota = rota or self.rand_rota()
        self.peso = self.calcular_peso()
        self.valor = self.calcular_valor()
        self.tempo = self.calcular_tempo()
        self.fit = self.fitness()

    def rand_rota(self):
        rota = np.random.permutation(self.dados.cidades)
        while rota[0] == "Escondidos" or rota[1] == "Escondidos":
            rota = np.random.permutation(self.dados.cidades)
        return ["Escondidos"] + rota.tolist()

    def mutacao(self):
        nova_rota = copy.deepcopy(self.rota)
        i, j = random.sample(range(2, len(nova_rota)), 2)
        nova_rota[i], nova_rota[j] = nova_rota[j], nova_rota[i]
        if nova_rota[1] == "Escondidos":
            return self.mutacao()
        return Individuo(self.dados, rota=nova_rota)

    def check_rota(self):
        if self.rota[0] != "Escondidos":
            return False
        if self.rota.count("Escondidos") != 2:
            return False
        if self.rota[1] == "Escondidos":
            return False
        return True

    def rota_de_verdade(self):
        rota = []
        i = 1
        rota.append(self.rota[0])
        while self.rota[i] != 'Escondidos':
            rota.append(self.rota[i])
            i += 1
        rota.append(self.rota[i])
        return rota

    def rota_sem_escondidos(self):
        rota= []
        i = 1
        while self.rota[i] != 'Escondidos':
            rota.append(self.rota[i])
            i += 1
        return rota

    def calcular_tempo(self):
        tempo = 0
        rota_de_verdade = self.rota_de_verdade()
        rotas = self.dados.rotas
        
        for i in range(len(rota_de_verdade) - 1):
            cidade_atual = rota_de_verdade[i]
            proxima_cidade = rota_de_verdade[i+1]
            tempo += rotas[cidade_atual][proxima_cidade]["tempo_transporte"]
        return tempo
        
    def calcular_custo(self):
        custo = 0
        rotas = self.dados.rotas
        for i in range(len(self.rota) - 1):
            cidade_atual = self.rota[i]
            proxima_cidade = self.rota[i+1]
            custo += rotas[cidade_atual][proxima_cidade]["custo"]
        return custo

    def calcular_peso(self):
        items = self.dados.itens
        peso = 0
        rota = self.rota_sem_escondidos()
        for cidade in rota:
            peso += items[cidade]['peso']
        return peso

    def calcular_valor(self):
        valor = 0
        items = self.dados.itens
        rota = self.rota_sem_escondidos()
        for cidade in rota:
            valor += items[cidade]["valor"]
        return valor

    def fitness(self):
        if not self.check_rota():
            return float("-inf")
        if self.calcular_peso() > 20:
            return float("-inf")
        if self.calcular_tempo() > 72:
            return float("-inf")
        return self.calcular_valor() - self.calcular_custo()