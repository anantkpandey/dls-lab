from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        start = time.perf_counter()

        response = {
            "node": "ubuntu-sys",
            "experiment": "RPC over HTTP",
            "message": "Hello from Ubuntu!",
            "server_time": time.time()
        }

        body = json.dumps(response).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"{self.client_address[0]} {self.path} {elapsed_ms:.3f} ms")

    def log_message(self, format, *args):
        print(format % args)

server = HTTPServer(("0.0.0.0", 8080), Handler)
print("Listening on port 8080...")
server.serve_forever()
