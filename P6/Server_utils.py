from Seq1 import Seq
import pathlib
import jinja2
def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored("Message", "yellow"))
def format_command(command):
    return command.replace("\n", "").replace("\r","")
def ping():
    print_colored("PING command!", "green")
    response = "OK!"
    cs.send(str(response).encode())

def get(list_sequences, seq_number):
    context={
        "number": seq_number,
        "sequence": list_sequences[int(seq_number)]
    }
    contents = read_template_html_file("get.html").render(context=context)
    return contents

def info(sequence):
    s = Seq(sequence)
    info_dict = s.info_seq()
    response = f"""Total length {len(sequence)}
    A: {info_dict['A'][0]} ({info_dict['A'][1]}%)
    C: {info_dict['C'][0]} ({info_dict['C'][1]}%)
    G: {info_dict['A'][0]} ({info_dict['G'][1]}%)
    T: {info_dict['T'][0]} ({info_dict['T'][1]}%)"""
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'Info'
    }
    contents = read_template_html_file('operation.html').render(context=context)
    return contents

def comp(sequence):
    s = Seq(sequence)
    complement = s.complement()
    response = complement + '\n'
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'Comp'
    }
    contents = read_template_html_file('operation.html').render(context=context)
    return contents


def rev(sequence):
    s= Seq(sequence)
    rev = s.reverse()
    response = rev + '\n'
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'Rev'
    }
    contents = read_template_html_file('operation.html').render(context=context)
    return contents

def gene(seq_name):
    PATH ="./seqs/" + seq_name + '.txt'
    s1 = Seq()
    s1.read_fasta(PATH)
    context= {
        "gene_name": seq_name,
        "gene_contents": s1.strbases
    }
    contents = read_template_html_file("gene.html").render(context=context)
    return contents