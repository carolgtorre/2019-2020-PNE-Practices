import http.server
import socketserver
import termcolor
import pathlib
import jinja2
import json

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def read_json_file():
    content = {"Name": "Adenine",
    "Letter": "A",
    "Link": "https://en.wikipedia.org/wiki/Adenine",
    "Formula": "C5H5N5"}
    # content = connection.getcontent()
    # content = json.loads(content.read().decode())
    return content

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        if self.path == '/':
            contents = read_html_file('./html/index.html')
        elif self.path == '/info/A':
            # contents == {'Name': 'Adenine', 'Letter' : 'A' ,'Link': 'https://en.wikipedia.org/wiki/Adenine', 'Formula': 'C5H5N5'}
            # return contents
            contents = read_json_file()
        elif self.path == '/info/C':
            contents = read_html_file('./html/info/C.html')
        elif self.path == '/info/G':
            contents = read_html_file('./html/info/G.html')
        elif self.path == '/info/T':
            contents = read_html_file('./html/info/T.html')
        elif self.path.endswith('.html'):
            try:
                contents = read_html_file('./html' + self.path)
            except FileNotFoundError:
                contents = read_html_file('./html/ERROR.html')
        else:
            contents = read_html_file('./html/ERROR.html')

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        #       self.send_header('Content-Length', len(contents.encode()))
        # The header is finished
        self.end_headers()
        # Send the response message
        #       self.wfile.write(contents.encode())
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