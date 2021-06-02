import http.server
import socketserver
import termcolor
import colorama
from Seq1 import Seq
import Server_utils as su
from urllib.parse import urlparse, parse_qs
import http.client
import json
DICT_GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}


# Define the Server's port
PORT =8083

SERVER = 'rest.ensembl.org'
Parameters = "?content-type=application/json"


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
class TestHandler(http.server.BaseHTTPRequestHandler): # this class is inside the HTTP server therefore it inherit the BaseHTTPRequestHandler methods

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        connection = http.client.HTTPConnection(SERVER)
        # We just print a message
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        termcolor.cprint("  Path: " + self.path, "lightblue")
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)
        context = {}
        try:
            if path_name == "/":
                contents = su.read_template_html_file("./index.html").render(context=context)
            elif path_name == "/listSpecies":
                ENDPOINT = "/info/species"
                connection.request("GET", ENDPOINT + Parameters)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                species_list = []
                amount_species = len(response_dict["species"])
                context["amount_species"] = amount_species
                limit = int(arguments["limit"][0])
                context["limit"] = limit
                for n in range(0, limit):
                    species_list.append(response_dict["species"][n]["common_name"])
                if "check":
                    print("The checkbox was checked")
                else:
                    print("The checkbox was not checked")
                context["names"] = species_list
                contents = su.read_template_html_file("/listSpecies.html").render(context=context)
            elif path_name == "/karyotype":
                ENDPOINT = "info/assembly/"
                specie = arguments["species"][0]
                connection.request("GET", ENDPOINT + specie + Parameters)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                karyotype = response_dict["karyotype"]
                context["species"] = arguments["species"][0]
                context["karyotype"] = karyotype
                contents = su.read_template_html_file("./karyotype.html").render(context=context)
            elif path_name == "/chromosomeLength":
                ENDPOINT = "info/assembly/"
                specie = arguments["species"][0]
                connection.request("GET", ENDPOINT + specie + Parameters)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                chromosome = arguments["chromosome"][0]
                for n in range(0, len(response_dict["top_level_region"])):
                    if chromosome == response_dict["top_level_region"][n]["name"]:
                        length = response_dict["top_level_region"][n]["length"]
                context["length"] = length
                contents = su.read_template_html_file("./chromosomeLength.html").render(context=context)
        except KeyError:
            contents = su.read_template_html_file("./ERROR.html").render()
        except IndexError:
            contents = su.read_template_html_file("./ERROR.html").render()
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers() # we always need to call the end headers method which forces to create an empty line of the HTTP message

        # Send the response message
        self.wfile.write(contents.encode()) # wfile acts like a socket, its just something that we can write on

        # IN this simple server version:
        # We are NOT processing the client's request
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler # we create an instance of the child class TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()