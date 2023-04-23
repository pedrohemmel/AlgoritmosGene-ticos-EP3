class GeneticAlgorithm:
    def __init__(self, population, max_generations=50, min_error=0.01):
        self.population = population
        self.max_generations = max_generations
        self.min_error = min_error
        self.error = None
        self.generations = 1

    def get_final_error(self):
        if self.error is not None:
            return self.error
        else:
            return "Error value not available. Algorithm has not run yet."

    def get_number_of_generations(self):
        return self.generations

    def run(self):
        last_fitness = self.population.top_fitness()

        while self.generations <= self.max_generations:
            mutated_population = self.population.mutacao()
            crossover_population = self.population.crossover()
            self.population.selecionar(mutated_population, crossover_population)
            fitness = self.population.top_fitness()
            error = abs(fitness - last_fitness)
            last_fitness = fitness
            self.generations += 1
            if self.generations % 10 == 0:
                print(f"Generation: {self.generations}, Error: {error}, Fitness: {fitness}")
            if error <= self.min_error:
                self.error = error
                break
        return self.population.top_individuo()