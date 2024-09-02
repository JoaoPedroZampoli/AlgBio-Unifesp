from Bio import SeqIO
from matplotlib import pyplot as plt

Arquivo1 = "/Users/jpsza/OneDrive/Documentos/GitHub/Pessoal/AlgBio-Unifesp/Projeto_AlgBio/MN908947.3.fasta"
Arquivo2 = "/Users/jpsza/OneDrive/Documentos/GitHub/Pessoal/AlgBio-Unifesp/Projeto_AlgBio/MT012098.fasta"
Arquivo3 = "/Users/jpsza/OneDrive/Documentos/GitHub/Pessoal/AlgBio-Unifesp/Projeto_AlgBio/MT324062.1.fasta"
Arquivo4 = "/Users/jpsza/OneDrive/Documentos/GitHub/Pessoal/AlgBio-Unifesp/Projeto_AlgBio/MZ264787.1.fasta"
Arquivo5 = "/Users/jpsza/OneDrive/Documentos/GitHub/Pessoal/AlgBio-Unifesp/Projeto_AlgBio/NC_019843.3.fasta"

for i in range(1,6):
    if i == 1:
        arquivo = Arquivo1
    elif i == 2:
        arquivo = Arquivo2
    elif i == 3:
        arquivo = Arquivo3
    elif i == 4:
        arquivo = Arquivo4
    elif i == 5:
        arquivo = Arquivo5

    with open(arquivo, "r") as handle:
        for Registro in SeqIO.parse(handle, "fasta"):
            print(Registro.id)
            print(Registro.description)
            #print(Registro.seq)
            print(len(Registro))
            