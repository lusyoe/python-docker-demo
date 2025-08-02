from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应状态码为 200
        self.send_response(200)
        # 设置响应头
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # 响应内容
        self.wfile.write(b"Hello, World")

if __name__ == "__main__":
    server_address = ('', 8000)  # 监听所有地址的8000端口
    httpd = HTTPServer(server_address, HelloHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
