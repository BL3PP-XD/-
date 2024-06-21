from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    @abstractmethod
    def method_a(self):
        pass

class ProductA1(AbstractProductA):
    def method_a(self):
        print("Продукт A1 метод A")

class ProductA2(AbstractProductA):
    def method_a(self):
        print("Продукт A2 метод A")

class AbstractProductB(ABC):
    @abstractmethod
    def method_b(self):
        pass

class ProductB1(AbstractProductB):
    def method_b(self):
        print("Продукт B1 метод B")

class ProductB2(AbstractProductB):
    def method_b(self):
        print("Продукт B2 метод B")

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    product_a1 = factory1.create_product_a()
    product_b1 = factory1.create_product_b()

    product_a1.method_a()
    product_b1.method_b()

    factory2 = ConcreteFactory2()
    product_a2 = factory2.create_product_a()
    product_b2 = factory2.create_product_b()

    product_a2.method_a()
    product_b2.method_b()
