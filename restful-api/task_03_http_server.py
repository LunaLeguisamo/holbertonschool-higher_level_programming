#!/usr/bin/python3
"""
Module that def a function

"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(self.data).encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.wfile.write(json.dumps(self.info).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server(server_class=HTTPServer, handler_class=Server, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor corriendo en el puerto {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()