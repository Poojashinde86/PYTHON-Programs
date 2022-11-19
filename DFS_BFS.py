from collections import defaultdict
def visit(i):
    for j in adj_list[i]:
        if j not in visited:
            if j not in exploring:
                print(j," ",end=' ')
                exploring.append(j)
                visit(j)
                exploring.pop()
                visited.append(j)
            
n = int(input("Enter number of nodes: "))
adj_list = defaultdict(list)
num_of_edges = int(input("Enter number of edges: "))
if(num_of_edges):
    print("To add an edge, enter node numbers to which the edge is incident on and then hit enter")
for i in range(num_of_edges):
    u,v =input().split()
    u = int(u); v = int(v)
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = []
exploring =[]
#dfs
for i in range(1,n+1):
    if i not in visited:
        exploring.append(i)
        print(i," ",end=' ')
        visit(i)
        exploring.pop()
        visited.append(i)
