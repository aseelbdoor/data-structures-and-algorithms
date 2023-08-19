from python.graph.graph import Graph
import pytest

@pytest.fixture
def filled_graph():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    e = g.add_vertix('E')
    c = g.add_vertix('C')
    d = g.add_vertix('D')

    g.add_edge(a,b)
    g.add_edge(a,c)
    g.add_edge(b,d)
    g.add_edge(b,e)
    g.add_edge(e,d)
    g.add_edge(e,c)
    return g,a

def test_add_vertix():
    g = Graph()
    a = g.add_vertix('A')
    actual=str(a)
    expected="A"
    assert actual==expected

def test_add_edge():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    g.add_edge(a,b)
    actual=str(g.get_neighbors(a)[0])
    expected="B,0"
    assert actual==expected

def test_vertices(filled_graph):
    graph,a=filled_graph
    actual=[str(i) for i in graph.get_vertices()]
    expected=['A', 'B', 'E', 'C', 'D']
    assert actual == expected

def test_collection(filled_graph):
    graph,a=filled_graph
    actual=graph.breadth_first(a)
    expected=['A', 'B', 'C', 'D', 'E']
    assert actual == expected

def test_size(filled_graph):
    graph,a=filled_graph
    actual=graph.size()
    expected=5
    assert actual == expected

def test_edge_with_weight():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    g.add_edge(a,b,10)
    actual=str(g.get_neighbors(a)[0])
    expected="B,10"
    assert actual==expected

def test_one_vertex():
    g = Graph()
    a = g.add_vertix('A')
    actual=g.breadth_first(a)
    expected=["A"]
    assert actual==expected

def test_depth_first(filled_graph):
    graph,a=filled_graph
    actual=graph.depth_first(a)
    expected=['A', 'B', 'D', 'E', 'C']
    assert actual == expected
