import pytest
from python.hashmap_left_join.hashmap_left_join import left_join,HashTable

@pytest.fixture
def filled_hash_table1():
    ht1 = HashTable()
    ht1.set('diligent', 'employed')
    ht1.set('fond', 'enamored')
    ht1.set('guide', 'usher')
    ht1.set('outfit', 'garb')
    ht1.set('wrath', 'anger')
    return ht1

@pytest.fixture
def filled_hash_table2():
    ht2 = HashTable()
    ht2.set('diligent', 'idle')
    ht2.set('fond', 'averse')
    ht2.set('guide', 'follow')
    ht2.set('flow', 'jam')
    ht2.set('wrath', 'delight')
    return ht2

@pytest.fixture
def empty_hash_table():
    return HashTable()


def test_happy_path(filled_hash_table1,filled_hash_table2):
    actual=left_join(filled_hash_table1,filled_hash_table2)
    expected=[['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outfit', 'garb', 'Null'], ['wrath', 'anger', 'delight']]
    assert actual==expected

def test_empty1(empty_hash_table,filled_hash_table2):
    actual=left_join(empty_hash_table,filled_hash_table2)
    expected=[]
    assert actual == expected

def test_empty2(filled_hash_table1,empty_hash_table):
    actual=left_join(filled_hash_table1,empty_hash_table)
    expected=[['diligent', 'employed', 'Null'], ['fond', 'enamored', 'Null'], ['guide', 'usher', 'Null'], ['outfit', 'garb', 'Null'], ['wrath', 'anger', 'Null']]
    assert actual == expected
