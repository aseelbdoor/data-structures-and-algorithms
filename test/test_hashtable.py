import pytest
from python.hashtable.hashtable import HashTable

@pytest.fixture
def empty_hash_table():
    return HashTable()

@pytest.fixture
def filled_hash_table():
    ht = HashTable()
    ht.set('key1', 'value1')
    ht.set('key2', 'value2')
    ht.set('key3', 'value3')
    return ht

def test_set(empty_hash_table):

    empty_hash_table.set('key1', 'value1')
    retrieved_value = empty_hash_table.get('key1')
    assert retrieved_value == 'value1'


def test_set_and_get(empty_hash_table):

    empty_hash_table.set('key2', 'value2')
    retrieved_value = empty_hash_table.get('key2')
    assert retrieved_value == 'value2'

def test_get_non_existent_key(empty_hash_table):
    assert empty_hash_table.get('non_existent_key') is None

def test_get_non_existent_key2(empty_hash_table):
    assert empty_hash_table.get('aseel') is None

def test_keys(filled_hash_table):
    keys = filled_hash_table.keys
    assert keys == ['key1', 'key2', 'key3']

def test_collision_handling(empty_hash_table):
    empty_hash_table.set('key1', 'value1')
    empty_hash_table.set('key2', 'value2')
    empty_hash_table.set('evidence', 'value3')
    assert empty_hash_table.get('key1') == 'value1'
    assert empty_hash_table.get('key2') == 'value2'
    assert empty_hash_table.get('evidence') == 'value3'

def test_retrieve_from_bucket_with_collision(filled_hash_table):
    filled_hash_table.set('evidence', 'value3')
    assert filled_hash_table.get('evidence') == 'value3'


def test_hashing_in_range(filled_hash_table):
    hashing = 832
    index = filled_hash_table._HashTable__hash("test")
    assert index == hashing

def test_hashing_in_range(filled_hash_table):
    hashing = 270
    index = filled_hash_table._HashTable__hash("aseel")
    assert index == hashing

# [116, 101, 115, 116] = 448 * 283 % 1024 =736