
import pytest
from python.hashtable.hashtable import HashTable

@pytest.fixture
def empty_hash_table():
    return HashTable()

def test_str1(empty_hash_table):
    a="Once upon a time, there was a brave princess who..."
    actual=empty_hash_table.repeated_word(a)
    expected="The first word to occur more than once in this string is (a) that repeated : 2 times"
    assert actual==expected

def test_str2(empty_hash_table):
    a="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual=empty_hash_table.repeated_word(a)
    expected="The first word to occur more than once in this string is (it) that repeated : 10 times"
    assert actual==expected

def test_str3(empty_hash_table):
    a="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual=empty_hash_table.repeated_word(a)
    expected="The first word to occur more than once in this string is (summer) that repeated : 2 times"
    assert actual==expected

def test_str4(empty_hash_table):
    a=""
    with pytest.raises(Exception):
        empty_hash_table.repeated_word(a)