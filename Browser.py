import Constants
import time
from EdgeGateway import EdgeGateway
from PublicDNS import dns
from RealPizzaClient import RealPizzaClient

domain_name = "pizza.service.com"

print(f"Public DNS status: {dns.status()}")

resolved_ip, resolved_port = dns.resolve(domain_name)
print(f"Browser resolved {domain_name} -> {resolved_ip}")

client = RealPizzaClient(domain_name, resolved_ip, resolved_port)
client.order_pizza("margherita", 2)
