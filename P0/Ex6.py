import Seq0

ID = "U5.txt"
U5_Seq = Seq0.seq_read_fasta(ID)
dna = U5_Seq[0:20]

bases = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T'}
rev_seq = ''.join([bases[base] for base in dna[::-1]])
print("-----| Exercise 6 |-----")
print(rev_seq)