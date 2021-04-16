import socket
import Server_utils
import termcolor
from Seq1 import Seq

list_sequences = ["AAAA", "CCCC", "TTTT", "GGGG", "ACTG"]
# gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
IP = "127.0.0.1"
PORT = 6463

SEQ_GET = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("Seq server is configured!")
client_address_list = []
count_connections = 0
while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        print("A client has connected to the server!")
        client_address_list.append((cs, client_ip_port))
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        formatted_msg = Server_utils.format_command(msg)
        formatted_msg = formatted_msg.split(" ")

        command = formatted_msg[0]
        try:
            argument = formatted_msg[1]
        except IndexError:
            argument = ""
        response = ""
        if command == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!"
            print(response)

        elif command == "GET":
            #Server_utils.get(list_sequences, cs, argument)
            termcolor.cprint("GET", 'yellow')
            response = SEQ_GET[int(argument)]
            print(response)
            #termcolor.cprint("GET", 'green')
            #response = get_cmd(int(arg))

        elif command == "INFO":
            cs.send(response.encode())

        elif command == "COMP":
            termcolor.cprint('COMP', 'green')
            s = Seq(argument)
            complement = s.complement()
            response = complement + '\n'
            cs.send(response.encode())
            print(response)

        elif command == "REV":
            termcolor.cprint('REV', 'green')
            s = Seq(argument)
            rev = s.reverse()
            response = rev + '\n'
            cs.send(response.encode())
            print(response)

        elif command == "GENE":
            gene = "../P0/seqs/"
            termcolor.cprint("GENE", 'green')
            s = Seq()
            s.read_fasta(gene + argument + ".txt")
            response = str(s) + '\n'
            print(response)
            cs.send(response.encode())

        else:
            response = "Not available command"
            termcolor.cprint(response, "red")
            cs.send(response.encode())