# Processes Pizza Orders
import os
import sys
from flask import Flask, request

app = Flask(__name__)

@app.route("/order", methods=["POST"])
def make_order():
  # Process the order
  return {"status" : "created"}

# DO NOT HARDCODE: app.run(port=8080)
# WHY? Replicas of this program / service ...

# Professional way
# 1. Read from an environment var passed in by scheduler
# 2. Or, Read from a command-line argument
# 3. Fall back to 8080
assigned_port = int(os.environ.get("PORT"), sys.argv[1] if len(sys.argv) > 1 else 8080)

app.run(host="0.0.0.0", port=assigned_port)


# lets say it is run my cluster manager on machines:
# machine 1 (10.0.1.10:8080)
# machine 2 (10.0.1.15:9090)

# fyi, this is the port of the machine
# when network traffic arrives on this machine's network card
# the OS routes traffic for port 8080 to the pizza serivce process

# how it works
# cluster / scheduler (10.0.1.10) decides where to run this program
# it finds a free port
# finds 8081 free
# PORT=8081 python3 PizzaServer.py

# want to run a second replica on same machine?
# find a free port, execute
# PORT=8082 python3 PizzaServer.py

# The cluster manager keeps storing this stuff in its registry:
# 10.0.1.10:8081, 10.0.1.10:8082, ... 

# HOW WILL YOU FIND THIS APP / PROGRAM / SERVICE
# This is how google does this:
# In the cluter manager, it stores logical names
# My phone wants to talk to pizza service
# I type in pizza.khizar.com
# Public DNS Server (phone/laptop knows where it is) resolves to Public IP
# Routes to a fixed Public IP
# Phone is connected to that server
# Now that server itself will act as an internal client for that service/program
# That edge server sees our HTTP request
# It routes our domain to the target service (pre-mapped)
# eg, doman: pizza.service.com" routes to target_service: "pizza_service"
# Then the gateway/server takes this target service name and queries the internal directory
# "Give me action endpoints of this service"
# Directory returns: ["10.0.1.10:8081", "10.0.1.11:8082"]
# Gateway forwards our http to one of these