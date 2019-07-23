from Stack import Stack


def get_stock_spans(stock):
    s = Stack()
    spans = [1]
    s.push(0)
    for x in range(1, len(stock)):
        while not s.is_empty() and stock[s.peek()] <= stock[x]:
            s.pop()
        spans.append(x + 1 if s.is_empty() else x - s.peek())
        s.push(x)
    return spans


if __name__ == "__main__":
    print(get_stock_spans([10, 4, 5, 90, 120, 80]))
