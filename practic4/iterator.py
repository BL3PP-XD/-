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
    vec = [4, 5, 6, 7, 83]

    it = Iterator(vec)

    while it.has_more():
        print(it.value(), end=" ")
        it.next()
