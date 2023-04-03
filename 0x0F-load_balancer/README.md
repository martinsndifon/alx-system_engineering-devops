# Load Balancers
Load balancing is the method of distributing network traffic equally across a
pool of resources that support an application. Modern applications must process
millions of users simultaneously and return the correct text, videos, images,
and other data to each user in a fast and reliable manner. To handle such high
volumes of traffic, most applications have many resource servers with duplicate
data between them. A load balancer is a device that sits between the user and
the server group and acts as an invisible facilitator, ensuring that all
resource servers are used equally.

## What are the benefits of load balancing?
Load balancing directs and controls internet traffic between the application
servers and their visitors or clients. As a result, it improves an
application’s availability, scalability, security, and performance.

### Application availability
Server failure or maintenance can increase application downtime, making your
application unavailable to visitors. Load balancers increase the fault
tolerance of your systems by automatically detecting server problems and
redirecting client traffic to available servers. You can use load balancing to
make these tasks easier:
- Run application server maintenance or upgrades without application downtime
- Provide automatic disaster recovery to backup sites
- Perform health checks and prevent issues that can cause downtime

### Application scalability
You can use load balancers to direct network traffic intelligently among
multiple servers. Your applications can handle thousands of client requests
because load balancing does the following:
- Prevents traffic bottlenecks at any one server
- Predicts application traffic so that you can add or remove different servers,
if needed
- Adds redundancy to your system so that you can scale with confidence

### Application security
Load balancers come with built-in security features to add another layer of
security to your internet applications. They are a useful tool to deal with
distributed denial of service attacks, in which attackers flood an application
server with millions of concurrent requests that cause server failure. Load
balancers can also do the following:
- Monitor traffic and block malicious content
- Automatically redirect attack traffic to multiple backend servers to minimize
impact
- Route traffic through a group of network firewalls for additional security

### Application performance
Load balancers improve application performance by increasing response time and
reducing network latency. They perform several critical tasks such as the
following:

- Distribute the load evenly between servers to improve application performance
- Redirect client requests to a geographically closer server to reduce latency
- Ensure the reliability and performance of physical and virtual computing
resources

## What are load balancing algorithms?
A load balancing algorithm is the set of rules that a load balancer follows to
determine the best server for each of the different client requests. Load
balancing algorithms fall into two main categories.

### Static load balancing
Static load balancing algorithms follow fixed rules and are independent of the
current server state. The following are examples of static load balancing.

### Round-robin method
In the round-robin method, an authoritative name server does the load balancing
instead of specialized hardware or software. The name server returns the IP
addresses of different servers in the server farm turn by turn or in a
round-robin fashion.

### Weighted round-robin method
In weighted round-robin load balancing, you can assign different weights to
each server based on their priority or capacity. Servers with higher weights
will receive more incoming application traffic from the name server.

### IP hash method
In the IP hash method, the load balancer performs a mathematical computation,
called hashing, on the client IP address. It converts the client IP address to
a number, which is then mapped to individual servers.

### Dynamic load balancing 
Dynamic load balancing algorithms examine the current state of the servers
before distributing traffic. The following are some examples of dynamic load
balancing algorithms.

### Least connection method
A connection is an open communication channel between a client and a server.
When the client sends the first request to the server, they authenticate and
establish an active connection between each other. In the least connection
method, the load balancer checks which servers have the fewest active
connections and sends traffic to those servers. This method assumes that all
connections require equal processing power for all servers.

### Weighted least connection method
Weighted least connection algorithms assume that some servers can handle more
active connections than others. Therefore, you can assign different weights or
capacities to each server, and the load balancer sends the new client requests
to the server with the least connections by capacity.

### Least response time method
The response time is the total time that the server takes to process the
incoming requests and send a response. The least response time method combines
the server response time and the active connections to determine the best
server. Load balancers use this algorithm to ensure faster service for all
users.

### Resource-based method
In the resource-based method, load balancers distribute traffic by analyzing
the current server load. Specialized software called an agent runs on each
server and calculates usage of server resources, such as its computing capacity
and memory. Then, the load balancer checks the agent for sufficient free
resources before distributing traffic to that server.
