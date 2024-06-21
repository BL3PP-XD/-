class Iterator:
    def __init__(self, container):
        self._container = container
        self._index = 0

    def next(self):
        self._index += 1

    def value(self):
        return self._container[self._index]

    def has_more(self):
        return self._index < len(self._container)

if __name__ == "__main__":
    vec = [12, 21, 37, 73, 88]

    it = Iterator(vec)

    while it.has_more():
        print(it.value(), end=" ")
        it.next()
