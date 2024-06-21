class Target:
    def request(self):
        pass

class Adaptee:
    def specific_request(self):
        print("Выполняем запрос от Adapter'a")

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    adapter.request()
