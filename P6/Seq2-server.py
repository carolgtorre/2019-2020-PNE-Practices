import http.server
import socketserver
import termcolor
import pathlib
import jinja2
from urllib.parse import urlparse, parse_qs
import Server_utils as su

list_sequences = ["ACGTAAAAGTTTAAGCGCCAAT", "AGTCCCCCCAAAATTTTGGGGGAATAT", "AGAGAGAGGATTATTATATACTCTTC", "GGGGGGGGGGGTTTTTTTTTAAAAAACCCC", "AAAAAATTTTTCGAAAAAAA"]

list_genes = ['ADA', 'FRAT1', 'FXN', 'RNU6_269P', 'U5']
bases_information = {
    'A': {'link': "https://en.wikipedia.org/wiki/Adenine",
          'formula': "C5H5N5",
          'name': "ADENINE",
          'colour': 'lightgreen'
    },
    'C': {'link': "https://en.wikipedia.org/wiki/Cytosine",
          'formula': "C4H5N30",
          'name': "CYTOSINE",
          'colour': 'yellow'
    },
    'G': {'link': "https://en.wikipedia.org/wiki/Guanine",
          'formula': "C5H5N50",
          'name': "GUANINE",
          'colour': 'lightblue'
    },
    'T': {'link': "https://en.wikipedia.org/wiki/Thymine",
          'formula': "C5H6N202",
          'name': "THYMINE",
          'colour': 'pink'
    }
}

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)
        context = {}
        if path_name == '/':
            context["n_sequences"] = len(list_sequences)
            context["list_genes"] = list_genes
            contents = su.read_template_html_file('./index.html').render(context=context)
        elif path_name == "/test":
            contents = su.read_template_html_file("./test.html").render()
        elif path_name == "/ping":
            contents = su.read_template_html_file("./ping.html").render()
        elif path_name == "/get":
            number_sequence = arguments["sequence"][0]
            contents = su.get(list_sequences, number_sequence)
        elif path_name == "/gene":
            gene = arguments["gene"][0]
            contents = su.gene(gene)
        elif path_name == "/operation":
            sequence = arguments["sequence"][0]
            calculation = arguments["calculation"][0]
            if calculation == "Info":
                contents = su.info(sequence)
            elif calculation == "Comp":
                contents = su.comp(sequence)
            elif calculation == "Rev":
                contents = su.rev(sequence)
            else:
                contents = su.read_template_html_file('./ERROR.html').render()
        else:
            contents = su.read_template_html_file("./ERROR.html").render()
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(contents.encode())
        return
# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()