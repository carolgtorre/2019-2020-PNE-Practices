from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")
IP = "192.168.1.144"
PORT = 139
c = Client(IP, PORT)

PROJECT_PATH = "../P0/seqs/"

s1 = Seq()
s1.read_fasta(PROJECT_PATH + 'FRAT1.txt')
print(s1)

count = 0
i = 0
while i < len(s1.strbases) and count < 5:
    fragment = s1.strbases[i:i+10]
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
    #print(c.talk(fragment))

