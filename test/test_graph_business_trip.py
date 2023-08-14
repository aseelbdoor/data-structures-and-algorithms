from python.graph.graph import Graph
from python.graph.graph_business_trip import business_trip
import pytest

@pytest.fixture
def filled_graph():
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
    return g

def test_one(filled_graph):
    a=['Arendelle','Monstropolis', 'Naboo']
    actual=business_trip(filled_graph,a)
    expected='$115'
    assert actual==expected

def test_two(filled_graph):
    a=['Narnia', 'Arendelle', 'Naboo']
    actual=business_trip(filled_graph,a)
    expected=None
    assert actual==expected

def test_three(filled_graph):
    a=['Naboo', 'Pandora']
    actual=business_trip(filled_graph,a)
    expected=None
    assert actual==expected

def test_four(filled_graph):
    a=['Metroville', 'Pandora']
    actual=business_trip(filled_graph,a)
    expected='$82'
    assert actual==expected