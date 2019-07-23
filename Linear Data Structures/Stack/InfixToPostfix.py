from Stack import Stack


def infix_to_postfix(expression):
    s = Stack()
    result = ''
    operands = ["-", "+", "*", "/", "%", "^"]
    for c in expression:
        if c != " ":
            if c not in operands + ["(", ")"]:
              result += c
            elif c not in ["(", ")"]:
                if s.is_empty():
                    s.push(c)
                elif "(" in s.get_items():
                    s.push(c)
                elif operands.index(c) > operands.index(s.peek()):
                    s.push(c)
                else:
                    while not s.is_empty():
                        d = s.peek()
                        if d in ["(", ")"]:
                            s.push(c)
                        else:
                            if operands.index(d) >= operands.index(c):
                                result += d
                                s.pop()
                            else:
                                break
                    s.push(c)
            else:
                if c == "(":
                    s.push(c)
                else:
                    while s.peek() != "(":
                        result += s.pop()
                    s.pop()
    while not s.is_empty():
        result += s.pop()
    return result


if __name__ == "__main__":
    print(infix_to_postfix("a+b*c+d"))
    print(infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i"))
