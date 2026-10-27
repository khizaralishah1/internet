import Constants
import socket
import threading

class EdgeGateway:
  def __init__(self, ip_addr: str, port: int = 8080):
    self.ip_addr = ip_addr
    self.port = port
    self.routes = {}
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind((self.ip_addr, self.port))

  def add_route(self, domain: str, internal_service_name: str):
    ''' Infrastructure team does this '''
    self.routes[domain] = internal_service_name

  def start(self):
    self.socket.listen(128)
    print(f"Edge gateway listening on {self.ip_addr}:{self.port}...")
    self.listen_loop()

  def listen_loop(self):
    try:
      # runs forever, one thread per client so a slow client doesn't block others
      while True:
        conn, addr = self.socket.accept()
        threading.Thread(target=self.handle_connection, args=(conn,), daemon=True).start()
    finally:
      self.socket.close()

  def handle_connection(self, conn: socket.socket):
    try:
      raw_data = conn.recv(2048).decode('utf-8')
      print('[EDGE GATEWAY RECEIVED RAW TCP PACKET]')
      print(raw_data.strip())

      # parse to find host header
      host_header = ''
      for line in raw_data.split('\r\n'): 
        if line.lower().startswith('host:'): 
          host_header = line.split(':', 1)[1].strip()
          break
      print(f"Gateway extracted Host Header: {host_header}")

      if host_header in self.routes:
        internal_target = self.routes[host_header]
        print(f"Routing rule matched: {host_header} to service {internal_target}")
        
        # Query the service registry
        endpoints = self.registry.get_endpoints(internal_target)
        print(f"Endpoints: {endpoints}")

        

        response_body = f"Routed successfully to {internal_target}"
        http_response = (
          'HTTP/1.1 200 OK\r\n'
          'Content-Type: text/plain\r\n'
          f'Content-Length: {len(response_body)}\r\n'
          'Connection: close\r\n'
          '\r\n' + response_body
        )
      else:
        http_response = 'HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n'

      # send back to client
      conn.sendall(http_response.encode('utf-8'))
    finally:
      conn.close()

if __name__ == '__main__':
  edge_gateway = EdgeGateway(Constants.edge_gateway_ip_addr, Constants.edge_gateway_port)
  edge_gateway.add_route("pizza.service.com", "pizza-service")

  # Runs until stopped with Ctrl+C
  try:
    edge_gateway.start()
  except KeyboardInterrupt:
    print("\nEdge gateway shutting down")