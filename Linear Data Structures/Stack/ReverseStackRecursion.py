from Stack import Stack


def insert_at_bottom(S, value):
    if not S.is_empty():
        v = S.pop()
        S = insert_at_bottom(S, value)
        S.push(v)
        return S
    else:
        S.push(value)
        return S


def reverse_stack(S):
    if not S.is_empty():
        value = S.pop()
        S = reverse_stack(S)
        insert_at_bottom(S, value)
        return S
    else:
        return S


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s = reverse_stack(s)
    print(s.get_items())
