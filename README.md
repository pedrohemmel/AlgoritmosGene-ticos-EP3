# Algoritmos Genéticos
## Introdução 
Uma técnica de busca e otimização inspirada na Biologia. Se baseia nos conceitos genéticos, como a seleção natural, recombinação e mutação para encontrar a melhor solução para um problema específico.
Empregam uma estratégia de busca paralela e estruturada, mas aleatória.
## Funcionamento
O Algoritmo é iniciado com a criação de uma população base (inicial). A partir dessa população os indivíduos são avaliados por uma função de aptidão que mede a qualidade da solução em relação ao problema a ser analisado.

A função de aptidão que irá especificar, com base no problema analisado, qual será o foco do algoritmo para encontrar a melhor solução possível.
### Exemplo: 
- Função de restrição -> Para esses casos a função de aptidão terá como foco considerar as retrições base do problema para resolvê-lo.

Logo após a avaliação realizada através do tipo de função de aptidão, são selecionados os indivíduos mais aptos para se cruzarem, o que irá gerar uma nova população de soluções. O processo é realizado de forma repetida em um intervalo, gerando novas soluções que se aproximam cada vez mais da solução "ótima" do problema analisado.

## Parâmetros Genéticos
Alguns parâmetros possuem uma importância muito relevante para a demanda de tempo e qualidade do algoritmo.
### Exemplos:
- <b>Tamanho da População:</b> Quanto maior a população, maior será a cobertura do espaço de busca, o que ocasionará um melhor desempenho. Porém, maior será a necessidade de recursos computacionais ou que o tempo de execução do algoritmo seja maior.
- <b>Taxa de Cruzamento:</b> Quanto maior a taxa de cruzamento, mais rapidamente serão introduzidas novas estruturas na população. Porém é necessário ter o conhecimento que uma taxa muito elevada pode ocorrer a perca de estruturas de alta aptidão e uma taxa muito baixa ocasionará um processo mais lento.
- <b>Taxa de Mutação:</b> Uma taxa de mutação mais baixa previne que uma dada posição fique estagnada em um valor só e com uma taxa mais elevada a busca se torna aleatória.
- <b>Intervalo de Geração:</b> Essa taxa controla a porcentagem da população que será substituída a cada processo do algoritmo e assim como a taxa de cruzamento, valores muito altos podem ocasionar a perda de estruturas de alta aptidão e valores mais baixos ocasionarão uma lentidão no algoritmo.

## Problema
"Joana era uma desenvolvedora de software com grande experiência em Inteligência Artificial. Sua vida mudou ao receber um desafio da Agência Internacional do Crime (AIC): conseguir fazer um grande roubo em diversas cidades com o menor tempo possível e conseguir carregar o maior valor possível e se tornar uma especialista da instituição. Como estava muito entediada com o seu trabalho atual, topou o desafio.

Para manter a discrição, Joana deve viajar por diversas cidades apenas por rodovias, aeroportos ou ferrovias usando transporte coletivo pago. O deslocamento leva tempo e Joana tem 72 horas para cumprir o seu objetivo. Cada roubo demora um tempo determinado e Joana não poderá dormir durante os deslocamentos por estar atenta a polícia.

Ela deve levar uma mochila iguais de mochileiros em viagens que consegue levar até 20 kg de peso. Outra regra importante é que Joana deve ir de uma cidade a outra carregando os itens já roubados. 

Com a quantidade máxima, deve ir a sede da AIC para receber a seu prêmio. Joana irá sair e retornar a sede AIC na cidade de Escondidos."

## Objetivo
Nosso objetivo foi criar um Algoritmo Genético que traçasse a melhor rota (maximizando o ganho de Joana) com base nas retrições acima, uso do crossover e mutação.

Obs: É necessário executar o código pelo Visual Studio Code!!
