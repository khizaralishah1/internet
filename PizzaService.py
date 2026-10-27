import socket
import threading

class PizzaService:
  def __init__(self, replica_id: str, ip_addr: str, port: int):
    self.replica_id = replica_id
    self.ip_addr = ip_addr
    self.port = port
    self.server_socket = None

  def start():
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server_socket.bind((self.ip_addr, self.port))
    self.server_socket.listen(5)
    print(f"Pizza service running at {self.ip_addr}:{self.port}")

    def listen_loop():
      while True:
        conn, addr = self.server_socket.accept()
        raw_data = conn.recv(2048).decode("utf-8")
        response_body = (
          f"Order fulfilled by {self.replica_id} at {self.ip_addr}:{self.port}"
        )
        http_response

  def handle_order(self, order_text):
    self.orders.append(order_text)
    return f"Order confirmed: '{order_text}' by {self.name}"

