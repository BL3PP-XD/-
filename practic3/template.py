from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

class TemplateMethodClass(AbstractClass):
    def step1(self):
        print("Шаг 1 выполнен")

    def step2(self):
        print("Шаг 2 выполнен")

    def step3(self):
        print("Шаг 3 выполнен")

if __name__ == "__main__":
    template_method = TemplateMethodClass()
    template_method.template_method()
