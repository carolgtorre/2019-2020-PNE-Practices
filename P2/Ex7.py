from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")
IP = "127.0.0.1"
PORT = 52123
PORT_2 = 25625
c = Client(IP, PORT)
c_2 = Client(IP, PORT_2)

PROJECT_PATH = "../P0/seqs/"

s1 = Seq()
s1.read_fasta(PROJECT_PATH + 'FRAT1.txt')
print(s1)

count = 0
i = 0
while i < len(s1.strbases) and count < 10:
    fragment = s1.strbases[i:i+10]
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
