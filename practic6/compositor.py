class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print("Leaf: выполнение операции.")

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        print("Composite: выполнение операции для всех дочерних компонентов.")
        for child in self.children:
            child.operation()

if __name__ == "__main__":
    composite = Composite()
    composite.add(Leaf())
    composite.add(Leaf())
    composite.operation()
