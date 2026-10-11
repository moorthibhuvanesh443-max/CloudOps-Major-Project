from http.server import BaseHTTPRequestHandler, HTTPServer

class CloudOpsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <body style="font-family: Arial; text-align: center;">
            <h1>Welcome to My CloudOps Project!</h1>
            <p>Cloud Computing and DevOps Internship</p>
            <p>Application is running successfully.</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8000), CloudOpsHandler)
print("Application running at http://0.0.0.0:8000")
server.serve_forever()
