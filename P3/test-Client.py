# update
from Client1 import Client

ID = "127.0.0.1"
PORT = 8590
c = Client(ID, PORT)

print("Testing Ping...")
c.talk("PING")

print("Testing Get...")
for i in range(0, 5):
    msg = "GET " + str(i)
    c.talk(msg)

print("Testing Info...")
c.talk("INFO AACCGTA")

print("Testing Comp...")
c.talk("COMP AACCGTA")

print("Testing Rev...")
c.talk("REV AACCGTA")

print("Testing Gene...")
gene_list = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
for gene in gene_list:
    msg = "GENE " + gene
    c.talk(msg)