import PizzaService
import ServiceRegistry

replica_1 = PizzaService.PizzaService(name = "Replica 1 @ 10.0.1.10:8080")
replica_2 = PizzaService.PizzaService(name = "Replica 2 @ 10.0.1.11:9090")

registry = ServiceRegistry.ServiceRegistry()
registry.register("pizza_service", replica_1)
registry.register("pizza_service", replica_2)