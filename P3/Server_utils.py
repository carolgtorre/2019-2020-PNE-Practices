# update
import termcolor
import colorama
from Seq1 import Seq

list_sequences = ["AAAA", "CCCC", "TTTT", "GGGG", "ACTG"]

SEQ_GET = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]

def print_colored(message, color):
    colorama.init(strip="False")
    print(termcolor.colored("Message", "yellow"))
def format_command(command):
    return command.replace("\n", "").replace("\r", "")
def ping():
    termcolor.cprint("PING command!", "yellow")
    response = "OK!"
    print(response)

def get(cs, SEQ_GET, argument):
    termcolor.cprint("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)

def info(cs, argument):
    termcolor.cprint("INFO", "yellow")
    s = Seq(argument)
    length = Seq.len(s)
    a, c, g, t = s.count_bases()
    # a = dict_count['A'][0]
    pa = (a * 100) / length
    # c = dict_count['C'][0]
    pc = (c * 100) / length
    # g = dict_count['G'][0]
    pg = (g * 100) / length
    # t = dict_count['T'][0]
    pt = (t * 100) / length
    first = 'Total length: ' + str(len(argument)) + '\n'
    second = 'A: ' + str(a) + ' ' + str(pa) + '%' + '\n'
    third = 'C: ' + str(c) + ' ' + str(pc) + '%' + '\n'
    fourth = 'G: ' + str(g) + ' ' + str(pg) + '%' + '\n'
    fifth = 'T: ' + str(t) + ' ' + str(pt) + '%' + '\n'
    print(first, second, third, fourth, fifth)

def comp(Seq, argument):
   termcolor.cprint("COMP", "yellow")
   s = Seq(argument)
   complement = s.complement()
   response = complement + "\n"
   print(response)

def rev(Seq, argument):
        # -- Create the object sequence from the string
        termcolor.cprint('REV', "yellow")
        s = Seq(argument)
        reverse = s.reverse()
        print(reverse)

def gene(Seq, argument):
    gene_path = './seqs/'
    termcolor.cprint('GENE', "yellow")
    # s = Seq(argument)
    s = Seq()
    s.read_fasta(gene_path + argument + '.txt')
    response = str(s) + '\n'
    print(response)