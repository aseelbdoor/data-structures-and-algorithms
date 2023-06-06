# Stack Queue Brackets
Write a function called validate_brackets that takes a string as input and returns a boolean value indicating whether or not the brackets in the string are balanced. Brackets can be one of three types: (), [], or {}. Your function should check if the opening and closing brackets are properly nested and balanced. Consider all other characters in the string as irrelevant

## Whiteboard Process
![bracket](./brackets.png)

## Approach & Efficiency
- The validate_brackets function checks whether the brackets in a given string are balanced.
- It uses a stack data structure to keep track of the opening brackets encountered.
- The function assumes the availability of a custom Stack object, which is not a built-in class in Python.
- The opening brackets are defined in a list called openn, which contains '(', '[', and '{'.
- The corresponding closing brackets are defined in a list called close, which contains ')', ']', and '}'.
- The function iterates over each character in the input string.
- If the character is an opening bracket, it is pushed onto the stack using the push method of the Stack object.
- If the character is a closing bracket, the function checks if the stack is empty using the is_empty method of the Stack object.
- If the stack is empty, it means there is no corresponding opening bracket for the closing bracket, and the function returns False to indicate unbalanced brackets.
- If the stack is not empty, the function compares the closing bracket with the top of the stack.
- If the closing bracket does not match the corresponding opening bracket, the function returns False.
- After processing all characters in the string, the function checks if the stack is empty using the is_empty method.
- If the stack is empty, it means all opening brackets have been matched and closed, and the function returns True to indicate balanced brackets.
- If the stack is not empty, it means there are unmatched opening brackets, and the function returns False to indicate unbalanced brackets.

## Solution
To run the code: `python3 python/stack_queue_brackets/stack_queue_brackets.py`


|Input|Output|
|:-----|:------|
|"{}"|True|
|"{}(){}"|True|
|"()[[Extra Characters]]"|True|
|"(){}[[]]"|True|
|"{}{Code}[Fellows](( ))"|True|
|"[({}]"|False|
|"(]("|False|
|"{(})"|False|

[Open the code](./stack_queue_brackets.py)
