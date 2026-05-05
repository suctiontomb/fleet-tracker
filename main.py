
def valid_parentheses(parentheses: str) -> bool:
    correct = []
    for i in parentheses:
        if i == '(':
            correct.append(')')
        elif i == '[':
                correct.append(']')
        elif i == '{':
            correct.append('}')
        if i not in "([{":
            if i != correct.pop():
                return False
    return len(correct) == 0



