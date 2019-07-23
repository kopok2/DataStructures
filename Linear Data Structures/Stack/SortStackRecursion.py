from Stack import Stack


def sort_stack(S):
    if not S.is_empty():
        value = S.pop()
        S = sort_stack(S)
        sorted_insert(S, value)
    return S


def sorted_insert(S, value):
    if S.is_empty() or value > S.peek():
        S.push(value)
    else:
        v = S.pop()
        sorted_insert(S, value)
        S.push(v)


if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(3)
    s.push(-2)
    s.push(5)
    print(s.get_items())
    s = sort_stack(s)
    print(s.get_items())
