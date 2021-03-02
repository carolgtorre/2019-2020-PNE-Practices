import Seq0

GENE_FOLDER = "./seqs/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 3 |-----")
for gene in gene_list:
    seq = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene", gene, "---> Length:", Seq0.seq_len(seq))
