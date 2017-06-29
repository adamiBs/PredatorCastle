from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json
from collections import namedtuple

import profile


PORT_NUMBER = 8080

# This class will handles any incoming request from
# the browser

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

class routing(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        # if self.path == "/":
        #     self.send_response(200)
        #     self.send_header('Content-type', 'text/html')
        #     self.end_headers()
        #     # Send the html message
        #     self.wfile.write("Hello World !")
        #     return
        if self.path.split('/')[1] == "friends":
            profile.getFriends(self)
            return

        if self.path.split('/')[1] == "personal":
            profile.getPersonal(self)
            return

        # Redirect on invalid path
        self.send_response(302)
        self.send_header('Location', "/")
        self.end_headers()

        return

    # Handler for the POST requests
    def do_POST(self):
        if self.path == "/":
            data = self.rfile.read(int(self.headers['Content-Length']))
            self.send_response(200)
            self.end_headers()
            data = json2obj(data)
            print data.username
            print data.password
            return

        return
try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), routing)
    print 'Started httpserver on port ', PORT_NUMBER
    # Wait forever for incoming httP requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()