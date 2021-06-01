import http.client
import json
from Seq1 import Seq
from termcolor import colored

def print_colored(message, data, color):
    print(colored(message, color), end="")
    print(data)

DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226906",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMETERS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
try:
    user_gene = input("Enter the Gene that you want to analyse: ")
    ID = DICT_GENES[user_gene]
    connection.request("GET", ENDPOINT + ID + PARAMETERS)
    response = connection.getresponse()
    print("\nSERVER: ", SERVER)
    print("URL: ", SERVER + ENDPOINT + ID + PARAMETERS)
    print("Response received:", response.status, response.reason, "\n")
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        print_colored("GENE: ", user_gene, "yellow")
        print_colored("Description: ", response_dict["desc"], "yellow")
        sequence = Seq(response_dict["seq"])
        seq_length = sequence.len()
        count_dict = sequence.count_bases()
        # most_frequent_base = sequence.most_frequent_base(count_dict)
        info_dict = sequence.info_seq()
        A = info_dict['A']
        G = info_dict['G']
        C = info_dict['C']
        T = info_dict['T']
        bases_dict = {'G': G[0], 'A': A[0], 'C': C[0], 'T': T[0]}
        max_value = max(bases_dict, key=bases_dict.get)
        print(colored("Total length:", "yellow"), seq_length, "\n", colored(f"""A: {A[0]} ({round(A[1], 1)}%)
 C: {C[0]} ({round(C[1], 1)}%)
 G: {G[0]} ({round(G[1], 1)}%)
 T: {T[0]} ({round(T[1], 1)}%)""", "blue"), "\n", colored("Most frequent base:", "yellow"), max_value)
except KeyError:
    print("The gene is not inside our database. Choose one of the following", list(DICT_GENES.keys()))