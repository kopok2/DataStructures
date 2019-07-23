from Stack import Stack


def reverse_string(str):
    s = Stack()
    for c in str:
        s.push(c)
    result = ''
    while not s.is_empty():
        result += s.pop()
    return result


if __name__ == "__main__":
    print(reverse_string("abcd"))
