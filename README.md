You open a browser, type in a domain name and Enter. The http request goes to a Public DNS server whose ip you already know. This server responds with an http request that contains the ip of the domain you typed in.

Your browser sends an http request (to bring main html page) to that ip.

For now, that ip was of an edge gateway. This gateway will accept this request and see the domain name. It will find the service associated with this domain name from its service registery. How it was added is another story.

Gateway finds a list of endpoints where this service, just a python app, is running. It routes our http request to a relevant endpoint - which is one of the many replicas of this service running in any of the machines in the data center

domain -> service name -> end machines

dns: domain -> ip
     ip -> edge gateway
     edge gateway sees domain in http. uses internal routing to route to service name
     find endpoints from service name
     choose suitable endpoint
     send request to that endpoint