import csv

class DataLoader:
    def __init__(self):
        self.items = self.dictionary_items()
        self.round_trip_route = self.dictionary_rotes()
        self.cities = self.cities_list()
    
    def dictionary_items(self):
        items = {}
        with open('items.csv', encoding='utf-8') as items_file:
            treated_items = csv.reader(items_file)
            for treated_item in treated_items:
                item, weight, time, value, cidade = treated_item        
                items[cidade] = {'item': item, 
                                 'weight': int(weight), 
                                 'time': int(time),
                                 'value': int(value)}
        return items
  
    def dictionary_rotes(self):
        rotes = {}
        with open('cidades.csv', encoding='utf-8') as cidades_file:
            treated_cidades = csv.reader(cidades_file)
            for treated_cidade in treated_cidades:
                origin_cidade, destiny_cidade, time, cost = treated_cidade                  

                if origin_cidade not in rotes:
                    rotes[origin_cidade] = {}
                rotes[origin_cidade][destiny_cidade] = {'cost': float(cost), 
                                                        'time': float(time)}

                if destiny_cidade not in rotes:
                    rotes[destiny_cidade] = {}
                rotes[origin_cidade][destiny_cidade] = {'cost': float(cost),
                                                        'time': float(time)}
        
        return rotes

    def cities_list(self):
        cities = []
        with open('cidades.csv', encoding='utf-8') as cidades_file:
            treated_cidades = csv.reader(cidades_file)
            for treated_cidade in treated_cidades:
                origin_cidade, destiny_cidade, distance, value = treated_cidade
                if origin_cidade not in cities:
                    cities.append(origin_cidade)
        return cities
