import http.server
import socketserver
import threading

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

class CustomTCPServer(socketserver.TCPServer):
    allow_reuse_address = True  # Ensure the socket is reusable after shutdown

def run_server():
    with CustomTCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        global server_instance
        server_instance = httpd
        httpd.serve_forever()

def stop_server():
    if server_instance:
        server_instance.shutdown()  # Stop the server loop
        server_instance.server_close()  # Unbind the socket
        print("Server stopped and socket unbound.")

# Start the server in a separate thread
server_instance = None
server_thread = threading.Thread(target=run_server)
server_thread.daemon = True
server_thread.start()

# Wait for user input to stop the server
try:
    input("Press Enter to stop the server...\n")
finally:
    stop_server()
    server_thread.join()
