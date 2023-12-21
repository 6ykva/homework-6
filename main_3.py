from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    
    @staticmethod
    def __get_index():
        filename = "homework.html"
        with open(filename, encoding="utf-8") as file:
            html_list = file.read()
        return html_list
    
    def do_GET(self):
        page_content = self.__get_index()
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    
    webServer.server_close()
    print("Server stopped.")
