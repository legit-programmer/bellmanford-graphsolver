from colorama import Fore, Style
import networkx as net
import matplotlib.pyplot as plt

welcome = """----------------------------------
Make sure you properly read the instructions and provide the input.

"""
print()
print(Fore.GREEN, 'Bellman Ford algorithm solver')
print(welcome)
print(Style.RESET_ALL)
n = int(input("Enter the number of nodes: "))

box = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

joints = {}
costMap = {}
distanceMap = {
    'A':0, 
}


def dumpPaths():
    for i in range(n):
        joint = input(f"Enter paths for {box[i]} (seperate with commas if multiple): ").upper()
        jointlst = [] if joint=='' else joint.split(',')
        joints[box[i]] = jointlst

def dumpCosts():
    for i in joints:
        costlst = []
        for j in joints[i]:
            cost = input(f"Enter cost for {i} to {j}: ")
            costlst.append(int(cost))
        costMap[i] = costlst


def setWeightsToInfinite():
    for i in range(1, n):
        distanceMap[box[i]] = 'inf'



def relax():
    for i in joints:
        if distanceMap[i]=='inf':
            continue

        for j in joints[i]:                
            if distanceMap[j]!='inf':
                if distanceMap[i] + costMap[i][joints[i].index(j)]<distanceMap[j]:
                    distanceMap[j] = distanceMap[i] + costMap[i][joints[i].index(j)]
                continue
            distanceMap[j] = distanceMap[i] + costMap[i][joints[i].index(j)]


def createGraph():
    G = net.DiGraph(directed=True)

    for i in distanceMap:
        G.add_node(i, weight=distanceMap[i])

    for u in joints:
        for v in joints[u]:
            costIndex:list = joints[u]
            G.add_edge(u, v, weight = costMap[u][costIndex.index(v)])
    
    pos = net.circular_layout(G)
    net.draw(G, pos, with_labels=True)

    print(G.edges(data=True))

    edge_labels = {(u, v):d['weight'] for u,v,d in G.edges(data=True)}
    net.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    fig = plt.gcf()
    dpi = fig.dpi
    width, height = fig.get_size_inches()

    plt.text(-0.5, -1, distanceMap, fontsize=12, ha='center', va='center')
    plt.show()

def main():
    
    dumpPaths()
    dumpCosts()
    setWeightsToInfinite()

    for i in range(n-1):
        relax()

    print(distanceMap)
    createGraph()



main()