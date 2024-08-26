f = open('Volta_das_aulas\AulaArquivos\dados.txt', 'r')
for i in f.readlines():
    # print(i)
    print(i[:-1])
f.close()