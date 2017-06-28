from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import profile


PORT_NUMBER = 8080

# This class will handles any incoming request from
# the browser


class routing(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write("Hello World !")
            return

        if self.path == "/profile":
            profile.returnAdami(self)
            return

        # Redirect on invalid path
        self.send_response(302)
        self.send_header('Location', "/")
        self.end_headers()

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