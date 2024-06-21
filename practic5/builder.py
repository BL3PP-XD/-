class Product:
    def __init__(self):
        self.part_a = ""
        self.part_b = ""
        self.part_c = ""

    def set_part_a(self, part_a):
        self.part_a = part_a

    def set_part_b(self, part_b):
        self.part_b = part_b

    def set_part_c(self, part_c):
        self.part_c = part_c

    def show(self):
        print(f"Части продукта: {self.part_a}, {self.part_b}, {self.part_c}")

class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_product(self):
        pass

class SomeBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.set_part_a("Часть A")

    def build_part_b(self):
        self.product.set_part_b("Часть B")

    def build_part_c(self):
        self.product.set_part_c("Часть C")

    def get_product(self):
        return self.product

class Director:
    def set_builder(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()

if __name__ == "__main__":
    builder = SomeBuilder()
    director = Director()
    director.set_builder(builder)

    director.construct()
    product = builder.get_product()
    product.show()
