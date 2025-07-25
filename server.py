import http.server
import socketserver
import subprocess

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/start':
            subprocess.Popen(["python", "eye_mouse_control.py"])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Started eye control script")
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Server running at http://localhost:{PORT}")
    httpd.serve_forever()
