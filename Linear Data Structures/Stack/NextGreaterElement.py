from Stack import Stack


def next_greater_element(array):
    s = Stack()
    element = 0
    next = 0
    result = {}
    s.push(array[0])
    for x in range(1, len(array)):
        next = array[x]
        if not s.is_empty():
            element = s.pop()
            while element < next:
                result[str(element)] = next
                if s.is_empty():
                    break
                element = s.pop()
            if element > next:
                s.push(element)
        s.push(next)
    while not s.is_empty():
        element = s.pop()
        result[str(element)] = -1
    return result


if __name__ == "__main__":
    print(next_greater_element([1, 2, 3, 4]))
    print(next_greater_element([1, 2, 3, 2]))
    print(next_greater_element([5, 4, 4, 3]))
    print(next_greater_element([5, 4, 4, 100]))
