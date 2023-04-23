import csv

# import csv

# class Dados:
#     def __init__(self):
#         self.cidades = self.get_cidades()
#         self.itens = self.get_itens()
#         self.rotas = self.get_rotas()

#     def get_cidades(self):
#         cidades = []
#         with open('Source/cidades.csv', 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 origem, destino, tempo_transporte, custo = row
#                 if origem not in cidades:
#                     cidades.append(origem)
#                 if destino not in cidades:
#                     cidades.append(destino)

#         return cidades
    
#     def get_itens(self):
#         itens = {}
#         with open('Source/itens.csv', 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 # separando cada coluna do arquivo
#                 item, peso, tempo_roubo, valor, cidade = row
#                 peso = int(peso)
#                 tempo_roubo = int(tempo_roubo)
#                 valor = int(valor)
#                 # adicionando o item ao dicionário
#                 itens[cidade] = {'item': item, 'peso': peso, 'tempo_roubo': tempo_roubo, 'valor': valor}

#         return itens

#     def get_rotas(self):
#         rotas = {}
#         with open('Source/cidades.csv', 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 origem, destino, tempo_transporte, custo_transporte = row
#                 tempo_transporte = int(tempo_transporte)
#                 custo_transporte = int(custo_transporte)
                
#                 # Adicionando rotas, tanto origem -> destino, quanto destino -> origem
#                 if origem not in rotas:
#                     rotas[origem] = {}
#                 rotas[origem][destino] = {'tempo_transporte': tempo_transporte, 'custo': custo_transporte}

#                 if destino not in rotas:
#                     rotas[destino] = {}
#                 rotas[destino][origem] = {'tempo_transporte': tempo_transporte, 'custo': custo_transporte}

#         return rotas

class Dados:
    def __init__(self):
        self.cidades = self.load_cities()
        self.itens = self.load_items()
        self.rotas = self.load_routes()

    def load_cities(self):
        cities = []
        with open('Source/cidades.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                origin, destination, transport_time, cost = row
                if origin not in cities:
                    cities.append(origin)
                if destination not in cities:
                    cities.append(destination)
        return cities

    def load_items(self):
        items = {}
        with open('Source/itens.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                item, weight, theft_time, value, city = row
                weight = int(weight)
                theft_time = int(theft_time)
                value = int(value)
                items[city] = {'item': item, 'peso': weight, 'tempo_roubo': theft_time, 'valor': value}
        return items

    def load_routes(self):
        routes = {}
        with open('Source/cidades.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                origin, destination, transport_time, transport_cost = row
                transport_time = int(transport_time)
                transport_cost = int(transport_cost)
                if origin not in routes:
                    routes[origin] = {}
                routes[origin][destination] = {'tempo_transporte': transport_time, 'custo': transport_cost}
                if destination not in routes:
                    routes[destination] = {}
                routes[destination][origin] = {'tempo_transporte': transport_time, 'custo': transport_cost}
        return routes