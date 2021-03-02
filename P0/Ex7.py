# noinspection PyUnresolvedReferences
import Seq0
ID = "U5.txt"

U5_Seq = Seq0.seq_read_fasta(ID)
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

original = U5_Seq[0:20]
comp = "".join(complement[letter] for letter in original)

print("-----| Exercise 7 |-----")
print("The complement is : {}".format(comp))