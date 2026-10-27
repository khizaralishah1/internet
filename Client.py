import random

class PizzaClient:
  def __init__(self, service_name, registry):
    self.service_name = service_name
    self.registry = registry

  def order_pizza(self, pizza_name):
    available_servers = self.registry.get_servers()