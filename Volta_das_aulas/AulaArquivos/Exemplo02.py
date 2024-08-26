f = open('Volta_das_aulas\AulaArquivos\dados.txt', 'r')
s = open('Volta_das_aulas\AulaArquivos\saida.txt', 'w')

for i in f.readlines():
    s.write(i+' lido')

s.close()
f.close()