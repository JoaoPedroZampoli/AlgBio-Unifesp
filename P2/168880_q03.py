# Exercício 03 - Perguntas teóricas sobre Alinhamento Blast.

# Questão 1. Explique o funcionamento básico do algoritmo BLAST (Basic Local Alignment Search Tool) e como ele difere dos métodos de alinhamento global, como o algoritmo de Needleman-Wunsch.

# Resposta: É uma ferramenta utilizada para encontrar regiões de similaridade local entre sequências (DNA, RNA e/ou Proteínas)
# Ele verifica por segmentos de alta similaridade entre as sequências, ao invés de comparar a sequência inteira e a compara com um banco de dados (subject)
# Depois disso, ele tenta encontrar em ambas as direções para encontrar alinhamentos locais significativos e ao final, retorna um score de similaridade entre as sequências.
# A principal diferença entre o Needleman-Wunsch e o BLAST é que o Needleman-Wunsch é um algoritmo de alinhamento global, ou seja, ele compara a sequência inteira com outra sequência inteira, enquanto o BLAST compara segmentos de alta similaridade entre as sequências.


# Questão 2. Compare o BLAST e o algoritmo Smith-Waterman em termos de precisão e eficiência.  Em quais situações é mais apropriado utilizar o BLAST em vez do Smith-Waterman e vice-versa?

# Resposta: O algoritmo Smith-Waterman é um algoritmo de alinhamento local, que é mais preciso que o BLAST, porém é mais lento e consome mais recursos computacionais.
# O BLAST é mais rápido e consome menos recursos computacionais, porém é menos preciso que o Smith-Waterman, portanto, ele é melhor em cenários de grandes bancos de dados e quando a precisão não é tão importante.
# Já o Smith-Waterman é mais apropriado quando a precisão é mais importante que a eficiência.


# Questão 3. O que é query e subject dentro do programa BLAST?

# Resposta: 
# Query é a sequência que está sendo comparada com o banco de dados (subject) 
# Subject é o banco de dados que está sendo comparado com a sequência (query).


# Questão 4. Descrever o que é gap match e mismatch:

# Resposta:
# Gap match é a penalidade aplicada quando um gap é aberto na sequência.
# Mismatch é a penalidade aplicada quando um nucleotídeo ou aminoácido diferente é encontrado na sequência.


# Questão 5. Descreva as seguintes definições da saída do BLAST Query e E-Value:

# Resposta:
# O Blast Query Score é formado pelo Max Score e Total Score, onde o Max Score é o maior score que pode ser obtido no alinhamento e o Total Score é o valor obtido pelo alinhamento
# E-Value é o número esperado de hits com um score igual ou maior que o observado, por acaso, em um banco de dados de tamanho igual ao do subject.
