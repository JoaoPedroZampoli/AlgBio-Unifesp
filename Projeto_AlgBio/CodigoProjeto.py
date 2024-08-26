# Importando as bibliotecas necessárias
from Bio import Entrez, SeqIO
from Bio.SeqUtils import gc_fraction, MeltingTemp as mt
from Bio.Seq import Seq
from Bio.Align import PairwiseAligner
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt

# Configurando o email para o NCBI
Entrez.email = "seu_email@exemplo.com"

# IDs das sequências
seq_ids = ["MN908947.3", "MT012098", "MT324062.1", "MZ264787.1", "NC_019843.3"]

# Função para baixar e ler as sequências do GenBank
def fetch_sequences(seq_ids):
    sequences = {}
    for seq_id in seq_ids:
        handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text")
        record = SeqIO.read(handle, "fasta")
        handle.close()
        sequences[seq_id] = record
    return sequences

# Baixar as sequências
sequences = fetch_sequences(seq_ids)

# a) Descrição das informações (organismo e origem)
def describe_sequences(sequences):
    descriptions = {}
    for seq_id, record in sequences.items():
        descriptions[seq_id] = record.description
        print(f"ID: {seq_id}")
        print(f"Descrição: {record.description}")
    return descriptions

# Descrever as sequências
describe_sequences(sequences)

# b) Leitura dos arquivos FASTA e tamanho das sequências
def sequence_lengths(sequences):
    lengths = {}
    for seq_id, record in sequences.items():
        lengths[seq_id] = len(record.seq)
        print(f"ID: {seq_id} | Tamanho: {len(record.seq)}")
    return lengths

# Calcular o tamanho das sequências
sequence_lengths(sequences)

# c) Gráfico de barras com a frequência dos nucleotídeos
def nucleotide_frequencies(sequences):
    for seq_id, record in sequences.items():
        freqs = {nuc: record.seq.count(nuc) for nuc in "ACGT"}
        plt.bar(freqs.keys(), freqs.values())
        plt.title(f"Frequência de nucleotídeos - {seq_id}")
        plt.xlabel("Nucleotídeo")
        plt.ylabel("Frequência")
        plt.show()

# Plotar os gráficos de frequência dos nucleotídeos
nucleotide_frequencies(sequences)

# d) Cálculo do conteúdo gc_fraction e temperatura de melting
def gc_content_and_melting_temp(sequences):
    for seq_id, record in sequences.items():
        gc_content = gc_fraction(record.seq)
        melting_temp = mt.Tm_GC(record.seq)
        print(f"ID: {seq_id} | gc_fraction%: {gc_content:.2f} | Temperatura de Melting: {melting_temp:.2f}°C")

# Calcular o conteúdo gc_fraction e a temperatura de melting
gc_content_and_melting_temp(sequences)

# e) Alinhamento global dos primeiros 300 nucleotídeos
def pairwise_alignment(sequences):
    aligner = PairwiseAligner()
    for i in range(len(seq_ids)):
        for j in range(i+1, len(seq_ids)):
            seq1 = sequences[seq_ids[i]].seq[:300]
            seq2 = sequences[seq_ids[j]].seq[:300]
            score = aligner.score(seq1, seq2)
            alignment = aligner.align(seq1, seq2)[0]
            print(f"Alinhamento entre {seq_ids[i]} e {seq_ids[j]}")
            print(f"Score: {score:.2f}")
            print(alignment)
            print("\n")

# Realizar o alinhamento global
pairwise_alignment(sequences)

# f) Tradução das sequências e gráfico de frequência de aminoácidos
def protein_translation_and_frequency(sequences):
    for seq_id, record in sequences.items():
        protein_seq = record.seq.translate()
        analyzed_seq = ProteinAnalysis(str(protein_seq))
        amino_acids = analyzed_seq.count_amino_acids()
        plt.bar(amino_acids.keys(), amino_acids.values())
        plt.title(f"Frequência de aminoácidos - {seq_id}")
        plt.xlabel("Aminoácido")
        plt.ylabel("Frequência")
        plt.show()

# Traduzir as sequências e plotar o gráfico de frequência de aminoácidos
protein_translation_and_frequency(sequences)

# g) Análise da estrutura secundária das proteínas
def secondary_structure_analysis(sequences):
    for seq_id, record in sequences.items():
        protein_seq = record.seq.translate()
        analyzed_seq = ProteinAnalysis(str(protein_seq))
        secondary_structure_fraction = analyzed_seq.secondary_structure_fraction()
        print(f"ID: {seq_id} | Estrutura secundária: {secondary_structure_fraction}")

# Analisar a estrutura secundária das proteínas
secondary_structure_analysis(sequences)
