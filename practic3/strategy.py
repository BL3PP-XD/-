from abc import ABC, abstractmethod

class IStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class Strategy1(IStrategy):
    def execute(self):
        print("Выполнение стратегии 1")

class Strategy2(IStrategy):
    def execute(self):
        print("Выполнение стратегии 2")

class Context:
    def __init__(self, strategy: IStrategy):
        self._strategy = strategy

    def set_strategy(self, new_strategy: IStrategy):
        self._strategy = new_strategy

    def execute_strategy(self):
        self._strategy.execute()

if __name__ == "__main__":
    strategy1 = Strategy1()
    strategy2 = Strategy2()

    context = Context(strategy1)
    context.execute_strategy()

    context.set_strategy(strategy2)
    context.execute_strategy()
