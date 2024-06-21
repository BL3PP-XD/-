class Visitor:
    def visit_element_a(self, element):
        pass

    def visit_element_b(self, element):
        pass

class Element:
    def accept(self, visitor):
        pass

class ElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)

    def operation_a(self):
        print("Операция с элементом №1")

class ElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)

    def operation_b(self):
        print("Операция с элементом №2")

class SomeVisitor(Visitor):
    def visit_element_a(self, element):
        element.operation_a()

    def visit_element_b(self, element):
        element.operation_b()

if __name__ == "__main__":
    element_a = ElementA()
    element_b = ElementB()
    visitor = SomeVisitor()

    element_a.accept(visitor)
    element_b.accept(visitor)
