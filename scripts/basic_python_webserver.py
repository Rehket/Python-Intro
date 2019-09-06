import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

my_server = socketserver.TCPServer(("", PORT), Handler)

print("Your server has started on port", PORT)

my_server.serve_forever()
