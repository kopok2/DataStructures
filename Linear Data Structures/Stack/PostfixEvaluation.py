from InfixToPostfix import infix_to_postfix
from Stack import Stack


def evaluate_postfix(postfix, mapping):
    s = Stack()
    for c in postfix:
        if c not in ["-", "+", "*", "/", "%", "^"]:
            s.push(c)
        else:
            c1 = s.pop()
            v1 = mapping[c1]
            v2 = mapping[s.pop()]
            value = eval("{0}{1}{2}".format(v1, c, v2).replace("^", "**"))
            mapping[c1] = value
            s.push(c1)
    return mapping[s.pop()]


if __name__ == "__main__":
    print(evaluate_postfix(infix_to_postfix("a+b*c"), {"a": 1, "b": 2, "c": 2}))
