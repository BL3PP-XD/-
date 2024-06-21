class Mediator:
    def send_message(self, message, colleague):
        pass

class Colleague:
    def __init__(self, mediator=None):
        self.mediator = mediator

    def receive_message(self, message):
        pass

    def send_message(self, message):
        if self.mediator:
            self.mediator.send_message(message, self)

    def set_mediator(self, mediator):
        self.mediator = mediator

class SomeColleague(Colleague):
    def __init__(self, name, mediator=None):
        super().__init__(mediator)
        self.name = name

    def receive_message(self, message):
        print(f"{self.name} получил: {message}")

class SomeMediator(Mediator):
    def __init__(self):
        self.colleagues = []

    def add_colleague(self, colleague):
        self.colleagues.append(colleague)
        colleague.set_mediator(self)

    def send_message(self, message, colleague):
        for col in self.colleagues:
            if col != colleague:
                col.receive_message(message)

if __name__ == "__main__":
    mediator = SomeMediator()
    colleague1 = SomeColleague("Коллега 1", mediator)
    colleague2 = SomeColleague("Коллега 2", mediator)

    mediator.add_colleague(colleague1)
    mediator.add_colleague(colleague2)

    colleague1.send_message(" Привет от Коллеги  1")
    colleague2.send_message(" Привет от Коллеги  2")
