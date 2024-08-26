arq = "/Users/jpsza/OneDrive/Documentos/GitHub/Pessoal/AlgBio-Unifesp/Volta_das_aulas/Aula2Arquivos/Corona_genomic.fasta"
e = {}
l = []

f = open(arq, 'r')

linhas = f.readlines()

for i in linhas:
    if(i[0] == '>'):
        l.append(e.copy())
        e['Descrição'] = i
        e['Sequência'] = ''
    else:
        e['Sequência'] = e['Sequência'] + i[0:-2]

l.remove({})
print(e)
f.close()

arq = "/Users/jpsza/OneDrive/Documentos/GitHub/Pessoal/AlgBio-Unifesp/Volta_das_aulas/Aula2Arquivos/multifasta.fasta"