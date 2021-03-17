from Seq1 import Seq

GENE_FOLDER = "./seqs/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print("-----| Exercise 10 |-----")

for gene in gene_list:
    s1 = Seq()
    seq = Seq.read_fasta(Seq, GENE_FOLDER + gene + ".txt")
    print("Gene", gene, ": Most frequent base:", Seq.most_frequent_base(Seq.seq_count(Seq)))