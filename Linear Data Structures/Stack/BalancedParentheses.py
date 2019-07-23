from Stack import Stack


def has_balanced_parentheses(expression):
    s = Stack()
    for c in expression:
        if c == '(':
            s.push(c)
        elif c == ')':
            if not s.is_empty():
                if s.peek() == "(":
                    s.pop()
                else:
                    return False
            else:
                return False
    return s.is_empty()


if __name__ == "__main__":
    print(has_balanced_parentheses("(semir"))
    print(has_balanced_parentheses("(semir)"))
    print(has_balanced_parentheses("semir)"))
    print(has_balanced_parentheses("((semir)"))
    print(has_balanced_parentheses("((semir))"))
    print(has_balanced_parentheses("((se()mir))"))
    print(has_balanced_parentheses("((se()m)ir))"))
