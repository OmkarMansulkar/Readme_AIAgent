import random

servers = [0,0,0,0]
index=0

def choose_Server(algorithm):
    global index
    if algorithm == "round_robin":
        s=index
        index = (index+1) % len(servers)
    elif algorithm == "least_connections":
        s = servers.index(min(servers))
    elif algorithm == "random":
        s = random.randint(0,len(servers)-1)
    else:
        raise ValueError("Invalid algorithm")  
    servers[s]+=1
    return s


algo = input("Enter the load balancing algorithm (round_robin, least_connections, random): ").strip().lower()
for _ in range (20):
    sid = choose_Server(algo)
    print(f"Server {sid} is chosen")
    
print("FInal server load")
for i,load in enumerate(servers):
    print(f"Server {i} load: {load}")