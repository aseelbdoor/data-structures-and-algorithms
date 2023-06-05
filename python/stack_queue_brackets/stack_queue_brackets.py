
def validate_brackets(string):
    """
    Validates if the brackets in the given string are balanced.

    Parameters:
        string (str): The string containing brackets to be validated.

    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    li = []
    openn = ['(', '[', '{']
    close = [')', ']', '}']
    for i in string:
        if i in openn:
            li.append(i)
        elif i in close:
            if not li:
                return False 
            opene = li.pop()
            if openn.index(opene) != close.index(i):
                return False
    return len(li) == 0



#main
if __name__=="__main__":
    a="{}"
    print(validate_brackets(a))