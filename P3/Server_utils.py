def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored("Message", "yellow"))
def format_command(command):
    return command.replace("\n", "").replace("\r", "")
def ping():
    termcolor.cprint("PING command!", "green")
    response = "OK!"
    print(response)
    cs.send(str(response).encode())

def get(cs, SEQ_GET, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())
   # termcolor.cprint("GET", 'green')
   # response = get_command(int(argument))
   # print(response)
def info(argument, cs, list_sequence):
    termcolor.cprint("INFO", "yellow")
    s = Seq(argument)
    dict_count = s.count_genes_info()
    a = dict_count['A'][0]
    pa = dict_count['A'][1]
    c = dict_count['C'][0]
    pc = dict_count['C'][1]
    g = dict_count['G'][0]
    pg = dict_count['G'][1]
    t = dict_count['T'][0]
    pt = dict_count['T'][1]
    first = 'Total length: ' + str(len(argument)) + '\n'
    cs.send(first.encode())
    second = 'A: ' + str(a) + ' ' + str(pa) + '%' + '\n'
    cs.send(second.encode())
    third = 'C: ' + str(c) + ' ' + str(pc) + '%' + '\n'
    cs.send(third.encode())
    fourth = 'G: ' + str(g) + ' ' + str(pg) + '%' + '\n'
    cs.send(fourth.encode())
    fifth = 'T: ' + str(t) + ' ' + str(pt) + '%' + '\n'
    cs.send(fifth.encode())
    print(first, second, third, fourth, fifth)

def comp(Seq):
   # termcolor.cprint("COMP", 'green')
   # response = list_sequences[argument]
   # print(response)
   s = Seq-Server(Seq)
   return s.complement()

def rev(argument, cs):
        # -- Create the object sequence from the string
        seq = Seq(Seq)
        return seq.reverse()