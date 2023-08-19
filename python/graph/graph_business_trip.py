# from graph import Graph
from python.graph.graph import Graph

def business_trip(gr,arr):
    """
    Calculate the cost of a business trip through a weighted graph.

    Parameters:
        gr (Graph): The graph representing locations and connections.
        arr (list): An array of vertex values representing the trip route.

    Returns:
        str or None: A string containing the calculated cost with dollar sign ($) or None if the trip is not possible.
    """
    vertices=gr.get_vertices()
    verticex=[]
    for i in arr:
        for j in vertices:
            if j.value==i:
                verticex.append(j)
    if len(verticex)==len(arr):
        cost=0
        for i in range(len(verticex)-1):
            neighbors=gr.get_neighbors(verticex[i])
            for j in neighbors:
                if j.vertix==verticex[i+1]:
                    cost+=j.weight
        if cost>0:
            return f'${cost}'
        return None
    else:
        return None

if __name__=="__main__":
    g = Graph()
    a = g.add_vertix('Pandora')
    b = g.add_vertix('Metroville')
    e = g.add_vertix('Narnia')
    c = g.add_vertix('Arendelle')
    d = g.add_vertix('Monstropolis')
    f = g.add_vertix('Naboo')

    g.add_edge(a,b,82)
    g.add_edge(a,c,150)
    g.add_edge(b,d,105)
    g.add_edge(b,e,37)
    g.add_edge(b,c,99)
    g.add_edge(b,f,26)
    g.add_edge(e,f,250)
    g.add_edge(f,d,73)
    g.add_edge(c,d,42)

    print(business_trip(g,['Metroville', 'Pandora']))