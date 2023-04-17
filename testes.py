import data_loader as dl

#-------------------  TESTES  --------------------
#Fábria de dados  
    # Cidades - ok
    # Itens - ok
    # Viagens- ok

# Geração de 1 indivíduo
    # Aleatório
    # Preset
    # Fitness automático na geração de ambos
    # Geração de rotas
    # Mutação

# Geração de uma população
    # Mutação
    # Top
    # Selecionar o melhor
    # Crossover

# Fluxo do Algoritmo Genético
    #selfs
    # if fitness > ultimo_fitness:
    # break

d = dl.DataLoader()

#Verificar a Fábrica de Dados
print(d.cities)
print("")
print(d.items)
print("")
print(d.round_trip_route)

# print("")
# print(f"As cidades são únicas? {len(f.cidades) == len(set(f.cidades))}")

# #Teste de geração de indivíduo
# print("")
# ind_rand = rota.Rota(f)
# print("Individuo aleatório:")
# print(ind_rand)
# print("")


# # Teste de gerar individuos aleatórios até que o peso seja maior que 20 ou o tempo maior que 72
# print("Gerando individuos aleatórios até que o peso seja maior que 20 ou o tempo maior que 72...")
# count = 0
# while True:
#     print(f"tentativa: {count}")
#     count += 1
#     ind_rand = rota.Rota(f)
#     if ind_rand.peso > 20 or ind_rand.tempo_total > 72:
#         if ind_rand.fitness_val > float('-inf'):
#             print("Indivíduo inválido gerado:")
#             print (ind_rand)

#             print(" ")
#             print("Testando criar um indivíduo com a rota do indivíduo inválido:")
#             ind_preset = rota.Rota(f, ind_rand.rota)
#             print(ind_preset)
#             print("")
#             print("Testando re-fitnessear o indivíduo inválido:")
#             ind_preset.fitness = ind_preset.fitness()
#             print(ind_preset)
#             break


# ind_teste = rota.Rota(f, rota =['Escondidos', 'Algas', 'Leão', 'Campos', 'Riacho de Fevereiro', 'Leão', 'Além-do-Mar', 'Campos', 'Guardião', 'Santa Paula', 'Riacho de Fevereiro', 'Algas', 'Escondidos', 'Além-do-Mar'])

# print(ind_teste)

# pop = rotas.Rotas(f)

# mutados = pop.mutacao()

# for i in range(len(mutados)):
#     print(f"Mutado {i+1}:")
#     print(mutados[i])
#     print("")