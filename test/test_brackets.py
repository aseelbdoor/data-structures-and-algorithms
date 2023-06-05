from python.stack_queue_brackets.stack_queue_brackets import validate_brackets

def test1():
    actual=validate_brackets("{}")
    expected= True
    assert actual == expected

def test2():
    actual=validate_brackets("{}(){}")
    expected= True
    assert actual == expected

def test3():
    actual=validate_brackets("()[[Extra Characters]]")
    expected= True
    assert actual == expected

def test4():
    actual=validate_brackets("(){}[[]]")
    expected= True
    assert actual == expected

def test5():
    actual=validate_brackets("{}{Code}[Fellows](())")
    expected= True
    assert actual == expected

def test6():
    actual=validate_brackets("[({}]")
    expected= False
    assert actual == expected

def test7():
    actual=validate_brackets("(](")
    expected= False
    assert actual == expected

def test8():
    actual=validate_brackets("{(})")
    expected= False
    assert actual == expected